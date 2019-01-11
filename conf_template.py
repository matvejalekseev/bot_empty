from aiosocksy import Socks5Auth
import os

# Определение режима запуска test или prom
mode = "test"
# Использование прокси, если True - необходима настройка прокси Socks5
use_proxy = False
# Токены бота для двух режимов, досточно заполнить только один и его использовать
telegrambot_test = ""
telegrambot_prom = ""
# определение файла для хранения БД для двух режимов
db_filename_test = "test_database.db"
db_filename_prom = "prom_database.db"
# определение файла для хранения лога для двух режимов
log_filename_test = "test.log"
log_filename_prom = "prom.log"

# определение списка администраторов бота, массивом идентификаторов пользователей в Телеграм
ADMIN_IDS = [109099327]

# Настройка прокси Socks5
proxy_url = 'socks5://ip:port'
proxy_login = 'login'
proxy_password = 'password'


LOG_DIRECTORY = "./logs"
if use_proxy:
    PROXY_URL = proxy_url
    PROXY_AUTH = Socks5Auth(login=proxy_login, password=proxy_password)
else:
    PROXY_URL = None
    PROXY_AUTH = None

if mode == "prom":
    TOKEN = telegrambot_prom
    DB_FILENAME = db_filename_prom
    LOG_FILENAME = os.path.join(LOG_DIRECTORY, log_filename_prom)
else:
    TOKEN = telegrambot_test
    DB_FILENAME = db_filename_test
    LOG_FILENAME = os.path.join(LOG_DIRECTORY, log_filename_test)