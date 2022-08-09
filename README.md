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
* Эта конструкция обязательна в любом файле где используется пакет
```angular2html
connect = Connect(SandboxClient())
```
### Работа с Production Serves
После тестирования для работы с production сервисом поменяйте данные в файле .
env, уберите SandboxClient из Connect.
```angular2html
connect = Connect()
```
## Получатель
#### Создать получателя донатов
* name - обязательно
* phone_number - обязательно

Вариант 1
```angular2html
receiver = Receivers('Иван', '+79180060100')
response = receiver.create()
if response:
    print('Получатель создан: {response.get("data")}')
```
Вариант 2
```angular2html
receiver = Receivers('Иван', '+79180060100').create()
if receiver.get('succeed'):
    print(f'Получатель создан. {receiver}')
```

## Заведения
#### Получить информацию по всем заведениям ТСП
```angular2html
places = Places().get()
if places.get('succeed'):
    print(f'Все заведения: {places.get("data")}')
```

## Карты
#### Получение списка карт получателя
* user_id - обязательно
```angular2html
cards = Cards(user_id).get()
if cards.get('succeed'):
    print(cards.get('data'))
else:
    print(cards.get('errors'))
```

## Накопления
#### Получить общую сумму донатов, по сотруднику.
* user_id - обязательно
```angular2html
accumulations = Accumulations(user_id).get()
if accumulations.get('succeed'):
    print(accumulations.get('data'))
```