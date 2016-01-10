from importworkaround import *

SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

def handle_events(events):
    exit = False

    for event in events:
        if event.type == 'KEYDOWN':
            exit = exit or handle_key(event)

    if exit:
        return True

def handle_key(event):
    global playerx, playery

    key = event.keychar

    if key == 'F11':
        set_fullscreen(not get_fullscreen())
    elif key == 'ESCAPE':
        return True

    # character movement

    elif key == 'UP' or key.lower() == 'w':
        playery -= 1
    elif key == 'DOWN' or key.lower() == 's':
        playery += 1
    elif key == 'LEFT' or key.lower() == 'a':
        playerx -= 1
    elif key == 'RIGHT' or key.lower() == 'd':
        playerx += 1


#############################################
# Initialization & Main Loop
#############################################

set_font('arial10x10.png', greyscale=True, altLayout=True)
console = init(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/tutorial')
set_fps(LIMIT_FPS)

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2

while not event.is_window_closed():

    console.draw_char(playerx, playery, '@')

    flush()

    console.draw_char(playerx, playery, ' ')

    exit = handle_events(event.get())

    if exit:
        break
