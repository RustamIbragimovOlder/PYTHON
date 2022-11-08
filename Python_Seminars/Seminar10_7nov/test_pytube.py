from pytube import YouTube


# def yt_download(url):
#     yt = YouTube(url)
#     yt.streams.filter(res="360p", file_extension="mp4").first().download(filename=f"name.mp4")

# yt_download(input())

yt = YouTube(url)
yt.streams.filter(res="360p", file_extension="mp4").first().download(filename=f"name.mp4")
print(yt.title)