from jinja2 import Template
from markupsafe import Markup, escape

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17300},
    {'model': 'Volvo', 'price': 44300}
]

digs = [1, 2, 3, 4, 5]

'''
sum - вычисление суммы
sum(iterable, attribute=None, start=0)
Фильтров несколько десятков(таблица 50)'''

tpl = "Суммарная стоимость автомобилей: {{ cs | sum(attribute='price') }}"
tpl2 = "Вывод списка автомобилей: {{ cs }}"
tpl3 = "Сумма чисел digs: {{ cs | sum}}"
tpl4 = "Автомобиль с максимальной стоимостью: {{ cs | max(attribute='price') }}"
tpl5 = "Автомобиль с максимальной стоимостью, модель: {{ (cs | max(attribute='price')).model }}"
tpl6 = "Автомобиль с минимальной стоимостью, модель: {{ (cs | min(attribute='price')).model }}"
tpl7 = "Рандомный автомобиль: {{ (cs | random).model }}"

tm = Template(tpl)
msg = tm.render(cs = cars)

print(msg)

tm2 = Template(tpl2)
msg2 = tm2.render(cs = cars)
print(msg2)

tm3 = Template(tpl3)
msg3 = tm3.render(cs = digs)
print(msg3)

tm4 = Template(tpl4)
msg4 = tm4.render(cs = cars)
print(msg4)

tm5 = Template(tpl5)
msg5 = tm5.render(cs = cars)
print(msg5)

tm6 = Template(tpl6)
msg6 = tm6.render(cs = cars)
print(msg6)

tm7 = Template(tpl7)
msg7 = tm7.render(cs = cars)
print(msg7)

'''
{% filter <название фильтра> %}
<фрагмент для применения фильтра>
{% endfilter %}'''

persons = [
    {'name': 'max', 'old': 40, 'weight': 78},
    {'name': 'alex', 'old': 28, 'weight': 65},
    {'name': 'lev', 'old': 35, 'weight': 68}
]

tpl8 = '''
{%- for u in users -%}
{% filter title %}{{u.name}}{% endfilter %}
{% endfor -%}'''

tm8 = Template(tpl8)
msg8 = tm8.render(users = persons)
print(msg8)

# macros
html = '''
{% macro input(name, value='', type='text', size=20) -%}
    <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
{%- endmacro %}

<p>{{ input('username') }}
<p>{{ input('email') }}
<p>{{ input('password') }}
<p>{{ input('value') }}

'''

tm9 = Template(html)
msg9 = tm9.render()

print(msg9)

'''
Вложенные макросы - call
{% call[()] <вызов макроса> %}
<вложенный шаблон>
{% endcall %}
'''

html2 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}}
{%- endfor %}
</ul>
{%- endmacro %}

{{list_users(users)}}
'''

tm10 = Template(html2)
msg10 = tm10.render(users = persons)
print(msg10)

html3 = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}}  {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall %}
'''

tm11 = Template(html3)
msg11 = tm11.render(users = persons)
print(msg11)
