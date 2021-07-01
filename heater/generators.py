# Copyright (c) 2021 K.M Ahnaf Zamil

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from heater.code import get_code_for_library, get_extension_for_library
from heater.utils import create_file, create_folder, is_blank, purify_folder_name

import os
import typing


def generate_boilerplate_code(project_type: str, extension_folder: str):
    """Generates boilerplate bot code"""

    print("Generating boilerplate code...")

    # Generating bot.py
    print("Creating bot.py...")
    code = get_code_for_library(project_type)
    create_file("bot.py")
    with open("bot.py", "w") as f:
        f.write(code)

    # Generating cogs/plugins
    print(f"Creating {extension_folder} folder...")
    create_folder(extension_folder)
    code = get_extension_for_library(project_type)
    with open(os.path.join(extension_folder, "hello.py"), "w") as f:
        f.write(code)


def generate_env(token: str, prefix: str):
    """Generates .env file"""

    print("Creating .env...")
    create_file(".env")

    with open(".env", "a") as f:
        f.write(f"BOT_TOKEN={token}\nBOT_PREFIX={prefix}")


def generate_requirements(project_type: str, dependencies: typing.List[str]):
    """Generates requirements.txt"""

    print("Creating requirements.txt...")
    create_file("requirements.txt")

    with open("requirements.txt", "a") as f:
        f.write("python-dotenv\n")
        if project_type == "discord.py":
            f.write("discord.py\n\n")
        else:
            f.write("hikari-lightbulb\n\n")

        # Additional dependencies
        for x in dependencies:
            if not is_blank(x):
                f.write(f"{x.replace(' ', '')}\n")


def generate(
    project_name: str,
    project_type: str,
    token: str,
    prefix: str,
    dependencies: typing.List[str],
):
    """Generates files, folders and some boilerplate code"""

    project_type = "hikari" if project_type.lower()[0] == "h" else "discord.py"
    extension_folder = "cogs" if project_type == "discord.py" else "plugins"

    # Create folder for project
    folder_name = purify_folder_name(project_name)

    print("\bCreating project folder...")
    create_folder(folder_name)
    os.chdir(os.path.join(os.getcwd(), folder_name))

    # Writing boilerplate code to bot.py and requirements.txt
    generate_boilerplate_code(project_type, extension_folder)

    # Generating requirements.txt
    generate_requirements(project_type, dependencies)

    # Generating .env and requirements.txt
    generate_env(token, prefix)
