class Calculator():
    def __init__(self):
        self.current_number = 1

    def press_up(self):
        self.current_number += 1

    def press_down(self):
        if self.current_number > 0:
            self.current_number -= 1

    def set_number(self, number):
        self.current_number = number

    def get_number(self):
        return self.current_number
