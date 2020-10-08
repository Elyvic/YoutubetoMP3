from tkinter import *
import youtube_dl
import os

def Download():
    #grab the string in the entry box
    global urlString
    urlString = urlEntry.get()

    #if not os.path.exists('./downloads'):
        #os.makedirs('./downloads')

    #to get info of the url inputted on the entry
    video_info = youtube_dl.YoutubeDL().extract_info(url = urlString, download = False)
    filename = f"{video_info['title']}" + ".%(ext)s"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': 'downloads/' + filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    #this downloads the video and converts it to mp3
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    urlEntry.delete(0, END)
    urlEntry.insert(0, "")

def OpenFolder():
    path = "downloads"
    path = os.path.realpath(path)
    os.startfile(path)



#GUI stuff
urlString = " "

root = Tk()

root.title("Youtube MP3 downloader")
root.geometry("400x120")
root.resizable(False, False)

urlLabel = Label(root, text = "URL")
urlEntry = Entry(root, textvariable = " ", width = 50)
downloadButton = Button(root, text = "Download", command = Download)
folderButton = Button(root, text = "Folder", command = OpenFolder)

urlLabel.place(x = 30, y = 30)
urlEntry.place(x = 60, y = 30)
downloadButton.place(x = 160, y = 60)
folderButton.place(x = 355, y = 95)

mainloop()
