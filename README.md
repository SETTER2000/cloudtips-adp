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

```angular2html
Grant_type=password
Client_id=Partner
UserName=<your_email>
Password=<your_password>
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
После тестирования и работы с production сервисом измените в файле .env или 
в вашем окружение данные и убрать SandboxClient из Connect.
```angular2html
connect = Connect()
```


