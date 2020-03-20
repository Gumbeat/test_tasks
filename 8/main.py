rows = [
    1,
    3,
    5,
    7
]


def row_to_multipliers(number):
    multipliers = {
        1: 0,
        2: 0,
        4: 0
    }
    temp_num = number
    while temp_num > 0:
        if temp_num >= 4:
            multipliers[4] += 1
            temp_num -= 4
        elif temp_num >= 2:
            multipliers[2] += 1
            temp_num -= 2
        else:
            multipliers[1] += 1
            temp_num -= 1
    return multipliers


def row_num_subtraction(multipliers_list, search_num, substract_num):
    for i in range(len(multipliers_list)):
        if not multipliers_list[i][search_num] == 0:
            rows[i] -= substract_num
            break


def is_in_dict(x, y):
    for list_value in y:
        if x[list_value] == 0:
            return False
    return True


def row_nums_subtraction(multipliers_list, numlist):
    for i in range(len(multipliers_list)):
        if is_in_dict(multipliers_list[i], numlist):
            rows[i] -= sum(numlist)
            return True
    return False


def print_rows_data():
    for i in range(len(rows)):
        print(f'Строка {i + 1}: {rows[i]}')


def player_move():
    print()
    print('ход игрока')
    print()
    row_num = int(input('Введите номер строки: ')) - 1
    while row_num not in range(0, 4):
        row_num = int(input('Некорректный ввод, введите повторно: '))
    num_to_remove = int(input('Введите число для вычитания из этой строки: '))
    while not check_num_to_remove(num_to_remove, row_num):
        num_to_remove = int(input('Некорректный ввод, введите повторно: '))
    rows[row_num] -= num_to_remove


def check_if_one_row_left():
    return rows.count(0) == 3


def computer_move():
    print()
    print('ход компьютера')
    print()
    if check_if_one_row_left():
        for i in range(len(rows)):
            if not rows[i] == 0:
                rows[i] = 0
                return 0
    row_multipliers_list = [row_to_multipliers(row) for row in rows]
    n_1 = n_2 = n_4 = 0
    for multipliers in row_multipliers_list:
        n_1 += multipliers[1]
        n_2 += multipliers[2]
        n_4 += multipliers[4]
    n1_res = n_1 % 2
    n2_res = n_2 % 2
    n4_res = n_4 % 2
    if n1_res == 1 and n2_res == 0 and n4_res == 0:
        row_num_subtraction(row_multipliers_list, 1, 1)
    elif n1_res == 0 and n2_res == 1 and n4_res == 0:
        row_num_subtraction(row_multipliers_list, 2, 2)
    elif n1_res == 0 and n2_res == 0 and n4_res == 1:
        row_num_subtraction(row_multipliers_list, 4, 2)
    elif n1_res == 1 and n2_res == 1 and n4_res == 0:
        if not row_nums_subtraction(row_multipliers_list, [1, 2]):
            row_num_subtraction(row_multipliers_list, 2, 1)
    elif n1_res == 1 and n2_res == 0 and n4_res == 1:
        if not row_nums_subtraction(row_multipliers_list, [1, 4]):
            row_num_subtraction(row_multipliers_list, 4, 3)
    elif n1_res == 0 and n2_res == 1 and n4_res == 1:
        if not row_nums_subtraction(row_multipliers_list, [2, 4]):
            row_num_subtraction(row_multipliers_list, 4, 2)
    elif n1_res == 1 and n2_res == 1 and n4_res == 1:
        if not row_nums_subtraction(row_multipliers_list, [1, 2, 4]):
            row_num_subtraction(row_multipliers_list, 4, 1)
    else:
        print('Где-то ошибка')


def is_game_over():
    s = 0
    for row in rows:
        s += row
    return s == 0


def check_num_to_remove(n, rn):
    return rows[rn] >= n


print('Начало игры')
print()
print('Выигрывает тот, кто последним обнулит все строчки')
print()
computer_won = player_won = False
print_rows_data()
while True:
    player_move()
    if is_game_over():
        player_won = True
        break
    print_rows_data()
    computer_move()
    print_rows_data()
    if is_game_over():
        computer_won = True
        break
if player_won:
    print('Победа игрока')
elif computer_won:
    print('Победа компьютера')
