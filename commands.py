import click
from database import Database
from os import getenv


@click.group()
def cli():
    pass


@click.command()
def setup():
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')


@click.command()
@click.argument('category')
@click.argument('url')
def add(category: str, url: str):
    print('Dodaję nowy adres url')
    db = Database(getenv('DB_NAME'))
    db.insert ('urls', None, category, url)


@click.command(name='categories')
def fetch_categories():
    print('Lista kategorii:')
    db = Database(getenv('DB_NAME'))
    categories = db.fetch_distinct('urls', 'category')

    for name in categories:
        print(name[0])


@click.command()
@click.argument('category')
def index(category: str):
    print(f'Lista linków z kategorii {category}:')
    db = Database(getenv('DB_NAME'))
    links = db.fetch_all('urls', category=category)

    for link in links:
        print(link[2])

