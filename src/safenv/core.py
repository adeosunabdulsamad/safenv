import typer
from pathlib import Path
from typing import Annotated
import urllib.request

app = typer.Typer()
p = Path(".")
gitignores = list(p.glob("**/*.gitignore"))
from InquirerPy import inquirer

options = {
    "AL": None,
    "Actionscript": None,
    "Ada": None,
    "AdventureGameStudio": None,
    "Agda": None,
    "Android": None,
    "Angular": None,
    "AppEngine": None,
    "AppceleratorTitanium": None,
    "ArchLinuxPackages": None,
    "Autotools": None,
    "Ballerina": None,
    "C": None,
    "C++": None,
    "CFWheels": None,
    "CMake": None,
    "CUDA": None,
    "CakePHP": None,
    "ChefCookbook": None,
    "Clojure": None,
    "CodeIgniter": None,
    "CommonLisp": None,
    "Composer": None,
    "Concrete5": None,
    "Coq": None,
    "CraftCMS": None,
    "D": None,
    "DM": None,
    "Dart": None,
    "Delphi": None,
    "Deno": None,
    "Dotnet": None,
    "Drupal": None,
    "EPiServer": None,
    "Eagle": None,
    "Elisp": None,
    "Elixir": None,
    "Elm": None,
    "Erlang": None,
    "ExpressionEngine": None,
    "ExtJs": None,
    "Fancy": None,
    "Finale": None,
    "Firebase": None,
    "FlaxEngine": None,
    "Flutter": None,
    "ForceDotCom": None,
    "Fortran": None,
    "FuelPHP": None,
    "GWT": None,
    "Gcov": None,
    "GitBook": None,
    "GitHubPages": None,
    "Gleam": None,
    "Go": None,
    "Godot": None,
    "Gradle": None,
    "Grails": None,
    "HIP": None,
    "Haskell": None,
    "Haxe": None,
    "IAR": None,
    "IGORPro": None,
    "Idris": None,
    "JBoss": None,
    "JENKINS_HOME": None,
    "Java": None,
    "Jekyll": None,
    "Joomla": None,
    "Julia": None,
    "Katalon": None,
    "KiCad": None,
    "Kohana": None,
    "Kotlin": None,
    "LabVIEW": None,
    "LangChain": None,
    "Laravel": None,
    "Lasal": None,
    "Lean": None,
    "Leiningen": None,
    "LemonStand": None,
    "Lilypond": None,
    "Lithium": None,
    "Lua": None,
    "Luau": None,
    "Magento": None,
    "Maven": None,
    "Mercury": None,
    "MetaProgrammingSystem": None,
    "ModelSim": None,
    "Modelica": None,
    "MoonBit": None,
    "Nanoc": None,
    "Nestjs": None,
    "Nextjs": None,
    "Nim": None,
    "Nix": None,
    "Node": None,
    "OCaml": None,
    "Objective-C": None,
    "Opa": None,
    "OpenCart": None,
    "OracleForms": None,
    "Packer": None,
    "Perl": None,
    "Phalcon": None,
    "PlayFramework": None,
    "Plone": None,
    "Prestashop": None,
    "Processing": None,
    "PureScript": None,
    "Python": None,
    "Qooxdoo": None,
    "Qt": None,
    "R": None,
    "ROS": None,
    "Racket": None,
    "Rails": None,
    "Raku": None,
    "ReScript": None,
    "RhodesRhomobile": None,
    "Ruby": None,
    "Rust": None,
    "SCons": None,
    "SSDT-publish": None,
    "Salesforce": None,
    "Sass": None,
    "Scala": None,
    "Scheme": None,
    "Scrivener": None,
    "Sdcc": None,
    "SeamGen": None,
    "SketchUp": None,
    "Smalltalk": None,
    "Solidity": None,
    "Stella": None,
    "SugarCRM": None,
    "Swift": None,
    "Symfony": None,
    "SymphonyCMS": None,
    "TeX": None,
    "Terraform": None,
    "TestComplete": None,
    "Textpattern": None,
    "TurboGears2": None,
    "TwinCAT3": None,
    "Typo3": None,
    "Unity": None,
    "UnrealEngine": None,
    "VBA": None,
    "VVVV": None,
    "VisualStudio": None,
    "Waf": None,
    "WordPress": None,
    "Xojo": None,
    "Yeoman": None,
    "Yii": None,
    "ZendFramework": None,
    "Zephir": None,
    "Zig": None,
    "ecu.test": None,
    "esp-idf": None,
    "ros2": None,
}


def question():
    gitignore_template = inquirer.text(
        message="What language is your project running on:",
        completer=options,
        validate=lambda result: result in options,
        invalid_message="Please select a valid option from the list.",
        multicolumn_complete=True,
    ).execute()
    return gitignore_template


@app.command()
def check_gitignore():
    """Check if there is a gitignore file in the project folder

    Returns:
        has_gitignore (bool): True if the folder has a gitignore file(s), else False
        no_of_gitignores: Total number of gitignore files found in project folder
    """
    if len(gitignores) < 1:
        print("Error: There is no gitignore file in this project folder\n")
        return [False, 0]
    elif len(gitignores) > 1:
        print(
            "There are multiple gitignore files in this project folder. Run safenv -j to join the gitignore files to 1"
        )
        return [True, len(gitignores)]
    else:
        print("Pass: There is a gitignore file present")
        return [True, 1]


def join_gitignores(
    gitignores: Annotated[
        list[Path],
        typer.Option(help="List of gitignore files present in the working directory"),
    ],
):
    """
    Join multiple gitignore files together to One

    Args:
        gitignores (list[path]): List of gitignore files present in the working directory

    Returns:
        gitignore: A single gitignore file
    """
    pass


def append_text(path: Path, text: str):
    """Add files that git should ignore if there is already a gitignore file present

    Args:
        path (str): Realative path of the gitignore file
        text (str): The file extension to add to the gitignore
    """

    with path.open("a", encoding="utf-8") as f:
        f.write(text)


@app.command()
def find_env(
    file_path: Annotated[
        Path, typer.Argument(help="The path of the file that is being searched")
    ],
):
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
    has_gitignore, no_of_gitignores = check_gitignore()
    if not has_gitignore:
        print("Proceeding to create a new gitignore file")
        template = question()
        template_url = f"https://raw.githubusercontent.com/github/gitignore/refs/heads/main/{template}.gitignore"
        urllib.request.urlretrieve(template_url, p / ".gitignore")
        print("Gitignore file successfully created")
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
