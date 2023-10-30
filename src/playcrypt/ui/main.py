import pygame as pg
from playcrypt.ui.text import Text
from playcrypt.ui.button import Button

def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()

    text_box_1 = Text((100, 100))
    text_box_2 = Text((100, 200))
    text_box_3 = Text((100, 300))
    text_box_4 = Text((200, 100))
    text_box_5 = Text((200, 200))
    text_box_6 = Text((200, 300))
    submit = Button((400, 150))
    text_box_list = [text_box_1, text_box_2, text_box_3, text_box_4, text_box_5, text_box_6]
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user click on the input_box rect.
                text = ''
                for tb in text_box_list:
                    tb.click(event.pos)
                submit.click(event.pos)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

                for tb in text_box_list:
                    tb.set_text(text)

        screen.fill((30, 30, 30))
        for tb in text_box_list:
            screen.blit(tb.get_text_surface(), (tb.get_input_box().x+5, tb.get_input_box().y+5))
            pg.draw.rect(screen, tb.get_color(), tb.get_input_box(), 2)
        screen.blit(submit.get_text_surface(), (submit.get_input_box().x+5, submit.get_input_box().y+5))
        pg.draw.rect(screen, submit.get_color(), submit.get_input_box(), 2)
        if submit.is_clicked():
            for tb in text_box_list:
                print(tb.get_text())
            submit.set_click(False)
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()