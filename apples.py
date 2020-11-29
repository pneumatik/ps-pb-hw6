def plural_form(number, form1, form2, form3):
    q = number
    if int(q)%100 == 11:
        print(f"{number} {form3}")
    elif  q == 1 or int(q)%10 == 1:
        print(f"{number} {form1}")
    elif q > 1 and q < 5 or (int(q)%10 > 1 and int(q)%10 < 5):
        print(f"{number} {form2}")
    else:
        print(f"{number} {form3}")
    
q = input('введите количество яблок: ')

plural_form(int(q), 'яблоко', 'яблока', 'яблок')