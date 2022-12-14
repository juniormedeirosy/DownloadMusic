from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import subprocess

class Application:
    def __init__(master=None):
        print('██████╗░░█████╗░██╗██╗░░██╗░█████╗░██████╗░  ██╗░░░██╗██╗██████╗░███████╗░█████╗░  ███████╗')
        print('██╔══██╗██╔══██╗██║╚██╗██╔╝██╔══██╗██╔══██╗  ██║░░░██║██║██╔══██╗██╔════╝██╔══██╗  ██╔════╝')
        print('██████╦╝███████║██║░╚███╔╝░███████║██████╔╝  ╚██╗░██╔╝██║██║░░██║█████╗░░██║░░██║  █████╗░░')
        print('██╔══██╗██╔══██║██║░██╔██╗░██╔══██║██╔══██╗  ░╚████╔╝░██║██║░░██║██╔══╝░░██║░░██║  ██╔══╝░░')
        print('██████╦╝██║░░██║██║██╔╝╚██╗██║░░██║██║░░██║  ░░╚██╔╝░░██║██████╔╝███████╗╚█████╔╝  ███████╗')
        print('╚═════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝╚═════╝░╚══════╝░╚════╝░  ╚══════╝')
        print('░█████╗░██╗░░░██╗██████╗░██╗░█████╗░')
        print('██╔══██╗██║░░░██║██╔══██╗██║██╔══██╗')
        print('███████║██║░░░██║██║░░██║██║██║░░██║')
        print('██╔══██║██║░░░██║██║░░██║██║██║░░██║')
        print('██║░░██║╚██████╔╝██████╔╝██║╚█████╔╝')
        print('╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝░╚════╝░')
        print('\n')
        print("URL VIDEO")
        urlVideo = input("-> ")
        print("DIRETORIO DE SALVAMENTO DOS ARQUIVOS")
        dirFile = input("-> ")
        print('\n')

        if urlVideo == '' or dirFile == '':
            print("Preencha os dados necessarios!!!")
        else:
            print("Aguarde...")

            #DOWNLOAD VIDEO
            video = YouTube(urlVideo).streams.get_highest_resolution()
            video.download(r'' + dirFile)

            #CONVERT VIDEO TO AUDIO
            videoMP4 = dirFile + '\\' + video.default_filename
            audioMP3 = dirFile + '\\' + video.title + '.mp3'

            VideoClip = VideoFileClip(videoMP4)
            audioClip = VideoClip.audio

            audioClip.write_audiofile(audioMP3)
            #OPEN VIDEO LOCATION
            subprocess.run(["explorer.exe", dirFile + '\\' + video.default_filename])

            print("Sucesso ao salvar os arquivos")

Application()
