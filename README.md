# Choropleth-Map
Choropleth Map to show some data using Flask.
Project also contain script file to fast install on Ubuntu.

Some instructions to run it on Ubuntu or Windows(Vagrant)

  Инструкция по запуску в Ubuntu
1) Необходимо переместить архив в удобную вам директорию.
2) Далее заходим в терминал и вводим следующие значения:
sudo unzip Choropleth-Map-master.zip && sudo ./start.sh
3) После окончания установки перейдите в директорию  с приложением, откройте консоль и введите:
python main.py

	Инструкция по запуску через Vagrant(Windows)
1) Переходим на сайт Virtual Box и скачиваем последнюю версию. 
2) Переходим на сайт Vagrant и скачиваем последнюю версию. 
3) Создаем директорию в удобном месте.
4) Помещаем в неё файл, который можно скачать в источнике.
http://vm.datascience-school.com/content/files/python/Vagrantfile
5) Добавляем строку в этот файл (Открыть с помощью Notebook)
master.vm.network :forwarded_port, host: 8080, guest: 8080, auto_correct: true
6) Зажимаем Shift и нажимаем правой кнопкой мыши, нажимаем «Открыть окно команд здесь»
7) Вводим следующее:
vagrant up
vagrant ssh
8) Необходимо переместить архив в директорию с Vagrantfile. 
9) Далее заходим в терминал и вводим следующие значения:
sudo unzip Choropleth-Map-master.zip && sudo ./start.sh
10) После окончания установки перейдите в директорию  с приложением, откройте консоль и введите:
python main.py

Screenshots of results in folder 'screenshots':







