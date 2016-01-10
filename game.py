from tdl import Console, TDLError, Window, absolute_import, division, event, flush, forceResolution, force_resolution, getFPS, getFullscreen, get_fps, get_fullscreen, init, int_types, map, noise, print_function, screenshot, setFPS, setFont, setFullscreen, setTitle, set_font, set_fps, set_fullscreen, set_title, style, unicode_literals

SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

def handle_events(events):
    for event in events:
        if event.type == 'KEYDOWN':
            handle_key(event)

def handle_key(event):
    return
    global playerx, playery

    key = console_check_for_keypress(events)  #real-time
    #key = console_wait_for_keypress(True)  #turn-based

    if key.vk == KEY_ENTER and key.lalt:
        set_fullscreen(not get_fullscreen())

    elif key.vk == KEY_ESCAPE:
        return True

    #movement keys
    if console_is_key_pressed(KEY_UP):
        playery -= 1

    elif console_is_key_pressed(KEY_DOWN):
        playery += 1

    elif console_is_key_pressed(KEY_LEFT):
        playerx -= 1

    elif console_is_key_pressed(KEY_RIGHT):
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
