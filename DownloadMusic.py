from pytube import YouTube
from tkinter import *
from moviepy.editor import *
import subprocess

class Application:
    def __init__(self, master=None):
        #FONTE PADRAO
        self.fontePadrao = ("Arial", "10")

        #CONTAINER
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        #TITULO
        self.titulo = Label(self.primeiroContainer, text="Baixar audio dos vídeos do youtube")
        self.titulo["font"] = ("Arial", "20", "bold")
        self.titulo.pack()

        #ERROR MSG
        self.errorMsg = Label(self.primeiroContainer, text="", fg="#FF0000")
        self.errorMsg["font"] = ("Arial", "10", "bold")
        self.errorMsg.pack()

        #URL LABEL
        self.urlLabel = Label(self.segundoContainer,text="URL do vídeo", font=self.fontePadrao)
        self.urlLabel.pack(side=LEFT)

        #INPUT URL
        self.url = Entry(self.segundoContainer)
        self.url["width"] = 30
        self.url["font"] = self.fontePadrao
        self.url.pack(side=LEFT)

        #DIRETORIO LABEL
        self.diretorioLabel = Label(self.terceiroContainer, text="Diretorio", font=self.fontePadrao)
        self.diretorioLabel.pack(side=LEFT)

        #INPUT DIRETORIO
        self.diretorio = Entry(self.terceiroContainer)
        self.diretorio["width"] = 30
        self.diretorio["font"] = self.fontePadrao
        self.diretorio.pack(side=LEFT)

        #BOTAO DE BAIXAR
        self.baixar = Button(self.quartoContainer)
        self.baixar["text"] = "Baixar audio"
        self.baixar["font"] = ("Calibri", "8")
        self.baixar["width"] = 12
        self.baixar["command"] = self.baixarVideo
        self.baixar.pack()

    def baixarVideo(self):
        urlVideo = self.url.get()
        diretorioVideo = self.diretorio.get()

        if urlVideo is None or diretorioVideo is None:
            self.errorMsg = "Preencha o formulario"
        else:
            video = YouTube(urlVideo).streams.get_highest_resolution()
            video.download(r'' + diretorioVideo)

            videoMP4 = diretorioVideo + '\\' + video.default_filename
            audioMP3 = diretorioVideo + '\\' + video.title + '.mp3'

            VideoClip = VideoFileClip(videoMP4)
            audioClip = VideoClip.audio

            audioClip.write_audiofile(audioMP3)

            subprocess.run(["explorer.exe", diretorioVideo + '\\' + video.default_filename])

root = Tk()
root.title("Music Download")
root.iconbitmap("icon.ico")
Application(root)
root.mainloop()