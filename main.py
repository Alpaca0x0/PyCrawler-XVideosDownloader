# -*- coding: utf-8 -*
class _info():
	def __init__(self):
		self.name="XD"
		self.athr="Alpaca羊駝"
		self.ver="1.2"
		self.update="2021/06/29"
_info=_info()
"""
作者：Alpaca羊駝
版本：ver. 1.2

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMNMMMMMMMMMMMMdsNMMMMMMMNmmdhhdNMMMMMMMMMMMMMM
MMMMMMh: .hMMMMMMMMm:  `oMMMMs`        `:odMMMMMMMMMM
MMMMMMd.   oMMMMMMs`   `yMMMM:             .yMMMMMMMM
MMMMMMMN/   :mMMN:    :mMMMMM.    +++/:`     /MMMMMMM
MMMMMMMMM+   `yh.   `yMMMMMMM.    NMMMMMh:    +MMMMMM
MMMMMMMMMMs        :mMMMMMMMM.   `MMMMMMMMo    mMMMMM
MMMMMMMMMMM+      :MMMMMMMMMM.   `MMMMMMMMM`   hMMMMM
MMMMMMMMMM+        .sNMMMMMMM.   `MMMMMMMMN    dMMMMM
MMMMMMMMd.    :+`    `+mMMMMM.   `MMMMMmds.   -MMMMMM
MMMMMMMo    -dMMNy-     -sNMM.    :-.`       +NMMMMMM
MMMMMd-   .yMMMMMMMm+`   `yMM`            .+mMMMMMMMM
MMMMMo. .yMMMMMMMMMMMNs./NMMm.-----//+oydMMMMMMMMMMMM
MMMMMMMmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
"""
print("\
__        __   _                           \n\
\\ \\      / /__| | ___ ___  _ __ ___   ___  \n\
 \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ \n\
  \\ V  V /  __/ | (_| (_) | | | | | |  __/ \n\
   \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___| \n\
 _____       _   _           __  ______  \n\
|_   _|__   | | | |___  ___  \\ \\/ /  _ \\ \n\
  | |/ _ \\  | | | / __|/ _ \\  \\  /| | | |\n\
  | | (_) | | |_| \\__ \\  __/  /  \\| |_| |\n\
  |_|\\___/   \\___/|___/\\___| /_/\\_\\____/ \n\
")
print("Version:	"+_info.ver)
print("Last Update:	"+_info.update)
print("")

import sys
sys.path.append("modules")
import loading_bar as ld_b
ld_b.create_bar(bar_width=30,bar_text='Loading：')
ld_b.load(bar_flow=10)

import requests
from bs4 import BeautifulSoup as soup
# signal 判斷ctrl+c
import signal
# 正規表達
import re
# 偽裝請求
from fake_useragent import UserAgent

# 運行參數
sys_debug=False
if ("--debug" in sys.argv) or ("-d" in sys.argv):
	sys_debug=True;

def exit(signum, frame):
    print('\n Stoped Downloader！ \n')
    sys.exit()
signal.signal(signal.SIGINT, exit)
signal.signal(signal.SIGTERM, exit)

def set_header_user_agent():
    user_agent = UserAgent()
    return user_agent.random

####################################################

ld_b.load(bar_flow=20)
ld_b.end_bar('Loaded! (Use \"Ctrl+C\" to exit.)\n')

while True:
	# 參數定義
	req_url=input("XVideo URL: ")
	print("Checking...")
	# 過濾參數
	req_url=req_url.replace(" ","")
	pattern = re.compile(r"(^(http)(s)?://)(\w+)?\.?(xvideos\.com/\w+)")
	result = pattern.match(req_url)
	if not result:
		print("This is not a XVideo URL, Try again.\n")
		continue
	# 請求網站
	print("Requesting...\n")
	req_useragent=set_header_user_agent()
	req_headers={"User-Agent": req_useragent}
	req=requests.get(req_url,headers=req_headers,timeout=15)
	# 查看回應
	if sys_debug:
		print("HOST => HTTP: "+req.url)
		print("HOST <= HTTP: "+str(req.status_code)+"\n")
	if req.status_code != requests.codes.ok:
		print("Um... Bad request :/\n")
		continue
	# 解析
	req.encoding="utf-8"
	req=soup(req.text,"html.parser")
	data_title=req.title.string
	data_url=(req.select("div#video-player-bg script")[3]).string
	pattern = re.compile(r"html5player\.setVideoUrlHigh\(\'.*") 
	data_url=re.findall(pattern,data_url)[0]
	if sys_debug:
		print("Got: "+data_url+"\n")
	pattern = re.compile(r"http.*\'")
	data_url=re.findall(pattern,data_url)[0]
	data_url=data_url.replace(" ","")
	data_url=data_url.replace("\'","")
	if sys_debug:
		print("Analyzed: "+data_url+"\n")
	# 下載
	import download
	download.download(req_headers=req_headers,data_title=data_title,data_url=data_url,sys_debug=sys_debug)
