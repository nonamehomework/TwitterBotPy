import setuptools
import os
from shutil import copy
from botkun.config import default_config_path
 
setuptools.setup()

# create config file
exists = [p for p in default_config_path if os.path.isfile(p)]
if len(exists) == 0:
    destination_path = default_config_path[0]
    source_path = "./.botkun.toml"

    copy(source_path, destination_path)
