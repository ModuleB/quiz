## Описание приложения 'Quiz':
<br>
Приложение принимает POST запросы на эндпойнт '/questions'
<br>Ожидает параметр 'questions_num' в диапазоне от 1 до 500
<br>Скачивает с сервиса jservice указанное количество вопросов. сохраняет их в базу данных.
<br>Возвращает последний сохраненный вопрос из предыдущего запроса.
<br>Приложение и база данных запускаются с помощью docker compose

### Доступно по адресу:
 - при локальном запуске: http://localhost:8020
 - на удаленном сервере: <b><i>http://< IP адрес сервера >:8020</b></i>

### Пример запроса: 
 - адрес: http://192.168.48.56:8020/questions
 - тип: <b><i>JSON</b></i>
 - содержимое: <b><i>{questions_num: 3}</b></i>




### Используемая база данных --> Postgres
Сохраняет данные в папку с приложением в директорию pg_data (данные сохраняются при удалении docker контейнера)
### Параметры подключения к базе данных:
 - POSTGRES_USER: <b><i>quiz</b></i>
 - POSTGRES_PASSWORD: <b><i>quiz</b></i>
 - POSTGRES_DB: <b><i>quiz</b></i>
 - PGPORT: <b><i>5434</b></i>
 - HOST:
   - при локальном запуске: <b><i>localhost</b></i>
   - на удаленном сервере: <b><i><IP адрес сервера></b></i>

<br><hr>

# Запуск приложения на локальном компьютере
На компьютере должны быть установлены: 
 - [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download/#section=mac)
 - [Docker](https://www.docker.com/)
 - [Postman](https://www.postman.com/)

## 1. Клонируем образ проекта с Github
### Запускаем PyCharm
<p><img src="https://i2.paste.pics/c9f2f9773ec79ce587248544f5d90b88.png"
alt="Запускаем PyCharm"></p>

### Создаем новый проект
<p><a href="https://i2.paste.pics/47127d601043f2b29194c07e4fbf8178.png">
<img src="https://i2.paste.pics/47127d601043f2b29194c07e4fbf8178.png"
width="700" alt="Создаем новый проект"></a></p>

### Вводим ссылку на проект
https://github.com/ModuleB/quiz.git
<p><a href="https://i2.paste.pics/23fcebef19579c5b3f4cc796b077763e.png">
<img src="https://i2.paste.pics/23fcebef19579c5b3f4cc796b077763e.png"
width="700" alt="Вводим ссылку на проект"></a></p>

### Разрешаем исполнение
<p><a href="https://i2.paste.pics/75974628a1aa67fdc92a20962e70a865.png">
<img src="https://i2.paste.pics/75974628a1aa67fdc92a20962e70a865.png"
width="500" alt="Разрешаем исполнение"></a></p>

### Запускаем Docker и возвращаемся в PyCharm
<p><img src="https://i2.paste.pics/a5831ce97c0d896040d339736b5eaf27.png"
alt="Запускаем Docker и возвращаемся в PyCharm"></p>

## 2. Собираем образ:
### Во вкладке 'терминал' вводим команду:
```docker compose build```
<p><a href="https://i2.paste.pics/2f0bf1ddcda9dcf1bedb591f88dc0597.png">
<img src="https://i2.paste.pics/2f0bf1ddcda9dcf1bedb591f88dc0597.png"
width="700" alt="Переходим в Docker и убеждаемся, что все работает"></a></p>

## 3. Запускаем образ:
```docker compose up -d```

### Переходим в Docker и убеждаемся, что все работает
<p><a href="https://i2.paste.pics/4897d158c1f30956b780feaff5ab7b49.png">
<img src="https://i2.paste.pics/4897d158c1f30956b780feaff5ab7b49.png"
width="700" alt="Переходим в Docker и убеждаемся, что все работает"></a></p>

## 4. Тестируем:
### Запускаем Postman:
<p><img src="https://i2.paste.pics/3ea7d62d43458a4fe610500b1f6af184.png"
alt="Запускаем Postman"></p>

### Устанавливаем параметры запроса
тип: <b><i>POST</u></b>
<br>адрес: http://localhost:8020/questions/
<br>контент: <i><b>body --> row</b></u>
<br>тип контента: <i><b>JSON</b></u>
<br>параметры: <i><b>{"questions_num": "ЧИСЛО ОТ 0 ДО 500"}</b></u>

<p><a href="https://i2.paste.pics/c74b2217d40140185ce2fd61857df78e.png">
<img src="https://i2.paste.pics/c74b2217d40140185ce2fd61857df78e.png"
width="600" alt="Устанавливаем параметры запроса"></a></p>

### Отправляем запрос:
<p><img src="https://i2.paste.pics/460a8804ab339c5a8322b4743cbe11c7.png"
width="120" alt="SEND"></p>

При первой попытке запроса, получаем пустой объект, так как база данных пустая.
<br>При последующих запросах, приложение будет отправлять последний сохраненный вопрос.

### Завершаем приложение:
```docker compose stop```

<br><hr>
# Запуск приложения на удаленном сервере
На сервере должен быть установлен Docker. <a href="https://docs.docker.com/engine/install/">Инструкция</a>
### Повторяем пункт 1 из предудущего руководства.
В последующих командах заменяем root --> на имя вашего пользователя на сервере, 192.168.0.1 --> на ip адрес вашего сервера
### Подключаемся к серверу
В терминале вводим команду:
```ssh root@192.168.0.1```
### Создаем папку для приложения
```mkdir quiz```
### Отключаемся от сервера
```exit```
### Копируем файл Docker
```scp Dockerfile root@192.168.0.1:quiz/Dockerfile```
### Копируем файл docker-compose.yml
```scp docker-compose.yaml root@192.168.0.1:quiz/docker-compose.yaml```
### Вновь подключаемся к серверу
```ssh root@192.168.0.1```
### Переходим в папку quiz
```cd quiz```
### Скачиваем docker образ
```docker compose pull```
### Запускаем
```docker compose up -d```
### Тестируем так же как и на локальном компьютере (пункт 4 в предыдущем руководстве)
Для отправки запросов в Postman меняем адрес с 'localhost' на IP адрес вашего сервера, например http://192.168.0.1:8020/questions/

### Завершаем приложение:
```docker compose stop```
<br>
<br>
<hr>

# Доступ к базе данных
Для доступа к базе данных можно использовать программу
[pgAdmin](https://www.pgadmin.org/download/).

## Создаем новое подключение
<p><a href="https://i2.paste.pics/fea43104a39e39436d80026c92ea2a72.png">
<img src="https://i2.paste.pics/fea43104a39e39436d80026c92ea2a72.png" 
width="500 alt="Создаем новое подключение"></a></p>


### <i><b>Вкладка 'General'</b></i>
Name: Любое имя на ваш выбор
<p><a href="https://i2.paste.pics/ea6fd76b2641b9dff15a422c72065ad5.png">
<img src="https://i2.paste.pics/ea6fd76b2641b9dff15a422c72065ad5.png"
width="400" alt="Вкладка 'General'"></a></p>


### Вкладка 'Connection'
user: <i><b>quiz</b></u>
<br>password: <i><b>quiz</b></u>
<br>port: <i><b>5434</b></u>
<br>host:
 - если приложение запущено локально: <i><b>localhost</b></u>
 - если работает на удаленном сервере: <i><b>< IP адрес сервера ></b></u>


<p><a href="https://i2.paste.pics/278bced929716253a8d1b145472763ab.png">
<img src="https://i2.paste.pics/278bced929716253a8d1b145472763ab.png"
width="400" alt="Вкладка 'Connection'"></a></p>

### Сохраняем
<p><img src="https://i2.paste.pics/eada6d9513c6e55918f38c6dc05bc6c1.png"
width="120" alt="Сохраняем"></p>

## Получаем данные
### Переходим к таблице 'quiz'
<p><a href="https://i2.paste.pics/c272a61826f05301b1d821adf690c587.png">
<img src="https://i2.paste.pics/c272a61826f05301b1d821adf690c587.png"
width="700" alt="Переходим к таблице 'quiz'"></a></p>

### Выбираем пункт 'View Data --> All Rows'
<p><a href="https://i2.paste.pics/931edde38f73d0e248b839f8fa092346.png">
<img src="https://i2.paste.pics/931edde38f73d0e248b839f8fa092346.png"
width="400" alt="Выбираем пункт 'View Data --> All Rows'"></a></p>

### Получаем данные:
<p><a href="https://i2.paste.pics/44de8cb3d51e49073691e2b6ed5c6bca.png">
<img src="https://i2.paste.pics/44de8cb3d51e49073691e2b6ed5c6bca.png"
width="700" alt="Получаем данные"></a></p>


