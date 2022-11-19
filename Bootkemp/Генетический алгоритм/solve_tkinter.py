import random
from tkinter import *

c = [9.95, 3.66, 57.05, 10.485, 11.97, 18.17, 13.425, 3.28, 18.16] # средства, выделяемые конкретным ЦФО на ....
M = 55.83 # плановый годовой объем финансовых средств, выделяемых центральной компанией на реализацию ....
r = 11 # допустимая средняя прибыль на 1 руб. затрат (норма прибыли на капитал)
p = 1 # ограничение на суммарную рискованность инвестиционного портфеля

risk = [] # риск по проектам
marja = [] # прибыль от проектов
costs = [] # стоимость проектов
names = [] # имена проектов

# 0 регион
risk.append([2.73, 1.63])
marja.append([15.31, 14.68])
costs.append([10.42, 9.48])
names.append(["реконструкция офисных зданий и сооружений",
            "выделение группы технологического аудита в обособленную группу"])

# 1 регион
risk.append([1.7])
marja.append([14.77])
costs.append([7.32])
names.append(["разработка и внедрение специальных средств упаковки ценных грузов"])

# 2 регион
risk.append([1.52, 1.64, 2.32, 1.12])
marja.append([14.03, 15.76, 15.7, 13.08])
costs.append([11.31, 10.85, 13.51, 10.87])
names.append(["приобретение и оборудование бронеавтомобилей",
            "разработка и внедрение специальных средств упаковки ценных грузов",
            "установка спутниковых датчиков GPS по отслеживанию выполнения маршрута",
            "приобретение и доукомплектование грузового и легкового автотранспорта"])

# 3 регион
risk.append([1.44, 2.83])
marja.append([15.25, 14.49])
costs.append([6.38, 14.59])
names.append(["приобретение и доукомплектование грузового и легкового автотранспорта",
            "сдача в аренду сторонним организациям части площади"])

# 4 регион
risk.append([1.73, 1.42])
marja.append([13.39, 14.95])
costs.append([13.71, 10.23])
names.append(["приобретение и доукомплектование грузового и легкового автотранспорта",
            "установка спутниковых датчиков GPS по отслеживанию выполнения маршрута"])

# 5 регион
risk.append([1.19, 2.54, 1.51])
marja.append([17.39, 13.18, 13.27])
costs.append([13.16, 12.15, 11.03])
names.append(["закупка запчастей",
              "реконструкция офисных зданий и сооружений",
              "приобретение и оборудование бронеавтомобилей"])

# 6 регион
risk.append([2.57, 2.63])
marja.append([17.05, 16.81])
costs.append([14.95, 11.9])
names.append(["переход на заправку по топливным картам, отказ от заправки за наличные средства",
            "установка спутниковых датчиков GPS по отслеживанию выполнения маршрута"])

# 7 регион
risk.append([2.24])
marja.append([14.41])
costs.append([6.56])
names.append(["приобретение и оборудование бронеавтомобилей"])

# 8 регион
risk.append([1.05, 1.08, 1.14])
marja.append([13.93, 14.05, 16.41])
costs.append([11.55, 13.69, 11.08])
names.append(["приобретение базы (г. Находка)",
            "приобретение и доукомплектование шрузового и легкового автотранспорта",
            "разработка и внедрение специальных средств упаковки ценных грузов"])

projects_in_region = [2, 1, 4, 2, 2, 3, 2, 1, 3] # количество проектов по регионам
regions = 9

childs = 100 # количество экземпляров (решений) в одном поколении
generations = 100 # количество поколений

x = [] # пока пустой массив с экземплярами
pokolenie = []  # пустое поколение

up_cost = 0   # с + М, надо посчитать
pobeditel = []

def first_x(): # заполнили поколение случайным образом
    global pokolenie
    for k in range(childs):
        x = []
        for i in range(regions): # создаем случайный ответ
            pr = []
            for y in range(projects_in_region[i]): 
                pr.append(random.randint(0, 1))
            x.append(pr)
        pokolenie.append(x)

def fitness(X): # функция определения значений целевой функции (считается прибыль этого варианта)
    max = 0
    for i in range(regions):
        for j in range(len(X[i])):
            # исходная функция, которую надо максимизировать
            max = max + X[i][j] * marja[i][j]
    return max

def seek_max(): # функция нахождения максимального значения целевой функции во всем поколении (чемпион)
    # old_generation = x.copy() # копирование всего поколения
    f_max = 0
    for i in range(childs):
        f = fitness(pokolenie[i])
        if f > f_max:
            f_max = f
    return f_max

def up_limit(): # функция нахождения предела затрат (считаем край бюджета) и сохранение его в up_cost
    global up_cost
    up_cost = M
    for i in c:
        up_cost += c[0]

def test_costs(X): # функция определения стоимости реализации особо (сравнение этого значения и чтобы не было больше c + M)
    s = True
    stoimost = 0
    for i in range(regions):
        for j in range(len(X[i])):
            # исходная функция, которую надо максимизировать
            stoimost = stoimost + X[i][j] * costs[i][j]
    return stoimost

def test_one_project(X): # функция определения наличия хотя бы одного проекта
    rez = True
    s = 0
    for i in range(regions):
        s = 0
        for j in range(len(X[i])):
            s = s + X[i][j]
        if s == 0:
            rez = False
    return rez

def new_generation(): # вся суть задачи - формирование нового поколения
    global pokolenie
    old_generation = pokolenie.copy() # копируем все предыдущее поколение
    s = seek_max() # находим чемпиона и значение целевой функции (максимальную прибыль в предыдущем поколении)
    pokolenie = []
    for i in range(childs): # оставляем все особи (хромосомы), у которых целевая функция больше чем 80% от максимального значения
        if fitness(old_generation[i]) >= 0.8 * s and test_costs(old_generation[i]) <= up_cost and test_one_project(old_generation[i]) == True:
            pokolenie.append(old_generation[i])
    for k in range(childs - len(pokolenie)): # далее дозаполняем случайными значениями
        x = []
        for i in range(regions):
            pr = []
            for y in range(projects_in_region[i]):
                pr.append(random.randint(0, 1))
            x.append(pr)
        pokolenie.append(x)

def seek_winner(): # функция нахождения чемпиона в поколении
    winners = []
    for i in range(childs):
        if fitness(pokolenie[i]) >= seek_max() * 0.5 and test_costs(pokolenie[i]) <= up_cost and test_one_project(pokolenie[i]) == True:
            winners.append([pokolenie[i], fitness(pokolenie[i])])
        max_cf = 0
        for i in winners:
            if i[1] > max_cf:
                return i[0]

up_limit() # находим предел затрат (считаем край бюджета)

first_x() # генерируем случайные значения первого поколения

new_generation() # генерируем новое поколение, но оставляем часть старого

for i in range(generations): # проводим эволючию заданное количество поколений
    new_generation()

w = seek_winner()
print(w) # вывод победителя
print("Прибыль от победителя - ", fitness(w)) # вывод прибыли от победителя (должно быть 246,82)
print("Затраты на реализацию проектов победителя - ", test_costs(w)) # проверка стоимости реализации ....
print("Лимит трат на реализацию - ", up_cost) # вывод на экран


root = Tk()

out=[]
out.append(['Прибыль','Риск','Стоимость','Название проекта','ЦФО','Одобрен'])

def fill_out(): # Заполнение таблицы
    global out
    sum_cost = 0
    sum_marja = 0
    count_projects = 0 # Число одобренных проектов
    for i in range(regions): # создаем случайный образ
        out.append(["","","","ЦФО № "+str(i),"",""])
        for j in range(projects_in_region[i]):
            if w[i][j]==1:
                r="ДА"
                count_projects+=1
                sum_cost += costs[i][j]
                sum_marja+=marja[i][j]
            else:
                r="НЕТ"
            out.append([marja[i][j],risk[i][j],costs[i][j],names[i][j],i,r])
    out.append([str(round(sum_marja,2)),"",str(round(sum_cost,2)),"ВСЕГО ОДОБРЕНО "+str(count_projects)+" ПРОЕКТОВ, ЛИМИТ ДЕНЕГ СОСТАВЛЯЕТ "+str(up_cost),"",""])
fill_out()


root.title("Портфель инвестиций")
for i in range(len(out)):
    for j in range(6):
        l = Label(text=str(out[i][j]), relief=RIDGE)
        l.grid(row=i, column=j, sticky=NSEW)

root.mainloop()