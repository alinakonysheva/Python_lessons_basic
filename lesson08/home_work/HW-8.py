import random
import time


class Matrix:
    def __init__(self):
        self.board = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
        self.dim = 5

    def is_valid(self, x, y):
        if self.board[y][x] == " ":
            return True
        else:
            return False

    def move_x(self, x, y):
        self.board[y][x] = "X"

    def move_0(self, x, y):
        self.board[y][x] = "0"

    def is_win(self, m):
        for x in range(0, self.dim):
            for y in range(0, self.dim):
                if self.board[y][x] == m:
                    if x + 1 < self.dim and y + 1 < self.dim and x + 2 < self.dim and y + 2 < self.dim and self.board[y][x] == self.board[y + 1][x + 1] and self.board[y + 1][x + 1] == self.board[y + 2][x + 2]:
                        return True
                    elif x + 1 < self.dim and x + 2 < self.dim and self.board[y][x] == self.board[y][x + 1] and self.board[y][x + 1] == self.board[y][x + 2]:
                        return True
                    elif y + 1 < self.dim and y + 2 < self.dim and self.board[y][x] == self.board[y+1][x] and self.board[y+1][x] == self.board[y+2][x]:
                        return True
                    elif x - 1 > -1 and y - 1 > -1 and x - 2 > -2 and y - 2 > -2 and self.board[y][x] == self.board[y - 1][x - 1] and self.board[y - 1][x - 1] == self.board[y - 2][x - 2]:
                        return True
        return False

    def is_win_x(self):
        return self.is_win("X")

    def is_win_0(self):
        return self.is_win("0")

    def print(self):
        print("-----------Игровое-поле-----------")
        for x in range(0, self.dim):
            print(self.board[x])
        print("----------------------------------")


class HumanMind:
    def __init__(self, board, is_x, is_human):
        self.board = board
        self.is_x = is_x
        self.is_human = is_human

    def move(self):
        if self.is_human:
            xy = input("Введите координаты крестика, в формате х, у. Внимание, доска начинается с координаты 0,0  ")
            xa, ya = xy.split(',')
            x = int(xa)
            y = int(ya)
        else:
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            time.sleep(random.randint(1, 3))
            if self.is_x:
                print("Крестики ходят на {},{}".format(x, y))
            else:
                print("Нолики ходят на {},{}".format(x, y))

        if not self.board.is_valid(x, y):
            print("Указанные координаты заняты или выходят за размер поля")
            print("Попробуйте еще раз!")
            self.move()
        else:
            if self.is_x:
                self.board.move_x(x, y)
            else:
                self.board.move_0(x, y)


class Game:
    def __init__(self, is_human):
        self.board = Matrix()
        self.player1 = HumanMind(self.board, True, is_human)
        self.player2 = HumanMind(self.board, False, is_human)

    def move_player_1(self):
        self.player1.move()

    def move_player_2(self):
        self.player2.move()

    def start(self):
        while not self.board.is_win_0() and not self.board.is_win_x():
            self.board.print()
            self.move_player_1()
            if self.board.is_win_x():
                print("Крестики выиграли, ура!")
                break

            self.board.print()
            self.move_player_2()
            if self.board.is_win_0():
                print("Нолики выиграли, ура!")
                break

        print("Игра окончена, поздравляем победителя!")
        self.board.print()

game1 = Matrix()
game1.move_x(0, 2)
game1.move_x(1, 1)
game1.move_x(2, 0)
game1.is_win_x()

r = True
print("Добро пожаловать в захватывающий мир крестиков-ноликов!")
print("Если Вам станет грустно, в любой момент Вы можете покинуть игру.")
print("Для этого просто нажмите ctrl + c.")
print("Если Вы устали, то можете понаблюдать за игрой искуственных интеллектов.")
print("Если Вы достаточно бодры, то можете выбрать активную игру с другим разумным существом.")

try:
    is_human = input("Нажмите Enter, если хотите посмотреть на битву ИИ и любой символ, если желаете сразиться сами")
    while r:
        game = Game(is_human)
        game.start()
        a = input("Желаете отыграться (y/n)?  ")
        if a == 'y':
            r = True
        else:
            r = False
except KeyboardInterrupt:
    print("До скорых встреч!")


