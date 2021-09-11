import yaml
import os
import jinja2
import sys

with open("_config.yml", 'r') as stream:
    data_loaded = yaml.load(stream, Loader=yaml.FullLoader)
    print(data_loaded)
print(type(data_loaded))

templates_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('_templates'))
out = templates_environment.get_template('index.html').render(data_loaded)
print(out)