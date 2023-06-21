questions=[{ 'question' : 'Первый элемент в таблице Менделеева?',
             'answer' : ['Магний','Железо','Водород'],
             'right_answer' : 3},
           {'question' : 'Кто открыл Америку?',
            'answer' : ['Диего Колон','Христофор Колумб','Васко да Гама'],
            'right_answer' : 2},
           {'question' : 'Как называется корабль Джека Воробья из фильма «Пираты Карибского моря»?',
            'answer' : ['Черная жемчужина','Летучий Голландец','Месть королевы Анны'],
            'right_answer' : 1},
           {'question' : 'Какая планета расположена ближе всех к Солнцу?',
            'answer' : ['Венера','Меркурий','Марс'],
            'right_answer' : 2},
           {'question' : 'Что быстрее: свет или звук?',
            'answer' : ['Звук','Свет','Одинаковой скорости'],
            'right_answer' : 2}
]
point = 0
name=input('Введите свое имя: ')
for question in questions:
    print (question.get('question'))
    counter_answers = 0
    for answer in question['answer']:
        counter_answers += 1
        print(counter_answers, ')', answer)
    user_answer = int(input('Выберите номер ответа: '))
    if user_answer == question.get('right_answer'):
        print('Верно!')
        point += 1
    else:
        print('Ответ не верный :(')
    print('_' * 100)
if point>=3:
    print('Ты победил')
else:
    print('Ты проиграл')
print('Количество правельных ответов: ', point)
f=open("results.txt","a",encoding='utf-8')
f.write('Игрок ' + name + ' набрал ' + str(point) + ' очков \n')
f.close()