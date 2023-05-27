<<<<<<< HEAD
# EOR

Порядок установки 

cd ./learning_platform
pip -m pip install Django
pip -m pip install rsa
python -m pip install Pillow
python manage.py runserver
=======
Здравствуйте! 
Вашему вниманию представляется интерактивная образовательная платформа по модулю "Криптография"

Чтобы быстро развернуть наш проект вам потребуется Docker

Если у вас есть Docker, то для запуска пропишите из корневого католога проекта(EOR) следующие команды:

- docker-compose up 

И далее в браузере следует прописать адрес http://127.0.0.1:8000/

Если у вас нет Docker, то необходимо его устаовить, следуя следующим шагам:

LINUX:

- sudo apt update

- sudo apt install apt-transport-https ca-certificates curl software-properties-common

- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

- sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"

- sudo apt update

- apt-cache policy docker-ce

- sudo apt install docker-ce

- sudo docker-compose install

Далее действуем пошагово, как было указано в начале: 

- docker-compose up 



>>>>>>> 67cb884e5494a68b62488be5ef1012b71a3a14e7
