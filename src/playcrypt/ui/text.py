import pygame as pg


class Text:
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')

    def __init__(self, pos):
        self.color = Text.color_inactive
        self.input_box = pg.Rect(pos[0], pos[1], 100, 32)
        self.active = False
        self.font = pg.font.Font(None, 32)
        self.text = ""
        self.text_surface = self.font.render(self.text, True, self.color)

    def click(self, pos):
        if self.input_box.collidepoint(pos):
            self.active = True
            self.color = Text.color_active

        else:
            self.active = False
            self.color = Text.color_inactive

    def set_text(self, text):
        if self.active:
            self.text = text
            self.text_surface = self.font.render(text, True, self.color)
            # Resize the box if the text is too long.
            self.input_box.w = 100

    def get_text_surface(self):
        return self.text_surface

    def get_input_box(self):
        return self.input_box

    def get_color(self):
        return self.color

    def get_text(self):
        return self.text