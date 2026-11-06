import typer
from pathlib import Path
from sys import argv
app = typer.Typer()
p = Path('.')

@app.command()
def find_gitignore(gitignores):
    """
    Checks if there is a gitignore file in the project folder
    """
    if len(gitignores) < 1:
        print("Error: There is no gitignore file in this project folder")
        return [False, 0]
    elif len(gitignores) > 1:
        print("There are multiple gitignore files in this project folder. Run safenv -j to join the gitignore files to 1")
        return [True, len(gitignores)]
    else:
        print("Pass: There is a gitignore file present")
        return [True, 1]

@app.command()
def find_env():
    """
    Checks if there is a .env file in the project directory
    """
    pass

@app.command()
def read_gitignore():
    """
    Checks if there is a .env file in the project directory
    """
    pass

@app.command()
def create_gitignore():
    """Create a gitignore file with .env in case no gitignore file presently"""
    try:
        gitignore_file = Path(".gitignore")
        gitignore_file.write_text(".env")
        print("Gitignore file has been successfully created and .env has been added")
    except Exception as e:
        print(f"Gitignore file was not created. Error is {e}")

@app.command()
def safe_env():
    """
    Python module for checking if you do not have any exposed api keys and your gitignore file includes .env
    """
    gitignores = list(p.glob('**/*.gitignore'))
    if len(argv) > 1 and argv[1] == "-h":
        print("Here is all you need to know about this module")
        return
    has_gitignore, no_of_gitignores = find_gitignore(gitignores)
    if not has_gitignore:
        create_gitignore()
    
if __name__ == "__main__":
    app()