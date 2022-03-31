from tkinter import *
import requests
import json
import datetime

response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')

json_dict = json.loads(response.text)
date_now = datetime.date.today()

euro_dic = json_dict[1]
# print(round(euro_dic, 2))
usd_dic = json_dict[0]
btc_dic = json_dict[2]

# print(euro_dic.get("buy"))
# print(usd_dic)
# print(btc_dic)

root = Tk()
root.geometry('450x320+500+200')
root.title('Конвертер валют')
root.resizable(False, False)


def change():
    sum = int(e_entry.get())
    if sum != "":
        l_usd_in['text'] = '{0:.2f}'.format(sum * float(usd_dic.get("buy")), 2)
        l_eur_in['text'] = '{0:.2f}'.format(sum * float(euro_dic.get("buy")), 2)
        l_btc_in['text'] = '{0:.2f}'.format(sum * float(usd_dic.get("buy")) * float(btc_dic.get("buy")), 2)
        l_usd_out['text'] = '{0:.2f}'.format(sum * float(usd_dic.get("sale")), 2)
        l_eur_out['text'] = '{0:.2f}'.format(sum * float(euro_dic.get("sale")), 2)
        l_btc_out['text'] = '{0:.2f}'.format(sum * float(usd_dic.get("sale")) * float(btc_dic.get("sale")), 2)


l_title = Label(root, text=f'Курс на {date_now}', font='Arial 15')
l_title.pack(fill=X, expand=0)

f_cur = Frame(root)
f_cur.pack()

j = 1
for i in json_dict:
    l_main = Label(f_cur)
    l_main.grid(row=0, column=j)
    l_ccy = Label(f_cur, text=i.get('ccy'), font='Arial 10', height=1, width=10)
    l_ccy.grid(row=2, column=j)
    l_base = Label(f_cur, text=i.get('base_ccy'), font='Arial 10', height=1, width=10)
    l_base.grid(row=3, column=j)
    l_buy = Label(f_cur, text=i.get('buy'), font='Arial 10', height=1, width=10)
    l_buy.grid(row=4, column=j)
    l_sale = Label(f_cur, text=i.get('sale'), font='Arial 10', height=1, width=10)
    l_sale.grid(row=5, column=j)
    j += 1

l_entry = Label(f_cur, text='Введите сумму для обмена', font='Arial 10', height=1, width=20)
l_entry.grid(row=6, columnspan=4, pady=15)
e_entry = Entry(f_cur)
e_entry.insert(0, '1000')
e_entry.grid(row=7, column=1)
e_button = Button(f_cur, text='Обменять', font='Arial 10', command=change)
e_button.grid(row=7, column=2)

l_usd_in = Label(f_cur, font='Arial 10', height=0, width=10)
l_usd_in.grid(row=8, column=1, pady=10)
l_eur_in = Label(f_cur, font='Arial 10', height=0, width=10)
l_eur_in.grid(row=8, column=2, pady=10)
l_btc_in = Label(f_cur, font='Arial 10', height=0, width=15)
l_btc_in.grid(row=8, column=3, pady=10)
l_usd_out = Label(f_cur, font='Arial 10', height=0, width=10)
l_usd_out.grid(row=9, column=1)
l_eur_out = Label(f_cur, font='Arial 10', height=0, width=10)
l_eur_out.grid(row=9, column=2)
l_btc_out = Label(f_cur, font='Arial 10', height=0, width=15)
l_btc_out.grid(row=9, column=3)

l_buy1 = Label(f_cur, text='Покупка', font='Arial 10', height=0, width=10)
l_buy1.grid(row=4, column=0)
l_buy2 = Label(f_cur, text='Продажа', font='Arial 10', height=0, width=10)
l_buy2.grid(row=5, column=0)
l_buy3 = Label(f_cur, text='Выдать', font='Arial 10', height=0, width=10)
l_buy3.grid(row=8, column=0)
l_buy4 = Label(f_cur, text='Получить', font='Arial 10', height=0, width=10)
l_buy4.grid(row=9, column=0)

root.mainloop()
