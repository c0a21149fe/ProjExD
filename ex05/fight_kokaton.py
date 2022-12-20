import pygame as pg
import random
import sys
import time


SCREENRECT = pg.Rect(0, 0, 1600, 900)


class Screen: #スクリーン
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


class Bird: #こうかとんのクラス
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, fname, zoom, xy):
        self.sfc = pg.image.load(fname)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.eating = -1 #ticks

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):

        key_dct = pg.key.get_pressed()

        if key_dct[pg.K_SPACE]:  # スペースキーが押されたら
            self.eat_bomb()
        
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]*2 #食べてない時は速度が速い
                self.rct.centery += delta[1]*2
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]*2
                self.rct.centery -= delta[1]*2
        self.blit(scr)

        # self.eating -= 1 #tick毎に-1

    def eat_bomb(self): #スペースが押されたら爆弾を食べる
        global bombs
        for i, bomb in enumerate(bombs):
            #xとyから300以内に爆弾があれば
            if abs(self.rct.centerx - bomb.rct.centerx) < 300 \
                and abs(self.rct.centery - bomb.rct.centery) < 300: 
                
                del bombs[i] #該当ボムを一つ削除する
                self.eating = 1000 #tick
                # for val in Bird.key_delta.values(): #こうかとんの動きを速くする
                #     val[0] *= 2
                #     val[1] *= 2
                break

class eatingBird: #こうかとんのクラス
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, fname, zoom, xy):
        self.sfc = pg.image.load(fname)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):

        key_dct = pg.key.get_pressed()
        
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)

class Texts:
    def __init__(self):
        self.font = pg.font.SysFont('msgothic', 50)

    def update(self, scr:Screen, now, bgn):
        self.txt = self.font.render(
            f"経過時間:{now-bgn:.2f}", True, (65, 105, 225)
        )  # 経過時間のテキスト
        scr.sfc.blit(self.txt, (100, scr.rct.height-100))

class Uma:
    def __init__(self):
        self.font = pg.font.SysFont('msgothic', 30)

    def update(self, scr:Screen, kokaton):
        self.txt = self.font.render(
            "うまうまっ！", True, (199, 21, 133)
        )
        scr.sfc.blit(self.txt, (kokaton.rct.centerx+50, kokaton.rct.centery-50))



class Bomb: #爆弾のクラス
    def __init__(self, color, rad, vxy, scr: Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))  # 正方形の空のSurface
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    global fullscreen, bombs
    clock = pg.time.Clock()
    bgn = time.time()
    # 練習１

    scr = Screen("逃げろ！こうかとん", SCREENRECT.size, "fig/pg_bg.jpg")
    fullscreen = False #フルスクリーン無効

    # 練習３
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    kkt.blit(scr)

    # kkt = Bird("fig/6.png", 2.0, (900, 400))
    # kkt.update(scr)

    # 練習５
    bombs = [] #爆弾オブジェクトを格納するリスト
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    bombs.append(bkd)
    bkd.update(scr)

    bomb_timer = 1 #爆弾発生の時間計測用

    texts = Texts()

    # 練習２
    while True:
        now = time.time()
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    scr.full_window()

        #updates
        if kkt.eating == 0:
            kkt.rct.center = eating_kkt.rct.center
        elif kkt.eating < 0:
            kkt.update(scr)
        elif kkt.eating == 999: #kktがeatし始めたとき
            eating_kkt = eatingBird("fig/8.png", 2.0, kkt.rct.center)
            eating_kkt.update(scr)
            uma = Uma()
        else: #kktがeatingのときは
            eating_kkt.update(scr)
            uma.update(scr, eating_kkt)
            
        kkt.eating -= 1  # eating時間を1減らす
        print(kkt.eating)
        #bomb
        for i in range(len(bombs)):
            bombs[i].update(scr)
            if kkt.eating < 0: #kktがeatingでないとき
                if kkt.rct.colliderect(bombs[i].rct): #衝突するかを検査する
                    return
        #texts
        texts.update(scr, now, bgn)
        

        #一定時間ごとに爆弾を増やす
        if bomb_timer % 2000 == 0:
            bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
            bombs.append(bkd)
            bkd.update(scr)

        bomb_timer += 1
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
