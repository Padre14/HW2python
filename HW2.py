
'''
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
'''

n=int(input())
x=int(input())
from random import randint
list = [randint(0, 10) for i in range(n)]
print(list)
count=0
for i in range(len(list)):
    if list[i] == x:
        count += 1
print(count)



'''
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в 
массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X
'''

n=int(input())
from random import randint
list = [randint(0, 10) for i in range(n)]
print(list)
x=int(input())
min_raznica = abs(x-list[0])
for i in range(len(list)):
    if x==list[i]:
        print(list[i])
        break
    else:
        if abs(x-list[i]) <= min_raznica:
            min_raznica==x-list[i]
            element=list[i]
print(element) 
'''
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки распределяются 
так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, 
что на вход подается только одно слово, которое содержит либо только английские, 
либо только русские буквы.
'''

text=str(input())
list_1 = [text[i] for i in range(len(text))]
#for i in range(len(text)):
    #list_1.append(text[i])

scrabble_point={1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4:'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
sum=0
for i in range(len(list_1)):
    for k,v in scrabble_point.items():
        if list_1[i].upper() in v:
            sum += k
print(sum)
