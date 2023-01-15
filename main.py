#Обычный калькулятор, подробно расписан, что бы было понятно что за что отвечает
from tkinter import * #Это graphical user interface(GUI) (стандартная)библиотека работы с графическим интерфейсом.
                      #Звёздочка даёт использование всех модулей из библиотеки


window = Tk() # - Переменная с незаурядным названием "Окно", с классом "Окна":)
window.title("Калькулятор") # Называем наше приложение
window.geometry("320x250") # И даём ему разрешение

def input_entry(symbol): #Пишем END, что бы цифры вводились форматом 123, а не 321
    entry.insert(END,symbol)
def clear(): #Функция для кнопки Delete, ничего не пишем в ней, и удаляем всё от 0 до END
    entry.delete(0,END)
def result():   #Прописываем для кнопки равно, сплитим наш текст(флоат пишем т.к. не используем формат текста, а числа
    text = entry.get()
    result = 0
    if '+' in text:
        splitted_text = text.split("+")
        a = float(splitted_text[0])
        b = float(splitted_text[1])
        result = a+b
        print(result)
    if '-' in text:
            splitted_text = text.split("-")
            a = float(splitted_text[0])
            b = float(splitted_text[1])
            result = a - b
            print(result)
    if '/' in text:
            splitted_text = text.split("/")
            a = float(splitted_text[0])
            b = float(splitted_text[1])
            print(result)

    if '*' in text:
            splitted_text = text.split("*")
            a = float(splitted_text[0])
            b = float(splitted_text[1])
            result = a * b
            print(result)
    clear()
    entry.insert(0,result)



entry = Entry(window, background="grey",font=('', 26),foreground="black",width= 15) #Окошко для ввода, меняем фон, шрифт, цвет цифр, и их кол-во в поле для ввода
entry.place(x=12,y=30)

baton1 = Button(window, bg='black', fg='white',font= 12, text="1",command=lambda: input_entry("1")) #Переменная(кнопка) - окошком с фоном, цветом цифр, шрифтом и текстом в ней, а так же лямбдой для "работы" циферки
baton1.place(x=12,y=100,width=40) #Местоположение

baton2 = Button(window, bg='black', fg='white',font= 12, text="2",command=lambda: input_entry("2"))
baton2.place(x=52,y=100,width=40)

baton3 = Button(window, bg='black', fg='white',font= 36, text="3",command=lambda: input_entry("3"))
baton3.place(x=92,y=100,width=40)

baton4 = Button(window, bg='black', fg='white',font= 12, text="4",command=lambda: input_entry("4"))
baton4.place(x=12,y=130,width=40)

baton5 = Button(window, bg='black', fg='white',font= 12, text="5",command=lambda: input_entry("5"))
baton5.place(x=52,y=130,width=40)

baton6 = Button(window, bg='black', fg='white',font= 12, text="6",command=lambda: input_entry("6"))
baton6.place(x=92,y=130,width=40)

baton7 = Button(window, bg='black', fg='white',font= 12, text="7",command=lambda: input_entry("7"))
baton7.place(x=12,y=160,width=40)

baton0 = Button(window, bg='black', fg='white',font= 12, text=".",command=lambda: input_entry("."))
baton0.place(x=92,y=220,width=40)

baton8 = Button(window, bg='black', fg='white',font= 12, text="8",command=lambda: input_entry("8"))
baton8.place(x=52,y=160,width=40)

baton9 = Button(window, bg='black', fg='white',font= 12, text="9",command=lambda: input_entry("9"))
baton9.place(x=92,y=160,width=40)

baton_plus = Button(window, bg='black', fg='white',font= 12, text="+",command=lambda: input_entry("+"))
baton_plus.place(x=130,y=100,width=40)

baton_minus = Button(window, bg='black', fg='white',font= 12, text="-",command=lambda: input_entry("-"))
baton_minus.place(x=130,y=130,width=40)

baton_divide = Button(window, bg='black', fg='white',font= 12, text="/",command=lambda: input_entry("/"))
baton_divide.place(x=130,y=160,width=40)

baton_multiply = Button(window, bg='black', fg='white',font= 12, text="*",command=lambda: input_entry("*"))
baton_multiply.place(x=170,y=130,width=40)

baton_result = Button(window, bg='black', fg='white',font= 12, text="=",command=result) #Функции для равно и очистки написаны в начале, сюда только их название
baton_result.place(x=170,y=160,width=40)

baton_clear = Button(window, bg='black', fg='white',font= 12, text="CE",command= clear)
baton_clear.place(x=170,y=100,width=40)

baton_dot = Button(window, bg='black', fg='white',font= 12, text="0",command=lambda: input_entry("0"))
baton_dot.place(x=12,y=190,width=198)

window.mainloop() #Что бы приложение работала нон стоп, циклим работу этой командой