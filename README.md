# Py Crawler — XVideos Downloader
 - 萌新初入Python練習爬蟲，鼻要鞭太大力QQ
 - 原本打算PornHub版，但驗證跟hash部份有點麻煩，還是算了ㄎㄎ
 - <del>反正XVideos的族群也不在少數www</del>

# 所需函式庫:
    import sys
    import requests
    from bs4 import BeautifulSoup as soup
    import signal
    import re
    from fake_useragent import UserAgent
    import time
    import os

# Info
    作者： Alpaca羊駝
    版本： ver. 1.1
    最後更新： 2019/01/14 00:34
    

# 更動
 - 美觀
   - 將名稱由「**XVideosDownloader**」更改為「**XD**」
   - 下載的檔案存放目錄名稱由「**d_html**」及「**d_mp4**」更改為「**save_html**」、「**save_mp4**」
   - 新增了「**Welcome To Use XD**」啟動畫面
   - ***modules/loading_bar.py***、***download.py*** 格式稍做修改
     - ***modules/loading_bar.py*** 及 ***download.py*** 中的Bar, Flow符號
     - ***download.py*** 中顯示的格式 及 新增了顯示自訂時間的 function — **time_str()**
    

# Bug
 - 美觀
     - Loading Bar在運作時，若視窗無法在一行內容納下Loading Bar所輸出的字串，則畫面會被重複寫入，造成刷頻 (不過這問題在很多知名套件都有發生，應該可以說是不可必免得事情，所以... <del>就不修了</del>  )
 - 解析
     - ***main.py*** 裡 **data_url=re.findall(pattern,data_url)[0]** 取資料時，不明的原因導致有機率發生資料抓空進而出現錯誤「**list index out of range**」的問題

