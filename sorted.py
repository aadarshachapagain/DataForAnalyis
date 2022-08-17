import os
import glob
import shutil
from os import path
import pathlib


currentpath = pathlib.Path().resolve()
filename = [f for f in os.listdir('.') if os.path.isfile(f)]

pdfs = ['.pdf']
words = ['.docx', '.doc', '.txt']
media = ['.jpeg', '.jpg', '.svg', '.png', '.PNG', '.mp4', '.mp3']
setupFiles = ['.java', '.msi']
compressedFiles = ['.zip']
files = ['.apk']
WordsLocation = pathlib.PurePath(currentpath, 'Words')
PdfsLocation = pathlib.PurePath(currentpath, 'Pdfs')
mediaLocation = pathlib.PurePath(currentpath, 'Media')
setupFilesLocation = pathlib.PurePath(currentpath, 'SetupFiles')
compressedFilesLocation = pathlib.PurePath(currentpath, 'CompressedFiles')
FilesLocation = pathlib.PurePath(currentpath, 'Otherfiles')

for file in filename:
    if os.path.splitext(file)[1] in pdfs:
        if(path.exists(PdfsLocation)):
            shutil.move(file, PdfsLocation)
        else:
            os.mkdir(PdfsLocation)
            shutil.move(file, PdfsLocation)
    if os.path.splitext(file)[1] in words:
        if(path.exists(WordsLocation)):
            shutil.move(file, WordsLocation)
        else:
            os.mkdir(WordsLocation)
            shutil.move(file, WordsLocation)
    if os.path.splitext(file)[1] in media:
        if(path.exists(mediaLocation)):
            shutil.move(file, mediaLocation)
        else:
            os.mkdir(mediaLocation)
            shutil.move(file, mediaLocation)
    if os.path.splitext(file)[1] in setupFiles:
        if(path.exists(setupFilesLocation)):
            shutil.move(file, setupFilesLocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file, setupFilesLocation)
    if os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(compressedFilesLocation)):
            shutil.move(file, compressedFilesLocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file, compressedFilesLocation)
    if os.path.splitext(file)[1] in files:
        if(path.exists(FilesLocation)):
            shutil.move(file, FilesLocation)
        else:
            os.mkdir(FilesLocation)
            shutil.move(file, FilesLocation)
