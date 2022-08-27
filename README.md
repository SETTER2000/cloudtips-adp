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
pip install python-dotenv requests python-magic dependency-injector
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
CTA_GRANT_TYPE=password
CTA_CLIENT_ID=Partner
CTA_USER_NAME=<your_email>
CTA_PASSWORD=<your_password>
CTA_PLACE_ID=<your_placeId>

# Production. Раскомментировать
#CTA_BASE_URL = 'https://identity.cloudtips.ru'
#CTA_BASE_URL_API = 'https://api.cloudtips.ru/api'

# Production. Закомментировать
CTA_BASE_URL = 'https://identity-sandbox.cloudtips.ru'
CTA_BASE_URL_API = 'https://api-sandbox.cloudtips.ru'
```

#  Работа с пакетом

### Подключение 
```angular2html
from cloudtipsadp import Cloudtipsadp

cta = Cloudtipsadp()
```


## Получатель
#### Создать получателя донатов
```angular2html
response = cta.receivers_create(name, phone_number)
```
#### Удалить получателя из скоупа
```angular2html
response = cta.receivers_detach_agent(user_id)
```
#### Все получатели донатов
```angular2html
response = cta.receivers_pages()
```
#### Загрузка фотографии получателя
```angular2html
response = cta.receivers_photo(user_id, photo_path)
```

#### Вариант просмотра результата ответа сервера
```angular2html
if type(response) == dict and response.get('succeed'):
    print(response.get('data'))
else:
    print(response)
```


## Заведения
#### Информация по всем заведениям ТСП
```angular2html
response = cta.places_get()
```
#### Привязка получателя к заведению. Отправить сотруднику на его номер телефона код в смс сообщении.
```angular2html
response = cta.places_send_sms(user_id)
```
#### Подтверждение привязки телефона (пользователя) к предприятию. Передать код из смс.
```angular2html
response = cta.places_confirm(user_id, code)
```



## Карты
#### Список карт получателя
```angular2html
response = cta.cards_get(user_id)
```
#### Отправить криптограмму
```angular2html
response = cta.cards_auth(user_id, checkout)
```
#### Изменить карту, которая по умолчанию
```angular2html
response = cta.cards_default(user_id, card_token)
```
#### Удаление карты получателя. Карту по умолчанию удалить нельзя
```angular2html
response = cta.cards_delete(user_id, card_token)
```



## Накопления
#### Накопления по получателю
```angular2html
response = cta.accums_summary(user_id)
```
#### Выплата накопления получателю
```angular2html
response = cta.accums_payout_receiver(user_id)
```



## Транзакции
#### Получение всех транзакций выплат получателям менеджера
```angular2html
response = cta.payouts()
```

### Возможные проблемы
____

[^1]: Если возникли проблемы с установкой пакета python-magic на macos 
установите:

```angular2html
brew install libmagic 
pip uninstall python-magic
pip install python-magic-bin
```