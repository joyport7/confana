#!/usr/bin/env python
# coding: utf-8
import os
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import re

class parseUrl:
    def __init__(self, *args):
        if len(args) == 1:
            self.site = args[0].site
            self.conf = args[0].conf_prefix
            self.cachedir = args[0].cachedir
        elif len(args) == 2:
            yr = args[1]
            self.site = args[0].site
            self.conf = args[0].conf_prefix + yr
            self.cachedir = args[0].cachedir
        
        if re.search('ICLR',self.conf):
            self.setICLRop()
        elif re.search('CoRL',self.conf):
            self.setCoRLop()
        elif re.search('NeurIPS',self.conf):
            self.setNeurIPSop()
        
        self.sltime = 5

    def egcap(self):
        capabilities = {
            "browserName": "MicrosoftEdge",
            "ms:edgeOptions": {
                "args": ["--headless"]
            }
        }
        return capabilities

    def setNeurIPSop(self):
        yr = re.search('[0-9][0-9][0-9][0-9]',self.conf)
        print(yr[0])
        if yr[0] == '2023':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'accept-oral'
            self.posterpt = 'accept-poster'
            self.slpt = 'accept-spotlight'
        elif yr[0] == '2022':
            self.oralheld = True
            self.slheld = False
            self.posterheld = False
            self.oralpt = 'accepted-papers'
            self.posterpt = ''
            self.slpt = ''
        elif yr[0] == '2021':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'oral-presentations'
            self.posterpt = 'poster-presentations'
            self.slpt = 'spotlight-presentations'

    def setICLRop(self):
        yr = re.search('[0-9][0-9][0-9][0-9]',self.conf)
        print(yr[0])
        if yr[0] == '2018':
            self.oralheld = True
            self.slheld = False
            self.posterheld = True
            self.oralpt = 'accepted-oral-papers'
            self.posterpt = 'accepted-poster-papers'
            self.slpt = ''
        elif yr[0] == '2019':
            self.oralheld = True
            self.slheld = False
            self.posterheld = True
            self.oralpt = 'oral-presentations'
            self.posterpt = 'poster-presentations'
            self.slpt = ''
        elif yr[0] == '2020':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'oral-presentations'
            self.posterpt = 'poster-presentations'
            self.slpt = 'spotlight-presentations'
        elif yr[0] == '2021':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'oral-presentations'
            self.posterpt = 'poster-presentations'
            self.slpt = 'spotlight-presentations'
        elif yr[0] == '2022':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'oral-submissions'
            self.posterpt = 'poster-submissions'
            self.slpt = 'spotlight-submissions'
        elif yr[0] == '2023':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'notable-top-5-'
            self.posterpt = 'poster'
            self.slpt = 'notable-top-25-'
        elif yr[0] == '2024':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'accept-oral'
            self.posterpt = 'accept-poster'
            self.slpt = 'accept-spotlight'
        elif yr[0] == '2025':
            self.oralheld = True
            self.slheld = True
            self.posterheld = True
            self.oralpt = 'accept-oral'
            self.posterpt = 'accept-poster'
            self.slpt = 'accept-spotlight'

    def setCoRLop(self):
        yr = re.search('[0-9][0-9][0-9][0-9]',self.conf)
        if yr[0] == '2021':
            self.oralheld = True
            self.slheld = False
            self.posterheld = True
            self.oralpt = 'accept--oral-'
            self.posterpt = 'accept--poster-'
            self.slpt = '-'
        elif yr[0] == '2022':
            self.oralheld = True
            self.slheld = False
            self.posterheld = True
            self.oralpt = 'accept--oral-'
            self.posterpt = 'accept--poster-'
            self.slpt = '-'
        elif yr[0] == '2023':
            self.oralheld = True
            self.slheld = False
            self.posterheld = True
            self.oralpt = 'accept--oral-'
            self.posterpt = 'accept--poster-'
            self.slpt = '-'

    def selenium_sub(self,url,pt):
        
        print(url)
        try:
            bs = []
            chopt = Options()
            #chopt.add_argument("--headless") # headless mode
            #driver = webdriver.Chrome(executable_path='./chromedriver',options=chopt) # locate appropriate webdriver in the executable-file directory
            capabilities = self.egcap()
            driver = webdriver.Edge(executable_path='./msedgedriver', capabilities=capabilities)
            driver.get(url)
            time.sleep(self.sltime)
            
            soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
            """
            fname = re.sub('[\:\/\?]','-',url) + '.txt'
            with open(fname, mode='w') as f:
                f.write(str(soup.prettify()))
            """
            bs.append(soup)
            a_item = driver.find_element(By.CSS_SELECTOR, ("div[id="+pt+"]"))
            elems = a_item.find_elements(By.TAG_NAME, ("nav"))

            if len(elems) != 0:
                a_item = elems[0]
                try:
                    a_items = a_item.find_elements(By.CLASS_NAME, ("right-arrow"))
                    max_page = int(a_items[1].get_attribute("data-page-number"))
                    print(max_page,' pages')
                    print(end='#')
                    for ii in range(1,max_page):
                        print(end='#')
                        a_item = driver.find_element(By.CSS_SELECTOR, ("div[id="+pt+"]"))
                        a_item = a_item.find_element(By.TAG_NAME, ("nav"))
                        a_item = a_item.find_element(By.LINK_TEXT, str(ii+1))
                        a_item.click()
                        time.sleep(self.sltime)
                        bs.append(BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser'))
                    print('\n')
                except:
                    a_items = a_item.find_elements(By.TAG_NAME, ("a"))
                    ii = 1
                    max_page = 1
                    while 1:
                        for it in a_items:
                            try:
                                pn = int(it.text)
                                if pn > max_page:
                                    max_page = pn
                            except:
                                pass
                        #print(end='#')
                        print(r'{0}/{1}'.format(ii,max_page))
                        if ii == max_page:
                            break
                        a_item = driver.find_element(By.CSS_SELECTOR, ("div[id="+pt+"]"))
                        a_item = a_item.find_element(By.TAG_NAME, ("nav"))
                        a_item = a_item.find_element(By.LINK_TEXT, str(ii+1))
                        a_item.click()
                        time.sleep(self.sltime)
                        bs.append(BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser'))
                        a_item = driver.find_element(By.CSS_SELECTOR, ("div[id="+pt+"]"))
                        elems = a_item.find_elements(By.TAG_NAME, ("nav"))
                        a_item = elems[0]
                        a_items = a_item.find_elements(By.TAG_NAME, ("a"))
                        ii += 1

        except WebDriverException as e:
            print("Error: ",e)

        finally:
            driver.quit()
        
        return bs

    def selenium(self):
        sltime = self.sltime
        #chopt = Options()
        #chopt.add_argument("--headless") # headless mode
        #driver = webdriver.Chrome(executable_path='./chromedriver',options=chopt) # locate appropriate webdriver in the executable-file directory
        capabilities = self.egcap()
        driver = webdriver.Edge(executable_path='./msedgedriver', capabilities=capabilities) # locate appropriate webdriver in the executable-file directory
        fname = self.cachedir + "/" + re.sub("[\:\/\.]","_",self.url) + ".txt"

        bs, bs_oral, bs_sl, bs_poster = None, None, None, None

        if re.search("ICLR|CoRL|NeurIPS",self.conf):
            oralheld, slheld, posterheld = (self.oralheld, self.slheld, self.posterheld)
            oralpt, slpt, posterpt = (self.oralpt, self.slpt, self.posterpt)

            yr = re.search('[0-9][0-9][0-9][0-9]',self.url)
            if yr[0] in ('2024','2025'):
                url_oral, url_sl, url_poster = tuple(self.url + '#tab-' + s for s in (oralpt, slpt, posterpt))
            else:
                url_oral, url_sl, url_poster = tuple(self.url + '#' + s for s in (oralpt, slpt, posterpt))

            if oralheld:
                bs_oral = self.selenium_sub(url_oral,oralpt)
            if slheld:
                bs_sl = self.selenium_sub(url_sl,slpt)
            if posterheld:
                bs_poster = self.selenium_sub(url_poster,posterpt)
        else:
            try:
                if os.path.isfile(fname):
                    with open(fname, encoding='utf-8') as f:
                        bs = BeautifulSoup(f.read(), 'html.parser')
                else:
                    driver.get(self.url)
                    time.sleep(sltime)
                    bs = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                    with open(fname, mode='w') as f:
                        f.write(str(bs.prettify()))
            except WebDriverException as e:
                print("Error: ",e)
            finally:
                driver.quit()

        return bs, bs_oral, bs_poster, bs_sl
            
    def beautifulsoup(self,url):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            print("Error: ",e)

        bs = BeautifulSoup(response.text, 'html.parser')
        return bs
    
    def parseCVFsite(self,url):
        normal = False
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
        normal = True
        return normal, author, title

    def parseCVF(self): 
        normal = False
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
        author, title = [], [] 
        
        print(url)
        bs = self.beautifulsoup(url)

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
            elif re.search("(MoAIP)|(MoBIP)|(TuAIP)|(TuBIP)|(WeAIP)|(WeBIP)|(MoSP)|(MoPL)|(TuSP)|(TuPL)|(WeSP)|(WePL)",session):
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
        return normal, author, title
    
    def IEEERAS(self,url):
        normal = False
        author, title = [], [] 

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

        return normal, author, title
 
    def parseACL(self,url):
        normal = False
        author, title = [], [] 

        #fname = re.sub("[\:\/\.]","_",url) + ".txt"
        #url = self.site
        print(url)
        bs = self.beautifulsoup(url)
        
        blks = bs.find_all('span',{'class':"d-block"})

        ii = 0
        for blk in blks:
            if ii < 2:
                ii += 1
                continue
            else:
                ii += 1
            ttl = blk.find('a',{'class':'align-middle'}).get_text().strip()
            if ttl == 'pdf':
                continue
            aublks = blk.find_all('a')
            authors = []
            jj = 0
            for aublk in aublks:
                if jj == 0:
                    jj += 1
                    continue
                else:
                    jj += 1
                au = aublk.get_text().strip()
                authors.append(au)
            title.append(ttl)
            author.append(authors)

        #with open(fname, mode='w') as f:
        #    f.write(str(bs.prettify()))
        
        normal = True
        return normal, author, title

    def parseOpenReview(self,url):
        normal = False
        title_list, author_list = [], []

        self.url = url
        bs, bs_orals, bs_posters, bs_sls = self.selenium()
        

        numoral = 0
        if self.oralheld:
            for ii in range(0,len(bs_orals)):
                oralblock = bs_orals[ii].find("div",{"id":self.oralpt})
                tts = oralblock.find_all("h4")
                aus = oralblock.find_all("div",{"class":"note-authors"})

                numoral += len(tts)
                for jj in range(0,len(tts)):
                    title_list.append(tts[jj].get_text().strip())
                    author_list.append(aus[jj].get_text().strip().split(', '))
                
        numsl = 0
        if self.slheld:
            for ii in range(0,len(bs_sls)):
                slblock = bs_sls[ii].find("div",{"id":self.slpt})
                tts = slblock.find_all("h4")
                aus = slblock.find_all("div",{"class":"note-authors"})

                numsl += len(tts)
                for jj in range(0,len(tts)):
                    title_list.append(tts[jj].get_text().strip())
                    author_list.append(aus[jj].get_text().strip().split(', '))
        
        numposter = 0
        if self.posterheld:
            for ii in range(0,len(bs_posters)):
                posterblock = bs_posters[ii].find("div",{"id":self.posterpt})
                tts = posterblock.find_all("h4")
                aus = posterblock.find_all("div",{"class":"note-authors"})

                numposter += len(tts)
                for jj in range(0,len(tts)):
                    title_list.append(tts[jj].get_text().strip())
                    author_list.append(aus[jj].get_text().strip().split(', '))

        
        normal = True
        return normal, author_list, title_list, numoral, numsl, numposter
    
    def Gscholar(self,maxpage):
        normal = False
        name, link, aff, citation = [], [], [], []
        ourl = self.site
        capabilities = self.egcap()

        bRet = False
        for ii in range(0,maxpage):
            print(ii)
            fname = self.cachedir + "/" + re.sub("[\:\/\.]","_",ourl) + "_" + str(ii) + ".txt"
            ftestname = self.cachedir + "/" + re.sub("[\:\/\.]","_",ourl) + "_" + str(ii) + "_test.txt"
            if os.path.isfile(fname):
                with open(fname, encoding='utf-8') as f:
                    bs = BeautifulSoup(f.read(), 'html.parser')
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
                    driver = webdriver.Edge(executable_path='./msedgedriver', capabilities=capabilities) # locate appropriate webdriver in the executable-file directory
                    driver.get(url)
                    time.sleep(self.sltime)
                    bs = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                    with open(ftestname, mode='w') as f:
                        f.write(str(bs.prettify()))
                    driver.quit()
 
                    tmp = tmp.find('button',{'class':'gs_btnPR gs_in_ib gs_btn_half gs_btn_lsb gs_btn_srt gsc_pgn_pnx'})

                    url = re.sub('window\.location=|\'','',tmp['onclick'])
                    url = re.sub('\\\\x3d','=',url)
                    url = re.sub('\\\\x26','&',url)
                    url = 'https://scholar.google.jp' + url

                    bRet = True

                    os.rename(ftestname,fname)

                else:
                    a_item = driver.find_element(By.CSS_SELECTOR, '[aria-label="次へ"]')
                    a_item.click()
                    time.sleep(self.sltime)

                    bs = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                    with open(fname, mode='w') as f:
                        f.write(str(bs.prettify()))
                    bRet = False
                    
            names = bs.find_all('h3',{'class':'gs_ai_name'})
            affs = bs.find_all('div',{'class':'gs_ai_aff'})
            cits = bs.find_all('div',{'class':'gs_ai_cby'})
            for jj in range(0,len(names)):
                name.append(re.sub('\n|\s\(.+?\)|\(.+?\)|\s\(.+?）|\s（.+?）|（.+?）$|\s\/.+','',names[jj].get_text().strip()))
                link.append(names[jj].find('a').get('href'))
                af = affs[jj].get_text().strip()
                af = re.sub('.*Professor.*, |.*Professor.* of .+?, |.*Professor.* of |, .*Professor|\s*\(.+?\)\s*|.+? at |.*Scientist, |.*Researcher, |.*Engineering, |.*Science, |Group, |.*Robotics, |.*Vision, |, CEO|, Founder','',af).strip()
                aff.append(af)
                citation.append(int(re.sub('被引用数: ','',cits[jj].get_text())))
        
        normal = True
        return normal, name, link, aff, citation

    def GscholarInd(self, names, nmlinks):
        normal = False
        nmindcite = {}

        for ii in range(0,len(names)):
            print(f'{ii}/{len(names)}')
            nm = names[ii]
            linksuf = nmlinks[ii]
            nmindcite[nm] = 0
            self.url = f'https://scholar.google.jp{linksuf}'
            print(self.url)
            bs = self.selenium()

            gfname = re.split('\s',nm)
            if len(gfname)==2:
                cname = f'{gfname[0][0]} {gfname[1]}'
            elif len(gfname)==3:
                cname = f'{gfname[0][0]}{gfname[1][0]} {gfname[2]}'

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

    def csvwrite(self,fname, *lists):
        with open(fname, 'w', encoding = "utf_8") as file:
            for items in zip(*lists):
                line = '\t'.join(str(item) for item in items) + '\n'
                file.write(line)
                