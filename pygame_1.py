# Проект pygame


# Задачи
# названия файлов на латыни +
# во время показа все названия поменять!
# pep 8 +-
# заставка и экран конца игры +
# count   +
# newgame +
# музон   +
# просмотр ходов +
import os
import os.path
import pygame
import math

w = 400
n = 8
v = 2
# инициализация pygame:
pygame.init()
# размеры окна:
size = width, height = w + 250, w
running = True
fps = 60
clock = pygame.time.Clock()
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('white'))
sound1 = pygame.mixer.music.load('C:/Users/Элвин/Desktop/Sia — Chandelier (1).mp3')
pygame.mixer.music.play()
moves = []


class Checker:
    def __init__(self, color, coords):
        self.color = color
        self.coords = coords
        self.can_kick = []
        self.great = False

    def check(self, coords2, serious=True):
        if not self.great:
            kick = False
            for i in board.board:
                for el in i:
                    if bool(el) and el.color == self.color and bool(el.can_kick):
                        kick = True
            if self.color == 'white' and board.preference == 'white' or not serious:
                if coords2[1] - self.coords[1] == -1:
                    if math.fabs(coords2[0] - self.coords[0]) == 1:
                        if not self.check_kick() and not kick:
                            if serious:
                                board.preference = 'black'
                            return True
            elif self.color == 'black' and board.preference == 'black' or not serious:
                if coords2[1] - self.coords[1] == 1:
                    if math.fabs(coords2[0] - self.coords[0]) == 1:
                        if not self.check_kick() and not kick:
                            if serious:
                                board.preference = 'white'
                            return True
            if self.check_kick() and self.color == board.preference or not serious:
                if math.fabs(coords2[1] - self.coords[1]) == math.fabs(coords2[0] - self.coords[0]):
                    if math.fabs(coords2[1] - self.coords[1]) == 2:
                        for w in self.can_kick:
                            if w[1] == coords2:
                                for el in all_sprites:
                                    if el.rect.x == 50 * w[0][0] and el.rect.y == 50 * w[0][1]:
                                        if serious:
                                            all_sprites.remove(el)
                                            board.board[w[0][1]][w[0][0]] = 0
                        if serious:
                            self.coords = coords2
                        if not self.check_kick() and serious:
                            if board.preference == 'black':
                                board.preference = 'white'
                            elif board.preference == 'white':
                                board.preference = 'black'
                        return True
        else:
            if self.check_kick_great():
                if self.color == board.preference:
                    target = False
                    block = False
                    if self.coords[0] > coords2[0]:
                        step1 = -1
                    else:
                        step1 = 1
                    if self.coords[1] > coords2[1]:
                        step2 = -1
                    else:
                        step2 = 1
                    for i in range(self.coords[0], coords2[0], step1):
                        for j in range(self.coords[1], coords2[1], step2):
                            if math.fabs(self.coords[0] - i) == math.fabs(self.coords[1] - j):
                                if bool(board.board[j][i]) and [i, j] != list(self.coords):
                                    if not target and self.color != board.board[j][i].color:
                                        trg = [j, i]
                                        target = True
                                    else:
                                        block = True
                    if target and not block:
                        if serious:
                            self.coords = coords2
                            for el in all_sprites:
                                if el.rect.x == 50 * trg[1] and el.rect.y == 50 * trg[0]:
                                    all_sprites.remove(el)
                            board.board[trg[0]][trg[1]] = 0
                            if not self.check_kick_great():
                                if board.preference == 'black':
                                    board.preference = 'white'
                                elif board.preference == 'white':
                                    board.preference = 'black'
                        return True
            else:
                if self.color == board.preference or not serious:
                    block = False
                    if self.coords[0] > coords2[0]:
                        step1 = -1
                    else:
                        step1 = 1
                    if self.coords[1] > coords2[1]:
                        step2 = -1
                    else:
                        step2 = 1
                    for i in range(self.coords[0], coords2[0], step1):
                        for j in range(self.coords[1], coords2[1], step2):
                            if math.fabs(self.coords[0] - i) == math.fabs(self.coords[1] - j):
                                if bool(board.board[j][i]) and [i, j] != list(self.coords):
                                    block = True
                    if not block:
                        crds = self.coords
                        if math.fabs(crds[0] - coords2[0]) == math.fabs(crds[1] - coords2[1]):
                            if serious:
                                self.coords = coords2
                                if board.preference == 'black':
                                    board.preference = 'white'
                                elif board.preference == 'white':
                                    board.preference = 'black'
                            return True
        return False

    # а вдруг он может кого- бить:
    def check_kick(self):
        if not self.great:
            self.can_kick = []
            x1, x2 = self.coords[0] + 1, self.coords[0] - 1
            y1, y2 = self.coords[1] + 1, self.coords[1] - 1
            for coords2 in [[x1, y1], [x1, y2], [x2, y1], [x2, y2]]:
                if coords2[0] > 0 and coords2[0] < 7 and coords2[1] > 0 and coords2[1] < 7:
                    kicked = board.board[coords2[1]][coords2[0]]
                    n = board.board[2 * coords2[1] - self.coords[1]][2 * coords2[0] - self.coords[0]]
                    nextone = n
                    if bool(kicked) and not bool(nextone) and kicked.color != self.color:
                        if [kicked.coords, ((2 * coords2[0] - self.coords[0]),
                                            (2 * coords2[1] - self.coords[1]))] not in self.can_kick:
                            self.can_kick.append([kicked.coords,
                                                  ((2 * coords2[0] - self.coords[0]),
                                                   (2 * coords2[1] - self.coords[1]))])
                        return True
            return False
        else:
            return self.check_kick_great()

    def check_kick_great(self):
        self.can_kick = []
        ans = False
        # всего 4 проверки
        xmin, ymin = self.coords[0], self.coords[1]
        xmax, ymax = self.coords[0], self.coords[1]
        # 1
        while True:
            xmin -= 1
            ymin -= 1
            if xmin < 0 or ymin < 0:  # ВАЖНЫЙ МОМЕНТ
                break
            check_er = board.board[ymin][xmin]
            if check_er != 0:
                if check_er.color == self.color:
                    break
                else:
                    if xmin >= 1 and ymin >= 1:
                        if board.board[ymin - 1][xmin - 1] == 0:
                            self.can_kick.append([[xmin, ymin], [xmin - 1, ymin - 1]])
                            ans = True
                        else:
                            break
        xmin, ymin = self.coords[0], self.coords[1]
        # 2
        while True:
            xmin -= 1
            ymax += 1
            if xmin < 0 or ymax > 7:  # ВАЖНЫЙ МОМЕНТ
                break
            check_er = board.board[ymax][xmin]
            if check_er != 0:
                if check_er.color == self.color:
                    break
                else:
                    if xmin >= 1 and ymax <= 6:
                        if board.board[ymax + 1][xmin - 1] == 0:
                            self.can_kick.append([[xmin, ymax], [xmin - 1, ymax + 1]])
                            ans = True
                        else:
                            break
        xmin, ymax = self.coords[0], self.coords[1]
        # 3
        while True:
            xmax += 1
            ymax += 1
            if xmax > 7 or ymax > 7:  # ВАЖНЫЙ МОМЕНТ
                break
            check_er = board.board[ymax][xmax]
            if check_er != 0:
                if check_er.color == self.color:
                    break
                else:
                    if xmax <= 6 and ymax <= 6:
                        if board.board[ymax + 1][xmax + 1] == 0:
                            self.can_kick.append([[xmax, ymax], [xmax + 1, ymax + 1]])
                            ans = True
                        else:
                            break
        xmax, ymax = self.coords[0], self.coords[1]
        # 4
        while True:
            xmax += 1
            ymin -= 1
            if xmax > 7 or ymin < 0:  # ВАЖНЫЙ МОМЕНТ
                break
            check_er = board.board[ymin][xmax]
            if check_er != 0:
                if check_er.color == self.color:
                    break
                else:
                    if xmax <= 6 and ymin >= 1:
                        if board.board[ymin - 1][xmax + 1] == 0:
                            self.can_kick.append([[xmax, ymin], [xmax + 1, ymin - 1]])
                            ans = True
                        else:
                            break
        return ans

    def change_great(self):
        self.great = True
        for el in all_sprites:
            if el.rect.x == 50*self.coords[0] and el.rect.y == 50*self.coords[1]:
                all_sprites.remove(el)
                # создадим спрайт
                sprite = pygame.sprite.Sprite()
                # определим его вид
                if self.color == 'white':
                    white_name2 = "C:/Users/Элвин/Desktop/white2.png"
                    sprite.image = pygame.transform.scale(load_image(white_name2, -1), (50, 50))
                else:
                    black_name2 = "C:/Users/Элвин/Desktop/black2.png"
                    sprite.image = pygame.transform.scale(load_image(black_name2, -1), (50, 50))
                # и размеры
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = 50 * self.coords[0]
                sprite.rect.y = 50 * self.coords[1]
                all_sprites.add(sprite)

    def change_back(self):
        self.great = False
        for el in all_sprites:
            if el.rect.x == 50*self.coords[0] and el.rect.y == 50*self.coords[1]:
                all_sprites.remove(el)
                # создадим спрайт
                sprite = pygame.sprite.Sprite()
                # определим его вид
                if self.color == 'white':
                    white_name2 = "C:/Users/Элвин/Desktop/white1.png"
                    sprite.image = pygame.transform.scale(load_image(white_name2, -1), (50, 50))
                else:
                    black_name2 = "C:/Users/Элвин/Desktop/black1.png"
                    sprite.image = pygame.transform.scale(load_image(black_name2, -1), (50, 50))
                # и размеры
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = 50 * self.coords[0]
                sprite.rect.y = 50 * self.coords[1]
                all_sprites.add(sprite)

    def cantmove(self):
        self.nes = board.preference
        self.coords1 = self.coords
        self.great1 = self.great
        for i in range(8):
            for el in range(8):
                board.preference = self.nes
                self.coords = self.coords1
                if self.check([i, el], False):
                    board.preference = self.nes
                    self.coords = self.coords1
                    if self.great and not self.great1:
                        self.change_back()
                    return False
        return True


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
    image.set_colorkey(colorkey)
    return image


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]

        # значения по умолчанию
        self.preference = 'white'  # первый ход
        self.left = 0
        self.top = 0
        self.cell_size = 50
        self.count = [12, 12]

        self.a_b = 0  # actual_button

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # рисуем
    def render1(self):
        for i in range(self.height):
            for j in range(self.width):
                if ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                    pygame.draw.rect(screen, pygame.Color('black'),
                                     (w * i // n, w * j // n, w // n, w // n), 0)
                if not ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                    if i in range(8) and j in range(3):
                        # создадим спрайт
                        sprite = pygame.sprite.Sprite()
                        # определим его вид
                        black_name = "C:/Users/Элвин/Desktop/black1.png"
                        sprite.image = pygame.transform.scale(load_image(black_name, -1), (50, 50))
                        # и размеры
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = 50 * i
                        sprite.rect.y = 50 * j
                        ch = Checker('black', [i, j])
                        self.board[j][i] = ch
                        # добавим спрайт в группу
                        if sprite not in all_sprites:
                            all_sprites.add(sprite)
                    elif i in range(8) and j in range(5, 8):
                        # создадим спрайт
                        sprite = pygame.sprite.Sprite()
                        # определим его вид
                        white_name = "C:/Users/Элвин/Desktop/white1.png"
                        sprite.image = pygame.transform.scale(load_image(white_name, -1), (50, 50))
                        # и размеры
                        sprite.rect = sprite.image.get_rect()
                        sprite.rect.x = 50 * i
                        sprite.rect.y = 50 * j
                        ch = Checker('white', [i, j])
                        self.board[j][i] = ch
                        # добавим спрайт в группу
                        if sprite not in all_sprites:
                            all_sprites.add(sprite)
        all_sprites.draw(screen)

    def render_next(self):
        for i in range(self.height):
            for j in range(self.width):
                if not ((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)):
                    pygame.draw.rect(screen, pygame.Color('white'),
                                     (w * i // n, w * j // n, w // n, w // n), 0)
        all_sprites.draw(screen)
        for i in range(8):
            for j in range(8):
                if (j, i) == self.a_b:
                    pygame.draw.rect(screen, pygame.Color('brown'),
                                     ((j * 50 + 1, i * 50 + 1), (48, 48)), 1)

    # диспетчер
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    # координаты
    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x in range(self.left, self.left + self.cell_size*self.width):
            if y in range(self.top, self.top + self.cell_size*self.height):
                return ((x - self.left)//self.cell_size, (y - self.top)//self.cell_size)
        return None

    # что-то делает
    def on_click(self, cell_coords):
        if bool(cell_coords):
            if bool(self.board[cell_coords[1]][cell_coords[0]]):
                if self.a_b != 0 and bool(self.board[self.a_b[1]][self.a_b[0]]):
                    all_sprites.draw(screen)  # чтобы замазюкать предыдущие актуальные спрайты
                self.a_b = cell_coords
            elif bool(self.a_b):
                if self.board[self.a_b[1]][self.a_b[0]].check(cell_coords):
                    moves.append([self.board[self.a_b[1]][self.a_b[0]].color,
                                  ['ABCDEFGH'[self.a_b[0]], str(8 - self.a_b[1])],
                                  ['ABCDEFGH'[cell_coords[0]], str(8 - cell_coords[1])]])
                    for i in all_sprites:
                        if (i.rect.x // 50, i.rect.y // 50) == self.a_b:
                            i.rect.x, i.rect.y = 50*cell_coords[0], 50 * cell_coords[1]
                    self.board[cell_coords[1]][cell_coords[0]] = self.board[self.a_b[1]][self.a_b[0]]
                    self.board[cell_coords[1]][cell_coords[0]].coords = cell_coords
                    self.board[self.a_b[1]][self.a_b[0]] = 0
                    self.a_b = 0
                    self.count = [0, 0]
                    for i in self.board:
                        for el in i:
                            if bool(el):
                                el.check_kick()
                                if el.coords[1] == 0 and el.color == 'white':
                                    el.change_great()
                                elif el.coords[1] == 7 and el.color == 'black':
                                    el.change_great()
                                if el.color == 'white':
                                    self.count[0] += 1
                                elif el.color == 'black':
                                    self.count[1] += 1


ind = -1


def draw(ind):
    global moves1
    global statusbar
    try:
        can_go = []
        for i in board.board:
            for el in i:
                if bool(el) and not el.cantmove():
                    if el.color not in can_go:
                        can_go.append(el.color)
        if len(can_go) == 1:
            if can_go[0] == 'white' and board.preference == 'black':
                statusbar = 'белые топ'
            elif board.preference == 'white' and can_go[0] == 'black':
                statusbar = 'черные топ'
            else:
                statusbar = 'новая игра'
    except Exception:
        pass

    font = pygame.font.SysFont("TimesNewRoman", 25)
    text = font.render(statusbar, 2, pygame.Color('red'))
    text_x = w + 75
    text_y = 20
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(screen, pygame.Color('white'), (text_x - 10, text_y - 10,
                                                     text_w + 20, text_h + 20), 0)
    text1 = font.render("счет: " + str(12 - board.count[1]) + ":" + str(12 - board.count[0]),
                        2, pygame.Color('white'))
    text_x1 = w + 85
    text_y1 = 70
    text2 = font.render("история ходов:", 2, pygame.Color('white'))
    text_x2 = w + 50
    text_y2 = 110
    pygame.draw.rect(screen, pygame.Color('beige'), [[440, 150], [180, 230]], 0)
    moves2 = []
    moves1 = []
    for el in range(len(moves)):
        moves2.append(moves[el])
        if (el + 1) % 11 == 0:
            moves1.append(moves2)
            moves2 = []
    if len(moves) > 11:
        moves1.append(moves[-11:])
    else:
        moves1.append(moves)
    if bool(moves1):
        for el in moves1[ind]:
            font = pygame.font.SysFont("TimesNewRoman", 20)
            textel = font.render((str(el[0]) + ': ' + ' '.join(el[1]) + '->' + ' '.join(el[2])),
                                 2, pygame.Color('black'))
            textel_y = 90 + (moves1[ind].index(el) + 3) * 20
            textel_x = w + 50
            screen.blit(textel, (textel_x, textel_y))

    screen.blit(text, (text_x, text_y))
    screen.blit(text1, (text_x1, text_y1))
    screen.blit(text2, (text_x2, text_y2))


def begin():
    font = pygame.font.SysFont("TimesNewRoman", 25)
    text = font.render("Новая игра?", 2, pygame.Color('red'))
    text_x = w // 2 + 60
    text_y = w // 2 - 50
    text_w = text.get_width()
    text_h = text.get_height()
    pygame.draw.rect(screen, pygame.Color('beige'), (text_x - 10, text_y - 10,
                                                     text_w + 20, text_h + 60), 0)
    pygame.draw.rect(screen, pygame.Color('grey'), (text_x - 10, text_y - 10,
                                                    text_w + 20, text_h + 60), 2)
    text1 = font.render("  Да      Нет ", 2, pygame.Color('red'))
    text_x1 = w // 2 + 60
    text_y1 = w // 2 - 15
    text_w1 = text.get_width()
    text_h1 = text.get_height()
    pygame.draw.rect(screen, pygame.Color('grey'), (text_x1, text_y1 - 5,
                                                    text_w // 2 - 10, text_h1 // 2 + 25), 2)
    pygame.draw.rect(screen, pygame.Color('grey'), (text_x1 + 70, text_y1 - 5,
                                                    text_w // 2 - 10, text_h1 // 2 + 25), 2)
    screen.blit(text, (text_x, text_y))
    screen.blit(text1, (text_x1, text_y1))
    pygame.display.flip()


no = False
yes = False
changed = False
board = Board(8, 8)
last = []
board.render1()
beg = False
text_w = 130
text_h1 = 29
text_w1 = 114
begin()
statusbar = 'новая игра'
while running:
    pygame.draw.rect(screen, pygame.Color('brown'), (w, 0, 300, w), 0)
    draw(ind)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if not beg:
            if event.type == pygame.MOUSEMOTION:
                if event.pos[0] in range(260, 250 + text_w // 2):
                    if event.pos[1] in range(180, 205 + text_h1 // 2):
                        pygame.draw.rect(screen, pygame.Color('red'), (260, 180,
                                         text_w // 2 - 10, text_h1 // 2 + 25), 2)
                        pygame.draw.rect(screen, pygame.Color('grey'), (330, 180,
                                         text_w // 2 - 10, text_h1 // 2 + 25), 2)
                if event.pos[0] in range(330, 320 + text_w // 2):
                    if event.pos[1] in range(180, 205 + text_h1//2):
                        pygame.draw.rect(screen, pygame.Color('red'), (330, 180,
                                         text_w // 2 - 10, text_h1 // 2 + 25), 2)
                        pygame.draw.rect(screen, pygame.Color('grey'), (260, 180,
                                         text_w // 2 - 10, text_h1 // 2 + 25), 2)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(260, 250 + text_w // 2):
                    if event.pos[1] in range(180, 205 + text_h1 // 2):
                        yes = True
                        no = False
                if event.pos[0] in range(330, 320 + text_w // 2):
                    if event.pos[1] in range(180, 205 + text_h1 // 2):
                        no = True
                        yes = False
                if yes and not no:
                    name = 'C:/Users/Элвин/Desktop/Sia — Chandelier (1).mp3'
                    sound1 = pygame.mixer.music.load(name)
                    pygame.mixer.music.play()
                    statusbar = 'новая игра'
                    beg = True
                    moves = []
                    ind = -1
                    board.render1()
                elif no and not yes:
                    running = False
        if beg:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] in range(w) and event.pos[1] in range(w):
                    board.get_click(event.pos)
                    board.render_next()
                else:
                    if event.pos[0] in range(465, 599):
                        if event.pos[1] in range(10, 39):
                            begin()
                            beg = False
                            # создадим группу, содержащую все спрайты
                            all_sprites = pygame.sprite.Group()
                            board.__init__(8, 8)
            if event.type == pygame.KEYDOWN:
                if event.key == 273:  # вверх
                    if len(moves) > 11:
                        if ind < 0 and math.fabs(ind - 1) in range(len(moves1) + 1):
                            ind -= 1
                if event.key == 274:
                    if len(moves) > 11:
                        if ind < -1 and math.fabs(ind + 1) in range(len(moves1) + 1):
                            ind += 1
    clock.tick(fps)
    pygame.display.flip()

# завершение работы:
pygame.quit()
