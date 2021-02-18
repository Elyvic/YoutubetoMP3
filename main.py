from tkinter import *
from tkinter import filedialog
import youtube_dl
import os

folder_name = ""


def Mp3Download():
    global folder_name
    #grab the string in the entry box
    #global urlString
    urlString = urlEntry.get()

    #if not os.path.exists('./downloads'):
        #os.makedirs('./downloads')

    #to get info of the url inputted on the entry
    video_info = youtube_dl.YoutubeDL().extract_info(url = urlString, download = False)
    filename = f"{video_info['title']}" + ".%(ext)s"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': folder_name + "/" + filename,
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


def Mp4Download():
    #do stuff below
    print("download video")

def OpenFolder():
    global folder_name
    path = folder_name
    path = os.path.realpath(path)
    os.startfile(path)

def SaveFolder():
    global folder_name
    folder_name = filedialog.askdirectory()


#GUI stuff
urlString = " "

root = Tk()

root.title("Youtube MP3 downloader")
root.geometry("400x120")
root.resizable(False, False)

savePhoto = PhotoImage(file = r"Resources/SaveButton.png")
folderPhoto = PhotoImage(file = r"Resources/folderButton.png")


urlLabel = Label(root, text = "URL")
urlEntry = Entry(root, textvariable = " ", width = 50)
mp3Button = Button(root, text = "Mp3", command = Mp3Download)
mp4Button = Button(root, text = "Mp4", command = Mp4Download)
folderButton = Button(root, command = OpenFolder, image = folderPhoto)
fileButton = Button(root, command = SaveFolder, image = savePhoto)


urlLabel.place(x = 30, y = 30)
urlEntry.place(x = 60, y = 30)
mp3Button.place(x = 160, y = 60)
mp4Button.place(x = 195, y = 60)
folderButton.place(x = 375, y = 95)
fileButton.place(x = 366, y = 28)

mainloop()
