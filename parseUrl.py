#!/usr/bin/env python
# coding: utf-8
import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import re

class parseUrl:
    def __init__(self, *args):
        if len(args)==2:
            self.site = args[0]
            self.conf = args[1]
        self.cachedir = './cache_gscholar'
        if not os.path.isdir(self.cachedir):
            os.mkdir(self.cachedir)

    def selenium(self,url,fname):

        try:
            #time_s = time.time()
            #fname = self.cachedir + "/" + re.sub("[\:\/\.]","_",url) + ".txt"
            if os.path.isfile(fname):
                with open(fname, encoding='utf-8') as f:
                    bs = BeautifulSoup(f.read(), 'html.parser')
            else:
                #chopt = Options()
                #chopt.add_argument("--headless") # headless mode
                #driver = webdriver.Chrome(executable_path='./chromedriver',options=chopt) # locate appropriate webdriver in the executable-file directory
                egopt = Options()
                egopt.add_argument('headless')
                driver = webdriver.Edge(executable_path='./msedgedriver',options=egopt) # locate appropriate webdriver in the executable-file directory
                driver.get(url)
                time.sleep(10)
                bs = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                #print(driver.page_source)
                with open(fname, mode='w') as f:
                    f.write(str(bs.prettify()))
                #time_e = time.time()
                #etime = time_e - time_s
                #print("elapsed time: {0:.2f}".format(etime))
        except driver.exceptions.RequestException as e:
            print("Error: ",e)
        finally:
            #driver.quit()
            pass
        return bs
            
    def beautifulsoup(self,url):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Error: ",e)

        bs = BeautifulSoup(response.text, 'html.parser')
        return bs
    
    def parseCVFsite(self,url):
        normal = -1
        author, title = [], []
        
        print(url)
        bs = self.beautifulsoup(url)
        titles = bs.find_all('dt',{'class':'ptitle'})
        ddlines = bs.find_all('dd')

        ii = 0
        for line in ddlines:
            authors = line.find_all('form')
            if authors:
                aut = []
                for au in authors:
                    au = re.sub('^[\t\s]*$','',au.get_text())
                    au = re.sub('\n','',au)
                    if au != '':
                        au = re.sub('\s*,\s*','',au)
                        aut.append(re.sub('^\s','',au))
                author.append(aut)
                try:
                    title.append(titles[ii].get_text())
                    ii += 1
                except:
                    print(f'failed:{line}')
                    print(titles[ii-1].get_text())
        normal = 1
        return normal, author, title

    def parseCVF(self): 
        normal = -1 
        author, title = [], [] 
        
        rootsite = self.site + self.conf
        
        print(rootsite)
        bs = self.beautifulsoup(rootsite)
        links = bs.find_all('a')
        
        allpageFound = 0
        indpageFound = 0
        for link in links:
            linksite = link.get('href')
            if re.search('all$',str(linksite)):
                allpageFound = 1
                targetsite = self.site + linksite
                normal, author, title = self.parseCVFsite(targetsite)
                return normal, author, title
        
        if not allpageFound: 
            print("Error: no all link found")
            for link in links:
                linksite = link.get('href')
    
                if re.search('20[0-2][0-9]-[01][0-9]-[0-3][0-9]',str(linksite)):
                    indpageFound = 1
                    targetsite = self.site + linksite
                    normal, author_tmp, title_tmp = self.parseCVFsite(targetsite)
                    if normal > 0:
                        author=author+author_tmp
                        title=title+title_tmp
                    else:
                        return normal, author, title
            if indpageFound:
                return normal, author, title
            else:
                normal, author, title = self.parseCVFsite(rootsite)
                return normal, author, title

    def parsePapercept(self,url):
        normal = False
        
        print(url)
        bs = self.beautifulsoup(url)

        title = []
        author = []
        ttlidx = 1
        
        sects = bs.find_all('tr',{'class':'pHdr'})
        for sect in sects:
            session = sect.find('a').get_text()
            if re.search("(MoB-PO)|(TuC-PO)",session):
                continue
            elif re.search("(MoAmPo)|(MoPmPo)|(TuAmPo)|(TuPmPo)|(WeAmPo)|(WePmPo)",session):
                continue
            elif re.search("(TuPS)|(WePS)",session):
                continue
            sect = sect.next_sibling
            sect = sect.next_sibling
            sp = sect.find('span',{'class':'pTtl'})
            try:
                ttl = sp.find('a').get_text()
            except:
                continue
                
            ttl = re.sub('\s\(.+','',ttl)
            ttlidx += 1
            title.append(ttl)
            
            sect = sect.next_sibling
            sect = sect.next_sibling
            sect = sect.next_sibling
            sect = sect.next_sibling
            
            authors = []
            while 1:
                try:
                    au = sect.find('a').get_text()
                except:
                    break
                if sect.find('div'): 
                    break
                if au != 'None':
                    au = re.sub(r'^(.+?), (.+?)$',r'\2 \1',au)
                    authors.append(au)
                else:
                    break
                sect = sect.next_sibling
                sect = sect.next_sibling
                
            author.append(authors) 
        
        normal = True

        return normal, title, author
    
    def IEEERAS(self,url):
        normal = False
        author = []
        title = []
        maxpages = 1000
        for ii in range(1,maxpages):
            #url = 'https://ieeexplore.ieee.org/xpl/conhome/9811522/proceeding?isnumber=9811357&sortType=vol-only-seq&pageNumber='

            turl=f'{url}{ii}'
            fname = re.sub("[\:\/\.]","_",turl) + ".txt"
            print(turl)
            bs = self.selenium(turl,fname)
            noresult = bs.find_all('li',{'class':'article-list-item no-results'})
            if noresult:
                break
            
            blks = bs.find_all('div',{'class':'col result-item-align px-3'})
            for blk in blks:
                aublk = blk.find('p',{'class':'author text-base-md-lh'})
                if aublk:
                    ttl = re.sub('^\s+|[\n\t]','',blk.find('h2').get_text())
                    ttl = re.sub('\s*$','',ttl)
                    authors = aublk.get_text().strip()
                    authors = re.sub('\s+;\s+',',',authors)
                    author.append(re.split(',',authors))
                    title.append(ttl)
        
        normal = True

        return normal, title, author
 
    def Gscholar(self):
        normal = False
        name = []
        aff = []
        citation = []
        ourl = self.site
        stime = 10
        maxpage = 1500

        bRet = False
        for ii in range(0,maxpage):
            fname = self.cachedir + "/" + re.sub("[\:\/\.]","_",ourl) + "_" + str(ii) + ".txt"
            if os.path.isfile(fname):
                with open(fname, encoding='utf-8') as f:
                    bs = BeautifulSoup(f.read(), 'html.parser')
                    #onclick="window.location='/citations?view_op\x3dsearch_authors\x26hl\x3dja\x26mauthors\x3dlabel:computer_vision\x26after_author\x3d-2cKAHD2__8J\x26astart\x3d4110'" type="button">
                tmp = bs.find('button',{'class':'gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx'})
                url = re.sub('window\.location=|\'','',tmp['onclick'])
                url = re.sub('\\\\x3d','=',url)
                url = re.sub('\\\\x26','&',url)
                url = 'https://scholar.google.jp' + url
                bRet = True
            else:
                if ii == 0:
                    url = ourl 
                if bRet or ii == 0:
                    #chopt = Options()
                    #chopt.add_argument("--headless") # headless mode
                    #driver = webdriver.Chrome(executable_path='./chromedriver',options=chopt) # locate appropriate webdriver in the executable-file directory
                    egopt = Options()
                    egopt.add_argument('headless')
                    driver = webdriver.Edge(executable_path='./msedgedriver',options=egopt) # locate appropriate webdriver in the executable-file directory
                    driver.get(url)
                    time.sleep(stime)
                    bs = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                    tmp = bs.find('button',{'class':'gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx'})
                    url = re.sub('window\.location=|\'','',tmp['onclick'])
                    url = re.sub('\\\\x3d','=',url)
                    url = re.sub('\\\\x26','&',url)
                    url = 'https://scholar.google.jp' + url
                    bRet = True
                    with open(fname, mode='w') as f:
                        f.write(str(bs.prettify()))
                else:
                    a_item = driver.find_element(By.CSS_SELECTOR, '[aria-label="次へ"]')
                    a_item.click()
                    time.sleep(stime)
                    bs = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                    with open(fname, mode='w') as f:
                        f.write(str(bs.prettify()))
                    bRet = False
            names = bs.find_all('h3',{'class':'gs_ai_name'})
            affs = bs.find_all('div',{'class':'gs_ai_aff'})
            cits = bs.find_all('div',{'class':'gs_ai_cby'})
            for jj in range(0,len(names)):
                name.append(re.sub('\n|\s\(.+?\)|\(.+?\)|\s\(.+?）|\s（.+?）|（.+?）$','',names[jj].get_text().strip()))
                af = affs[jj].get_text().strip()
                af = re.sub('.*Professor.*, |.*Professor.* of .+?, |.*Professor.* of |, .*Professor|\s*\(.+?\)\s*|.+? at |.*Scientist, |.*Researcher, |.*Engineering, |.*Science, |Group, |.*Robotics, |.*Vision, |, CEO|, Founder','',af).strip()
                aff.append(af)
                citation.append(int(re.sub('被引用数: ','',cits[jj].get_text())))
        
        normal = True
        return normal, name, aff, citation

    def GscholarInd(self, nmlist):
        normal = False
        nmindcite = {}

        for nm in nmlist:
            nmindcite[nm] = 0

            gfname = re.split('\s',nm)
            if len(gfname)==2:
                cname = f'{gfname[0][0]} {gfname[1]}'
                url = f'https://scholar.google.jp/citations?hl=ja&view_op=search_authors&mauthors={gfname[0]}+{gfname[1]}&btnG='
            elif len(gfname)==3:
                cname = f'{gfname[0][0]}{gfname[1][0]} {gfname[2]}'
                url = f'https://scholar.google.jp/citations?hl=ja&view_op=search_authors&mauthors={gfname[0]}+{gfname[1]}+{gfname[2]}&btnG='

            fname = self.cachedir + "/" + re.sub("[\:\/\.]","_",url) + ".txt"
            bs = self.selenium(url,fname)

            nmpart = bs.find('h3',{'class':'gs_ai_name'})
            linksuf = nmpart.find('a').get('href')

            url = f'https://scholar.google.jp{linksuf}'
            fname = self.cachedir + "/" + re.sub("[\:\/\.]","_",url) + ".txt"
            #print(f'{nm}: {url}')
            bs = self.selenium(url,fname)

            cpart = bs.find('div',{'class':'gsc_lcl gsc_prf_pnl'})
            pubs = cpart.find_all('tr',{'class':'gsc_a_tr'})
            for pub in pubs:
                npart = pub.find('div',{'class':'gs_gray'}).get_text().strip()
                if re.match(cname,npart,flags=re.IGNORECASE):
                    tmp = pub.find('td',{'class':'gsc_a_c'}).get_text().strip()
                    try:
                        nmindcite[nm] = int(re.search('^([0-9]+)',tmp).group())
                    except:
                        print(tmp)
                    break

        normal = True
        return normal, nmindcite
