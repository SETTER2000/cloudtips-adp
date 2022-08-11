# cloudtips-adp
CloudTips Adapter позволяет интегрировать прием донатов в Django приложение.

## Старт
Установка
```angular2html
pip install cloudtipsadp
```
Удаление пакета
```angular2html
pip uninstall cloudtipsadp
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
* Эта инструкция обязательна в любом файле где используется пакет
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
#### Установить зависимости
```angular2html
from cloudtipsadp.receivers import Receivers, receiver_create
```

#### Создать получателя донатов

```angular2html
response = receiver_create(Receivers(name, phone_number))
```

#### Вариант просмотра результата ответа сервера
```angular2html
if response.get('succeed'):
    print(response.get('data'))
else:
    response.get('errors')
```


## Заведения
#### Установить зависимости
```angular2html
from cloudtipsadp.places import (Places, place_send, place_get, place_confirm)
```
#### Информация по всем заведениям ТСП.
```angular2html
response = place_get(Places())
```
#### Привязка получателя к заведению. Отправить сотруднику на его номер телефона код в смс сообщении.
```angular2html
response = place_send(Places(user_id))
```
#### Подтверждение привязки телефона (пользователя) к предприятию. Передать код из смс.
```angular2html
response = place_confirm(Places(user_id, confirm_code))
```



## Карты
#### Установить зависимости
```angular2html
from cloudtipsadp.cards import Cards, card_get
```
#### Список карт получателя
```angular2html
response = card_get(Cards(user_id))
```

## Накопления
#### Установить зависимости
```angular2html
from cloudtipsadp.accumulations import Accumulations, acc_get
```
#### Получить общую сумму донатов, по сотруднику
```angular2html
response = acc_get(Accumulations(user_id))
```