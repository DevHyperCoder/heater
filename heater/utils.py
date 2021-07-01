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

from io import TextIOWrapper
import os


def purify_folder_name(raw: str) -> str:
    """Removes special characters and replaces spaces with underscores"""
    return (
        raw.lower()
        .translate({ord(c): "" for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+'\""})
        .replace(" ", "_")
    )


def is_blank(s: str) -> bool:
    """Checks if a string is blank or not"""
    return not bool(s and not s.isspace())


def create_folder(folder_name: str):
    """Creates folder in working directory"""
    path = os.path.join(os.getcwd(), folder_name)
    try:  # If folder exists
        return os.mkdir(path)
    except FileExistsError:
        return


def create_file(file_name: str) -> TextIOWrapper:
    """Creates a file"""
    return open(file_name, "w+")
