import math


# задание 1
WHITE_BG = '\u001b[47m'   
BLUE_BG  = '\u001b[44m' 
BLACK_BG = '\u001b[40m' 
RED_TEXT = '\033[31m' 
BLUE_TEXT = '\033[34m'
RESET    = '\033[0m'      

def Finland_flag(width=36, height=18, cross_thickness=None, vertical_pos=None):
    if cross_thickness is None:
        cross_thickness = max(1, height // 6)
    if vertical_pos is None:
        vertical_pos = width // 3

    horiz_y = height // 2  # верхняя строка горизонтальной полосы

    for y in range(height):
        row_parts = [] # список в кот мы собираем строку и печатаем целиком
        for x in range(width):
            # проверяем, попадает ли текущая позиция в вертикальную или горизонтальную полосу
            in_vertical = (vertical_pos <= x < vertical_pos + cross_thickness)
            in_horizontal = (horiz_y <= y < horiz_y + cross_thickness)
            if in_vertical or in_horizontal:
                row_parts.append(BLUE_BG + ' ')
            else:
                row_parts.append(WHITE_BG + ' ')
        # соединяем и сбрасываем цвет в конце строки
        print(''.join(row_parts) + RESET)

Finland_flag()


# задание 2  

def draw_two_circles(width=40, height=15, radius=4, aspect=2.0, distance=15):
    # Координаты центров двух кружков
    cx1 = width // 2 - distance // 2
    cx2 = width // 2 + distance // 2
    cy = height // 2  # общий центр по вертикали

    for y in range(height):
        row = ""
        for x in range(width):
            # Исправление пропорций по горизонталиё
            dx1 = (x - cx1) / aspect
            dx2 = (x - cx2) / aspect
            dy = y - cy

            # Проверяем, попадает ли точка в один из кругов
            in_circle1 = dx1**2 + dy**2 < radius**2
            in_circle2 = dx2**2 + dy**2 < radius**2

            if in_circle1 or in_circle2:
                row += BLACK_BG + " "
            else:
                row += WHITE_BG + " "
        print(row + RESET)

#draw_two_circles()

#задание 3         

def graph():
    width = 20   
    height = 10  

    for y in range(height, -1, -1):  
        line = ""
        for x in range(width + 1):   
            func_y = x / 2           
            #коэффициент растяжения, чтобы пропорции графика были нормальными
            display_y = func_y * (height / (width / 2)) 

            if abs(y - display_y) < 0.3:
                line += f"{RED_TEXT}#{RESET}"


            elif y == 0 and x == 0:
                line += "└"
            elif y == 0:
                line += "─"
            elif x == 0:
                line += "│"
            else:
                line += " "
        print(line)

graph()

#задание 4

f = open("/Users/canon652/lab 1/sequence.txt", "r")
m = []
for s in f:
    m.append(float(s.strip()))
f.close()

pos_sum = 0  # положительные (от 5 до 10)
neg_sum = 0  # отрицательные (от -10 до -5)
total_sum = 0  # сумма модулей всех подходящих чисел

for n in m:
    if 5 <= n <= 10:
        pos_sum += abs(n)
        total_sum += abs(n)
    elif -10 <= n <= -5:
        neg_sum += abs(n)
        total_sum += abs(n)


# Вычисляем процентное соотношение
pos_percent = pos_sum / total_sum * 100
neg_percent = neg_sum / total_sum * 100


pos_bar = "#" * int(pos_percent)
neg_bar = "#" * int(neg_percent)

print(f"Положительные (5..10): |{BLUE_TEXT}{pos_bar}{RESET}" + f" {pos_percent:.1f}%")
print(f"Отрицательные (-10..-5): |{RED_TEXT}{neg_bar}{RESET}" + f" {neg_percent:.1f}%")
