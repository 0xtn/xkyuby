#!/bin/bash
#PMF =[P]ython[M]odule[F]ixer
# >> Fix All Modules Imported And Installed For Python Correctly
# Worked With Win/Android(Termux/GNUroot)/Linux(Base:Debien/Ubuntu)
###########
#Check If Python HaveBeen Installed Or Not
th3C0d3r="Escan0r"
msg="9ader Ma Nigga ;)"
greetin='Tunisiens Hentai xD'
Start(){
if [ -d 'c:\' ];then
if [ -d 'c:\Python27' ];then
#To use Python With One Command Without Back To c:\Python27\
set PYTHONPATH=c:\\Python27\\
set PYTHONPATH=c:\\Python27\\Scripts;
python fy.py
else
echo -n " Install Python27 For Your Windows "
echo -n "link > https://www.python.org/downloads/"
echo -e "Press [Enter] To Exit ..."
read zz
exit
fi
elif [ -d "/data/data/com.termux/files/usr/" ]; then
if [ -f "/data/data/com.termux/files/usr/bin/python2" ];then
python2 fy.py
else
apt update && apt upgrade
apt-get install python2 
python2 fy.py
fi
elif [ -d "/usr/bin/" ];then
python2 fy.py
else
	echo -n "{!} ERROR ! CANT RUN WITH UR OS ..PLEASE CONTACT ESCANOR TO FIND A SOLU 4 U"
fi
}
if [ -d 'c:\' ];then
clear #using git or bash commands in windows but for cmd fix it by cls
else
	clear
fi
Start