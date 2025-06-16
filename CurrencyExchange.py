import tkinter
from tkinter import*
from tkinter.ttk import *
import requests
window=Tk()

window.title("Currency Exchange")
window.geometry('550x300')
window.configure(bg="#fa9eb3")

def convert():
    global baseURL
    global finalURL

    fromCurrency=comfrom.get()
    toCurrency=comto.get()
    apikey="K3MQO5ISZGAYC6NI"
    baseURL=r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    finalURL=baseURL+"&from_currency="+fromCurrency+"&to_currency="+toCurrency+"&apikey="+apikey
    print(finalURL)
    req_obj=requests.get(finalURL)
    result=req_obj.json()
    print(result)
    exchange_rate=float(result["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    print(exchange_rate)
    a = float(entry.get())
    final=a*exchange_rate
    resultlabel.configure(text="Result: "+str(final))
    print(final)

label1=Label(window,text="Currency Exchange",font=("Arial",15))
labelamount=Label(window,text="Amount",font=("Arial",12))
labelfrom=Label(window,text="From",font=("Arial",12))
labelto=Label(window,text="To",font=("Arial",12))
comfrom=Combobox(window)
comfrom ['values']=("USD","EUR","JPY","PLN","BGN","CZK")
comto=Combobox(window)
comto ['values']=("USD","EUR","JPY","PLN","BGN","CZK")
convertbutton=Button(window,text="Convert",command=convert)
entry=Entry(window)
resultlabel=Label(window,text="Result:",font=("Arial",12))

label1.place(x=195,y=20)
labelamount.place(x=60,y=60)
labelfrom.place(x=250,y=60)
labelto.place(x=440,y=60)
comfrom.place(x=200,y=90)
comto.place(x=380,y=90)
entry.place(x=30,y=90)
convertbutton.place(x=240,y=150)
resultlabel.place(x=250,y=200)

window.resizable(False,False)

window.mainloop()