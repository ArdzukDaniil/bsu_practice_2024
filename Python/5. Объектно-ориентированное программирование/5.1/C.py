class RedButton:
    def __init__(self):
        self.cou = 0

    def click(self):
        print('Тревога!')
        self.cou += 1

    def count(self):
        return self.cou
