import pyray

class InputService:
    def __init__(self):
        self.k = {}

        self.k['w'] = pyray.KEY_W
        self.k['a'] = pyray.KEY_A
        self.k['s'] = pyray.KEY_S
        self.k['d'] = pyray.KEY_D

        self.k['i'] = pyray.KEY_I
        self.k['j'] = pyray.KEY_J
        self.k['k'] = pyray.KEY_K
        self.k['l'] = pyray.KEY_L
    
    
    def is_key_down(self, key):
        pyray_key = self.k[key.lower()]

        return pyray.is_key_down(pyray_key)