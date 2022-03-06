from jinja2 import Template

'''
{% %} - спецификатор шаблона
{{ }} - выражение для вставки любых конструкций python в шаблон
{# #} - блок комментариев
# ## - строковый комментарий
'''

br = '-----'
name = 'максим'
tm = Template("Меня зовут {{ name }}") # экземпляр класса Template
msg = tm.render(name=name)
print(msg)
print(br)

# аналогичное применение в более простых случаях f-строк
msg1 = f"Привет {name}"
print(msg, msg1, sep="\n")
print(br)

age = 40
tm2 = Template("Мне {{ a }} лет и зовут {{ n }}")
tm3 = Template("Мне {{a*2}} лет и зовут {{n.title()}}")
msg21 = tm2.render(n=name, a=age)
msg22 = tm3.render(n=name, a=age)

print(msg21)
print(msg22)
print(br)

# используем класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

per = Person("Максим", 40)

tm31 = Template("Мне {{age}} лет и зовут {{name}}")
msg31 = tm31.render(name=per.name, age=per.age)

tm32 = Template("Мне {{p.age}} лет и зовут {{p.name}}") # с применением ссылки p
msg32 = tm32.render(p = per)

print(msg31)
print(msg32)
print(br)
print(br)

# используем геттер
class Personal:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

per = Personal(40, "Максим")
temp = Template("Меня зовут {{ p.getName() }} и мне {{ p.getAge() }} лет")
message = temp.render(p = per)
print(message)
print(br)

# с применением словаря
personal = {'name': 'Макс', 'age': 40}
tm4 = Template("Меня зовут {{ p.name }} и мне {{ p['age'] }} лет") # обращение по ключу словаря с двумя способами записи
msg4= tm4.render(p = personal)
print(msg4)
