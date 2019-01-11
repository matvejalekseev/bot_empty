# Установка
Python 3.6 - https://www.python.org</br>
```wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz```</br>
```tar -xvf Python-3.6.3.tgz```</br>
```cd Python-3.6.3```</br>
```./configure```</br>
```make```</br>
```make install```</br>
```python3.6 -V```</br>

SQLAlchemy - http://www.sqlalchemy.org/</br>
```pip3.6 install -U SQLAlchemy```

aiogram - https://aiogram.readthedocs.io/en/latest/index.html</br>
```pip3.6 install -U aiogram```

aiosocksy - https://pypi.org/project/aiosocksy/</br>
```pip3.6 install -U aiosocksy```


# Первый запуск
Настройка файла conf.py шаблон - conf_template.py</br>
```nano conf_template.py```</br>
Выполнение инициализирующего скрипта</br>
```python3.6 init.py```</br>
Добавление в базу индексов:</br>
```CREATE UNIQUE INDEX users_index_ids on Users (id);```</br>
Бот рабоатет в супер группах, где он админ и имеет право удалять сообщения и выгонять пользователей</br>
