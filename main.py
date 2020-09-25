from tkinter import *
import youtube_dl

def Download():
    global urlString
    urlString = urlEntry.get()
    video_info = youtube_dl.YoutubeDL().extract_info(url= urlString, download = False)
    filename = f"{video_info['title']}" + ".%(ext)s"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])



urlString = " "

root = Tk()

root.title("Youtube MP3 downloader")
root.geometry("400x120")
root.resizable(False, False)

urlLabel = Label(root, text = "URL")
urlEntry = Entry(root, textvariable = " ", width = 50)
downloadButton = Button(root, text= "Download", command = Download)

urlLabel.place(x = 30, y = 30)
urlEntry.place(x = 60, y = 30)
downloadButton.place(x = 160, y = 60)

mainloop()