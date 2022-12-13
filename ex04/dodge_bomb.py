import pygame as pg
import sys


def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん")  # タイトルバーに「逃げろこうかとん」と表示する
    scrn_sfc = pg.display.set_mode((1000, 600)) #メインのsurfaceを設定
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg") #背景画像をロード
    pgbg_rct = pgbg_sfc.get_rect()
    scrn_sfc.blit(pgbg_sfc, pgbg_rct)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit