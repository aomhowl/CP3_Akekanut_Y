menulist = []
pricelist = []

def showbill():
    total = 0
    print('---- Howl Restaurant ----')
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
        total += int(pricelist[number])
    print('Total : ', total)
    print('---- Thank You -----')

while True:
    menu = input('Please Enter Menu: ')
    if(menu.lower() == 'exit'):
        break
    else:
        menuprice = input('Price : ')
        menulist.append(menu)
        pricelist.append(menuprice)
showbill()
