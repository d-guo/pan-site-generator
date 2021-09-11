from shutil import copyfile
import jinja2

templates_environment = jinja2.Environment(loader=jinja2.FileSystemLoader('_templates'))

def writeToSite(text, file_name):
    with open(f'_site/{file_name}', 'w+') as f:
        f.write(text)

def copyFileToSite(file_name):
    copyfile(file_name, f"_site/{file_name.split('/')[-1]}")

def renderTemplate(template_name, data):
    return templates_environment.get_template(template_name).render(data)
