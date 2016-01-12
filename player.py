import controls
from character import Character

class Player(Character):
    def __init__(self):
        self.x = 0
        self.y = 0

    def tick(self):
        if Controls.key_states['w'] or Controls.key_states['up']:
            self.y -= 1
        elif Controls.key_states['s'] or Controls.key_states['down']:
            self.y += 1
        elif Controls.key_states['a'] or Controls.key_states['left']:
            self.x -= 1
        elif Controls.key_states['d'] or Controls.key_states['right']:
            self.x += 1
