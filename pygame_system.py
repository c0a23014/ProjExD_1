import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))
    img = pg.image.load("fig/pg_bg.jpg")
    img_2 = pg.transform.flip(img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center =  300, 200
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            kk_rct.move_ip([0, -1])
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip([0, +1])            
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip([-1, 0])            
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip([+2, 0])
        else:
            kk_rct.move_ip([-1, 0])

        x = tmr%3200
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(img, [-x, 0])
        screen.blit(img, [-x+3200, 0])
        screen.blit(img_2, [-x+1600, 0])
        screen.blit(img_2, [-x+4800, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()