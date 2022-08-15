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

### В общем установка зависимостей для модуля выглядит так
```angular2html
from cloudtipsadp.clients import Connect, SandboxClient
from cloudtipsadp import Cloudtipsadp

connect = Connect(SandboxClient())
cta = Cloudtipsadp()
```


## Получатель
#### Создать получателя донатов

```angular2html
response = cta.receivers_create(cta.receivers(name, phone_number))
```
#### Все получатели донатов
```angular2html
response = cta.receivers_pages(cta.receivers())
```

#### Вариант просмотра результата ответа сервера
```angular2html
if response.get('succeed'):
    print(response.get('data'))
else:
    response.get('errors')
```


## Заведения
#### Информация по всем заведениям ТСП.
```angular2html
response = cta.places_get(cta.places())
```
#### Привязка получателя к заведению. Отправить сотруднику на его номер телефона код в смс сообщении.
```angular2html
response = cta.places_send_sms(cta.places(user_id))
```
#### Подтверждение привязки телефона (пользователя) к предприятию. Передать код из смс.
```angular2html
response = cta.places_confirm(cta.places(user_id, confirm_code))
```



## Карты
#### Список карт получателя
```angular2html
response = cta.cards_get(cta.cards(user_id))
```
#### Отправить криптограмму
```angular2html
response = cta.cards_auth(cta.cards(user_id, checkout))
```

## Накопления
#### Получить общую сумму донатов, по сотруднику
```angular2html
response = cta.accums_get(cta.accums(user_id))
```