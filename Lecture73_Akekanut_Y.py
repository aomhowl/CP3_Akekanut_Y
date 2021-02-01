systemmenu = {'ข้าว':10,'ข้าวต้ม':15,'น้ำ':2}
menulist = []

def showbill():
    total = 0
    print('---- Howl Restaurant ----')
    for number in range(len(menulist)):
        print(menulist[number][0],menulist[number][1])
        total += int(menulist[number][1])
    print('total = ', total)
    print('---- Thank You ----')

while True:
    menu = input('Please Enter Menu: ')
    if(menu.lower() == 'exit'):
        break
    else:
        menulist.append([menu,systemmenu[menu]])

print(menulist)
showbill()
