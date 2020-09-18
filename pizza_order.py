import tkinter
import tkinter.ttk
from tkinter.ttk import Combobox
from tkinter import Spinbox

def click():
    dict_pizza = dict()
    dict_pizza['ПЕППЕРОНИ']={'Состав':{'Пепперони, моцарелла, томатный соус'},'Размер':{'S':395,'M':545}}
    dict_pizza['МАРГАРИТА']={'Состав':{'Томаты, моцарелла, томатный соус'},'Размер':{'S':395,'M':545}}
    dict_pizza['ГАВАЙСКАЯ']={'Состав':{'Курица, ветчина, ананас, моцарелла, томатный соус'},'Размер':{'S':415,'M':545}}
    
    pizza_order={'pizza':['ПЕППЕРОНИ','МАРГАРИТА','ГАВАЙСКАЯ'],'size':[size1.get(),size2.get(),size3.get()],'count':[count1.get(),count2.get(),count3.get()],'time':[time.get()],'your address':[address.get()],'your number':[number.get()]}
##    your_order.config(text=str(pizza_order))
    pizza_text = ''
    for i in range(len(pizza_order['size'])):
        for k in pizza_order:
            pizza_text += k + ': '
            try:
                pizza_text += str(pizza_order[k][i]) + ', '
            except IndexError:
                pass
    your_order.config(text=str(pizza_text))
    cost=[]
    for i in range(len(pizza_order['pizza'])):
        if pizza_order['size'][i] != '':
            cost.append(dict_pizza[pizza_order['pizza'][i]]['Размер'][pizza_order['size'][i]])
    itog_first=0
    for i in range(len(cost)):
        itog_first+=cost[i]*pizza_order['count'][i]


    import numpy as np

    itog=0

    if when.get()=='Завтра':
        if sum(pizza_order['count'])>=3:
            val, idx = min((val, idx) for (idx, val) in enumerate(cost))
            pizza_order['count'][idx]-=1
            count=np.array(pizza_order['count'])
            cost=np.array(cost)
            itog=0.95*(np.sum(count*cost))
            print('*** Пицца ',pizza_order['pizza'][idx],' с наименьшей стоимостью: ',val,' руб.')
            print()
            print('*** Убрали стоимость пиццы ',pizza_order['pizza'][idx],' из заказа')
            print()
            print('Скидка 5%: ',0.05*(np.sum(count*cost)),' руб.')
            print('Итог с учётом скидки: ',itog,' руб')
        elif sum(pizza_order['count'])<3:
            count=np.array(pizza_order['count'])
            cost=np.array(cost)
            itog=0.95*(np.sum(count*cost))
            print('Скидка 5%: ',0.05*(np.sum(count*cost)),' руб.')
            print('Итог с учётом скидки: ',itog,' руб')
    elif when.get()=='Сегодня':
        if sum(pizza_order['count'])>=3:
            val, idx = min((val, idx) for (idx, val) in enumerate(cost))
            pizza_order['count'][idx]-=1
            count=np.array(pizza_order['count'])
            cost=np.array(cost)
            itog=np.sum(count*cost)
            print('*** Пицца ',pizza_order['pizza'][idx],' с наименьшей стоимостью: ',val,' руб.')
            print()
            print('*** Убрали стоимость пиццы ',pizza_order['pizza'][idx],' из заказа')
            print()
            print('Итог с учётом скидки: ',itog,' руб')
        elif sum(pizza_order['count'])<3:
            count=np.array(pizza_order['count'])
            cost=np.array(cost)
            itog=np.sum(count*cost)
            print('Скидок нет(')
    result.config(text=itog)
    

root = tkinter.Tk()
##frame = tkinter.Frame(root)
##frame.pack()
##label1 = tkinter.Label(frame, text='Заказ пиццы')
##label1.pack() # вывод на экран

root.title("Заказ пиццы")

# 1 строка

tkinter.Label(root, text='Выбор пиццы:', borderwidth=8).grid(row=0,column=0)
tkinter.Label(root, text='Выберите размер:', borderwidth=8).grid(row=0,column=1)
tkinter.Label(root, text='Укажите количество:', borderwidth=8).grid(row=0,column=2)

tkinter.Label(root, text='ПЕППЕРОНИ', borderwidth=8).grid(row=1,column=0)
tkinter.Label(root, text='МАРГАРИТА', borderwidth=8).grid(row=2,column=0)
tkinter.Label(root, text='ГАВАЙСКАЯ', borderwidth=8).grid(row=3,column=0)
time=tkinter.StringVar()
tkinter.Label(root, text='Введите время заказа', borderwidth=8).grid(row=4,column=0)
tkinter.Entry(root,textvariable=time).grid(row=5,column=0)
address=tkinter.StringVar()
tkinter.Label(root, text='Введите адрес заказа', borderwidth=8).grid(row=4,column=1)
tkinter.Entry(root,textvariable=address).grid(row=5,column=1)
number=tkinter.StringVar()
tkinter.Label(root, text='Введите ваш номер телефона', borderwidth=8).grid(row=4,column=2)
tkinter.Entry(root,textvariable=number).grid(row=5,column=2)
tkinter.Label(root, text='Выберите дату заказа:', borderwidth=8).grid(row=7,column=1)
when=tkinter.StringVar()
Combobox(root,values=['Сегодня','Завтра'],textvariable=when).grid(row=8,column=1)
when.set('Сегодня') # - значение по умолчанию
tkinter.Label(root, text='Ваш заказ:', borderwidth=8).grid(row=9,column=1)
your_order=tkinter.Message(root)
your_order.grid(row=10,column=1)

tkinter.Label(root, text='Сумма заказа с учётом скидки:', borderwidth=8).grid(row=11,column=1)
result=tkinter.Label(root)
result.grid(row=12,column=1)
size1=tkinter.StringVar()
size2=tkinter.StringVar()
size3=tkinter.StringVar()
count1=tkinter.IntVar()
count2=tkinter.IntVar()
count3=tkinter.IntVar()


p1=Combobox(root,values=['S','M'],textvariable=size1)
p1.grid(row=1,column=1)
c1=Spinbox(root,from_= 0, to = 100,textvariable=count1)
c1.grid(row=1,column=2)

p2=Combobox(root,values=['S','M'],textvariable=size2)
p2.grid(row=2,column=1)
c2=Spinbox(root,from_= 0, to = 100,textvariable=count2)
c2.grid(row=2,column=2)
p3=Combobox(root,values=['S','M'],textvariable=size3)
p3.grid(row=3,column=1)
c3=Spinbox(root,from_= 0, to = 100,textvariable=count3)
c3.grid(row=3,column=2)



button1 = tkinter.Button(root, text='Заказать!',command=click)
button1.grid(row=13,column=1)

button2 = tkinter.Button(root, text='Выход',command=root.destroy)
button2.grid(row=14,column=1)



root.mainloop()
#print(size1.get())
#print(count1.get())

