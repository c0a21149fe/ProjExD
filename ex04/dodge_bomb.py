import pygame as pg
import sys
import random
import time

#軌跡, ボールの数, 反射, 時間計測

#画面外に出たかどうかを判定する関数
def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left <= scr_rct.left or obj_rct.right >= scr_rct.right:
        yoko = -1
    if obj_rct.top <= scr_rct.top or obj_rct.bottom >= scr_rct.bottom:
        tate = -1
    return tate, yoko


def main():
    bgn = time.time()
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろこうかとん")  # タイトルバーに「逃げろこうかとん」と表示する
    scrn_sfc = pg.display.set_mode((1600, 900)) #メインのsurfaceを設定
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg") #背景画像をロード
    pgbg_rct = pgbg_sfc.get_rect() #背景rect
    scrn_sfc.blit(pgbg_sfc, pgbg_rct) #背景をblit

    #こうかとん画像の表示
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct)

    #爆弾(無印)の表示
    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct)
    vx, vy = +1, +1 #爆弾の速度を設定

    #爆弾2の表示
    bomb_sfc_2 = pg.Surface((20, 20))
    bomb_sfc_2.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc_2, (255, 0, 0), (10, 10), 10)
    bomb_rct_2 = bomb_sfc_2.get_rect()
    bomb_rct_2.centerx = random.randint(0, scrn_rct.width)
    bomb_rct_2.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc_2, bomb_rct_2)
    vx_2, vy_2 = +1, +1  # 爆弾の速度を設定

    #時間用のフォント設定
    jikan_font = pg.font.SysFont('msgothic', 50)

    #反射機能の定数, 変数
    COOLTIME = 0 #クールダウン時間初期値(クールダウンタイムは5000)
    HANSHA = 1500 #反射時間
    flag = False #反射中かを表すフラグ(Trueが反射中)
    hansha_sfc = pg.image.load("fig/4.png") #座るこうかとんの画像
    hansha_sfc = pg.transform.rotozoom(hansha_sfc, 0, 2.0)
    hansha_rct = hansha_sfc.get_rect()
    hansha_rct.center = tori_rct.center
    hansha_font = pg.font.SysFont('msgothic', 50) #反射機能の状態表示用フォント

    

    while True:
        now = time.time()
        scrn_sfc.blit(pgbg_sfc, pgbg_rct)  # 背景をblit
        jikan_txt = jikan_font.render(f"経過時間:{now-bgn:.2f}", True, (65, 105, 225)) #経過時間のテキスト
        #反射時間のテキスト
        if flag == True:
            hansha_txt = hansha_font.render(f"残り反射時間:{HANSHA}ticks", True, (255, 20, 147))
        elif flag == False and COOLTIME < 0:
            hansha_txt = hansha_font.render(f"反射が利用可能です！！", True, (255, 0, 0))
        elif flag == False and COOLTIME >= 0:
            hansha_txt = hansha_font.render(f"クールタイム：{COOLTIME}ticks", True, (25, 25, 112))
        
        #テキストの表示
        scrn_sfc.blit(jikan_txt, (100, scrn_rct.height-100))
        scrn_sfc.blit(hansha_txt, (scrn_rct.width-600, scrn_rct.height-100))
        
        #×を押したら、ループから抜ける
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        if flag == False:
            #こうかとんを移動させる        
            key_dct = pg.key.get_pressed()
            if key_dct[pg.K_UP]:
                tori_rct.move_ip(0, -1)
            if key_dct[pg.K_DOWN]:
                tori_rct.move_ip(0, 1)
            if key_dct[pg.K_LEFT]:
                tori_rct.move_ip(-1, 0)
            if key_dct[pg.K_RIGHT]:
                tori_rct.move_ip(1, 0)

            #どこかしらはみ出ていたら
            if check_bound(tori_rct, scrn_rct) != (+1, +1):
                if key_dct[pg.K_UP]:
                    tori_rct.move_ip(0, 1)
                if key_dct[pg.K_DOWN]:
                    tori_rct.move_ip(0, -1)
                if key_dct[pg.K_LEFT]:
                    tori_rct.move_ip(1, 0)
                if key_dct[pg.K_RIGHT]:
                    tori_rct.move_ip(-1, 0)
            
            scrn_sfc.blit(tori_sfc, tori_rct)
        else:
            scrn_sfc.blit(hansha_sfc, hansha_rct)

        #爆弾(無印)の移動
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= tate
        vy *= yoko

        #爆弾2の移動
        bomb_rct_2.move_ip(vx_2, vy_2)
        scrn_sfc.blit(bomb_sfc_2, bomb_rct_2)
        yoko_2, tate_2 = check_bound(bomb_rct_2, scrn_rct)
        vx_2 *= tate_2
        vy_2 *= yoko_2
        
        #こうかとんと爆弾の衝突
        if flag == False:
            if tori_rct.colliderect(bomb_rct): #爆弾(無印)
                return
            if tori_rct.colliderect(bomb_rct_2): #爆弾2
                return
        else:
            if hansha_rct.colliderect(bomb_rct):
                vx *= -1
                vy *= -1
            if tori_rct.colliderect(bomb_rct_2):
                vx_2 *= -1
                vy_2 *= -1

        #反射機能
        if key_dct[pg.K_SPACE]: #スペースキーが押されたら
            if flag == False and COOLTIME < 0: #反射中でなく、クールタイムが終わっていたら
                flag = True #反射中にする
                hansha_rct.center = tori_rct.center
                HANSHA = 1500 #反射時間
            elif HANSHA < 0: #反射時間が終わったら
                flag = False #反射終了
                COOLTIME = 5000 #クールダウンタイム
                
        HANSHA -= 1 #残り反射時間を減らす
        COOLTIME -= 1 #残りクールタイムを減らす

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit