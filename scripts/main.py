import pygame as pg
from settings import  *
from player import Player
from levelGeneration import Level

pg.init()

start = True
#display = pg.display.set_mode(size,pg.FULLSCREEN)
display = pg.display.set_mode((WIDTH,HEIGHT))


map = Level('../levels/test.tmx')
background = map.Render('background','grounds')
gameObject = {
    'background': [],
    'static': map.GetCords('grounds'),
    'dynamic': []
}
player = Player(display,WIDTH/2,HEIGHT/2,(50,100),10,0)

while start:
    display.blit(background, (OFFSET['x'],OFFSET['y']))
    pg.draw.rect(display,(0,145,151),player._Player__rect)
    player.Update(gameObject['static'])
    pressedKeys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or  pressedKeys[pg.K_ESCAPE]:
            pg.quit()
    pg.time.Clock().tick(FPS)
    pg.display.update()

