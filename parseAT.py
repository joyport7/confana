#!/usr/bin/env python
# coding: utf-8
import re
from .jpnm import jpnm

class parseATlist:
    def __init__(self, *args):
        if len(args) == 1:
            print('parseATlist should be initialized with at least two parameters')
        elif len(args) ==2:
            self.num_papers = len(args[0])
            self.title_list = args[0]
            self.author_list = args[1]
        else:
            print('too many parameters for initialization')

    def selectJP(self):
        jpauthor = []
        jptitle = []
        numjppaper = 0
        numallauthors = 0
        numjpauthors = 0
        numallpapers = len(self.title_list)
        verbose = False

        jn = jpnm()
        
        for ii in range(0,self.num_papers):
            ttl = self.title_list[ii]
            jpp = False
            for au in self.author_list[ii]:
                numallauthors += 1
                if jn.check(au,verbose):
                    numjpauthors += 1
                    jpauthor.append(au)
                    jptitle.append(ttl)
                    jpp = True

            if jpp:
                numjppaper += 1
                
        return jpauthor, jptitle, numallauthors, numjpauthors, numallpapers, numjppaper

    def makehist(self,authors,yr):
        """make a histgram consisting of author x yr dictionary """
        hist = {}
        for author in authors:
            if author in hist.keys():
                if yr in hist[author].keys():
                    hist[author][yr] += 1
                else:
                    hist[author][yr] = 1
            else:
                hist[author] = {yr:1}
        return hist
    
    def mergehist(self,histall,hist,yr):
        if histall == {}:
            histall = hist
        else:
            for author in hist.keys():
                if author in histall.keys():
                    if yr in histall[author].keys():
                        histall[author][yr] += hist[author][yr]
                    else:
                        histall[author][yr] = hist[author][yr]
                else:
                    histall[author] = {yr:hist[author][yr]}

        return histall
    



