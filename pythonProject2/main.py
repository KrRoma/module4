goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
        {'quantity': 0, 'price': 0},
        {'quantity': 0, 'price': 0},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
        {'quantity': 0, 'price': 0},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
        {'quantity': 0, 'price': 0},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
for item in goods:
     item_name = item
     item_id = goods[item]
     for i in range(1):
         inf=store.get(item_id)
         inf1=inf[0]
         inf2=inf[1]
         inf3=inf[2]
         item_price=inf1.get('quantity')*inf1.get('price')+inf2.get('quantity')*inf2.get('price')+inf3.get('quantity')*inf3.get('price')
         print(item_name,' - ',inf1.get('quantity')+inf2.get('quantity')+inf3.get('quantity'),' штук,',' стоисмость ',item_price,' рублей')