#!/usr/bin/python3
import vlc
import pafy
import threading
import requests
import time

server_url = "http://10.186.115.241:8000/youtube-remote-player/1/"

class RequestData:
    def __init__(self, json_data):
        self.is_playing = json_data["isPlaying"]
        self.current_link = json_data["currentLink"]

        data = json_data["playList"].split("|")
        self.play_name_list = data[0::2]
        self.play_link_list = data[1::2]
        self.json_data = json_data

class YoutubeAudioPlayer:
    def __init__(self, json_data):
        self.request_data = RequestData(json_data)
        self.lock = threading.Lock()

        self.is_playing = False
        self.current_link = ""

        self.play_link_list = self.request_data.play_link_list

    def mediaEndCallback(self, event, data):
        self.lock.acquire()
        self.play_link_list = self.request_data.play_link_list

        if self.current_link in self.play_link_list:
            current = self.play_link_list.index(self.current_link)
            if self.play_link_list[current] == self.play_link_list[-1]:
                current = 0
            else:
                current = current + 1
        else:
            current = 0
        self.current_link = self.play_link_list[current]

        data = self.request_data.json_data
        data["currentLink"] = self.current_link
        result = requests.put(server_url, json=data)

        self.lock.release()

        print("mediaEndCallback : " + self.current_link);
        self.play(self.current_link)

    def play(self, link):
        self.lock.acquire()
        if link in self.play_link_list:
            self.current_link = link

            media = pafy.new(link)
            best_audio = media.getbestaudio()
            self.player = vlc.MediaPlayer(best_audio.url)
            self.eventManager = self.player.event_manager()
            self.eventManager.event_attach(vlc.EventType.MediaPlayerEndReached, self.mediaEndCallback, None)
            self.player.play()
            self.is_playing = True
            print("play : " + link)
        else:
            print("This link is not in playlist : " + link)
        self.lock.release()

    def stop(self):
        self.lock.acquire()
        self.player.stop()
        self.is_playing = False
        self.lock.release()
        print("stop")

    def getCurrentLink(self):
        return self.current_link

    def syncWithServer(self):
        while True:
            time.sleep(1)
            self.lock.acquire()

            result = requests.get(server_url)
            if result.status_code != 200:
                print("GET operation error")
            else:
                print(result.json())
                self.request_data = RequestData(result.json())
            self.lock.release()

            if self.current_link != self.request_data.current_link:
                if self.is_playing == True:
                    self.stop()
                self.current_link = self.request_data.current_link

            if self.is_playing == False and self.request_data.is_playing == True:
                self.play(self.getCurrentLink())

            if self.is_playing == True and self.request_data.is_playing == False:
                self.stop()

if __name__ == "__main__":
    result = requests.get(server_url)
    if result.status_code != 200:
        print("GET operation error")
    else:
        print(result.json())

    player = YoutubeAudioPlayer(result.json())
    if (player.request_data.is_playing):
        player.play(player.request_data.current_link)

    player.syncWithServer()
