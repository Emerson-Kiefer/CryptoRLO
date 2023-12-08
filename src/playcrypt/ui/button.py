import pygame as pg


class Button:
    color = pg.Color('blanchedalmond')

    def __init__(self, pos):
        self.input_box = pg.Rect(pos[0], pos[1], 100, 32)
        self.active = False
        self.font = pg.font.Font(None, 32)
        self.text_surface = self.font.render("Attack", False, self.color)
        self.is_pushed = False

    def click(self, pos):
        if self.input_box.collidepoint(pos):
            print('submit')
            self.is_pushed = True
        else:
            self.is_pushed = False

    def get_text_surface(self):
        return self.text_surface

    def get_input_box(self):
        return self.input_box

    def get_color(self):
        return self.color

    def set_click(self, clicked=True):
        self.is_pushed = clicked

    def is_clicked(self):
        return self.is_pushed

