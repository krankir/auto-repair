# auto-repair-shop
Приложение для авторемонтной организации. Реализован доступ к заявке на разных этапах работы, разными членами персонала, от написания заявки клиентом до подтверждения качества ремонта мастером(со всеми промежуточными стадиями).

### В проекте реализованно:
- **Блокировка конкретных IP адресов, с занисением в чёрный список**
- **Регистрация с подтверждением через email**
- **Добавлены транзакции на уровне проекта с выводом ошибок в формате JSON**
- **регистрация пользователей через подтверждение по электронной почте**

### Технологии:

Python, Django, PostgreSQL

### Пользовательские роли
- **CUSTOMER (Клиент)** — создаёт заявку на ремонт.
- **TECHNICIAN (Техник)** — просматривает заявку, корректирует и принимает её в работу.
- **WORKER (Слесарь)** — берёт заявку в работу, после окончания работ закрывает заявку.
- **MASTER (Мастер)** — проверяет выполнение работ, вследствие чего он может закрыть заявку либо отправить на переработку.

## Как запустить проект локально

1. Скачайте код проекта с GitHub
```
git clone https://github.com/krankir/auto-repair
```
2. Создайте виртуальное окружение, активируйте его и установите зависимости
```
python -m venv venv
source venv/Scripts/activate если у вас Windows
source venv/bin/activate если у вас macOS или Linux
pip install -r requirements.txt
```
3. Перейдите в директорию auto_repair_shop/ и выполните миграции
```
python manage.py migrate
```
4. Запустите сервер
```
python manage.py runserver
```
5. Откройте сайт в браузере
```
http://127.0.0.1:8000/
```

### Автор backend'а:

Редько Анатолий 2023 г.
