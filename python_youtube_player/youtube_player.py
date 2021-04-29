#!/usr/bin/python3

import vlc
import pafy
import time


# url of the media
url = "https://youtu.be/SJk5Nks2Xvg"

# creating pafy object of the media
media = pafy.new(url)

# getting best audio stream
best_audio = media.getbestaudio()

# creating vlc media player object
player = vlc.MediaPlayer(best_audio.url)

# start playing video
player.play()

while True:
    time.sleep(1)
