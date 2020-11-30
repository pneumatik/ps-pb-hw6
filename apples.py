def plural_form(number, form1, form2, form3):
""" Вывод множественной формы числительных.
:param number: числительное
:form1: Именительный падеж
:form2: Родительный падеж
:form3: Множественный родительный падеж
"""
    q = number
    if int(q)%100 == 11:
        print(f"{number} {form3}")
    elif  q == 1 or int(q)%10 == 1:
        print(f"{number} {form1}")
    elif q > 1 and q < 5 or (int(q)%10 > 1 and int(q)%10 < 5):
        print(f"{number} {form2}")
    else:
        print(f"{number} {form3}")
    

q = input('введите количество: ')

plural_form(int(q), 'яблоко', 'яблока', 'яблок')
plural_form(int(q), 'студент', 'студента', 'студентов')