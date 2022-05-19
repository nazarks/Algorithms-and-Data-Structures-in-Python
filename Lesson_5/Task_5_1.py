"""
5.1 Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""
from collections import namedtuple

START_FIELD_POSITION = 1
END_FIELD_POSITION = 5

Property = namedtuple('Property',
                      ['name', 'quarter_income_1', 'quarter_income_2', 'quarter_income_3', 'quarter_income_4',
                       'year_income'],
                      defaults=[None, 0, 0, 0, 0, 0])

property_count = int(input("Введите количество предприятий: "))
property_list = []
total_income = 0
property_result = {'bad': [], 'good': []}
for i in range(property_count):
    p = Property(name=None,
                 quarter_income_1=0,
                 quarter_income_2=0,
                 quarter_income_3=0,
                 quarter_income_4=0,
                 year_income=0)
    p = p._replace(name=input(f'Введите имя {i + 1}-го предприятия: '))
    year_property_income = 0
    for k in range(START_FIELD_POSITION, END_FIELD_POSITION):
        field = p._fields[k]
        value = int(input(f'Предприятие {p.name}, введите доход {k}-й четверти: '))
        p = p._replace(**{field: value})
        year_property_income += value
    total_income += year_property_income
    p = p._replace(year_income=year_property_income)
    property_list.append(p)

average = total_income / property_count
print(f'Средний доход по предприятиям: {average}')

for p in property_list:
    print(f'Предприятие {p.name} заработало всего: {p.year_income}')
    if p.year_income > average:
        property_result['good'].append(p.name)
    elif p.year_income < average:
        property_result['bad'].append(p.name)

if property_result['good']:
    print(f'Список предприятий чья прибыль выше среднего: {", ".join(property_result["good"])}')
if property_result['bad']:
    print(f'Список предприятий чья прибыль ниже среднего: {", ".join(property_result["bad"])}')
