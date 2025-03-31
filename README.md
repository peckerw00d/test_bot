# Установка бота

1. Склонируйте репозиторий
```bash
git clone https://github.com/peckerw00d/test_bot
cd test_bot
```

2. Настройте переменные окружения

Создайте файл .env и заполните его:  
```
API_TOKEN=your_api_token
DB_PATH=your_db_path
DOWNLOADS_DIR=your_downloads_dir
```

3. Настройте проект
```bash
chmod +x setup.sh
./setup.sh
```

4. Запуск проекта
```bash
source venv/bin/activate
python main.py
```


