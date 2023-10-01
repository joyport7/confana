#!/usr/bin/env python
# coding: utf-8
import re

class jpnm:
    def __init__(self):
        self.sjppat="^(([aiueo]h*|[kgnhbmr][aiueo]h*|s[aueo]h*|j[aiuo]h*|t[aeo]|[kmgr]*y[auo]h*|[cs]h[auio]h*|shi|tsu|wa|fu|d[aeo]|z[aueo]h*)n*t*[' \.]*)+$"
        self.snjpwpat="[^n]'|-|[qxv]|[áčçøåÅÇØ]|[^aiueontkh\.][\s$]|nn[\s$]|\
aer|ahn|ajaka|[bjr]iao|riao|bodo|(ch|[bdj])ae|choe|eu[in]|eau|f[ieo]|hao|[bh]ee|hoai|oao|[jmys]oon|papi|pine|shore|dani|doo|guru|suchi|doan|saima|aitao|banjan|aharo|oee|chink|joan|deon|menon|goo|choo[ni]|\
janna|ce|el|zaa|che|yau|rohan|adeka|adegu|yi|rabi|jade|nanya|pant|jau|inigo|nue|aushik|gopan|pak|z[ea]he|ahoo|shuman|patt|naik|teimo|kia|pika|ksh|chitt|shiha|yuni|saini|yunbo|azuri|tton|muyao|derya|hui[\s$]|\
[hkg]yu[nk]|youn|guk|jia|hua|jie[^in]|nea|ksha|anton|bao|boja|debo|narayana|sundara|ram|rosen|baum|hasson|parat|moetes|poo|rissa|redd|opuri|pere|asank|zahid|june|aisha|teoh|iang|roman|shoo|shibo|biran|\
jas|jaso|jau|joko|john|jose|juho|jung|joua|shu[ioa]|rian|[sg]uo|seo[nk]|shan|eun[gk]|shai|shaha|naseri|njiza|tteo|zeika|gaga|charya|gaja|mohan|raja|mohana|domi|pou|baie|gudo|zere|tonya|akya|engyu|hyoji|\
nisha|mora|zade|ryan|pita|tanyu|nyuk|dorai|habi|biba|bukh|sundan|zeit|ragan|regin|giot|yuho|nachike|ling|ezra|aragon|hoang|\
[bdfghjklmpqrvwxyz][bcdfgjklmpqrtvwxz]|c[^h]|t[^taeos\s]|s[^saueoh]|ss*h[^aiuo]|tt*s[^u]|m[^bdpaiueo]|[tk]h$|[in]h$|[rsyn][ai]ni$|haran$|dat$|bot$|[ds]ah$|neh|[ds]eem$|r*[jy]an$|rek$|to[rs]o$|daan$|ksha$|rak[\s$]|sen$|nen$|sek[\s$]|[fy]uan$|uri[\s$]"
        self.snjpgpat="\
(([JN]|Sh|Ch)i|Bin|[GKd]e|Bo|Hai|[TH]ao|Bei|Ku[in]|\
A[ae]*ron|Abayomi|Aman|Amanda|Ameya|Annan|Ami[tn]|Anita|Anki|Ankita|Annika|Antoine*|Anuja|Aran|Arya|Arun|Aida|Aren|Arezou|Aria|Aryan|Ata|\
Bao|Babak|Bee|Beibei|Benaim|Benjamin|Bodo|Bojan|Burak|Bukun|Burin|\
Chaehun|Chajin|Chanjin|Chau|Chiara|Da|Dabin|Dakai|Dami[ae]n|Dann*a|Dario|Debora|Depanshu|Derya|Dohwan|Dominik|Dongoh|Doreen|Doron|\
Ebuka|Edo|Erik|Ehsan|Eshaan|Eugene|Ewa|Eze|Gene|Gyumin|Gunawan|Haechan|Haian|Han|Hanbin|Hani|Hanna|Hannah|Hasan|He|Heiko|Henri|Hogun|Hooman|Hugo|\
Inaki|Inkyu|Imin|Itai|Isha|Jamie|Jan|Jane|Janne|Jason|Jikai|Jina|Jimin|Jirak|Jose|Johan|John|Joao|Joko|Joni|Ju|Juan|Junni|Juho|Juhee|Junho|Junhyuk|\
Kaan|Kannan|Kanika|K[ai]ran|Kate|Kenan|Kenneth|Kiana|Ki[ae]n|Kochise|Koushik|Leda|Lorenzo|\
Maatei|Matteo|Madonna|Mainak|Man|Manikanta|Marek|Marion|Masha|Matan|Mateja|Matt|Mayank|Mazen|Masoumeh|Meena|Meike|Mengu|Menoua|Miao|Mihai|Min|Minho*|Minji|Min[jJ]oon|Min[jJ]un*|Minsu|Minkyo|Mu|Mubarak|Moein|Mohi|Mohsen|Moin|Monika|Moon|Moonsoo|Moran|Mouna|Musa|Murat|\
Na|Nageen|Namo|Nariman|Neha|Nikita|Nima|Nirat|Nona|Nooshin|Nuno|\
Okan|Oren|Ori|Oladayo|Osama|Oya|Pere|Pouya|Pu|Ramana|Rami|Ranjan|Renshuai|Reuben|Reza|Rishi|Ruben|Rohit|Roi|Rosa|Ruwan|Ruhi|Ryan|\
Sachin|Sage|Sagie|Sanchari|Saikat|Sandaru|Saman|Samit*|Samitha|Samira|Sarah|Sayan|Sean|Seba|Sek|Semion|Sen|Shagan|Shaurya|Shasha|Shayak|Shayan|Shai|Shichao|Shirine|Shishira|Shujon|Soomin|Sun|Suman|Suranjana|Suren|Sunita|Taha|Taman|Tanaya|Tapani|Teresa|Tarasha|\
Udana|Wa[hi]|Yan|Yani|Yanrui|Yangyu|Yaochu|Yasaman|Yohan|Yuanbiao|Yue|Yumin|Yun|Yunji|Yunmo|Yuru|Yunhao|Zarena|Zarana|Zerui|Zeyu)"
        self.snjpfpat="\
((Ch|N)a|(Ch|Sh|[YSHFOLGMB])[uo]|[YSHFOLGMKZ]e|[EH]o|An|([TYHGW]|[BDL]|Shu)ai|[BGHYMR]ao|([YRG]u|Ch|[LYHTWGNM])an|[BNJ]i|Jia|[JM]iao|[GS]ui|[YS]un|[KGZ]uo|[LM]ei|Heo|[YH]ou|Choi|Yoo|Yoon|\
Aakanksha|Achan|Acharya|Arora|Ahuja|Aksak|Akshara|Amani|Amini|Aminzadeh|Amit|Amin|Aneke|Antebi|Aran|Ari|Ariyanto|Aryan|\
Ba|Baka|Badea|Basu|Bilen|Bahadori|Bandara|Bauza|Ben|Bennett|Benton|Benjamin|Benson|Bera|Bian|Bianchi|Bin|Birant|Bok|Boneh|Bouma|Bouman|Bui|Chai|Cho[ou]|Ch[iu]|Chikina|\
Dagan|Desai|Dami[ae]n|Damak|Damaine|Dewan|Do|Dorent|Doshi|Eak|Egiazarian|Emonet|Erat|Esen|Gat|Gia|Gini|Gianchandani|Gu|Guha|Guhan|Guedon|\
Ha|Hanan|Hariyono|Hakimi|Hanna|Hansen|Heidari|Himayat|Huh|Hui|Huo|Ho|Ie|Imani|Inza|\
Jagadeesan|Jahani|Jain|Jaipuria|Jamnik|Janda|Jansen|Jayasuriya|Juge|John|Johnson|Joo|Joshi|Ju|Junge|\
Kao|Kahn|Kahnsari|Kate|Kazemi|Kee|Keshishian|Khurana|Ki|Kiani|Kijak|Kim|Kishore|Koren|Koo|Kunze|Kumar|\
Laina|Ma|Madan|Maiya|Maman|Mania|Mangoubi|Maniat|Mannone|Manzanera|Masera|Mason|Masoomi|Mazaheri|Menna|Mi|Min|Minu|Mingyu|Miolane|Miranda|Memari|Me[no]|Mohan|Mok|Moniri|Monteiro|Moore|Mozeika|Munaro|Munjiza|\
Nabizadeh|Narayan|Narayanan|Neeman|Nayak|Nabi|Naik|Natarajan|Naowarat|Nauta|Nichani|Nizan|Neumann|Ngo|Noh|Nona|Nowara|\
Oh|Ohana|Omena|Oza|Pai|Pajarinen|Pan|Parekh|Pateraki|Pei|Pepik|Podee|Popa|Poranne|Pore|Poria|Potapenko|Potechin|Pu|Puri|\
Ra|Rai|Raja|Rajan|Rajawat|Rakhsha|Ramamohanarao|Ramyaa|Ran|Rana|Rane|Rau|Raket|Rakshit|Razazadeh|Razaei|Razani|Razaei|Rohani|Reinke|Ren|Riba|Ridao|Roh|Rouhani|Ruta|Ruben|Ryu|\
Sabo|Sah|Saria|Sai|Saikin|Saporito|Saenko|Saha|Sain|Saini|Saman[oi]|Samangouei|Samanta|Samara.+?|Saket|Sani|Saran|Sarawagi|Shabanian|Shah|Shakeri|Shayani|Shi|Shin|Shou|Shoaran|Sohn|Souza|Suh|Sukan|Sundararaman|Suri|Susan|Suin|Tandon|Tasan|Tonekabori|\
Wanchoo|Watson|Yaesoubi|Yogatama|Yoran|Yu[eh]|Yu[ae]n|Zada|Zabih|Zadeh|Zaharia|Zontak|Zou)"
        self.snjpname="Jin Jin|Ran Tao|Ran Ben|Yuhe Jin|Jin Tao|Yu Tao|Jan Kotera|Ken Mai|Meina Kan|Jinko Kanno|Rui Tao|Ao Jin|Jun Dan|Rina Kumari|\
Ana Maria Tome|Shu Tao"
        self.snjppat="^"+self.snjpgpat+"\s|\s"+self.snjpfpat+"$|"+self.snjpname 
        self.dlm=",\s"

    def isJP(self,name):
        ret = False
        if re.search(self.sjppat,name):# jp-like name
            if not re.search(self.snjpwpat,name,flags=re.IGNORECASE):#non-jp-like
                if not re.search(self.snjppat,name,flags=re.IGNORECASE):#non-jp name
                    ret = True
                #else:
                #    print(f'non jp name: {name}')
        return ret
    
    def isJPlike(self,name,flg):
        ret = False

        if re.search(self.sjppat,name,flags=re.IGNORECASE):# jp-like name
            if flg:
                print('1')
            if not re.search(self.snjpwpat,name,flags=re.IGNORECASE):#non-jp-like
                if flg:
                    print('2')
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
        if self.isJPlike(au,verbose):
            if verbose:
                print('ok1')
            aus = re.split('\s',au)
            if len(aus) == 2:
                if self.isJPgiven(aus[0]):
                    if verbose:
                        print('ok2')
                    if self.isJPfamily(aus[1]):
                        if verbose:
                            print('ok2')
                        if self.isJPname(au):
                            if verbose:
                                print('ok3')
                            return True
            elif len(aus) == 3:
                if self.isJPgiven(aus[0]):
                    if verbose:
                        print('ok2')
                    if self.isJPfamily(aus[2]):
                        if verbose:
                            print('ok3')
                        if self.isJPname(au):
                            if verbose:
                                print('ok4')
                            return True
        return False
