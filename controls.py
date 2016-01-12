
key_states = {}

def handle_events(events):
    exit = False

    for event in events:
        if event.type == 'KEYDOWN':
            exit = exit or handle_key(event, True)
        elif event.type == 'KEYUP':
            handle_key(event, False)

    if exit:
        return True

def handle_key(event, is_down):
    key_states[event.keychar.lower()] = is_down

# add all the keys to the keystates dictionary

keynames = [
    'NONE',
    'ESCAPE',
    'BACKSPACE',
    'TAB',
    'ENTER',
    'SHIFT',
    'CONTROL',
    'ALT',
    'PAUSE',
    'CAPSLOCK',
    'PAGEUP',
    'PAGEDOWN',
    'END',
    'HOME',
    'UP',
    'LEFT',
    'RIGHT',
    'DOWN',
    'PRINTSCREEN',
    'INSERT',
    'DELETE',
    'LWIN',
    'RWIN',
    'APPS',
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'KP0',
    'KP1',
    'KP2',
    'KP3',
    'KP4',
    'KP5',
    'KP6',
    'KP7',
    'KP8',
    'KP9',
    'KPADD',
    'KPSUB',
    'KPDIV',
    'KPMUL',
    'KPDEC',
    'KPENTER',
    'F1',
    'F2',
    'F3',
    'F4',
    'F5',
    'F6',
    'F7',
    'F8',
    'F9',
    'F10',
    'F11',
    'F12',
    'NUMLOCK',
    'SCROLLLOCK',
    'SPACE',
]

for key in keynames:
    key_states[key.lower()] = False

for i in xrange(ord('a'), ord('z')+1):
    key_states[chr(i)] = False
