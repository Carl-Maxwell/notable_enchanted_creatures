from importworkaround import *

import input_manager
import player

SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 50

LIMIT_FPS = 20

#
# Initialization & Main Loop
#

set_font('arial10x10.png', greyscale=True, altLayout=True)
console = init(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/tutorial')
set_fps(LIMIT_FPS)

player.x = SCREEN_WIDTH/2
player.y = SCREEN_HEIGHT/2

while not event.is_window_closed():

    console.draw_char(player.x, player.y, '@')

    flush()

    console.draw_char(player.x, player.y, ' ')

    input_manager.handle_events(event.get())

    player.tick()

    if input_manager.key_states['escape']:
        break
