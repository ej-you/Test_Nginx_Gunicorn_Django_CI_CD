# Test_Nginx_Gunicorn_Django_JS

## Status of deployment:
[![All-Project-CD](https://github.com/Danil-114195722/Test_Nginx_Gunicorn_Django_CI_CD/actions/workflows/aeza_deploy_project.yml/badge.svg)](https://github.com/Danil-114195722/Test_Nginx_Gunicorn_Django_CI_CD/actions/workflows/aeza_deploy_project.yml)

<br>

.env file must contain the next info:

```dotenv
# Ключ django
SECRET_KEY='django-insecure-your-key'
# True/False
DEBUG=True-or-False
# IP/DNS через пробел
ALLOWED_HOSTS='your dns and/or ip'

# имя БД
MYSQL_DATABASE=db-name
# имя юзера
DB_USER=root
# пароль юзера
MYSQL_ROOT_PASSWORD=your-passwd
# IP БД
DB_HOST=db
# порт БД
PORT=33066
```

<hr>
