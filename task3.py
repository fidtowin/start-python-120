# CREATE LIST
# a= [1, 1.1, a, [1], (1, 1.1), {1, 2}, {a: 1} None, [True] # Список в котором: целое; вещественное, строковое, другой список, кортеж, множество; словарь, пустой тип; булевый тип
# a = [] # Пустой список
# b = list() # Пустой список
# a= (1, 2.1, 3) # Раньше я был кортежем
# list(a) # [1, 2.1, 3], но 'а' остался кортежем
# b = list('abc')# [a, b, 'c']
# RETRIVE LIST
# a = [1, 1/1, 'a']
# print(a) #[1.1.1, a]
# print([1, 1.1, 'a']) # [1, 1.1, 'a']
# a=[1, 11, 'a']
# a[0] # 1
# a[1] # 1.1
# a[2] # 'a'
# а[3] # Ошибка, вышли за границы
# a[-1] # 'a'
# a[-2] # 1.1
# a[-3] # 1
# а[-4] #. Ошибка, вышли за границы
# a=[1, 2, 3]
# a.index(3) #2. Возвращает индекс, где передаваемое значение стоит в списке. В примере вернется 2, так как значение 3 в списке стоит на 2-
# UPDATE LIST
# a = [1, 1.1, 'a']
# a[0] = 'a' # Teперь 'а' равно ['а', 1.1, 'a']
# a[1] = 'б'  # Tenерь "а' равно ['a', 'б', 'a']
# а[-1] = 'в' # Теперь 'а' равно ['а', '6', 'в']
# a = [1, 2, 3] # Tеперь 'а' равно [1, 2, 3]
# a = [1, 2, 3] # Добавляет значение (объект) в конец списка. Добавляет только один объект или значение. Теперь "а" [1, 2, 3, 4]
# a.append(['a', 'b']) # Теперь "а" [1, 2, 3, 4, ['a', 'b']]. Не забываем, что методы в списке изменяют значения и структуру в самом списке.
# a = [1, 2, 3]
# a.insert(0, 4) # Добавляет значение (объект), что стоит на втором месте (4) на место под индексом, что стоит на первом месте (0) В конкретном примере добавит 4 на О-ой индекс, т.е. вначало. Теперь "а" [4, 1, 2, 3]
# a = [1, 2, 3]# В конкретном примере добавит 4 на 3-ий индекс, т.е. вконец. Теперь a [1,2,3,4]
# a.insert(-1, 4) #Кажется, что здесь должно значение 4 добавиться в конец, но на самом деле 4 встанет в предпоследнее место. Теперь a [1, 2, 4, 3]
# a = [1, 2, 3]
# a.extend([4, 5, 6]) # Добавляет данные в список поэлементно. Теперь "а" [1,2,3,4,5,6]

list
group_120= ['Агафонов', 'Арасланов', 'Дудин', 'Дюндин', 'Жариков', 'Звягинцев', 'Кириллова', 'Колосков', 'Кураев', 'Кутовой', 'Лесовой', 'Мерзляков', 'Невзоров']
grup_1 = group_120[:6]
print(grup_1)
grup_2 = group_120[6:]
print(grup_2)


a = 1, 2, 3
b = str(a)
print(b)
print(type(b))


a = 1, 5.5, "hello"
b = list(a)
print(b)
print(type(b))


#числа фиксированного размера
value = 12.34567

print(f"{value:.2f}") # .2f - округление до двух знаков после запятой
Ответ: 12.35

a = int(input("Введите целое число: - "))

if a % 2 == 0:
    print(f'Число {a} является четным')
else:
    print(f'Число {a} является нечетным')




