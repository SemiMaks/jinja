from jinja2 import Environment, FileSystemLoader, FunctionLoader

persons = [
    {'name': 'max', 'old': 40, 'weight': 78},
    {'name': 'alex', 'old': 28, 'weight': 65},
    {'name': 'lev', 'old': 35, 'weight': 68}
    ]

def loadTpl(path):
    if path == "main.htm":
        return '''Имя {{u.name}}, возраст {{u.old}}'''
    else:
        return '''Данные: {{u}}'''

#file_loader = FileSystemLoader('templates') # есть разные лоадеры для разных источников загрузки
file_loader = FunctionLoader(loadTpl)
env = Environment(loader=file_loader)

tm = env.get_template('main.htm')
msg = tm.render(u = persons[0])

print(msg)
