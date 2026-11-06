import typer
from pathlib import Path
from sys import argv
app = typer.Typer()
p = Path('.')

@app.command()
def find_gitignore(gitignores: list[str]):
    """Check if there is a gitignore file in the project folder

    Args:
        gitignores (list[int]): A list of the gitignore files in the project folder

    Returns:
        has_gitignore (bool): True if the folder has a gitignore file(s), else False
        no_of_gitignores: Total number of gitignore files found in project folder
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

def append_text(path: Path,text: str):
    """Add files that git should ignore if there is already a gitignore file present
    
    Args:
        path (str): Realative path of the gitignore file
        text (str): The file extension to add to the gitignore
    """

    with path.open("a", encoding="utf-8") as f:
        f.write(text)

@app.command()
def find_env(file_path: Path):
    """
    Check if there is a .env file in the project directory

    Args:
        file_path (path): The path of the file that is being searched

    Returns:
        find_env (bool): True if .env is found in the file and false if not 
    """
    if ".env" in file_path.read_text(encoding="utf-8"):
        print("There is already a .env file present in your gitignore file")
        return True
    print("There is no .env file present in your gitignore file")
    return False

@app.command()
def read_gitignore():
    """
    Check if there is a .env file in the project directory
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
    elif no_of_gitignores == 1:
        if find_env(gitignores[0]):
            return
        try:
            append_text(gitignores[0], ".env\n")
            print("Added .env to the file")
        except Exception as e:
            print(f"Error when trying to add .env: {e}")

    
if __name__ == "__main__":
    app()