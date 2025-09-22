from pico2d import *

open_canvas()

char_attack = load_image('Attack_1.png')
char_attack2 = load_image('Attack_2.png')
char_attack3 = load_image('Attack_3.png')
char_run = load_image('Run.png')
char_dead = load_image('Dead.png')
char_jump = load_image('Jump.png')

while True:
    for x in range(0, 5):
        for frame in range(0, 6): # attack 1
            clear_canvas()
            char_attack.clip_draw(frame * 128, 0, 128, 128, 400, 380, 600, 600)
            update_canvas()
            delay(0.1)

        for frame in range(0, 4):
            clear_canvas()
            char_attack2.clip_draw(frame * 128, 0, 128, 128, 400, 380, 600, 600)
            update_canvas()
            delay(0.1)

        for frame in range(0, 3):
            clear_canvas()
            char_attack3.clip_draw(frame * 128, 0, 128, 128, 400, 380, 600, 600)
            update_canvas()
            delay(0.1)

    delay(1)

    for x in range(0, 5):
        for frame in range(0, 8):
            clear_canvas()
            char_run.clip_draw(frame * 128, 0, 128, 128, 400, 380, 600, 600)
            update_canvas()
            delay(0.1)

    delay(1)

    for x in range(0, 5):
        for frame in range(0, 6):  # attack 1
            clear_canvas()
            char_dead.clip_draw(frame * 128, 0, 128, 128, 400, 380, 600, 600)
            update_canvas()
            delay(0.15)

    delay(1)

    for x in range(0, 5):
        for frame in range(0, 15):  # attack 1
            clear_canvas()
            char_jump.clip_draw(frame * 128, 0, 128, 128, 400, 380, 600, 600)
            update_canvas()
            delay(0.1)



close_canvas()