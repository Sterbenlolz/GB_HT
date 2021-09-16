class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, weight, thiccness):
        return 'Масса асфальта: {} тонн'.format(self._length * self._width * weight * thiccness / 1000)


print(Road(5000, 15).calc(25, 5))
