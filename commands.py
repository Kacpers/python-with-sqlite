import click
from database import Database
from os import getenv
from repositories.urls import save, fetch_categories, fetch_urls


@click.group()
def cli():
    pass


@click.command()
def setup_command(name='setup'):
    print('Tworze tabele w bazie danych')
    db = Database(getenv('DB_NAME'))
    db.create_table('CREATE TABLE urls (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, url TEXT)')


@click.command(name='add')
@click.argument('category')
@click.argument('url')
def add_command(category: str, url: str):
    print('Dodaję nowy adres url')
    save(category, url)


@click.command(name='categories')
def list_command():
    print('Lista kategorii:')

    for name in fetch_categories():
        print(name[0])


@click.command(name='index')
@click.argument('category')
def index_command(category: str):
    print(f'Lista linków z kategorii {category}:')

    for link in fetch_urls(category):
        print(link[2])

