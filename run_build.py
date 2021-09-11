import yaml
import os
from collections import deque

import utils

# load data from _config.yml
with open("_config.yml", 'r') as stream:
    data = yaml.load(stream, Loader=yaml.FullLoader)
print('succesfully loaded site config from _config.yml')

# delete all files in _site
for file in os.listdir('_site'):
    os.remove(f'_site/{file}')
print('deleted previous files in _site')

# copy styling into _site
for styling in os.listdir('_styles'):
    utils.copyFileToSite(f'_styles/{styling}')
print('copied styling into _site')

# render all templates into _site
for template in os.listdir('_templates'):
    text = utils.renderTemplate(template, data)
    utils.writeToSite(text, template)
print('rendered templates into _site')

print('success')