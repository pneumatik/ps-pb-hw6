def plural_form(number, form1, form2, form3):
    
    q = number-1
    if q == 0 or q%10 == 1 :
        print(f"{number} {form1}")
    elif q > 0 and q < 4:
        print(f"{number} {form2}")
    else:
        print(f"{number} {form3}")
   
q = input('введите количество яблок ')

plural_form(int(q), 'яблоко', 'яблока', 'яблок')
