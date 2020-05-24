# Local development
## Requirements
Application was developed using Python 3.8, but it will probably work with 3.7 too (not tested.)

App uses SQLite db for now, so there's no need to install additional db client libraries.

## Setup project on linux

Install virtualenvrapper and go to root project directory.
 
Create virtualenv for this project:
```bash
mkvirtualenv -p <path to your python executable> ebcscrapper
``` 

Install Python libraries:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python3 manage.py migrate
```

## Run project

Run:
```bash
python3 manage.py runserver
``` 

Import rates:
```bash
python3 manage.py scrap_ebc
```
You can extend list of imported data by adding items to `CURRENCIES_TO_IMPORT` tuple in 
`/scrapper/services.py`.

Then open list of available currencies in your web browser:
```
http://127.0.0.1:8000/api/v1/currency/
```

Choose one (`symbol`) and open:
```
http://127.0.0.1:8000/api/v1/currency/rate/<symbol>-EUR/
```
Eg. use this to get latest USD-EURO rates:
```bash
http://127.0.0.1:8000/api/v1/currency/rate/USD-EUR/
```


