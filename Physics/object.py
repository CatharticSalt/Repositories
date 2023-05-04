class Object:
    def __init__(self, name, x, y):
        self._name = name
        self._x = x
        self._y = y
    
    def get_position(self):
        return (self._x, self._y)
    
    def __str__(self):
        return "{} with position ({}, {})".format(self._name, self._x, self._y)