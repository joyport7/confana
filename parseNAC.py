#!/usr/bin/env python
# coding: utf-8
import re


class parseNAClist:
    def __init__(self, *args):
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
        
        #Rina Kumari
        self.sjppat="^([AIUEO]|[BGKMNPR][aiueoAIUEO]|[BGKMNPR][yY][auoAUO]|D[aeoAEO]|S[aueoAUEO]|S[hH][aiouAIOU]|T[aeoAEO]|T[sS][uU]|Z[aueoAUEO]|Y[auoAUO]|\
H[aieoAIEO]|HY[auoAUO]|J[aiuoAIUO]|J[y][auoAUO]|C[hH][aiuoAIUO]|D[aeoAEO]|W[aA]|F[uU])\
([\s'nmhtkNMHTK]|[aiueoAIUEO]|([bgkmnprBGKMNPR]|[kK][kK]|[mM][mM]|[nN][nN]|[pP][pP])[aiueoAIUEO]|([bgkmnprBGKMNPR]|[kK][kK]|[mM][mM]|[nN][nN]|\
[pP][pP])[yY][auoAUO]|[dD][aeoAEO]|([sS]|[sS][sS])[aueoAUEO]|([sS]|[sS][sS])[hH][aiouAIOU]\
|([tT]|[tT][tT])[aeoAEO]|([tT]|[tT][tT])[sS][uU]|[zZ][aueoAUEO]|[yY][auoAUO]|[hH][aieoAIEO]|[hH][yY][auoAUO]|[jJ][aiuoAIUO]|[jJ][y][auoAUO]|([cC]|[cC][cC])[hH][aiuoAIUO]|[dD][aeoAEO]|[wW][aA]|[fF][uU]|[AIUEOKSTNHMYRW]\.)*?$"
        self.snjpwpat="[^n]'|-|[qxv]|[áčçøåÅÇØ]|[^aiueontkh\.][\s$]|nn[\s$]|\
aer|ahn|[bjr]iao|riao|bodo|(ch|[bdj])ae|choe|eu[in]|eau|f[ieo]|hao|[bh]ee|hoai|oao|[jmys]oon|papi|pine|shore|dani|doo|guru|suchi|doan|saima|aitao|banjan|aharo|oee|chink|joan|deon|\
janna|ce|el|zaa|che|yau|rohan|adeka|adegu|yi|rabi|jade|nanya|pant|jau|inigo|nue|aushik|gopan|pak|z[ea]he|ahoo|shuman|patt|naik|teimo|kia|pika|ksh|chitt|shiha|yuni|saini|\
[hkg]yu[nk]|youn|guk|jia|hua|jie[^in]|nea|ksha|anton|bao|boja|debo|narayana|sundara|ram|rosen|baum|hasson|parat|moetes|poo|rissa|redd|opuri|pere|asank|zahid|june|aisha|teoh|iang|\
jas|jaso|jau|joko|john|jose|juho|jung|joua|shu[ioa]|rian|[sg]uo|seo[nk]|shan|eun[gk]|shai|shaha|naseri|njiza|tteo|zeika|gaga|charya|gaja|mohan|raja|mohana|domi|pou|baie|gudo|zere|tonya|akya|engyu|hyoji|nisha|mora|zade|ryan|pita|tanyu|nyuk|dorai|habi|biba|bukh|\
[bdfghjklmpqrvwxyz][bcdfgjklmpqrtvwxz]|c[^h]|t[^taeos]|s[^saueoh]|ss*h[^aiuo]|tt*s[^u]|m[^bdpaiueo]|[tk]h$|[in]h$|[rsyn][ai]ni$|haran$|dat$|bot$|[ds]ah$|neh|[ds]eem$|r*[jy]an$|rek$|to[rs]o$|daan$|ksha$|rak[\s$]|sen$|nen$|sek[\s$]|[fy]uan$|uri[\s$]"
        self.snjpgpat="\
(([JN]|Sh|Ch)i|Bin|[GKd]e|Bo|Hai|[TH]ao|Bei|Ku[in]|\
Aa*ron|Abayomi|Aman|Amanda|Ameya|Annan|Ami[tn]|Anita|Anki|Ankita|Annika|Antoine*|Anuja|Aran|Arya|Arun|Aida|Aren|Arezou|Aria|Aryan|Ata|\
Bao|Babak|Bee|Beibei|Benaim|Benjamin|Bodo|Bojan|Burak|Bukun|Burin|\
Chaehun|Chajin|Chanjin|Chau|Chiara|Da|Dakai|Dami[ae]n|Dann*a|Dario|Debora|Depanshu|Dohwan|Dominik|Dongoh|Doreen|Doron|\
Ebuka|Edo|Erik|Ehsan|Eshaan|Eugene|Ewa|Eze|Gene|Gyumin|Gunawan|Haechan|Haian|Han|Hanbin|Hani|Hanna|Hannah|Hasan|He|Heiko|Henri|Hogun|Hooman|\
Inkyu|Imin|Itai|Isha|Jamie|Jan|Jane|Janne|Jason|Jikai|Jina|Jimin|Jirak|Jose|Johan|John|Joao|Joko|Joni|Ju|Juan|Junni|Juho|Juhee|Junho|Junhyuk|\
Kaan|Kannan|Kanika|K[ai]ran|Kate|Kenan|Kenneth|Kiana|Ki[ae]n|Kochise|Koushik|Leda|Lorenzo|\
Maatei|Matteo|Madonna|Mainak|Man|Manikanta|Marek|Marion|Masha|Matan|Mateja|Matt|Mayank|Mazen|Masoumeh|Meena|Meike|Mengu|Menoua|Miao|Mihai|Min|Minho*|Minji|Min[jJ]oon|Min[jJ]un*|Minsu|Minkyo|Mubarak|Moein|Mohi|Mohsen|Moin|Monika|Moon|Moonsoo|Moran|Mouna|Musa|\
Nageen|Namo|Nariman|Neha|Nikita|Nima|Nirat|Nona|Nooshin|Nuno|\
Okan|Oren|Ori|Oladayo|Osama|Oya|Pere|Pouya|Pu|Ramana|Rami|Ranjan|Renshuai|Reuben|Reza|Rishi|Ruben|Rohit|Roi|Ruwan|Ruhi|Ryan|\
Sachin|Sage|Sagie|Sanchari|Saikat|Sandaru|Saman|Sami|Samitha|Samira|Sarah|Sayan|Sean|Seba|Sek|Sen|Shagan|Shaurya|Shasha|Shayak|Shayan|Shai|Shichao|Shirine|Shishira|Shujon|Soomin|Sun|Suman|Suranjana|Suren|Sunita|Taha|Taman|Tanaya|Tapani|Teresa|Tarasha|\
Udana|Wa[hi]|Yan|Yani|Yanrui|Yangyu|Yaochu|Yasaman|Yohan|Yuanbiao|Yue|Yun|Yunmo|Yuru|Yunhao|Zarena|Zarana|Zerui|Zeyu)"
        self.snjpfpat="\
((Ch|N)a|(Ch|Sh|[YSHFOLGMB])[uo]|[YSHFOLGMKZ]e|[EH]o|An|([TYHGW]|[BDL]|Shu)ai|[BGHYMR]ao|([YRG]u|Ch|[LYHTWGNM])an|[BNJ]i|Jia|[JM]iao|[GS]ui|[YS]un|[KGZ]uo|[LM]ei|Heo|[YH]ou|Choi|Yoo|Yoon|\
Aakanksha|Achan|Acharya|Arora|Ahuja|Aksak|Akshara|Amani|Amini|Aminzadeh|Amit|Amin|Aneke|Antebi|Aran|Ariyanto|Aryan|\
Ba|Badea|Basu|Bilen|Bahadori|Bandara|Bauza|Ben|Bennett|Benton|Benjamin|Benson|Bera|Bian|Bianchi|Bin|Bok|Boneh|Bouma|Bouman|Bui|Chai|Cho[ou]|Chi|\
Dagan|Desai|Dami[ae]n|Damak|Damaine|Dewan|Do|Dorent|Doshi|Eak|Egiazarian|Emonet|Erat|Esen|Gat|Gia|Gini|Gianchandani|Gu|Guha|Guhan|Guedon|\
Ha|Hanan|Hariyono|Hakimi|Hanna|Hansen|Heidari|Himayat|Huh|Hui|Huo|Ho|Ie|Imani|\
Jagadeesan|Jahani|Jain|Jaipuria|Jamnik|Janda|Jansen|Jayasuriya|Juge|John|Johnson|Joo|Joshi|Ju|Junge|\
Kao|Kahn|Kahnsari|Kate|Kazemi|Kee|Keshishian|Khurana|Ki|Kiani|Kijak|Kim|Kishore|Koren|Koo|Kunze|Kumar|\
Laina|Ma|Madan|Maiya|Maman|Mania|Mangoubi|Maniat|Mannone|Manzanera|Masera|Mason|Masoomi|Mazaheri|Menna|Mi|Min|Minu|Mingyu|Miolane|Miranda|Memari|Men|Mohan|Mok|Moniri|Monteiro|Moore|Mozeika|Munaro|Munjiza|\
Nabizadeh|Narayan|Narayanan|Neeman|Nayak|Nabi|Naik|Natarajan|Naowarat|Nauta|Nichani|Nizan|Neumann|Ngo|Noh|Nona|Nowara|\
Oh|Ohana|Omena|Oza|Pai|Pajarinen|Pan|Parekh|Pateraki|Pei|Pepik|Podee|Popa|Poranne|Pore|Poria|Potapenko|Potechin|Pu|Puri|\
Ra|Rai|Raja|Rajan|Rajawat|Rakhsha|Ramamohanarao|Ramyaa|Ran|Rana|Rane|Rau|Raket|Rakshit|Razazadeh|Razaei|Razani|Razaei|Rohani|Reinke|Ren|Riba|Ridao|Roh|Rouhani|Ruta|Ruben|Ryu|\
Sabo|Sah|Saria|Saporito|Saenko|Saha|Sain|Saini|Saman[oi]|Samangouei|Samanta|Samara.+?|Saket|Sani|Saran|Sarawagi|Shabanian|Shah|Shakeri|Shayani|Shi|Shin|Shou|Shoaran|Sohn|Souza|Suh|Sukan|Sundararaman|Suri|Susan|Suin|Tandon|Tonekabori|\
Wanchoo|Watson|Yaesoubi|Yogatama|Yoran|Yu[eh]|Yu[ae]n|Zada|Zabih|Zadeh|Zaharia|Zontak|Zou)"
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
        jplink = []
        jpaff = []
        jpcite = []
        numjp = 0
        
        for ii in range(0,len(self.name_list)):
            name = self.name_list[ii]
            name = re.sub("  "," ",name)
            #tmp = re.search('[^/]+(?= /)',name)
            #if tmp:
            #    name = tmp.group()

            gfname = re.split('\s',name)
            if len(gfname) == 2:
                if self.isJPlike(gfname[0]+" "+gfname[1]):
                    if self.isJPgiven(gfname[0]):
                        if self.isJPfamily(gfname[1]):
                            if self.isJPname(name):
                                numjp += 1
                                jpname.append(name)
                                jplink.append(self.nm_link[ii])
                                jpaff.append(self.aff_list[ii])
                                jpcite.append(self.cite_list[ii])
            elif len(gfname) == 3:
                if self.isJPlike(gfname[0]+" "+gfname[2]):
                    if self.isJPgiven(gfname[0]):
                        if self.isJPfamily(gfname[2]):
                            if self.isJPname(name):
                                numjp += 1
                                jpname.append(name)
                                jplink.append(self.nm_link[ii])
                                jpaff.append(self.aff_list[ii])
                                jpcite.append(self.cite_list[ii])

        return jpname, jplink, jpaff, jpcite, numjp

    def convertname(self,jpname):
        for ii in range(0,len(jpname)):
            nm = jpname[ii]
            if nm == 'Sato Imari':
                nm = 'Imari Sato'
            elif nm == 'Okatani Takayuki':
                nm = 'Takayuki Okatani'
            elif nm == 'Shouno Hayaru':
                nm = 'Hayaru Shouno'
            elif nm == 'Shuuji Shuuji':
                nm = 'Shuuji Shuuji'
            elif nm == 'Okada Hiroyuki':
                nm = 'Hiroyuki Okada'
            elif nm == 'Endo Gen':
                nm = 'Gen Endo'
            elif nm == 'YAMADA Tomohiro':
                nm = 'Tomohiro YAMADA'
            elif nm == 'Obinata Goro':
                nm = 'Goro Obinata'
            elif nm == 'Ohya Akihisa':
                nm = 'Akihisa Ohya'
            elif nm == 'Nagata Fusaomi':
                nm = 'Fusaomi Nagata'
            elif nm == 'Miyoshi Tasuku':
                nm = 'Tasuku Miyoshi'
            elif nm == 'Fukui Rui':
                nm = 'Rui Fukui'
            elif nm == 'Sugaya Midori':
                nm = 'Midori Sugaya'
            elif nm == 'Sugaya Midori':
                nm = 'Midori Sugaya'
            elif nm == 'Sugaya Midori':
                nm = 'Midori Sugaya'
            elif nm == 'Sugaya Midori':
                nm = 'Midori Sugaya'
            elif nm == 'Sugaya Midori':
                nm = 'Midori Sugaya'
            elif nm == 'Sugaya Midori':
                nm = 'Midori Sugaya'
            jpname[ii] = nm

        return jpname
