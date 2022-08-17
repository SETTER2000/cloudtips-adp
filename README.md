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
Зависимости разрешить [^1]
```angular2html
pip install python-dotenv requests python-magic loguru
```
### Настройка переменных окружения
В корне проекта создать файл .env 

*Файл .env используется для тестов. В production установить переменные 
окружения уровня сеанса пользователя или системы.*

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

#  Работа с пакетом
### Работа с тестовым сервисом
Установка соединения c песочницей (тестовый сервис CloudTips)
* Эта инструкция обязательна в любом файле где используется пакет
```angular2html
cta.connect(sandbox=True)
```
### Работа с Production Serves
После тестирования для работы с production сервисом поменяйте данные в файле .
env и уберите "sandbox=True" из сonnect.
```angular2html
cta.connect()
```

### В общем установка зависимостей для модуля выглядит так. Вариант для работы с sandbox.
```angular2html
from cloudtipsadp import Cloudtipsadp

cta = Cloudtipsadp()
cta.connect(sandbox=True)
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
#### Загрузка фотографии получателя
```angular2html
response = cta.receivers_photo(cta.receivers(user_id, photo_path))
```

#### Вариант просмотра результата ответа сервера
```angular2html
if type(response) == dict and response.get('succeed'):
    print(response.get('data'))
else:
    print(response)
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

## Транзакции
#### Получение всех транзакций выплат получателям менеджера
```angular2html
response = cta.payouts_get(cta.payouts())
```

### Возможные проблемы
____

[^1]: Если возникли проблемы с установкой пакета python-magic на macos 
установите:
```angular2html
brew install libmagic 
```