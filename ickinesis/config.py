import os
import os.path


ICKINESIS_FOLDER = os.path.join(os.path.expanduser("~"), ".ickinesis")
CAPTURES_FOLDER = os.path.join(os.path.expanduser("~"), ".ickinesis/captures")


def create_config_dir():
    """Creates a folder named .ickinesis in user's home directory"""
    if not os.path.isdir(ICKINESIS_FOLDER):
        os.mkdir(ICKINESIS_FOLDER)
    if not os.path.isdir(CAPTURES_FOLDER):
        os.mkdir(CAPTURES_FOLDER)
