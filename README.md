# cloudtips-adp
CloudTips Adapter позволяет интегрировать прием донатов в Django приложение.

## Старт
Установка
```angular2html
pip install cloudtipsadp
```
Зависимости разрешить 
```angular2html
pip install python-dotenv requests
```
### Настройка переменных окружения
В корне проекта создать файл .env 

```angular2html
sudo touch .env
```
Для авторизации на CloudTips добавить настройки в файл .env

placeId - идентификатор вашего заведения (в админке CloudTips)

```angular2html
Grant_type=password
Client_id=Partner
UserName=<your_email>
Password=<your_password>

placeId=<your_placeId>
```

##  Работа с пакетом

```angular2html
from cloudtipsadp.clients import Connect, SandboxClient 
```
### Работа с тестовым сервисом
Установка соединения c песочницей (тестовый сервис CloudTips)
```angular2html
connect = Connect(SandboxClient())
```
### Работа с Production Serves
После тестирования и работы с production сервисом поменяйте данные в файле .
env 

и убрать SandboxClient из Connect.
```angular2html
connect = Connect()
```

## Создать получателя донатов
*Идемпотентный метод*

Вариант 1
```angular2html
receiver = Receivers('Иван', '+79180060100')
response = receiver.create_receiver()
if response:
    print('Получатель создан.')
```
Вариант 2
```angular2html
receiver = Receivers('Иван', '+79180060100').create_receiver()
```