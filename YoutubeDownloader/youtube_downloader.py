import youtube_dl, sys, getopt

print(""" __ __         _       _          ____                _           _         
|  |  |___ _ _| |_ _ _| |_ ___   |    \ ___ _ _ _ ___| |___ ___ _| |___ ___ 
|_   _| . | | |  _| | | . | -_|  |  |  | . | | | |   | | . | .'| . | -_|  _|
  |_| |___|___|_| |___|___|___|  |____/|___|_____|_|_|_|___|__,|___|___|_| """)



def file_format():

    video_url = None
    video_format = None
    argv = sys.argv[2:]

    try:
        opts, args = getopt.getopt(argv, "u:f:", 
                    ["video_url =",
                    "video_format ="])

    except:
        print("Usage: Pyhton youtube_downloader.py --url --format")

    for opt, arg in opts:
        if opt in ['-u', '--url']:
            video_url = arg
        elif opt in ['-f', '--format']:
            video_format = arg

    video_info = youtube_dl.YoutubeDL().extract_info(
    url = video_url,download=False)

    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    download(options, video_url, video_format)


def download(options, video_info, filename):

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
        file_format()


