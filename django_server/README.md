# django_server
This server is for providing player REST api.
At this project, we will use just one playlist only. So we don't use post and delete API.
If you use this api, this server can be broken.

# run
python3 manage.py runserver 0.0.0.0:8000

# db init
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate

# GET example
curl -X GET http://127.0.0.1:8000/youtube-remote-player/1/

# PUT example
curl -X PUT -d 'isPlaying=false' -d 'currentLink=https://www.youtube.com/watch?v=3iM_06QeZi8' -d 'playList=내 손을 잡아|https://www.youtube.com/watch?v=3iM_06QeZi8|잠 못 드는 밤 비는 내리고|https://www.youtube.com/watch?v=m7mvpe1fVa4' http://127.0.0.1:8000/youtube-remote-player/1/
