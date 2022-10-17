from unidecode import unidecode as udc

valid_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
control = True
block_1 = "░"
block_2 = "█"
x_label = []
y_label = []
vystup = {}

#y_label contents
num = 0
space = " "
while num <= 100:

    if num < 10:
        y_label.append(2*space + str(num) + space + "%")
    elif num < 100:
        y_label.append(space + str(num) + space + "%")
    elif num == 100:
        y_label.append(str(num) + space + "%")
    
    num += 5

#x_label contents
for letter in valid_letters:
    x_label.append(letter)
x_label.insert(0, 5*space)

#populate output dict
for letter in valid_letters:
        vystup.update([[letter, [0, 0]]])

def count(user_input: str):

    vstup = udc(user_input).upper()
    
    if vstup in valid_letters:
        vystup[vstup][0] += 1

def display_calculate():
    current_largest = 0
    scale = 0

    for list in vystup.values():
        if list[0] > current_largest:
            current_largest = list[0]

    scale = current_largest / 20

    for key in vystup:
        try:
            vystup[key][1] = round(vystup[key][0] / scale)
        except:
            pass

def display_draw():
    compare = 20
    for i in range(len(y_label)):
        if i != 0:
            print(y_label[-i], end = " ")
            for value in vystup.values():
                if value[1] <= compare:
                    print(block_1, end = " ")
                else:
                    print(block_2, end = " ")

            print("")
        compare -= 1

    print(*x_label)

    print(6*space, end = "")
    for value in vystup.values():
        print(value[0], end = " ")
 
while control == True:
    user_input = input("\n\ninsert path: ")
    if user_input == "00":
        control = False
    else:
        file = open(user_input, "r")
        while znak := file.read(1):
            count(znak)

        display_calculate()
        display_draw()
