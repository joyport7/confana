#!/usr/bin/env python
# coding: utf-8
import re
from .jpnm import jpnm


class parseNAClist:
    def __init__(self, *args):
        self.tcvlst = 'Sato Imari|Okatani Takayuki|Shouno Hayaru|Shuuji Shuuji|Okada Hiroyuki|Endo Gen|YAMADA Tomohiro|\
Obinata Goro|Ohya Akihisa|Nagata Fusaomi|Miyoshi Tasuku|Fukui Rui|Sugaya Midori|Takeuchi Ichiro|SHIMIZU Shohei|Suzuki Joe|\
Kawakami Kazuya|Akiyama Yutaka|Nagao Tomoharu|Kobayashi Hirofumi'

        if len(args) <= 2:
            print('parseATlist should be initialized with at least 4 parameters')
        elif len(args) == 4:
            self.name_list = args[0]
            self.nm_link = args[1]
            self.aff_list = args[2]
            self.cite_list = args[3]
            self.name_list = self.convertname(self.name_list)
        else:
            print('too many inputs for initialization')
        

    def selectJP(self):
        jpname = []
        jplink = []
        jpaff = []
        jpcite = []
        numjp = 0
        verbose = False

        jn = jpnm()

        for ii in range(0,len(self.name_list)):
            name = self.name_list[ii]
            if jn.check(name,verbose):
                numjp += 1
                jpname.append(name)
                jplink.append(self.nm_link[ii])
                jpaff.append(self.aff_list[ii])
                jpcite.append(self.cite_list[ii])

        return jpname, jplink, jpaff, jpcite, numjp
    
    def convertgf(self,name):
        nms = re.split('\s',name)
        return nms[1] + ' ' + nms[0]

    def convertname(self,nms):
        for ii in range(0,len(nms)):
            nm = nms[ii]
            if re.search(self.tcvlst,nm):
                nms[ii] = self.convertgf(nm)
        return nms
