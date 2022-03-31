from tkinter import *
import requests
import json
import datetime

response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
# response = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')

json_dict = json.loads(response.text)

date_now = datetime.date.today()

root = Tk()
root.geometry('400x220+500+200')
root.title('Currency')
root.iconbitmap('dol.ico')

l_title = Label(root, text=f'Курс на {date_now}', font='Arial 15')
l_title.pack(fill=X, expand=0)

f_cur = Frame(root)
f_cur.pack()

j = 0
for i in json_dict:
    l = Label(f_cur)
    l.grid(row=0, column=j)
    l_ccy = Label(f_cur, text=i.get('ccy'), font='Arial 10', height=2, width=10)
    l_ccy.grid(row=2, column=j)
    l_base = Label(f_cur, text=i.get('base_ccy'), font='Arial 10', height=2, width=10)
    l_base.grid(row=3, column=j)
    l_buy = Label(f_cur, text=i.get('buy'), font='Arial 10', height=2, width=10)
    l_buy.grid(row=4, column=j)
    l_sale = Label(f_cur, text=i.get('sale'), font='Arial 10', height=2, width=10)
    l_sale.grid(row=5, column=j)
    j += 1

root.mainloop()
