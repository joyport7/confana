#!/usr/bin/env python
# coding: utf-8
import re

class jpnm:
    def __init__(self):
        self.sjppat="^(([aiueo]h*|[kgnhbmr][aiueo]h*|s[aueo]h*|j[aiuo]h*|t[aieo]|[kmgr]*y[auo]h*|[cs]h[auio]h*|shi|tsu|wa|fu|d[aeo]|z[aueo]h*)n*t*[-' \.]*)+$"
        self.snjpwpat="[^n]['-]|[qxv]|[áčçøåÅÇØ]|[^aiueontkh\.][\s$]|nn[\s$]|[bdfghjklmpqrvwxyz][bcdfgjklmpqrtvwxz]|\
[bjr]iao|[bh]ee|[hjmys]oon|[hkg]yu[nk]|[aiueo]nton|[tk]h$|[in]h$|[rsyn][ai]ni$|[sg]uo|[ds]ah$|[ds]eem$|[fy]uan$|\
arirya|ankit|aibo|arien|amara|aisha|akya|abayo|ahoo|azuri|aushik|adeka|adegu|aer|ahn|ajaka|acha|aitao|aharo|asank|aison|aragon|\
baie|beriu|biran|baum|banjan|bagi|bao|bean|boja|bodo|bogi|biba|bukh|bot$|\
chau|chun|c[^h]|chana|charya|chaita|chitt|choo[ni]|chink|chad|choe|(ch|[bdj])ae|ce|che|\
datta|dorai|domi|debo|derya|dani|doo|doan|deon|deke|daan$|dat$|eu[in]|eau|eun[gk]|el|erank|engyu|ezra|eet|\
f[ieo]|giot|gaja|gauen|gopan|gaga|gene|geon|guru|guk|goo|gudo|gyao|hasson|haata|habi|hao|haran$|hoai|hua|hoang|hui[\s$]|hyoji|hojun|hoi|\
ir[ei][yn][ae]|inigo|ingyu|jau|jade|janna|jas|jaso|jia|jiho|jie[^in]|joko|john|jose|juho|jung|joua|joan|june|kanti|ksh|ksha|kebo|kia|katerina|ksha$|kenza|ling|\
miha|m[^bdpaiueo]|maa[\s$]|matei|makai|moti|mora|mohan|moari|mohana|muyao|moetes|mason|menon|\
ngyu|natasha|nea|naik|nan[ny]a|nisha|nue|naseri|njiza|narayana|nyuk|nachike|noit[\s$]|neh|nuja|nahon|\
oenka|osonde|oikono|oee|oao|oui|opuri|parat|patt|pant|papi|pere|pine|poo|pou|pika|pak|pita|\
rak[\s$]|reke|ranya|riti|regin|ragan|renren|ryan|raja|rian|ram|rosen|rouse|rohan|rissa|riao|redd|r*[jy]an$|rek$|rabi|\
shikun|sarin|sumit|shaja|sen$|nen$|sek[\s$]|sacha|teoh|iang|roman|shoo|shiyu|shibo|shiha|saini|shore|shu[ioa]|sundara|shuman|saima|seo[nk]|shan|shai|shaha|sundan|s[^saueoh]|ss*h[^aiuo]|sose|\
tito|tti|tian|tiago|tika|tteo|tton|tanya|tonya|tanyu|teimo|t[^taieos\s]|tt*s[^u]|to[rs]o$|uri[\s$]|unang|umaran|unika|uhan|\
warit[\s$]|yutao|yuho|yuni|yunbo|yuan|youn|yanu|yunke|yau|yi|zamani|zeit|zade|zahid|zaa|zeika|zere|z[ea]he"
        self.snjpgpat="\
(([tnhmrwbjz]|(ch|ny|my))*(aa*|ii*|uu*|ee*|oo*)|[GKd]e|Bo|Hai|[TH]ao|Bei|Ku[in]|\
A[ae]*ron|Abayomi|Aman|Amanda|Ameya|Annan|Ami[tn]|Anita|Anki|Ankita|Annika|Antoine*|Anuja|Aran|Arya|Arun|Aida|Aren|Arezou|Aria|Aryan|Ata|\
Bao|Babak|Bee|Beibei|Benaim|Benjamin|Bibit|Bin|Bodo|Bojan|Burak|Bukun|Burin|\
Chaehun|Chajin|Chanjin|Chau|Chiara|Da|Dabin|Dakai|Dami[ae]n|Dann*a|Dario|Debora|Depanshu|Derya|Dohwan|Dominik|Dongoh|Doreen|Doron|\
Ebuka|Edo|Erik|Ehsan|Eshaan|Eugene|Ewa|Eze|Gene|Gyumin|Gunawan|Ha|Haechan|Haian|Han|Hanbin|Hani|Hanna|Hannah|Hasan|He|Heiko|Henri|Hogun|Hooman|Hugo|\
Inaki|Inkyu|Imin|Itai|Isha|Jamie|Jan|Jane|Janne|Jason|Jikai|Jina|Jimin|Jirak|Jose|Johan|John|Joao|Joko|Joni|Ju|Juan|Junni|Juho|Juhee|Junho|Junhyuk|\
Kaan|Kannan|Kanika|Karima|K[ai]ran|Kate|Kenan|Kenneth|Kiana|Ki[ae]n|Kochise|Koushik|Leda|Lorenzo|\
Ma|Maatei|Matteo|Madonna|Mainak|Man|Manikanta|Marek|Marion|Masha|Matan|Mateja|Matt|Mayank|Mazen|Masoumeh|Meena|Meike|Mengu|Menoua|Miao|Mihai|Min|Minho*|Minji|Min[jJ]oon|Min[jJ]un*|Minsu|Minkyo|Mu|Mubarak|Moein|Mohi|Mohsen|Moin|Monika|Moon|Moonsoo|Moran|Mouna|Musa|Murat|\
Na|Nageen|Namo|Nariman|Neha|Nikita|Nima|Nirat|Nona|Nooshin|Nuno|\
Okan|Onat|Oren|Ori|Oladayo|Osama|Oya|Pere|Pouya|Pu|Ramana|Rami|Ranjan|Renshuai|Reuben|Reza|Rezaei|Rishi|Ruben|Rohit|Roi|Rosa|Ruwan|Ruhi|Ryan|\
Sachin|Sage|Sagie|Sanchari|Sanda|Saikat|Sandaru|Saman|Samit*|Samitha|Samira|Sarah|Sayan|Sean|Seba|Sek|Semion|Sen|Shagan|Shaurya|Shasha|Shayak|Shayan|Shai|Shi|Shichao|Shirine|Shishira|Shujon|Soomin|Sun|Suman|Suranjana|Suren|Sunita|Taha|Taman|Tanaya|Tapani|Teresa|Tarasha|\
Udana|Wa[hi]|Yan|Yake|Yani|Yanrui|Yangyu|Yao|Yaochu|Yasaman|Yohan|Yuanbiao|Yue|Yuhan|Yumin|Yun|Yunji|Yunmo|Yuru|Yunhao|Zarena|Zarana|Zerui|Zeyu)"
        self.snjpfpat="\
(Aakanksha|Achan|Acharya|Arora|Ahuja|Aksak|Akshara|Amani|Amini|Aminzadeh|Amit|Amin|Aneke|Antebi|Aran|Ari|Ariyanto|Aryan|\
Ba|Baka|Badea|Basu|Bianchini|Bilen|Bahadori|Bandara|Bauza|Ben|Bennett|Benton|Benjamin|Benson|Bera|Bian|Bianchi|Bin|Birant|Bok|Boneh|Bouma|Bouman|Bui|Chai|Cho[ou]|Ch[iu]|Chiu|Chikina|Chien|\
Dagan|Desai|Dami[ae]n|Damak|Damaine|Dewan|Do|Dorent|Doshi|Eak|Egiazarian|Emonet|Erat|Esen|Gat|Gia|Gini|Gianchandani|Gu|Guha|Guhan|Guedon|\
Ha|Hanan|Hariyono|Hakimi|Hanna|Hansen|Heidari|Himayat|Huh|Hui|Huo|Ho|Ie|Imani|Inie|Inza|\
Jagadeesan|Jahani|Jain|Jaipuria|Jamnik|Janda|Jansen|Jayasuriya|Juge|John|Johnson|Joo|Joshi|Ju|Junge|Juan|\
Kao|Kahn|Kahnsari|Kate|Kazemi|Kee|Keshishian|Khurana|Ki|Kiani|Kijak|Kim|Kishore|Koren|Koo|Kunze|Kumar|Laina|\
Ma|Madan|Maiya|Maman|Matei|Mania|Mangoubi|Maniat|Mannone|Manzanera|Masera|Mason|Masoomi|Mazaheri|Menna|Mi|Min|Minu|Mingyu|Miolane|Miranda|Memari|Me[no]|Mohan|Mou|Mok|Moniri|Monteiro|Moore|Mozeika|Munaro|Munjiza|\
Nabizadeh|Narayan|Narayanan|Neeman|Nayak|Nabi|Naik|Natarajan|Naowarat|Nauta|Nichani|Niu|Nizan|Neumann|Ngo|Noh|Nona|Nowara|\
Oh|Ohana|Omena|Oza|Pai|Pajarinen|Pan|Parekh|Pateraki|Pei|Pepik|Podee|Popa|Poranne|Pore|Poria|Potapenko|Potechin|Pu|Puri|\
R[au]|Rai|Raja|Rajan|Rajawat|Rakhsha|Ramamohanarao|Ramyaa|Ran|Rana|Rane|Rau|Raket|Rakshit|Razazadeh|Razaei|Razani|Rezaei|Rohani|Reinke|Ren|Riba|Ridao|Roh|Rouhani|Ruta|Ruben|Ryu|\
Sabo|Sah|Saria|Sai|Saikin|Saporito|Saenko|Saha|Sain|Saini|Saman[oi]|Samangouei|Samanta|Samara.+?|Saket|Sani|Saran|Sarawagi|Shabanian|Shah|Shakeri|Shayani|Shi|Shin|Shou|Shoaran|\
Son|Sohn|Souza|Suh|Sukan|Sundararaman|Suri|Susan|Suin|Tandon|Tasan|Tonekabori|\
Uban|Ure|Wanchoo|Watson|Yaesoubi|Yogatama|Yoran|Yu[eh]|Yu[ae]n|Zada|Zabih|Zadeh|Zaharia|Zontak|Zou|\
(Ch|Sh|[YSHFOLGMB])[uo]|[YSHFOLGMKZ]e|[EH]o|An|([TYHGW]|[BDL]|Shu)ai|[BGHYMR]ao|([YRG]u|Ch|[LYHTWGNM])an|[BNJ]i|Jia|[JM]iao|[GS]ui|[YS]un|[KGZ]uo|[LM]ei|Heo|[YH]ou|Choi|Yoo|Yoon)"
        self.snjpname="Ren Nie|Dan Nie|Jin Jin|Ran Tao|Shu Teo|Ran Ben|Yuhe Jin|Jin Tao|Yu Tao|Jan Kotera|Ken Mai|Meina Kan|Jinko Kanno|Rui Tao|Ao Jin|Jun Dan|Rina Kumari|Jun Jin|Rui Ai|Rui Jin|\
Ana Maria Tome|Shu Tao"
        self.snjppat="^"+self.snjpgpat+"\s|\s"+self.snjpfpat+"$|"+self.snjpname 
        self.dlm=",\s"

    def isJPlike(self,name,flg):
        ret = False

        if re.search(self.sjppat,name,flags=re.IGNORECASE):# jp-like name
            if flg:
                print('a')
            if not re.search(self.snjpwpat,name,flags=re.IGNORECASE):#non-jp-like
                if flg:
                    print('b')
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

    def check(self,au,verbose):
        if verbose:
            print(au)
        if self.isJPlike(au,verbose):
            if verbose:
                print('ok1')
            aus = re.split('\s',au)
            if verbose:
                print(len(aus))
            if len(aus) == 2:
                if self.isJPgiven(aus[0]):
                    if verbose:
                        print('ok2_1')
                    if self.isJPfamily(aus[1]):
                        if verbose:
                            print('ok2_2')
                        if self.isJPname(au):
                            if verbose:
                                print('ok2_3')
                            return True
            elif len(aus) == 3:
                if self.isJPgiven(aus[0]):
                    if verbose:
                        print('ok3_1')
                    if self.isJPfamily(aus[2]):
                        if verbose:
                            print('ok3_2')
                        if self.isJPname(au):
                            if verbose:
                                print('ok3_3')
                            return True
        return False
