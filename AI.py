from customtkinter import *

from sklearn import tree
import csv

window = CTk()
window.geometry("500x500+450+200")
window.resizable(False, False)
window.title("Narbeh's AI app")
lbl = CTkLabel(window, text="")
lbl.pack()
lable = CTkLabel(window, text="Hello this is my first AI app", font=('Helvetica', 22, 'bold'))
lable.pack()
labletemp = CTkLabel(window, text="")
labletemp.pack()
lable1 = CTkLabel(window, text="Please enter your Height: ")
lable1.pack()
input_height = CTkEntry(window)
input_height.pack()
lable2 = CTkLabel(window, text="Please enter your Weight: ")
lable2.pack()
input_weight = CTkEntry(window)
input_weight.pack()
lable3 = CTkLabel(window, text="Please enter your shoes size: ")
lable3.pack()
input_shoes = CTkEntry(window)
input_shoes.pack()
lable4 = CTkLabel(window, text="")
lable4.pack()

x = []
y = []
with open('list.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for i in data:
        x.append(i[0:3])
        y.append(i[3])
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


def res():
    h = int(input_height.get())
    w = int(input_weight.get())
    s = int(input_shoes.get())
    answer = [h, w, s]
    result = clf.predict([answer])
    lable6 = CTkLabel(window, text=f'I think you are a {str(result[0]).upper()}', font=('Helvetica', 20, 'bold'))
    lable6.pack()


button = CTkButton(window, text="see result", command=res)
button.pack()
lable5 = CTkLabel(window, text="")
lable5.pack()

window.mainloop()
