# -*- coding: utf-8 -*
import sys
import requests
import time
import os

def time_str(t_sec,days="day ",hours="hour ",minutes="min ",seconds="sec"):
	# t_sec is time sec(int)
	t_sec=int(t_sec)

	if int(t_sec/60)>0: # min >
		if int(t_sec/60/60)>0: # hour >
			if int(t_sec/60/60/24)>0: # day >
				return str(int(t_sec/60/60/24))+days+str(int(t_sec/60/60)).zfill(2)+hours+str(int(t_sec/60)).zfill(2)+minutes+str(int(t_sec%60)).zfill(2)+seconds
			else: # hour min sec
				return str(int(t_sec/60/60)).zfill(2)+hours+str(int(t_sec/60)).zfill(2)+minutes+str(int(t_sec%60)).zfill(2)+seconds
		else: # min sec
			return str(int(t_sec/60)).zfill(2)+minutes+str(int(t_sec%60)).zfill(2)+seconds
	else: # sec
		return str(int(t_sec%60)).zfill(2)+seconds

def download(req_headers,data_title,data_url,sys_debug=False):
	if sys_debug:
		print("Loaded download.py")
	print("Found: "+data_title+"\n")

	while True:
		data_dl_style=input("(1) Save mp4 (Default)\n(2) Save html\n(3) Save mp4, html\n(?) Cancel\nChoice download mode: ")
		print("")
		data_dl_style=data_dl_style.replace(" ","")
		# cancel
		if (data_dl_style==4):
			break

		data_download=requests.get(data_url,headers=req_headers,stream=True,timeout=15)
		n_filename={"/","|","\\","?","\"","*",":",">","<",".","\'"}
		for n_f in n_filename:
			filename=data_title.replace(n_f,"_")

		# save html
		if (data_dl_style=="2") or (data_dl_style=="3"):
			print("\nCreating link...")
			h_filepath="save_html/"
			h_filename=filename+".html"
			try:
				if sys_debug:
					print("Creating path...")
				os.makedirs(h_filepath)
			except FileExistsError:
				if sys_debug:
					print("Found path!")
			with open(h_filepath+h_filename,"w") as f:
				f.write('<!-- Github: Alpaca0x0 --><video controls="" autoplay="" name="media" style="height: 100%"><source src="'+data_url+'" type="video/mp4"></video>')
			print("Link created!\n")

		# save mp4
		if (data_dl_style=='') or (data_dl_style=="1") or (data_dl_style=="3"):
			m_filepath="save_mp4/"
			m_filename=filename+".mp4"
			try:
				if sys_debug:
					print("Creating path...")
				os.makedirs(m_filepath)
			except FileExistsError:
				if sys_debug:
					print("Found path!")
			bar_size=30
			size=0
			chunk_size = 1024
			content_size = int(data_download.headers['content-length'])
			start=time.time()
			with open(m_filepath+m_filename,"wb") as f:
				for data in data_download.iter_content(chunk_size=chunk_size):
					if data:
						f.write(data)
					size += len(data)
					now = time.time()
					sys.stdout.write('\r'+"Downloading: "+u"\u250b"+int(size/content_size*bar_size)*u"\u2588"+int(bar_size-(size/content_size*bar_size))*" "+u"\u250b"+"【"+str("%.02f"%round(size/chunk_size/1024,2))+"/"+str("%.02f"%round(float(content_size/chunk_size/1024),2))+" MB】"+"【"+str("%.02f"%round(float(size/content_size)*100,2))+"%"+"】【"+time_str(days="d ",hours="h ",minutes="m ",seconds="s",t_sec=int(now-start))+"】")
					sys.stdout.flush()
			end = time.time()
			print("\nSaved!")

		print("\n\n")
		break
