# Сокращение ссылок с помощью Битли
Создание коротких ссылок с помощью службы [Битли](https://bitly.com/) (Bitly). 
Подсчет количества переходов по короткой ссылке.

### Запуск программы:
Выполняется из командной строки в каталоге размещения.
```
python main.py _ваша_ссылка_
```
где 
#### если ссылка на ресурс в интернете, вернется сокращенная ссылка:
```
python main.py http://www.google.com
Битлинк: https://bit.ly/3faE7Pl
```
#### если ссылка является сокращенной с помощью службы Битли, вернется количество переходов по ней:
```
python main.py https://bit.ly/3faE7Pl
По вашей ссылки прошли 1 раза
```

### Как установить
Необходимо создать файл окружения .env в каталоге программы.
В файле с помощью редактора указать переменную окружения: 
```
BITLY_ACCESS_TOKEN=_ваш_токен_
```
Токен необходимо получить в службе [Битли](https://bitly.com/).

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [виртуальное окружение](https://docs.python.org/3/library/venv.html) для изоляции проекта. 

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).