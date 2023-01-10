import pygame as pg
import random
import time
import sys

SCREENRECT = pg.Rect(0, 0, 1364, 834)


class Screen:  # スクリーン
    def __init__(self, title, size, bgf):
        self.title = title
        self.size = size
        pg.display.set_caption(title)

        #FULLCREEN 変数
        self.winstyle = 0  # |FULLSCREEN
        self.bestdepth = pg.display.mode_ok(SCREENRECT.size, self.winstyle, 32)

        self.sfc = pg.display.set_mode(
            SCREENRECT.size, self.winstyle, self.bestdepth)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgf)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    def full_window(self):
        global fullscreen
        if not fullscreen:
            print("Changing to FULLSCREEN")
            screen_backup = self.sfc.copy()
            self.sfc = pg.display.set_mode(
                SCREENRECT.size, self.winstyle | pg.FULLSCREEN, self.bestdepth
            )
            self.sfc.blit(screen_backup, (0, 0))
        else:
            print("Changing to windowed mode")
            screen_backup = self.sfc.copy()
            self.sfc = pg.display.set_mode(
                SCREENRECT.size, self.winstyle, self.bestdepth
            )
            self.sfc.blit(screen_backup, (0, 0))
        pg.display.flip()
        fullscreen = not fullscreen


class Player:
    def __init__(self, color , rad, key_delta, scr : Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))  # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 100
        self.rct.centery = 100
        self.key_delta = key_delta

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):

        key_dct = pg.key.get_pressed()

        for key, delta in self.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            # if check_bound(self.rct, scr.rct) != (+1, +1):
            #     self.rct.centerx -= delta[0]
            #     self.rct.centery -= delta[1]
        self.blit(scr)
    

def main():
    global fullscreen

    scr = Screen("2Dテニス", SCREENRECT.size, "fig/tennis_court.png")
    fullscreen = False  # フルスクリーン無効

    key_delta_p1 = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }
    p1 = Player((255, 0, 0), 10, key_delta_p1, scr)
    p1.blit(scr)

    while True:
        scr.blit()
        p1.update(scr)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    scr.full_window()


        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()





