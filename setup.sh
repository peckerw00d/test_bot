python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

mkdir -p sqlite/
mkdir -p downloads/

chmod 600 .env
chmod -R 700 sqlite/
chmod -R 700 downloads/

echo "Проект успешно настроен. Запустите проект командой: source venv/bin/activate && python main.py"