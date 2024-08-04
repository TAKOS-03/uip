import random 
import os

def ua():
    tipecnc = random.choice(["T-Mobile"," vodafone ES"," vodafone"," TELCEL"," Android"," vodafone ES"," Viettel Telecom"," MegaFon"," cricket"," AIS"," Bouygues Telecom"," T-Mobile"," Telstra"," Telkomsel"," null"," Maxcom"," vodafone.de"," Yoigo"," PLAY (T-Mobile"," airtel"]) 
    cnc = random.choice(["fr_GN"," en_AU"," es_ES"," en_US"," in_ID"," en_GB"," id_ID"," cs_CZ"," pt_BR"," bg_BG"," fr_FR"," id_ID"," es_MX","th_TH","vi_VN","en_EG","fr_FR","sv_SE"]) 
    model2 = random.choice(['SM-G930F','SM-A720F','SM-G950U','SM-G925F','SM-N9005','SM-A205GN','SM-A505GN','SM-A505GN','SM-A205GN','SM-A205GN','SM-G955F','SM-G955F','SM-G970U1','SM-J730F','SM-A505GT','SM-A505GT','SM-G532G'])
    vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
    VAPP = random.randint(410000000,499999999)
    END ="[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,300))+str(random.randint(11,555)) +";[FBAN/FB4A;FBAV/"+str(random.randint(11,454))+'.0.0.'+str(random.randrange(10,60))+str(random.randint(100,200))+";FBPN/com.facebook.katana;FBLC/"+cnc+";FBBV/"+str(random.randint(11111111,99999999))+";FBCR/"+tipecnc+";FBMF/samsung;FBBD/samsung;FBDV/"+model2+";FBSV/"+str(random.randint(1,15))+";FBCA/armeabi-v7a:armeabi;FBDM/{density="+str(random.randint(1,5))+",width="+str(random.randint(360,2600))+",height="+str(random.randint(900,9999))+"};FB_FW/"+str(random.randint(1,10))+";FBRV/"+str(random.randint(11111111,99999999))+";]" 
    ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {random.choice(model2)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+END  
    return ua

    logo = ("""   \033[97;1m 
[*] d888888b  .d88b.   .d88b.  db      .d8888.
[*] `~~88~~' .8P  Y8. .8P  Y8. 88      88'  YP
[*]    88    88    88 88    88 88      `8bo.
[*]    88    88    88 88    88 88        `Y8b.
[*]    88    `8b  d8' `8b  d8' 88booo. db   8D
\033[97;1m══════════════════════════════════════════════
\033[1;32m[\033[1;31m=\033[1;32m] \033[1;36mUA
\033[1;32m[\033[1;31m=\033[1;32m] \033[1;36m𝐕𝐄𝐑𝐒𝐈𝐎𝐍   : \033[1;91m0.1
\033[97;1m═══════════════════════════════════════════""")
    print(logo)
def ux(n): 
  n = [] 
  for _ in range(n): 
    uag.append(n()) 
    return"\n \n".join(uag) 
    n = int(input("ENTER NO FO TIME: "))  
    print(ux(n))  