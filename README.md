# Local development
## Requirements
Application was developed using Python 3.8, but it will probably work with 3.6 or 3.7 too 
(not tested.)

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
