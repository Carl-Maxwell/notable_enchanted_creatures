import input_manager

x = 0
y = 0

def tick():
    global x, y

    if input_manager.key_states['w'] or input_manager.key_states['up']:
        y -= 1
    elif input_manager.key_states['s'] or input_manager.key_states['down']:
        y += 1
    elif input_manager.key_states['a'] or input_manager.key_states['left']:
        x -= 1
    elif input_manager.key_states['d'] or input_manager.key_states['right']:
        x += 1
