# from pytube import YouTube
# # import tkinter
# from tkinter.filedialog import *
# from tkinter.messagebox import *

# # url = "https://www.youtube.com/watch?v=hMy5za-m5Ew"

# # path_to_save_video = "C:\\Users\\Archit\\Desktop"
# # # #creating youtube object with url
# # ob = YouTube(url)
# # strms = ob.streams.first()

# # # print(strms.filesize)
# # # print(strms.title)

# # # print(ob.description)

# # # now downloading the video

# # strms.download(path_to_save_video)

# # print("Done....")

# file_size = 0

# def startDownloader():
# 	global file_size
# 	try:
# 		url = urlField.get()
# 		print(url)
# 		#change button text
# 		dBtn.config(text='Please Wait...')
# 		dBtn.config(state=DISABLE)
# 		path_to_save_video = askdirectory()
# 		if path_to_save_video is None:
# 			return 
# 		#creating youtube object with url
# 		ob = YouTube(url)
# 		strms = ob.streams.first()

# 		# print(strms.filesize)
# 		# print(strms.title)

# 		# print(ob.description)

# 		# now downloading the video

# 		strms.download(path_to_save_video)
# 		print("Done....")
# 		dBtn.config(text="Start Download")
# 		dBtn.config(state=NORMAL)
# 		showinfo("Download Finish", "Downloaded successfully")
# 		urlField.delete(0, END)
	
# 	except Exception as e:
# 		print(e)
# 		print("Error!!!")

# # starting GUI building

# main = Tk()

# #setting the title
# main.title("My Youtube Downloader")

# # set the icon
# # main.iconbitmap('.ico')
# main.geometry("500x600")
# # main.mainloop()

# # # heading icon
# # file=PhotoImage(file='youtube.png')
# # headingIcon = Label(main,image=file)
# # headingIcon.pack(side=TOP)

# # url textfield
# urlField=Entry(main, font=("verdana",18), justify=CENTER)
# urlField.pack(side=TOP, fill=X, padx=10)

# Btn = Button(main, text="Start download", font=("verdana",18), relief='ridge', command= startDownloader())
# Btn.pack(side=TOP, pady=10)

# main.mainloop()


import tkinter as tk
from tkinter import ttk
import os
from pytube import YouTube
from tkinter import messagebox as m_box

win = tk.Tk()
win.geometry("500x400")
win.title("YouTube Video Downloader")
win.minsize(500,400)
win.maxsize(500,400)
frame = ttk.LabelFrame(win)
frame.grid(row=0,column=0, padx=70, pady=90)

get_info = ttk.Label(frame, text="Enter YouTube Video Link : ")
get_info.grid(row=0, column=0, sticky=tk.W)

link = tk.StringVar()

yt_link = ttk.Entry(frame, width= 60, textvariable=link)
yt_link.grid(row=1, columnspan=3, padx=0, pady=3)
yt_link.focus()

get_info = ttk.Label(frame, text="Enter Downloading Path : ")
get_info.grid(row=3, column=0, sticky=tk.W)

path = tk.StringVar()

download_path = ttk.Entry(frame, width= 60, textvariable=path)
download_path.grid(row=4, columnspan=3, padx=0, pady=3)

get_file_name = ttk.Label(frame, text="Enter File Name : ")
get_file_name.grid(row=5, column=0, sticky=tk.W)

filename = tk.StringVar()

get_filename_entry = ttk.Entry(frame, width= 60, textvariable=filename)
get_filename_entry.grid(row=6, columnspan=3, padx=0, pady=3)

def onClick():
    got_link = link.get()
    got_path = path.get()
    got_filename = filename.get()
    try: 
        yt = YouTube(str(got_link))
    except: 
        m_box.showerror("Error", "Connection Problem !")
    else:
        videos = yt.streams.all()
        s = 1
        for v in videos:
            print(str(s)+". "+str(v))
            s += 1 
        n = int(1)
        vid = videos[n-1]
        destination = str(got_path)
        vid.download(destination)
        return m_box.showinfo('Successfully Downloaded', f"{got_filename} Video Downloaded Successfully.")
btn1 = ttk.Button(frame, text="Download Video", width=15, command=onClick)
btn1.grid(row=7, columnspan=3, padx= 13, pady= 7)

win.mainloop()