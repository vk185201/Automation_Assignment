from pytube import YouTube

# location of save videos
SAVE_PATH = "Downloads/ytFolder/"

# link of the video to be downloaded
# opening the file
link = open('links_file.txt', 'r')

for i in link:

    youtubeObject = YouTube(i)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(SAVE_PATH)
    except:
        print("An error has occurred while downlaoding")
print('Download Completed!')
