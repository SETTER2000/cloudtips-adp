# cloudtips-adp
CloudTips Adapter позволяет интегрировать прием донатов в Django приложение.

## Старт
Установка
```angular2html
pip install cloudtipsadp
```
### Настройка переменных окружения в файле .env
*В корне проекта создать файл .env 

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


