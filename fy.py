import sys ,os.path
import os
#lists
Modules=[]
zz=[]
zzz=[]
z3=[]
mm=[]
Modpl=[]
Mymod=[]
########
logo="""
                           ,d8888b
                           88P'   
                        d888888P  
?88,.d88b,  88bd8b,d88b   ?88'    
`?88'  ?88  88P'`?8P'?8b  88P     
  88b  d8P d88  d88  88P d88      
  888888P'd88' d88'  88bd88'      
  88P'                            
 d88    Python Module Fixer                          
 ?8P    By Escanor(github.com/0xtn)


"""
########
#Check Modules Not Avaible In Your Device And Install It
try: 
 from colorama import Fore, Back, Style
 r = Fore.RED
 w = Fore.WHITE
 y = Fore.YELLOW
except:
  if os.name=='nt':
    try:
      os.system('c:\Python27\Scripts\pip2.exe install colorama')
    except:
      print('{!} Sir ! Try To Get Python-Pip ')
  else:
   print "Installing colorama"
   pip.main['install','colorama']
def py(zz,temp):
  ss="""
  \r try:
  \r\t\timport {module}
  \r except ImportError:
  \r\t\tprint "Install {module} "
  \r\t\tos.system('pip2 install {module}')\n""".format(module=zz)
  temp.write(ss)
def winpy(zz,temp):
  ss="""
  \r try:
  \r\t\timport {module}
  \r except ImportError:
  \r\t\tprint "Install {module} "
  \r\t\tos.system('c:\Python27\Scripts\pip2.exe install {module}')\n""".format(module=zz)
  temp.write(ss)
def checkpip(rabbit):
  temp=open('fy_temp.py','a')
  temp.write('#Simple CheckerPip (-),(-)\nimport os,sys\ndef yo():')
  if os.name=='nt':
    for caroot in rabbit:
      winpy(caroot,temp)
    temp.write("\n\r print ' Done !'\n\r os.remove('fy_temp.py')\n\ryo()")
    temp.close()
    try:
     os.system('python fy_temp.py')
    except :
      print '%s{!} ERROR ! Something Wroung %s'%(r,w)
  else:
    for caroot in rabbit:
      py(caroot,temp)
    temp.write("\n\r print ' Done !'\n\r os.remove('fy_temp.py')\n\ryo()")
    temp.close()
    try:
     os.system('python2 fy_temp.py')
    except :
      os.remove('fy_temp.py')
#Cleaning And Extract Modules From The Code 
def pywork():
 with open (zz,'r') as zzz:
   for z1 in zzz:
    if "import " in z1:
      if "from " in z1:
        z1=z1.replace('from ','')
        pt=z1.index('import')
        z1z=z1[:pt]
        z1z=z1z.replace(' ','');z1z=z1z.replace('\t','');z1z=z1z.replace('\n','')
        #check if z1z isnt a Another Project Py Or A Dictory
        thabt=z1z.replace('.','/')
        thabeet=str(thabt)+'.py'
        if os.path.isfile(thabeet):
          pass
        elif os.path.isdir(thabt):
          pass
        else:
         Modules.append(z1z)
      
      else:
       z1=z1.replace('import ','')
       z2=z1.replace(',',' ');z2=z2.replace('  ',' ')
       z3=z2.split()
       for i in z3:
        if i ==' ':
          pass
        else:
          Modules.append(i)
 checkpip(Modules)     

#Start To Play
try:
 os.remove('fy_temp.py')#formatage 
except:
  pass
try:
 print logo
 try:
    zz=sys.argv[1]
 except:
  zz=raw_input('%s(!) Enter The Script : %s'%(y,w))
  if zz.endswith('.py'):
   pywork()
  else:
   print "%s{!} ERROR FILE !! PLEASE TRY ONLY WITH PYTHON %s"%(r,w)
except KeyboardInterrupt:
  print "%s{!} ERROR INPUT !! PLEASE TRY AGAIN  %s"%(r,w)

