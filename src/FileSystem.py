from __future__ import annotations
import os
import sys


SAVE_FILE_NAME = "save.json"
ICONS_FOLDER_NAME = "ui/icons"
FONTS_FOLDER_NAME = "ui/fonts"
ADDONS_NAME = "addons"

PROGRAM_DIR = os.path.dirname(os.path.abspath(__file__))

SAVE_FILE = os.path.join(PROGRAM_DIR, SAVE_FILE_NAME)
ICONS_FOLDER = os.path.join(PROGRAM_DIR, ICONS_FOLDER_NAME)
FONTS_FOLDER = os.path.join(PROGRAM_DIR, FONTS_FOLDER_NAME)
ADDONS_FOLDER = os.path.join(PROGRAM_DIR, ADDONS_NAME)

PLATFORM = sys.platform


def abspath(path: str) -> str | None:
    """Returns the absolute path. Returns None if the path does not exist."""
    _path = os.path.join(PROGRAM_DIR, path)
    return os.path.abspath(_path) if os.path.exists(_path) else None


def exists(path: str):
    """Returns True if the path exists. Returns False otherwise"""
    return os.path.exists(path)


def icon(icon_name: str) -> str | None:
    """Returns the absolute path of given icon. Returns None if the icon does not exist."""
    path = os.path.join(ICONS_FOLDER, icon_name)
    return os.path.abspath(path).replace("\\", "/") if os.path.exists(path) else None


def font(font_name: str) -> str | None:
    """Returns the absolute path of given font. Returns None if the font does not exist."""
    path = os.path.join(FONTS_FOLDER, font_name)
    return os.path.abspath(path).replace("\\", "/") if os.path.exists(path) else None


def open_file(file_path: str | None) -> None:
    if file_path is not None:
        if PLATFORM in ("win32",):
            os.startfile(file_path)
        elif PLATFORM in ("linux", "darwin"):
            os.system(f"xdg-open {file_path}")
