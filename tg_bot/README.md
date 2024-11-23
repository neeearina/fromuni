# Telegram bot

> Данный проект реализован по статье https://habr.com/ru/companies/amvera/articles/844092/.
> Пример телеграмм бота для проведения тестов, где вопросы и ответы хранятся в разных вкладках одной Google-таблицы.

# Инструкция по запуску проекта

### Получение API ключей

> Заполнить файл *credentials.json*, следуя [инструкции по ссылке](https://docs.gspread.org/en/latest/oauth2.html).
> Содержимое будет выглядеть примерно так:

```json
{
  "type": "service_account",
  "project_id": "api-project-XXX",
  "private_key_id": "2cd … ba4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nNrDyLw … jINQh/9\n-----END PRIVATE KEY-----\n",
  "client_email": "473000000000-yoursisdifferent@developer.gserviceaccount.com",
  "client_id": "473 … hd.apps.googleusercontent.com",
  ...
}
```

### Содержимое файла *config.py*

> Перед запуском проекта все данные поля должны быть заполнены

- *CREDENTIALS_FILENAME* - путь до файла с API ключами (*credentials.json* по умолчанию)
- *QUESTIONS_SPREADSHEET_URL* - ссылка на файл с таблицей. Её необходимо создать самостоятельно
- *BOT_TOKEN* - токен от телеграм бота, можно получить у *@BotFather*

### Установка зависимостей проекта

> Выполните в терминале команду, которая установит все необходимые зависимости:

 ```commandline
pip install -r requirements.txt
```

### Запуск

> Запустите файл *main.py*, после этого можно работать с ботом.
