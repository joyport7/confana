#!/usr/bin/env python
# coding: utf-8
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from selenium.webdriver.chrome.options import Options
import time
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#import chromedriver_binary

class parseUrl:
    def __init__(self, *args):
        if len(args)==2:
            self.site = args[0]
            self.conf = args[1]
    
    def selenium(self,url):

        try:
            time_s = time.time()
            
            fname = re.sub("[\:\/\.]","_",url) + ".txt"
            if os.path.isfile(fname):
                with open(fname, encoding='utf-8') as f:
                    bs = BeautifulSoup(f.read(), 'html.parser')
            else:
                opt = Options()
                opt.add_argument("--headless") # headless mode
                #driver = webdriver.Edge(options = opt,executable_path='/Users/jp29130/Documents/codes/common/msedgedriver')
                driver = webdriver.Edge(executable_path='/Users/jp29130/Documents/codes/common/msedgedriver')
                driver.get(url)
                time.sleep(10)
                bs = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                #print(driver.page_source)
                with open(fname, mode='w') as f:
                    f.write(str(bs.prettify()))
            time_e = time.time()
            etime = time_e - time_s
            print("elapsed time: {0:.2f}".format(etime))
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
        """
        ii = 0
        for line in ddlines:
            contentline = line.get_text()
            contentline = re.sub('[^A-z,][\s\n]+','',contentline)
            contentline = re.sub('\n','',contentline)
            if contentline[0:5] == '[pdf]':
                pass
            elif re.search('[Bb]ack$',contentline):
                pass
            elif re.search('[Bb]ack\]*$',contentline):
                pass
            else:
                author.append(re.split(',',contentline))
                try:
                    title.append(titles[ii].get_text())
                    ii += 1
                except:
                    print(f'failed:{contentline}')
                    print(titles[ii-1].get_text())
        """
        
        #for ii in range(0,len(titles)):
        #    print(author[ii],titles[ii])
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
            #if url[0]==2022:
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
            #print(ttlidx, ':', session, '\t', ttl)
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


