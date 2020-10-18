import pafy
import youtube_dl

url = "https://youtu.be/ZPSUimDt7N8?list=RDZPSUimDt7N8"
video = pafy.new(url)

audiostreams = video.audiostreams
for i in audiostreams:
    print(i.bitrate,i.extension, i.get_filesize())


audiostreams[3].download()