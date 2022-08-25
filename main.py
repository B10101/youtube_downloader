import pytube

def single_youtube_video():
    url = input('Enter a url: ')
    youtube_link_for_download = pytube.YouTube(url)
    a = youtube_link_for_download.streams.get_by_itag(22).download()
    

def playlists():
    url = input("Enter playlist url: ")
    youtube_link_for_download = pytube.Playlist(url)
    print(f'starting download of the playlist:')
    for i in youtube_link_for_download.videos:
        i.streams.get_by_itag(22).download()

playlists()
    
