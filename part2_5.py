group_1 =int(input('Введите количество учеников в первой группе: '))
group_2 =int(input('Введите количество учеников во второй группе: '))
group_3 =int(input('Введите количество учеников в третьей группе: '))
result = group_1//2 + group_2//2 + group_3//2
if group_1/2 == 0 and group_2/2 == 0 and group_3/2 == 0:
    print(result)
else: print(result + 1)
