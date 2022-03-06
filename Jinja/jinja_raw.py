from jinja2 import Template
from markupsafe import Markup, escape

data1 = '''Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение.'''

data2 = '''{% raw %}Модуль Jinja вместо
определения {{ name }}
подставляет соответствующее значение. {% endraw %}'''

tm1 = Template(data1)
msg1 = tm1.render(name='Максим')

tm2 = Template(data2)
msg2 = tm2.render(name='Максим')

print(msg1)
print()
print(msg2)
print()

link = '''В html-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

tm3 = Template(link)
msg3 = tm3.render()
print(msg3)
print()

# для отображения ссылки как текста а не как ссылки в браузере
tm4 = Template("{{ link | e}}")
msg4 = tm4.render(link=link)
print(msg4)
print()

# такое же экранирование, но уже с помощью функции escape
msg5 = escape(link)
print(msg5)
print()

'''
{% for<выражение>%}
<повторяемый фрагмент>
{% endfor %}'''

'''Блок для проверки условий
{% if <условие> %}
<фрагмент при истинности условия>
{% endif %}'''

cities = [{'id': 1, 'city': 'Москва'},
          {'id': 2, 'city': 'Тверь'},
          {'id': 3, 'city': 'Минск'},
          {'id': 5, 'city': 'Смоленск'}]

links = '''<select name='cities'>
{% for c in cities -%}
{% if c.id > 2 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% elif c.city == "Москва" -%}
    <option>{{c['city']}}</option>
{% else -%}
    {{c['city']}}
{% endif %}
{% endfor %}
</select>'''
# или {% ..... -%} чтобы строки шли без пропусков

tm6 = Template(links)
msg6 = tm6.render(cities = cities)

print(msg6)
