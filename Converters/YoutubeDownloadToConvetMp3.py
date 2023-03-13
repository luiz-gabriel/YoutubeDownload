from __future__ import unicode_literals

import uuid

import yt_dlp as youtube_dl

class generateFileName:
    def id():
        return uuid.uuid4().hex

class Mp3DownloadAndToConvert:
    def download(link):
        fileName = generateFileName.id()

        ydl_opts = {
            'format': 'bestaudio/best',
            'ignoreerrors': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }, ],
            'outtmpl': 'files/' + generateFileName.id()
        }
        you_dl = youtube_dl.YoutubeDL(ydl_opts)
        if you_dl.extract_info(link, download=False)['duration'] / 60 > 20:
            return {}, 401
        else:
             try:
                 with you_dl as ydl:
                    ydl.download([link])
                    return {"file": fileName}, 200
             except:
                 return {}, 500






