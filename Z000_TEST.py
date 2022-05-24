import random
import time
import pygame
from sys import exit
import tkinter

delays = [(0, 5), (5, 10), (10, 15), (15, 20), (20, 25), (25, 30), (30, 35)]
window = None

def funChooseA():
    global lab
    if a == delaytime:
        lab["text"] = '对'
    else:
        lab["text"] = '错'
    lab.pack()

def funChooseB():
    global lab
    if b == delaytime:
        lab["text"] = '对'
    else:
        lab["text"] = '错'
    lab.pack()


def tk():
    global lab
    window = tkinter.Tk()
    v = tkinter.IntVar()
    radioBtnA = tkinter.Radiobutton(window, text=str(delay[0]) + 'ms', variable=v, value=1, command=funChooseA)
    radioBtnA.pack()
    radioBtnB = tkinter.Radiobutton(window, text=str(delay[1]) + 'ms', variable=v, value=2, command=funChooseB)
    radioBtnB.pack()
    lab = tkinter.Label(window, text="")
    lab.pack()
    window.mainloop()


pygame.init()
screen = pygame.display.set_mode((1050, 660))
pygame.display.set_caption('能不能反应过来啊？（按esc选择结果）')
mouse_down_x = mouse_down_y = 0

delay = random.choice(delays)
a = random.choice(delay)
b = 0
for i in delay:
    b = i
    if a != b:
        break
delaytime = random.choice((a, b))
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            time.sleep(delaytime / 1000)
            mouse_down_x, mouse_down_y = event.pos
            screen.fill((0, 0, 0))
            pygame.draw.circle(screen, (255, 255, 255), (mouse_down_x, mouse_down_y), 10)
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:
            tk()
            delay = random.choice(delays)
            a = random.choice(delay)
            for i in delay:
                b = i
                if a != b:
                    break
            delaytime = random.choice((a, b))
        if event.type == pygame.QUIT:
            exit()
        pygame.display.update()