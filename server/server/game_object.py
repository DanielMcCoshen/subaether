from pickle import FALSE


class game_object:
    PLAYER = 0
    TORPEDO = 1
    MINE = 2
    ENVIRONMENT = 3

    def __init__(self, pos, aether, type):
        self._pos = pos
        self._aether = aether
        self._type = type
        self._destroyed = False
        pass

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value

    @property
    def type(self):
        return self._type

    @property
    def aether(self):
        return self._aether

    @aether.setter
    def aether(self, value):
        self._aether = value

    @property
    def destroyed(self):
        return self._destroyed

    def destroy(self):
        self._destroyed = True
