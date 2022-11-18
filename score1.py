from drawable import Drawable
class Score1(Drawable):
    def __init__(self, output_service):
        super().__init__(output_service)
        self._value = 0
        self._text = ""
        self.update_score(self.value)
        self.set_font_size(25)
    def display_score(self):
        print(f'Score: {self.value}')
    def update_score(self, points):
        self.value += points
        self._text = f"Score: {self.value}"


