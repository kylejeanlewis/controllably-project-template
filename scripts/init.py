from pathlib import Path
import sys
REPO = 'phbot-v2'
ROOT = str(Path().absolute()).split(REPO)[0]
sys.path.append(f'{ROOT}{REPO}')

from controllably import Helper, Factory
Helper.get_ports()

library = Helper.read_yaml(f'{ROOT}{REPO}\\library\\catalogue.yaml')
"""File reference for layout and config files"""
Helper.update_root_directory(library, REPO)
library = Factory.DottableDict(library)