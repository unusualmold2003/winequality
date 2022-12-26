import pandas as pd
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox as mb

window=tk.Tk()
window.geometry("1300x864")
window.title("WINE QUALITY PREDICTION")


img=Image.open('bg1.jpg')
render=ImageTk.PhotoImage(img)
img1=tk.Label(window,image=render)
img1.place(x=0,y=0)

def clr():
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    e10.delete(0, END)
    e11.delete(0, END)

def predict():
    global e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, model
    facid = e1.get()
    vacid = e2.get()
    cit_acid = e3.get()
    res_sugar = e4.get()
    chlorides = e5.get()
    free_sulfdio = e6.get()
    tot_sulfdio = e7.get()
    density = e8.get()
    ph = e9.get()
    sulphates = e10.get()
    alchohol = e11.get()

    wine_prop = [
        [facid, vacid, cit_acid, res_sugar, chlorides, free_sulfdio, tot_sulfdio, density, ph, sulphates, alchohol]]
    result = str(model.predict(sc.transform(wine_prop)))
    result = result.strip('[]')
    mb.showinfo('PREDICTION', f'THE PREDICTED WINE QUALITY IS {result}')




l1=tk.Label(window, text='FIXED ACID:',font=('Arial',13))
l1.place(x=70,y=50)
e1=tk.Entry(window)
e1.place(x=300,y=50)

l1=tk.Label(window, text='VOLATILE ACID:',font=('Arial',13))
l1.place(x=70,y=90)
e2=tk.Entry(window)
e2.place(x=300,y=90)

l1=tk.Label(window, text='CITRIC ACID:',font=('Arial',13))
l1.place(x=70,y=130)
e3=tk.Entry(window)
e3.place(x=300,y=130)

l1=tk.Label(window, text='RESIDUAL SUGAR:',font=('Arial',13))
l1.place(x=70,y=170)
e4=tk.Entry(window)
e4.place(x=300,y=170)

l1=tk.Label(window, text='CHLORIDES:',font=('Arial',13))
l1.place(x=70,y=210)
e5=tk.Entry(window)
e5.place(x=300,y=210)

l1=tk.Label(window, text='FREE SULPHURIC DIOXIDE:',font=('Arial',13))
l1.place(x=70,y=250)
e6=tk.Entry(window)
e6.place(x=300,y=250)

l1=tk.Label(window, text='TOTAL SULPHURIC DIOXIDE:',font=('Arial',13))
l1.place(x=70,y=290)
e7=tk.Entry(window)
e7.place(x=300,y=290)

l1=tk.Label(window, text='DENSITY:',font=('Arial',13))
l1.place(x=70,y=330)
e8=tk.Entry(window)
e8.place(x=300,y=330)

l1=tk.Label(window, text='ph Level:',font=('Arial',13))
l1.place(x=70,y=370)
e9=tk.Entry(window)
e9.place(x=300,y=370)

l1=tk.Label(window, text='SULPHATES:',font=('Arial',13))
l1.place(x=70,y=410)
e10=tk.Entry(window)
e10.place(x=300,y=410)

l1=tk.Label(window, text='ALCOHOL:',font=('Arial',13))
l1.place(x=70,y=450)
e11=tk.Entry(window)
e11.place(x=300,y=450)

b3 = tk.Button(window, text="Clear",command=clr)
b3.place(x=500, y=600)

b1=tk.Button(window, text='SEARCH', command=predict)
b1.place(x=500,y=500)

def quit():

    if mb.askyesno("Quit","Do you wanna Quit"):
        window.destroy()

b2=tk.Button(window,text='Quit',command=quit)
b2.place(x=600,y=600)

dataset=pd.read_csv("wine.csv")

#print(dataset.shape)
#print(dataset.head(5))

x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25,random_state=0)
print(x_train.shape)
print(x_test.shape)


from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state=0, max_iter=1000)
model.fit(x_train,y_train)





y_pred = model.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cm=confusion_matrix(y_test,y_pred)

print("Confusion Matrix:")
print(cm)

print("Accuracy of the Model: {0}%".format(accuracy_score(y_test,y_pred)*100))

window.mainloop()