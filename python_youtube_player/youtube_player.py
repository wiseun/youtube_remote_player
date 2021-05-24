#!/usr/bin/python3
import vlc
import pafy
import time
import threading

class YoutubeAudioPlayer:
    def __init__(self, playlist):
        self.playlist = playlist
        self.currentlink = None
        self.lock = threading.Lock()
        
    def mediaEndCallback(self, event, data):
        self.lock.acquire()
        if self.currentlink in self.playlist:
            current = self.playlist.index(self.currentlink)
            if self.playlist[current] == self.playlist[-1]:
                current = 0
            else:
                current += 1            
        else:
            current = 0
        self.currentlink = self.playlist[current]
        self.lock.release()
        
        print("mediaEndCallback : " + self.currentlink);
        self.play(self.currentlink)       
    
    def addItem(self, link):
        self.lock.acquire()
        if link in self.playlist:            
            self.lock.release()
            print("add fail")
            return False
        else:
            self.playlist.append(link)            
            self.lock.release()
            print("add : " + link)
            return True        

    def removeItem(self, link):
        self.lock.acquire()
        if link in self.playlist:
            self.playlist.remove(link)
            self.lock.release() 
            print("remove : " + link)
            return True
        else:
            self.lock.release()
            print("remove fail")
            return False
           
    def play(self, link):
        self.lock.acquire()
        if link in self.playlist:
            self.currentlink = link
        
            media = pafy.new(link)            
            best_audio = media.getbestaudio()
            self.player = vlc.MediaPlayer(best_audio.url)
            self.eventManager = self.player.event_manager()
            self.eventManager.event_attach(vlc.EventType.MediaPlayerEndReached, self.mediaEndCallback, None)   
            self.player.play()
            print("play : " + link)
        self.lock.release()
    
    def stop(self):
        self.lock.acquire()
        self.player.stop()
        self.currentlink = None
        self.lock.release()
        print("stop")
        
    def getCurrentLink(self):        
        return self.currentlink
    
    def dump(self):
        self.lock.acquire()
        for item in self.playlist:
            print(item)
        self.lock.release()   

if __name__ == "__main__":
    playlist = [
        "https://youtu.be/y_rtkY1AJ-c",        
        "https://youtu.be/AJPLgrfBiBo",
        "https://youtu.be/5GrKuaXBg4k",
        "https://youtu.be/3iM_06QeZi8"
    ]
    
    player = YoutubeAudioPlayer(playlist)
    player.play("https://youtu.be/y_rtkY1AJ-c")
    
    player.removeItem("https://youtu.be/AJPLgrfBiBo")
    player.addItem("https://youtu.be/AJPLgrfBiBo")
        
    time.sleep(1000)
    
    player.stop()
