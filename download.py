# -*- coding: utf-8 -*
import sys
import requests
import time
import os

def download(req_headers,data_title,data_url,sys_debug=False):
	if sys_debug:
		print("Loaded download.py")
	print("Found: "+data_title+"\n")

	while True:
		data_dl_style=input("(1) Save mp4 (Default)\n(2) Save html\n(3) Save mp4, html\n(4) Cancel\nChoice download mode: ")
		print("\n")
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
			print("Creating link...")
			h_filepath="d_html/"
			h_filename=filename+".html"
			try:
				if sys_debug:
					print("Creating path...")
				os.makedirs(h_filepath)
			except FileExistsError:
				if sys_debug:
					print("Found path!")
			with open(h_filepath+h_filename,"w") as f:
				f.write('<video controls="" autoplay="" name="media"><source src="'+data_url+'" type="video/mp4"></video>')
			print("Link created!\n")

		# save mp4
		if (data_dl_style=='') or (data_dl_style=="1") or (data_dl_style=="3"):
			m_filepath="d_mp4/"
			m_filename=filename+".mp4"
			try:
				if sys_debug:
					print("Creating path...")
				os.makedirs(m_filepath)
			except FileExistsError:
				if sys_debug:
					print("Found path!")
			bar_size=50
			size=0
			chunk_size = 1024
			content_size = int(data_download.headers['content-length'])
			start=time.time()
			with open(m_filepath+m_filename,"wb") as f:
				for data in data_download.iter_content(chunk_size=chunk_size):
					if data:
						f.write(data)
					size += len(data)
					print('\r'+"Downloading: "+int(size/content_size*bar_size)*"█"+" "+str(round(size/chunk_size/1024,2))+"/"+str(round(float(content_size/chunk_size/1024),4))+" MB"+"【"+str(round(float(size/content_size)*100,2))+"%"+"】",end="")
			end = time.time()
			print("\nTime: "+str((end-start)-((end-start)%1))+"s")
			print("Saved!\n")


		break
