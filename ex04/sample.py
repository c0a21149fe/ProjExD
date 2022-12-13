import pygame as pg
import sys


def main():
    pg.display.set_caption("初めてのpygame") #タイトルバーに「初めてのpygame」と表示する
    scrn_sfc = pg.display.set_mode((800, 600))
    
    pg.image.load("fig/6.png")
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

