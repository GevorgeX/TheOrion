import pygame as pg
from settings import  *
from player import Player
from levelGeneration import Level

pg.init()

start = True
#display = pg.display.set_mode(size,pg.FULLSCREEN)
display = pg.display.set_mode((WIDTH,HEIGHT))


map = Level('../levels/test.tmx')
surf = map.Render('background','grounds')
player = Player(display,WIDTH/2,HEIGHT/2,(100,200),10,0)

gameObject = {
    'background': [],
    'static': map.GetCords('grounds'),
    'dynamic': []
}

while start:
    display.blit(surf, (OFFSET['x'],OFFSET['y']))
    pressedKeys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or  pressedKeys[pg.K_ESCAPE]:
            pg.quit()
    player.Update(gameObject['static'])
    pg.time.Clock().tick(FPS)
    pg.display.update()

