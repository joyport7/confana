#!/usr/bin/env python
# coding: utf-8
import re


class parseNAClist:
    def __init__(self, *args):
        if len(args) <= 2:
            print('parseATlist should be initialized with at least two parameters')
        elif len(args) == 3:
            self.name_list = args[0]
            self.aff_list = args[1]
            self.cite_list = args[2]
        else:
            print('too many inputs for initialization')
        self.sjppat="^([AIUEO]|[BGKMNPR][aiueoAIUEO]|[BGKMNPR][yY][auoAUO]|D[aeoAEO]|S[aueoAUEO]|S[hH][aiouAIOU]|T[aeoAEO]|T[sS][uU]|Z[aueoAUEO]|Y[auoAUO]|\
H[aieoAIEO]|HY[auoAUO]|J[aiuoAIUO]|J[y][auoAUO]|C[hH][aiuoAIUO]|D[aeoAEO]|W[aA]|F[uU])\
([\s'nmhtkNMHTK]|[aiueoAIUEO]|([bgkmnprBGKMNPR]|[kK][kK]|[mM][mM]|[nN][nN]|[pP][pP])[aiueoAIUEO]|([bgkmnprBGKMNPR]|[kK][kK]|[mM][mM]|[nN][nN]|\
[pP][pP])[yY][auoAUO]|[dD][aeoAEO]|([sS]|[sS][sS])[aueoAUEO]|([sS]|[sS][sS])[hH][aiouAIOU]\
|([tT]|[tT][tT])[aeoAEO]|([tT]|[tT][tT])[sS][uU]|[zZ][aueoAUEO]|[yY][auoAUO]|[hH][aieoAIEO]|[hH][yY][auoAUO]|[jJ][aiuoAIUO]|[jJ][y][auoAUO]|([cC]|[cC][cC])[hH][aiuoAIUO]|[dD][aeoAEO]|[wW][aA]|[fF][uU]|[AIUEOKSTNHMYRW]\.)*?$"
        self.snjpwpat="[^n]'|-|[QXVqxv]|[áčçøåÅÇØ]|[^aiueontkh\.]\s|[^aiueontkh]$|nn\s|nn$|\
[aA]er|ahn|[bBjJ]iao|[bB]odo|([cC]h|[bdjBDJ])ae|[cC]hoe|[eE]ui|[eE]un|eau|[fF][ieo]|[hH]ao|Hee|[hH]oai|[hH]yun|[hH]yuk|Joon|[yY]oun|guk|[jJ]ia|[hH]ua|Niu|[jJ]ie[^in]|[hkgHKG]yun|nea|\
[sS]hui|rian|[sSgG]uo|[sS]eo[nk]|[sS]han|[sS]eung|[sS]huai|uan|\
([fF][yY]u)an$|\
[rsy]ani|rini|gudo|[zZ]ere|[kK]ede|[aA]hn|\
[bdfghjklmpqrvwxyzBCDFGHJKLMPQRTVWXYZ][bcdfgjklmpqrtvwxz]|c[^h]|[tT][^aeos]|s[^aueoh]|[sS]h[^aiuo]|[tT]s[^u]|[in]h$|[jJ]as"
        self.snjpgpat="\
(([JN]|Sh|Ch)i|Bin|[GKd]e|Bo|Hai|[TH]ao|Bei|Ku[in]|\
Aakanksha|Aa*ron|Akanksha|Amanda|Ameya|Ami[tn]|Anita|Anki|Ankita|Annika|Anton|Antoine*|Antonio|Anuja|Aran|Arya|Arun|Aida|Aren|Arezou|Aria|Aryan|Ata|\
Bao|Babak|Bee|Beibei|Benjamin|Bodo|Bojan|Burak|Bukun|Burin|\
Chaehun|Chajin|Chanjin|Chau|Chiara|Da|Dakai|Dami[ae]n|Dann*a|Dario|Debora|Depanshu|Dohwan|Dominik|Dongoh|Doreen|Doron|\
Erik|Ehsan|Eshaan|Eugene|Ewa|Eze|Gene|Gyumin|Gunawan|Haechan|Haian|Han|Hanbin|Hani|Hanna|Hannah|Hasan|Heiko|Henri|Hogun|\
Inkyu|Itai|Isha|Jamie|Jan|Jane|Janne|Jason|Jikai|Jimin|Jirak|Jose|John|Joao|Joko|Joni|Ju|Junni|Juho|Juhee|Junho|Junhyuk|\
Kaan|Kannan|Kanika|K[ai]ran|Kate|Kenan|Kenneth|Kiana|Kien|Koushik|Leda|Lorenzo|\
Maatei|Madonna|Mainak|Man|Manikanta|Marion|Masha|Matan|Mateja|Matt|Mayank|Mazen|Masoumeh|Meena|Meike|Mengu|Menoua|Miao|Mihai|Min|Minho*|Minji|Min[jJ]oon|Min[jJ]un*|Minsu|Minkyo|Mubarak|Moein|Mohi|Mohsen|Monika|Moon|Moonsoo|Moran|Mouna|\
Nageen|Namo|Nariman|Neha|Nikita|Nima|Nirat|Nooshin|\
Okan|Oren|Ori|Oladayo|Osama|Oya|Pere|Pouya|Pu|Ramana|Rami|Ranjan|Renshuai|Reuben|Reza|Rishi|Ruben|Rohit|Roi|Ruwan|Ruhi|Ryan|\
Sachin|Sage|Sanchari|Saikat|Sandaru|Saman|Sami|Samitha|Samira|Sarah|Sayan|Sean|Seba|Sek|Sen|Shagan|Shaurya|Shasha|Shayak|Shayan|Shai|Shichao|Shishira|Shujon|Soomin|Suman|Suranjana|Suren|Sunita|Taha|Taman|Tanaya|Tapani|Teresa|Tarasha|\
Udana|Wah|Yan|Yani|Yanrui|Yangyu|Yaochu|Yasaman|Yohan|Yuanbiao|Yue|Yun|Yunmo|Yuru|Yunhao|Zarena|Zarana|Zerui|Zeyu)"
        self.snjpfpat="\
((Ch|N)a|(Ch|Sh|[YSHFOLGMB])[uo]|[YSHFOLGMKZ]e|[EH]o|An|([TYHGW]|[BDL]|Shu)ai|[BGHYMR]ao|([YRG]u|Ch|[LYHTWGNM])an|[BNJ]i|Jia|[JM]iao|[GS]ui|[YS]un|[KGZ]uo|[LM]ei|Heo|[YH]ou|Choi|Yoo|Yoon|\
Aakanksha|Achan|Arora|Ahuja|Aksak|Akshara|Amani|Amini|Aminzadeh|Amit|Amin|Antebi|Aran|Ariyanto|Aryan|\
Badea|Basu|Bilen|Bahadori|Bandara|Bauza|Ben|Benton|Benjamin|Benson|Bera|Bian|Bin|Bok|Boneh|Bouma|Bouman|Bui|Chai|Cho[ou]|Chi|\
Desai|Dami[ae]n|Damak|Damaine|Dewan|Do|Dorent|Eak|Egiazarian|Emonet|Erat|Esen|Gat|Gia|Gianchandani|Gu|Guha|Guhan|Guedon|\
Ha|Hariyono|Hakimi|Hanna|Hansen|Heidari|Himayat|Huh|Hui|Huo|Ho|Ie|Imani|Jagadeesan|Jahani|Jain|Jaipuria|Jamnik|Janda|Jansen|Jayasuriya|Juge|John|Johnson|Joo|Joshi|Ju|Junge|\
Kahn|Kahnsari|Kate|Kazemi|Kee|Keshishian|Khurana|Ki|Kiani|Kijak|Kishore|Koren|Koo|Kunze|\
Laina|Ma|Madan|Maiya|Maman|Mania|Mangoubi|Maniat|Mannone|Manzanera|Masera|Mason|Masoomi|Mazaheri|Min|Mingyu|Miolane|Miranda|Memari|Men|Mohan|Mok|Moniri|Monteiro|Moore|\
Nabizadeh|Narayan|Narayanan|Neeman|Nayak|Nabi|Naik|Natarajan|Naowarat|Nauta|Nichani|Nizan|Neumann|Ngo|Noh|Nowara|\
Oh|Ohana|Oza|Pai|Pajarinen|Pan|Parekh|Pateraki|Pei|Pepik|Podee|Popa|Poranne|Pore|Poria|Potapenko|Potechin|Pu|Puri|\
Ra|Rai|Raja|Rajan|Rajawat|Rakhsha|Ramamohanarao|Ramyaa|Ran|Rana|Rane|Rau|Raket|Rakshit|Razazadeh|Razaei|Razani|Razaei|Rohani|Reinke|Ren|Riba|Ridao|Roh|Rouhani|Ruta|Ruben|Ryu|\
Sabo|Sah|Saria|Saporito|Saenko|Saha|Sain|Saini|Samano|Samangouei|Samanta|Samara.+?|Saket|Sani|Saran|Sarawagi|Shabanian|Shah|Shakeri|Shayani|Shi|Shin|Shou|Shoaran|Sohn|Souza|Suh|Sukan|Sundararaman|Suri|Susan|Suin|Tandon|Tonekabori|\
Wanchoo|Watson|Yaesoubi|Yogatama|Yoran|Yue|Yu[ae]n|Zada|Zabih|Zadeh|Zaharia|Zontak|Zou)"
        self.snjpname="Jin\sJin|Ran\sTao|Ran\sBen|Yuhe\sJin|Jin\sTao|Yu\sTao|Jan\sKotera|Ken\sMai|Meina\sKan|Jinko\sKanno|Rui\sTao"
        self.snjppat="^"+self.snjpgpat+"\s|\s"+self.snjpfpat+"$|"+self.snjpname 
        self.dlm=",\s"

    def isJP(self,name):
        ret = False
        if re.search(self.sjppat,name,flags=re.IGNORECASE):# jp-like name
            if not re.search(self.snjpwpat,name,flags=re.IGNORECASE):#non-jp-like
                if not re.search(self.snjppat,name,flags=re.IGNORECASE):#non-jp name
                    ret = True
        return ret
    
    def isJPlike(self,name):
        ret = False
        if re.search(self.sjppat,name,flags=re.IGNORECASE):# jp-like name
            if not re.search(self.snjpwpat,name,flags=re.IGNORECASE):#non-jp-like
                ret = True

        return ret

    def isJPgiven(self,name):
        ret = False
        if re.search(self.sjppat,name,flags=re.IGNORECASE):
            if not re.search(self.snjpwpat,name,flags=re.IGNORECASE):
                if not re.search('^'+self.snjpgpat+'$',name,flags=re.IGNORECASE):
                    ret = True
        return ret
    
    def isJPfamily(self,name):
        ret = False
        if re.search(self.sjppat,name,flags=re.IGNORECASE):
            if not re.search(self.snjpwpat,name,flags=re.IGNORECASE):
                if not re.search('^'+self.snjpfpat+'$',name,flags=re.IGNORECASE):
                    ret = True
        return ret
        
    def isJPname(self,name):
        ret = False
        if not re.search('^'+self.snjpname+'$',name,flags=re.IGNORECASE):
            ret = True
        return ret

    def selectJP(self):
        jpname = []
        jpaff = []
        jpcite = []
        numjp = 0

        
        for ii in range(0,len(self.name_list)):
            jpp = False
            name = self.name_list[ii]
            if self.isJPlike(name):
                names = re.split('\s',name)
                if len(names) == 2:
                    if self.isJPgiven(names[0]):
                        if self.isJPfamily(names[1]):
                            if self.isJPname(name):
                                numjp += 1
                                jpname.append(name)
                                jpaff.append(self.aff_list[ii])
                                jpcite.append(self.cite_list[ii])
                                jpp = True
                elif len(names) == 3:
                    if self.isJPgiven(names[0]):
                        if self.isJPfamily(names[2]):
                            if self.isJPname(name):
                                numjp += 1
                                jpname.append(name)
                                jpaff.append(self.aff_list[ii])
                                jpcite.append(self.cite_list[ii])
                                jpp = True

        return jpname, jpaff, jpcite, numjp

