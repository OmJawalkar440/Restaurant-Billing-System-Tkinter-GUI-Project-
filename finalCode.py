from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('1366x738')
root.title('Restaurant Billing System')

# Functionality
def total():
    # pizza price
    greekprice = int(greekEntry.get()) * 299
    ginoprice = int(ginoEntry.get()) * 399
    belgaprice = int(belgaEntry.get()) * 599
    motorinoprice = int(motorinoEntry.get()) * 499
    opsprice = int(opsEntry.get()) * 699
    nneaprice = int(nneaEntry.get()) * 399

    totalpizzaprice = greekprice + ginoprice + belgaprice + motorinoprice + opsprice + nneaprice
    pizzaPriceEntry.delete(0, END)  # Clear previous entry
    pizzaPriceEntry.insert(0, f'{totalpizzaprice} Rs.')

    # burger price
    juicyprice = int(juicyEntry.get()) * 200
    ausprice = int(ausEntry.get()) * 250
    onionprice = int(onionEntry.get()) * 400
    chineseprice = int(chineseEntry.get()) * 300
    bisonprice = int(bisonEntry.get()) * 270
    elkprice = int(elkEntry.get()) * 580

    totalburgerprice = juicyprice + ausprice + onionprice + chineseprice + bisonprice + elkprice
    buegerPriceEntry.delete(0, END)  # Clear previous entry
    buegerPriceEntry.insert(0, f'{totalburgerprice} Rs.')

    # drinks price
    cherryprice = int(cherryEntry.get()) * 189
    draftprice = int(draftEntry.get()) * 189
    forestprice = int(forestEntry.get()) * 189
    frozenprice = int(frozenEntry.get()) * 189
    legenprice = int(legenEntry.get()) * 189
    mountainprice = int(mountainEntry.get()) * 189

    totaldrinksprice = cherryprice + draftprice + forestprice + frozenprice + legenprice + mountainprice
    drinkPriceEntry.delete(0, END)  # Clear previous entry
    drinkPriceEntry.insert(0, f'{totaldrinksprice} Rs.')

    # Calculate Tax (example: 10% tax)
    pizzatax = round(totalpizzaprice * 0.10, 2)
    burgertax = round(totalburgerprice * 0.10, 2)
    drinktax = round(totaldrinksprice * 0.10, 2)

    pizzaTaxEntry.delete(0, END)
    pizzaTaxEntry.insert(0, f'{pizzatax} Rs.')

    buegerTaxEntry.delete(0, END)
    buegerTaxEntry.insert(0, f'{burgertax} Rs.')

    drinkTaxEntry.delete(0, END)
    drinkTaxEntry.insert(0, f'{drinktax} Rs.')

def bill_area():
    if nameEntry.get() == '':
        tmsg.showinfo('Suggestion', 'Please enter your Name.')
        return
    elif phoneEntry.get() == '':
        tmsg.showinfo('Suggestion', 'Please enter your Phone Number.')
        return

    # Fetching and displaying values in bill area
    total_pizza = pizzaPriceEntry.get()
    total_burger = buegerPriceEntry.get()
    total_drinks = drinkPriceEntry.get()

    pizza_tax = pizzaTaxEntry.get()
    burger_tax = buegerTaxEntry.get()
    drink_tax = drinkTaxEntry.get()

    total_cost = (float(total_pizza.split()[0]) + float(total_burger.split()[0]) + float(total_drinks.split()[0]))
    total_tax = (float(pizza_tax.split()[0]) + float(burger_tax.split()[0]) + float(drink_tax.split()[0]))

    grand_total = total_cost + total_tax

    # Displaying Bill Details
    textArea.delete('1.0', END)  # Clear previous bill
    textArea.insert(END, f"Customer Name: {nameEntry.get()}\n")
    textArea.insert(END, f"Phone Number: {phoneEntry.get()}\n")
    textArea.insert(END, f"Bill Number: {billEntry.get()}\n")
    textArea.insert(END, "=====================================\n")
    textArea.insert(END, f"Total Pizza Price: {total_pizza}\n")
    textArea.insert(END, f"Total Burger Price: {total_burger}\n")
    textArea.insert(END, f"Total Drinks Price: {total_drinks}\n")
    textArea.insert(END, f"Pizza Tax: {pizza_tax}\n")
    textArea.insert(END, f"Burger Tax: {burger_tax}\n")
    textArea.insert(END, f"Drinks Tax: {drink_tax}\n")
    textArea.insert(END, "-------------------------------------\n")
    textArea.insert(END, f"Grand Total: {grand_total} Rs.\n")
    textArea.insert(END, "=====================================\n")

# 1. USER INTERFACE GUI..
# heading..
Heading_label = Label(root, text = 'Restaurant Billing System', font = 'comic 30 bold', bg = 'ghostWhite',fg = 'DarkOrange', bd = '12',relief = GROOVE)
Heading_label.pack(fill = X)

# customer detail..
customerDetailLabelFrame = LabelFrame(root, text = 'Customer Detail',font = 'comic 15 bold',bg = 'ghostWhite',fg = 'DarkOrange',bd = '8',relief = GROOVE)
customerDetailLabelFrame.pack(fill = X)

nameLabel = Label(customerDetailLabelFrame, text = 'Name',bg = 'ghostWhite', font = 'comic 15 bold')
nameLabel.grid(row = 0, column = 0,padx = 20,pady = 2)
nameEntry = Entry(customerDetailLabelFrame, font = 'lucida 15',bd = 7, width = 18)
nameEntry.grid(row = 0, column = 1, padx = 8,pady = 2)

phoneLabel = Label(customerDetailLabelFrame, text = 'Phone_Number',bg = 'ghostWhite', font = 'comic 15 bold')
phoneLabel.grid(row = 0, column = 2,padx = 20,pady = 2)
phoneEntry = Entry(customerDetailLabelFrame, font = 'lucida 15',bd = 7, width = 18)
phoneEntry.grid(row = 0, column = 3, padx = 8,pady = 2)

billLabel = Label(customerDetailLabelFrame, text = 'Bill_Number',bg = 'ghostWhite', font = 'comic 15 bold')
billLabel.grid(row = 0, column = 4,padx = 20,pady = 2)
billEntry = Entry(customerDetailLabelFrame, font = 'lucida 15',bd = 7, width = 18)
billEntry.grid(row = 0, column = 5, padx = 8,pady = 2)

searchButton = Button(customerDetailLabelFrame,text = 'Search',bg = 'DarkOrange',fg = 'ghostWhite', font = 'comic 15 bold',bd = 6, relief = GROOVE, width=9)
searchButton.grid(row = 0, column = 6, padx = 35,pady = 18)

# product frame which contain different product sections(pizza,burger,drinks,bill)..
productFrame = Frame(root)
productFrame.pack(fill = X)

# pizza
pizzaLabelFrame = LabelFrame(productFrame,text = 'Pizza',font = 'comic 15 bold',bg = 'ghostWhite',fg = 'DarkOrange',bd = '8',relief = GROOVE)
pizzaLabelFrame.grid(row=0,column=0)

greeklabel = Label(pizzaLabelFrame,text = 'Greek Pizza',bg = 'ghostWhite', font = 'comic 15 bold')
greeklabel.grid(row=0,column=0,pady = 9,padx = 10,sticky = 'w')
greekEntry = Entry(pizzaLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
greekEntry.grid(row=0,column=1,pady = 9,padx = 10)
greekEntry.insert(0,0)

ginolabel = Label(pizzaLabelFrame,text = 'Gino Sorbillo',bg = 'ghostWhite', font = 'comic 15 bold')
ginolabel.grid(row=1,column=0,pady = 9,padx = 10,sticky = 'w')
ginoEntry = Entry(pizzaLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
ginoEntry.grid(row=1,column=1,pady = 9,padx = 10)
ginoEntry.insert(0,0)

belgalabel = Label(pizzaLabelFrame,text = 'Pizza Belga',bg = 'ghostWhite', font = 'comic 15 bold')
belgalabel.grid(row=2,column=0,pady = 9,padx = 10,sticky = 'w')
belgaEntry = Entry(pizzaLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
belgaEntry.grid(row=2,column=1,pady = 9,padx = 10)
belgaEntry.insert(0,0)

motorinolabel = Label(pizzaLabelFrame,text = 'Motorino Pizza',bg = 'ghostWhite', font = 'comic 15 bold')
motorinolabel.grid(row=3,column=0,pady = 9,padx = 10,sticky = 'w')
motorinoEntry = Entry(pizzaLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
motorinoEntry.grid(row=3,column=1,pady = 9,padx = 10)
motorinoEntry.insert(0,0)

opslabel = Label(pizzaLabelFrame,text = 'Ops   Brooklyn',bg = 'ghostWhite', font = 'comic 15 bold')
opslabel.grid(row=4,column=0,pady = 9,padx = 10,sticky = 'w')
opsEntry = Entry(pizzaLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
opsEntry.grid(row=4,column=1,pady = 9,padx = 10)
opsEntry.insert(0,0)

nnealabel = Label(pizzaLabelFrame,text = 'nNea   Amsterdam',bg = 'ghostWhite', font = 'comic 15 bold')
nnealabel.grid(row=5,column=0,pady = 9,padx = 10,sticky = 'w')
nneaEntry = Entry(pizzaLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
nneaEntry.grid(row=5,column=1,pady = 9,padx = 10)
nneaEntry.insert(0,0)

# Burger..
brgerLabelFrame = LabelFrame(productFrame,text = 'Burger',font = 'comic 15 bold',bg = 'ghostWhite',fg = 'DarkOrange',bd = '8',relief = GROOVE)
brgerLabelFrame.grid(row=0,column=1)

juicylabel = Label(brgerLabelFrame,text = 'Juicy Lucy',bg = 'ghostWhite', font = 'comic 15 bold')
juicylabel.grid(row=0,column=0,pady = 9,padx = 10,sticky = 'w')
juicyEntry = Entry(brgerLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
juicyEntry.grid(row=0,column=1,pady = 9, padx = 10)
juicyEntry.insert(0,0)

auslabel = Label(brgerLabelFrame,text = 'Australian Burger',bg = 'ghostWhite', font = 'comic 15 bold')
auslabel.grid(row=1,column=0,pady = 9,padx = 10,sticky = 'w')
ausEntry = Entry(brgerLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
ausEntry.grid(row=1,column=1,pady = 9, padx = 10)
ausEntry.insert(0,0)

onionlabel = Label(brgerLabelFrame,text = 'Onion Burger',bg = 'ghostWhite', font = 'comic 15 bold')
onionlabel.grid(row=2,column=0,pady = 9,padx = 10,sticky = 'w')
onionEntry = Entry(brgerLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
onionEntry.grid(row=2,column=1,pady = 9, padx = 10)
onionEntry.insert(0,0)

chineselabel = Label(brgerLabelFrame,text = 'Chinese hamburger',bg = 'ghostWhite', font = 'comic 15 bold')
chineselabel.grid(row=3,column=0,pady = 9,padx = 10,sticky = 'w')
chineseEntry = Entry(brgerLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
chineseEntry.grid(row=3,column=1,pady = 9, padx = 10)
chineseEntry.insert(0,0)

bisonlabel = Label(brgerLabelFrame,text = 'Bison Burger',bg = 'ghostWhite', font = 'comic 15 bold')
bisonlabel.grid(row=4,column=0,pady = 9,padx = 10,sticky = 'w')
bisonEntry = Entry(brgerLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
bisonEntry.grid(row=4,column=1,pady = 9, padx = 10)
bisonEntry.insert(0,0)

elklabel = Label(brgerLabelFrame,text = 'Elk Burger',bg = 'ghostWhite', font = 'comic 15 bold')
elklabel.grid(row=5,column=0,pady = 9,padx = 10,sticky = 'w')
elkEntry = Entry(brgerLabelFrame,font = 'lucida 15 bold',bd = 5, width = 7)
elkEntry.grid(row=5,column=1,pady = 9, padx = 10)
elkEntry.insert(0,0)

# Drinks..
drinkLabelFrame = LabelFrame(productFrame,text = 'Drinks',font = 'comic 15 bold',bg = 'ghostWhite',fg = 'DarkOrange',bd = '8',relief = GROOVE)
drinkLabelFrame.grid(row=0,column=2)

cherrylabel = Label(drinkLabelFrame,text = 'Cherry Limeade Slush',bg = 'ghostWhite', font = 'comic 15 bold')
cherrylabel.grid(row=0,column=0,pady = 9,padx = 10,sticky = 'w')
cherryEntry = Entry(drinkLabelFrame,font = 'lucida 15 bold',bd = 5, width =3)
cherryEntry.grid(row=0,column=1,pady = 9, padx = 10)
cherryEntry.insert(0,0)

draftlabel = Label(drinkLabelFrame,text = 'Draft Root Beer',bg = 'ghostWhite', font = 'comic 15 bold')
draftlabel.grid(row=1,column=0,pady = 9,padx = 10,sticky = 'w')
draftEntry = Entry(drinkLabelFrame,font = 'lucida 15 bold',bd = 5, width = 3)
draftEntry.grid(row=1,column=1,pady = 9, padx = 10)
draftEntry.insert(0,0)

forestlabel = Label(drinkLabelFrame,text = 'Frosted Lemonade',bg = 'ghostWhite', font = 'comic 15 bold')
forestlabel.grid(row=2,column=0,pady = 9,padx = 10,sticky = 'w')
forestEntry = Entry(drinkLabelFrame,font = 'lucida 15 bold',bd = 5, width = 3)
forestEntry.grid(row=2,column=1,pady = 9, padx = 10)
forestEntry.insert(0,0)

frozenlabel = Label(drinkLabelFrame,text = 'Frozen Coffee',bg = 'ghostWhite', font = 'comic 15 bold')
frozenlabel.grid(row=3,column=0,pady = 9,padx = 10,sticky = 'w')
frozenEntry = Entry(drinkLabelFrame,font = 'lucida 15 bold',bd = 5, width = 3)
frozenEntry.grid(row=3,column=1,pady = 9, padx = 10)
frozenEntry.insert(0,0)

legenlabel = Label(drinkLabelFrame,text = 'Legendary Iced Tea',bg = 'ghostWhite', font = 'comic 15 bold')
legenlabel.grid(row=4,column=0,pady = 9,padx = 10,sticky = 'w')
legenEntry = Entry(drinkLabelFrame,font = 'lucida 15 bold',bd = 5, width = 3)
legenEntry.grid(row=4,column=1,pady = 9, padx = 10)
legenEntry.insert(0,0)

mountainlabel = Label(drinkLabelFrame,text = 'Mountain Dew',bg = 'ghostWhite', font = 'comic 15 bold')
mountainlabel.grid(row=5,column=0,pady = 9,padx = 10,sticky = 'w')
mountainEntry = Entry(drinkLabelFrame,font = 'lucida 15 bold',bd = 5, width = 3)
mountainEntry.grid(row=5,column=1,pady = 9, padx = 10)
mountainEntry.insert(0,0)

# bill area.
billAreaFrame = Frame(productFrame,bd = 8,relief = GROOVE)
billAreaFrame.grid(row=0,column=3)

billAreaLabel = Label(billAreaFrame,text = 'Bill Area',font = 'lucida 15 bold',bd = 7,relief = GROOVE)
billAreaLabel.pack(fill = X)
billscroll = Scrollbar(billAreaFrame, orient = VERTICAL)
billscroll.pack(side = RIGHT,fill = Y)
textArea = Text(billAreaFrame,height = 18.3,width = 43, yscrollcommand = billscroll.set)
billscroll.config(command = textArea.yview)
textArea.pack()

# BillMenu..
BillMenuLabelframe = LabelFrame(root, text = 'Bill Menu',font = 'comic 15 bold',bg = 'ghostWhite',fg = 'DarkOrange',bd = '8',relief = GROOVE)
BillMenuLabelframe.pack(fill = X)

pizzaPriceLabel = Label(BillMenuLabelframe,text = 'Pizza Price',bg = 'ghostWhite', font = 'comic 15 bold')
pizzaPriceLabel.grid(row=0,column=0,pady = 1,padx = 10,sticky = 'w')
pizzaPriceEntry = Entry(BillMenuLabelframe,font = 'lucida 12 bold',bd = 5, width = 14)
pizzaPriceEntry.grid(row=0,column=1,pady = 1, padx = 10)

buegerPriceLabel = Label(BillMenuLabelframe,text = 'Burger Price',bg = 'ghostWhite', font = 'comic 15 bold')
buegerPriceLabel.grid(row=1,column=0,pady = 1,padx = 10,sticky = 'w')
buegerPriceEntry = Entry(BillMenuLabelframe,font = 'lucida 12 bold',bd = 5, width = 14)
buegerPriceEntry.grid(row=1,column=1,pady = 1, padx = 10)

drinkPriceLabel = Label(BillMenuLabelframe,text = 'Drinks Price',bg = 'ghostWhite', font = 'comic 15 bold')
drinkPriceLabel.grid(row=2,column=0,pady = 1,padx = 10,sticky = 'w')
drinkPriceEntry = Entry(BillMenuLabelframe,font = 'lucida 12 bold',bd = 5, width = 14)
drinkPriceEntry.grid(row=2,column=1,pady = 1, padx = 10)

pizzaTaxLabel = Label(BillMenuLabelframe,text = 'Pizza Tax',bg = 'ghostWhite', font = 'comic 15 bold')
pizzaTaxLabel.grid(row=0,column=2,pady = 1,padx = 10,sticky = 'w')
pizzaTaxEntry = Entry(BillMenuLabelframe,font = 'lucida 12 bold',bd = 5, width = 14)
pizzaTaxEntry.grid(row=0,column=3,pady = 1, padx = 10)

buegerTaxLabel = Label(BillMenuLabelframe,text = 'Burger Tax',bg = 'ghostWhite', font = 'comic 15 bold')
buegerTaxLabel.grid(row=1,column=2,pady = 1,padx = 10,sticky = 'w')
buegerTaxEntry = Entry(BillMenuLabelframe,font = 'lucida 12 bold',bd = 5, width = 14)
buegerTaxEntry.grid(row=1,column=3,pady = 1, padx = 10)

drinkTaxLabel = Label(BillMenuLabelframe,text = 'Drinks Tax',bg = 'ghostWhite', font = 'comic 15 bold')
drinkTaxLabel.grid(row=2,column=2,pady = 1,padx = 10,sticky = 'w')
drinkTaxEntry = Entry(BillMenuLabelframe,font = 'lucida 12 bold',bd = 5, width = 14)
drinkTaxEntry.grid(row=2,column=3,pady = 1, padx = 10)

# button frame in bilmenulabelFrame..
buttonFrame = Frame(BillMenuLabelframe,bd = 8,relief =GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton = Button(buttonFrame,text = 'Total',bg = 'DarkOrange',fg = 'ghostWhite', font = 'comic 15 bold',bd = 6, relief = GROOVE, width=10,command=total)
totalButton.grid(row=0,column=0,padx = 7,pady=12)

billButton = Button(buttonFrame,text = 'Bill',bg = 'DarkOrange',fg = 'ghostWhite', font = 'comic 15 bold',bd = 6, relief = GROOVE, width=10,command=bill_area)
billButton.grid(row=0,column=1,padx = 7,pady=12)

emailButton = Button(buttonFrame,text = 'Email',bg = 'DarkOrange',fg = 'ghostWhite', font = 'comic 15 bold',bd = 6, relief = GROOVE, width=10)
emailButton.grid(row=0,column=2,padx = 7,pady=12)

printButton = Button(buttonFrame,text = 'Print',bg = 'DarkOrange',fg = 'ghostWhite', font = 'comic 15 bold',bd = 6, relief = GROOVE, width=10)
printButton.grid(row=0,column=3,padx = 7,pady=12)

clearButton = Button(buttonFrame,text = 'Clear',bg = 'DarkOrange',fg = 'ghostWhite', font = 'comic 15 bold',bd = 6, relief = GROOVE, width=9)
clearButton.grid(row=0,column=4,padx = 7,pady=12)


root.mainloop()
# The rest of your UI code remains unchanged...
