import os,sys,re
#Dima Ghabraa
#remove space
def rm_spc():
   if not os.path.isdir('results/combos'):
          os.mkdir('results/combos')
   zaw =raw_input("list :")
   try:
    comboo=open(zaw,'r')
   except:
    print "{!} Error File";exit()
   for z in comboo:
     mark ="".join(re.split("\s+",str(z), flags=re.UNICODE))
     zz0=open('results/combos/comboa.txt','a')
     zz0.write(mark +'\n')
#remove duplicates
def rm_dup():
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
#work..
rm_spc()
rm_dup()