# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

#abc = input('Enter text using "абв" separated by spaces:\n')
#print(f'Source text: {abc}')
#find_abc = "абв"
#cba = [i for i in abc.split() if find_abc not in i]
#print(f'Text without "абв": {" ".join(cba)}')


# 2. Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

#from random import randint
#
#def input_dat(name):
#    x = int(input(f'{name}, how many candies do you want to take? Enter any number from 1 to 28: '))
#    while x < 1 or x > 28:
#        x = int(input(f"{name}, you can only take no more than 28 candies, please try again: "))
#    return x
#
#def p_print(name, k, value):
#    print(f'{name} took {k} candies. {value} candies left on the table.')
#
#player1 = input('What is your name, player 1? ')
#player2 = input('What is your name, player 2? ')
#value = int(input('How many candies are on the table? '))
#round = randint(0,2)
#if round:
#    print(f'{player1} goes first')
#else:
#    print(f'{player2} goes second')
#
#while value > 28:
#    if round:
#        k = input_dat(player1)
#        value -= k
#        round = False
#        p_print(player1, k, value)
#    else:
#        k = input_dat(player2)
#        value -= k
#        round = True
#        p_print(player2, k, value)
#
#if round:
#    print(f'{player1} won! HURRAY!')
#else:
#    print(f'{player2} won! HURRAY!')

# a) Добавьте игру против бота

#from random import randint
#
#def input_dat(name):
#    x = int(input(f'{name}, how many candies do you want to take? Enter any number from 1 to 28: '))
#    while x < 1 or x > 28:
#        x = int(input(f"{name}, you can only take no more than 28 candies, please try again: "))
#    return x
#
#def p_print(name, k, value):
#    print(f'{name} took {k} candies. {value} candies left on the table.')
#
#player1 = input('What is your name, player 1? ')
#player2 = 'Candy lover'
#value = int(input('How many candies are on the table? '))
#round = randint(0,2)
#if round:
#    print(f'{player1} goes first')
#else:
#    print(f'{player2} goes second')
#
#while value > 28:
#    if round:
#        k = input_dat(player1)
#        value -= k
#        round = False
#        p_print(player1, k, value)
#    else:
#        k = randint(1,29)
#        value -= k
#        round = True
#        p_print(player2, k, value)
#
#if round:
#    print(f'{player1} won! HURRAY!')
#else:
#    print(f'{player2} won! HURRAY!')

# b) Подумайте как наделить бота ""интеллектом""

#from random import randint
#
#def input_dat(name):
#    x = int(input(f'{name}, how many candies do you want to take? Enter any number from 1 to 28: '))
#    while x < 1 or x > 28:
#        x = int(input(f'{name}, you can only take no more than 28 candies, please try again: '))
#    return x
#
#def p_print(name, k, value):
#    print(f'{name} took {k} candies. {value} candies left on the table.')
#
#def candyBot(value):
#    k = randint(1,29)
#    while value-k <= 28 and value > 29:
#        k = randint(1,29)
#    return k
#
#player1 = input('What is your name, player 1? ')
#player2 = 'Candy lover'
#value = int(input('How many candies are on the table? '))
#round = randint(0,2)
#if round:
#    print(f'{player1} goes first')
#else:
#    print(f'{player2} goes second')
#
#while value > 28:
#    if round:
#        k = input_dat(player1)
#        value -= k
#        round = False
#        p_print(player1, k, value)
#    else:
#        k = candyBot(value)
#        value -= k
#        round = True
#        p_print(player2, k, value)
#if round:
#    print(f'{player1} won! HURRAY!')
#else:
#    print(f'{player2} won! HURRAY!')

# 3. Создайте программу для игры в ""Крестики-нолики"".

#board = list(range(1,10))
#
#def draw_board(board):
#   print('-' * 13)
#   for i in range(3):
#      print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
#      print('-' * 13)
#
#def take_input(player_token):
#   valid = False
#   while not valid:
#      player_answer = input('Where do we put ' + player_token + "? ")
#      try:
#         player_answer = int(player_answer)
#      except:
#         print('Invalid value! You should use only numbers from 1 to 9. Please, try again.')
#         continue
#      if player_answer >= 1 and player_answer <= 9:
#         if(str(board[player_answer-1]) not in "XO"):
#            board[player_answer-1] = player_token
#            valid = True
#         else:
#            print('This square is alredy occupied!')
#
#def check_win(board):
#   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#   for each in win_coord:
#       if board[each[0]] == board[each[1]] == board[each[2]]:
#          return board[each[0]]
#   return False
#
#def main(board):
#    counter = 0
#    win = False
#    while not win:
#        draw_board(board)
#        if counter % 2 == 0:
#           take_input('X')
#        else:
#           take_input('O')
#        counter += 1
#        if counter > 4:
#           tmp = check_win(board)
#           if tmp:
#              print(tmp, 'won!')
#              win = True
#              break
#        if counter == 9:
#            print('Friendship won')
#            break
#    draw_board(board)
#main(board)
#
#input('Press Enter to exit')

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('task4.txt', 'r') as data:
    code = data.read()

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

res = coding(code)
print(f'{res} - output data')

with open('task4d.txt', 'r') as data:
    code2 = data.read()

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

res = decoding(code2)
print(f'{res} - input data')