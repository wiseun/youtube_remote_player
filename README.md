# What is youtube_remote_player
My wife wants using her smart phone and playing youtube same time.
For this, I plan simple web server system using Raspberry Pi.
This is youtube_remote_player

# Requirement
These are simple senario and requirment.
* User request to play with youtube URL.
* User request to stop.
* User request to play with other youtube url during playing.

# Physical configuration diagram
This is physical configuration diagram
```
┌─────────────┐   ┌─────────────┐   ┌──────────────┐ 
│ Smart phone │───│ WiFi router |───| Raspberry Pi |
└─────────────┘   └─────────────┘   └──────────────┘
```

# Logical configuration diagram
This is logical configuration diagram

```
┌───────────┐   ┌───────────────┐   ┌───────────────────────┐
│ html page │───│ django server |───| python youtube player |
└───────────┘   └───────────────┘   └───────────────────────┘
```

# Description
The project consists of three small modules. Modules are these.
* django_server
* html_page
* python_youtube_player
Please cheak each readme file.
