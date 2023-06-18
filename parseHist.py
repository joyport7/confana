#!/usr/bin/env python
# coding: utf-8

import matplotlib.pylab as plt


class parseHist:
    def __init__(self,param,histall):
        self.param = param
        self.histall = histall
        
    def plotsorted(self):
        # dictionary to list conversion with sorting by year
        sumhist, detail = [], []
        for author in self.histall.keys():
            for year in range(self.param.yearFrom,self.param.yearTo,self.param.interval):
                yr = str(year)
                if yr not in self.histall[author].keys():
                    self.histall[author][yr] = 0
            myList = sorted(self.histall[author].items(), key = lambda x:x[0])
            x, y = zip(*myList)
            sumhist.append(sum(y))
            detail.append([author,sum(y),y])

        # sorting by total number of publications
        indices = [*range(len(sumhist))]
        sorted_indices = sorted(indices, key = lambda ii: -sumhist[ii])
        sumhist = [sumhist[ii] for ii in sorted_indices]
        detail = [detail[ii] for ii in sorted_indices]
        
        for ii in range(0,len(sumhist)):
            print(f'{detail[ii][0]}\t{detail[ii][1]}')

        # filtering of the list to plot
        show_indices = []
        for ii in range(0,len(sumhist)):
            if sumhist[ii] >= self.param.toShow:
                show_indices.append(ii)

        # output and plot of the results
        #print([detail[ii] for ii in show_indices])
        fig = plt.figure()
        for ii in show_indices:
            plt.plot(x, detail[ii][2],label = detail[ii][0:2])
        plt.grid()
        plt.legend(loc = (1.1, 0), ncol = 3)
        fig.savefig("test.png")
        plt.show()        
