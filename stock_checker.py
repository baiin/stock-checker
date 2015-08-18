from tkinter import *
import requests
import bs4

symbolfile = open("stock_symbols.txt")
symbolslist = symbolfile.read()
symbolslist = symbolslist.split("\n")

def get_stock_price(stock_symbol):
    url = "http://finance.yahoo.com/q?s=" + stock_symbol
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.content, 'html.parser')
    
    stock_title = soup.find("div", {"class": "title"}).h2.contents
    stock_price = soup.find("span", {"class": "time_rtq_ticker"}).span.contents

    return stock_title[0], stock_price[0]
    

def update_display_box(stock_symbol, input_box, display_box):
    stock_symbol = stock_symbol.upper()

    stock_title, stock_price = get_stock_price(stock_symbol)
    
    string_one = "STOCK NAME: " + stock_title
    string_two = "STOCK PRICE: " + stock_price
    string_three = "--------------------------"
    
    display_box.insert(END, string_one)
    display_box.see(END)
    display_box.insert(END, string_two)
    display_box.see(END)
    display_box.insert(END, string_three)
    display_box.see(END)
    
    input_box.delete(0, 'end')


def layout():
    root = Tk()
    root.minsize(300, 300)
    root.maxsize(400, 400)
    root.title("stock checker")

    input_label = Label(root, text="ENTER A STOCK SYMBOL")
    input_box = Entry(root)
    submit_box = Button(root, text="SUBMIT", command=lambda:update_display_box(input_box.get(), input_box, display_box))
    display_box = Listbox(root)
    scroller = Scrollbar(root)

    input_label.pack(fill=X)
    input_box.pack(fill=X)
    submit_box.pack(fill=X)
    display_box.pack(fill=BOTH, expand=TRUE)
    scroller.pack(side=RIGHT, in_=display_box, fill=Y)

    root.mainloop()
    root.destroy()
    

layout()
    

