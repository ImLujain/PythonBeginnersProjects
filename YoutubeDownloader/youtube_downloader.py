import youtube_dl, sys, getopt

print(""" __ __         _       _          ____                _           _         
|  |  |___ _ _| |_ _ _| |_ ___   |    \ ___ _ _ _ ___| |___ ___ _| |___ ___ 
|_   _| . | | |  _| | | . | -_|  |  |  | . | | | |   | | . | .'| . | -_|  _|
  |_| |___|___|_| |___|___|___|  |____/|___|_____|_|_|_|___|__,|___|___|_| """)



def file_format(video_url, video_format):


    video_info = youtube_dl.YoutubeDL().extract_info(
    url = video_url,download=False)

    #print(video_info)

    filename = f"{video_info['title']}.mp3"
    print(filename)
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

if __name__=='__main__':
    video_url = None
    video_format = None
    argv = sys.argv[1:]
    # try:
    opts, args = getopt.getopt(argv, "l:f:", ['link=',  'format='] )
    for opt, arg in opts:
            if opt in ['-l', '--link']:
                video_url = arg
            elif opt in ['-f', '--format']:
                video_format = arg
    file_format(video_url, video_format)
    # except Exception as e:
    #     print("Usage: Pyhton youtube_downloader.py --url --format")
    #     print(e)



