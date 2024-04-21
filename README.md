# totally setup alembic project

## Authors
Boris Le Bon

## Project description
It's a training project where the goal is to setup a database from scratch using alembic

## What is needed/what is used

- everything is written in the requirements.txt file, to install all, enter : `pip install -r requirements.txt`

Python 3.10+ is needed (i use python 3.10.7).
fastapi
uvicorn
sqlalchemy
alembic

## Comment about my work

### install the project

I am using a venv in order to install all the requirements, to install it : `pip install virtualenv`
once it's install, we need to add it on the project (on a mac) : `virtualenv -p python3 venv`
Then we activate it using `source venv/bin/activate`
when the venv is activate, all we need to do is a `pip install -r requirements.txt` in order to install all the requirements

### The configuration of alembic

The alembic.ini file has been configurated with these code : 
`script_location = src/alembic`
`sqlalchemy.url = sqlite:///Heroes.db`

the .env has been configurated with these : 
```python
# add your model's MetaData object here
# for 'autogenerate' support
install_models()
target_metadata = Base.metadata
```

and the migration is started like that 
`alembic revision --autogenerate`

an `alembic upgrade head` will update the head and migrate the data in the database