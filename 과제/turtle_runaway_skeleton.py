# -*- coding: utf-8 -*-

# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import turtle, random, time

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=50, init_dist=400):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup() # 그림 안 그려지게 함
        self.runner.setx(-init_dist / 2)    # 띄워놓음

        self.chaser.shape('turtle')
        self.chaser.color('green')
        self.chaser.penup()
        self.chaser.setx(+init_dist / 2)
        self.chaser.setheading(180) # 앞을 바라보게

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)  # 숨겨둔 거북이 (그림 그릴 때만 사용)
        self.drawer.hideturtle()
        self.drawer.penup()

        # Instantiate the Score
        self.score = 0
        self.high_score = 0


    def is_catch(self):
        p = self.runner.pos()
        q = self.chaser.pos()   # 두 거북이의 위치를 받아서
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2   # 거리 살핌 (가까이 있는지 아닌지 -> catch 검사)

    def start(self, ai_timer_msec=100):
        self.ai_timer_msec = ai_timer_msec  # ai가 돌아가는 시간 담음
        self.start_time = time.time()   # 시작 시간을 담음
        self.canvas.ontimer(self.step, self.ai_timer_msec)  # 시간에 step 함수 주기적으로 수행하도록

    def step(self):
        self.runner.run_ai(self.chaser) # 인자를 상대방으로 줌 (그대로 보내면 위험하므로 self 붙여줌)
        self.chaser.run_ai(self.runner)

        is_catched = self.is_catch()    # catch 검사
        self.drawer.undo()
        self.drawer.penup()
        self.drawer.setpos(-300, 300)
        elapse = time.time() - self.start_time
        is_catched = self.is_catch
        if(is_catched):
            self.score += 10    # 잡힐 때마다 10점씩 추가

        if self.score > high_score:
            high_score = score  # 최고 점수보다 높으면 갱신

        self.drawer.write(f'Is catched? {is_catched} / Score: {score:.0f} / Elapse: {elapse:.0f}')

        self.canvas.ontimer(self.step, self.ai_timer_msec)  # 100ms마다 step 함수 호출

class ManualMover(turtle.RawTurtle):    # 첫 번째 거북이
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')   # 키보드로 돌아감
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opponent):
        # 화면 밖으로 빠져 나갔는지 검사
        if self.xcor() > 300 or self.xcor() < -300:
            self.right(180)
        if self.ycor() > 300 or self.ycor() < -300:
            self.right(180)

class LessRandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, oppoenent):    # ai로 돌아감
        opp_pos = oppoenent.pos()
        opp_heading = oppoenent.heading()
        mode = random.random()
        if mode < 0.6:
            self.forward(self.step_move)    # 60%의 확률로 전진
        elif mode < 0.3:    # 30%의 확률로 왼쪽
            self.left(self.step_turn)
        else:   # 10%의 확률로 오른쪽
            self.right(self.step_turn)

if __name__ == '__main__':
    canvas = turtle.Screen()
    runner = LessRandomMover(canvas)
    chaser = ManualMover(canvas)

    game = RunawayGame(canvas, runner, chaser)
    game.start()    # 게임 시작
    canvas.mainloop()
