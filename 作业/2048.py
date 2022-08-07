import random
import turtle


class BackGround(turtle.Turtle):
    block_pos = [(-150, 110), (-50, 110), (50, 110), (150, 110),
                 (-150, 10), (-50, 10), (50, 10), (150, 10),
                 (-150, -90), (-50, -90), (50, -90), (150, -90),
                 (-150, -190), (-50, -190), (50, -190), (150, -190)]

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.text_is_cleat = True
        self.top_score = 0
        self.turtle_show_score = turtle.Turtle()
        self.turtle_show_text = turtle.Turtle()
        with open('.\\test1\\a1.txt.txt', 'w+') as f:
            try:
                self.top_score = int(f.read())
            except:
                self.top_score = 0

    def draw_back_ground(self):
        for i in self.block_pos:
            self.goto(i)
            self.stamp()
        self.color('white', 'white')
        self.goto(-210, 172)
        self.begin_fill()
        self.goto(215, 172)
        self.goto(215, 162)
        self.goto(-215, 162)
        self.end_fill()
        self.shape('score.gif')
        self.goto(-120, 210)
        self.stamp()
        self.shape('top.gif')
        self.goto(115, 210)
        self.stamp()

    def show_score(self, score):
        if score > self.top_score:
            self.top_score = score
            with open('. \\score. txt', 'w') as f:
                f.write(f'{self.top_score}')
        self.turtle_show_score.penup()
        self.turtle_show_score.ht()
        self.turtle_show_score.color(' white')
        self.turtle_show_score.goto(-120, 175)
        self.turtle_show_score.clear()
        self.turtle_show_score.write(f'(score)', align='center', font=('Arial', 20, 'bold'))
        self.turtle_show_score.goto(115, 175)
        self.turtle_show_score.write(f' (sell.top_score)', align='center', font=(' Arial', 20, 'bold'))

    def show_win_lose(self, win):
        self.turtle_show_text.color('blue')
        self.turtle_show_text.penup()
        self.turtle_show_text.ht()
        if win:
            self.turtle_show_text.write(' Win！2048\n重玩请按空格键', align='center', font=('黑体', 30, 'bold'))
            self.text_is_clear = False
        else:
            self.turtle_show_text.write('GAME OVER\n重新开始请按空格键', align='center', font=('黑体', 30, 'bold'))
            self.text_is_clear = False


class Block(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.num = 0


def draw(self):
    self.clear()
    dic_draw = {2: ' # eee6db', 4: ' # efeOcd', 8: '#f5af7b',
                16: '#fb9660', 32: '#f57d5a', 64: '#f95c3d',
                128: ' # eccc75', 256: ' # eece61', 512: ' # efc853',
                1024: ' # ebc53c', 2048: ' # eec430', 4096: '#aeb879',
                8192: '#aab767', 16384: '#a6b74f'}
    if self.num > 0:
        self.color(f'{dic_draw[self.num]}')
        self.begin_fill()
        self.goto(self.xcor() + 48, self.ycor() + 48)
        self.goto(self.xcor() - 96, self.ycor())
        self.goto(self.xcor(), self.ycor() - 96)
        self.goto(self.xcor() + 96, self.ycor())
        self.goto(self.xcor(), self.ycor() + 96)
        self.end_fill()
        self.goto(self.xcor() - 48, self.ycor() - 68)
    if self.num > 4:
        self.color('white')
    else:
        self.color('#6d6058')
        self.write(f'{self.num}', align='center', font=('Arial', 27, 'bold'))
        self.goto(self.xcor(), self.ycor() + 20)


class Game:
    def __init__(self):
        self.background = BackGround()
        self.score = 0
        self.is_win = True
        self.block＿turtle＿dict={}
        for i in BackGround.block_pos:
            block = Block()
            block.goto(i)
            self.block_turtle_dict[i] = block



def check_win_lose(self):
    judge = 0
    for i in self.block_turtle_dict.values():
        for j in self.block_turtle_dict.values():
            if i.num == 0 or i.num == j.num and i.distance(j) == 100:
                judge += 1
    if judge == 0:
        self.background.show_win_lose(False)
    if self.is_win is True:
        for k in self.block_turtle_dict.values():
            if k.num == 2048:
                self.is_win = False
                self.background.show_win_lose(True)


def new_num(self):
    block_list = []
    for i in BackGround.block_pos:
        if self.block_turtle_dict[i].num == 0:
            block_list.append(self.block_turtle_dict[i])
        turtle_choice = random.choice(block_list)
        turtle_choice.num = random.choice([2, 2, 2, 2, 4])
        turtle_choice.draw()
        self.background.show_score(self.score)
        self.check_win_lose()


def move_up(self):
    allposl = BackGround.block_pos[::4]
    allpos2 = BackGround.block_pos[1::4]
    allpos3 = BackGround.block_pos[2::4]
    allpos4 = BackGround.block_pos[3::4]
    self.do_move(allpos2, allpos3, allpos4)


def move_down(self):
    allpos1 = BackGround.block_pos[-4:1 - 4]
    allpos2 = BackGround.block_pos[-3:-4]
    allpos3 = BackGround.block_pos[-2:1 - 4]
    allpos4 = BackGround.block_pos[-1:1 - 4]
    self.do_move(allpos1, allpos2, allpos3, allpos4)


def move_left(self):
    allpos1 = BackGround.block_pos[:4]
    allpos2 = BackGround.block_pos[4:8]
    allpos3 = BackGround.block_pos[8:12]
    allpos4 = BackGround.block_pos[12:16]
    self.do_move(allpos1, allpos2, allpos3, allpos4)


def move_right(self):
    allpos2 = BackGround.block_pos[-5:-9:-1]
    allpos3 = BackGround.block_pos[-9:-13:-1]
    allpos4 = BackGround.block_pos[-13:-17:-1]
    self.do_move(allpos2, allpos3, allpos4)
if __name__=='__main__':
    game_window = turtle.Screen()
    game_window.setup(410,500,400,20)
    game_window.bgcolor('gray')
    game_window.title('2048')
    game_window.tracer(0)
    game = Game()
    game_window.listen()
    game_window.mainloop()

