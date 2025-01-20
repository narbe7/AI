from customtkinter import *
# window = CTk()
from sklearn import tree
import csv

x = []
y = []
with open('list.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for i in data:
        x.append(i[0:3])
        y.append(i[3])
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)
aa = int(input('Enter your Height: '))
bb = int(input('Enter your Weight: '))
cc = int(input('Enter your shoes size: '))
answer = [aa, bb, cc]
result = clf.predict([answer])
print(f'I think you are a {result}')
# window.mainloop()
