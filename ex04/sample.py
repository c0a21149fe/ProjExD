import pygame as pg
import sys
from time import sleep


def main():
    pg.display.set_caption("初めてのpygame") #タイトルバーに「初めてのpygame」と表示する
    scrn_sfc = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 90, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 400, 300
    scrn_sfc.blit(tori_sfc, tori_rct)
    # sleep(1)
    pg.display.update()
    # sleep(1)
    clock.tick(600)
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

