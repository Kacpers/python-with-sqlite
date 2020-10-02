from commands import cli, setup, add, fetch_categories, index
from dotenv import load_dotenv
load_dotenv()

cli.add_command(setup)
cli.add_command(add)
cli.add_command(fetch_categories)
cli.add_command(index)

if __name__ == '__main__':
    cli()

