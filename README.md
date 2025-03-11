# fastapi-microservice

## Описание

Простой микросервис по типу https://reqres.in, реализованный с помощью FastAPI.
Сервис предоставляет возможность совершать различные операции с пользователями:<br><br>
-Получить список пользователей<br>
-Получить пользователя по ID<br>
-Добавить пользователя<br>
-Изменить пользователя<br>
-Удалить пользователя<br>

Для проверки качества микросервиса написаны автотесты.

## Структура проекта

```
fastapi-microservice/
├── app/                         # Корневая папка для микросервиса
   ├── data/
      └── utils.py               # Методы для работы с json списка пользователей (загрузить/сохранить)
      └── users.json             # Список пользователей
   ├── models/
      └── models.py              # Модели FastAPI
   ├── tests/
      └── conftest.py            # Конфигурационный файл pytest
      └── test_users.py          # Файл с автотестами
├── reqres-tests/                # Корневая папка для тестов reqres.in
    └── conftest.py              # Конфигурационный файл pytest
    └── test_users.py            # Автотесты для проверки юзеров
    └── test_auth.py             # Автотесты для проверки авторизации (регистрация/логин)
├── requirements.txt             # Зависимости проекта
└── README.md                    # Документация

```

## Установка

Чтобы установить и запустить проект, выполните следующие шаги:

Клонируйте репозиторий:

```bash
      git clone https://github.com/fastapi-reqres-clone.git
```

Перейдите в каталог проекта:

```bash
    cd fastapi-microservice
```

Создайте и активируйте виртуальную среду:

```bash
    python3 -m venv .venv
source .venv/bin/activate  # Для Linux/MacOS
.venv\Scripts\activate     # Для Windows
```

Установите зависимости:

```bash
  pip install -r requirements.txt
```

## Запуск приложения

Чтобы запустить приложение, перейдите в корневую директорию и используйте команду:

```bash
   cd app
   python main.py
```

Приложение будет доступно по адресу http://localhost:8000

## API

**Получить список пользователей**<br>
GET /api/users/

Возвращает список всех пользователей.

Пример ответа:

```
{"results": [
     {
       "id": 1,
       "email": "janet.weaver@fast.api",
       "first_name": "Janet",
       "last_name": "Weaver"
     },
     {
       "id": 2,
       "email": "andrew.green@fast.api",
       "first_name": "Andrew",
       "last_name": "Green"
     }
   ]
}
```

**Получить пользователя по ID**<br>
GET /api/users/{user_id}

Получает информацию о пользователе по его ID.<br>
Пример ответа:

```
{"results" : {
      "id": 1,
      "email": "janet.weaver@fast.api",
      "first_name": "Janet",
      "last_name": "Weaver"
   }
}
```

**Создать нового пользователя**<br>
POST /api/users/

Создает нового пользователя.

Пример тела запроса:

```
{
     "email": "testmail@google.com",
     "first_name": "Jacob",
     "last_name": "Baskin"
 }
```

Пример ответа:

```
{
   "message": "User Created",
   "results": {
      "id": 5,
      "email": "testmail@google.com",
      "first_name": "Jacob",
      "last_name": "Baskin"
   }
}
```

**Обновить пользователя**<br>
PATCH /api/users/{user_id}

Обновляет информацию о пользователе.

Пример тела запроса:

```
{
     "email": "newmail@google.com",
     "first_name": "Robert",
     "last_name": "Roberts"
}
```

Пример ответа:

```
{
   "message": "User Successfully Updated",
   "results": {
      "id": 3,
       "email": "newmail@google.com",
       "first_name": "Robert",
       "last_name": "Roberts"
   }
}
```

**Удалить пользователя**<br>
DELETE /api/users/

Удаляет пользователей по ID.

Пример тела запроса:

```
{
     "ids": [3, 4]
}
```

Пример ответа:

```
{
   "message": f"Users [3, 4] Successfully Deleted",
   "results": [
      {
       "id": 1,
       "email": "janet.weaver@fast.api",
       "first_name": "Janet",
       "last_name": "Weaver"
      },
      {
       "id": 2,
       "email": "andrew.green@fast.api",
       "first_name": "Andrew",
       "last_name": "Green"
      }
   ]
}
```

## Тесты

Тесты написаны с помощью pytest и моковых данных.

**Запуск тестов**<br>
Для запуска тестов перейдите в корневую директорию микросервиса и выполните команду:

```bash
   cd app
   pytest
```

Список тестов:<br>
-Получить список пользователей<br>
-Получить пользователя по ID<br>
-Создать двух пользователей<br>
-Изменить пользователя<br>
-Удалить двух пользователей<br>
