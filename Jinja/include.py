from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {'name': 'max', 'old': 40, 'weight': 78},
    {'name': 'alex', 'old': 28, 'weight': 65},
    {'name': 'lev', 'old': 35, 'weight': 68}
    ]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.htm')
msg = tm.render(domain='http://crewcut.ru', title="Изделия из кожи")

print(msg)