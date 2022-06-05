import pygame as pg
import settings 
from player import Player
from levelGeneration import Level
pg.init()
start = True
size = (settings.WIDTH,settings.HEIGHT)
#display = pg.display.set_mode(size,pg.FULLSCREEN)
display = pg.display.set_mode(size)
gameObject = {
    'background': [],
    'static': [],
    'dynamic': []
}
surf = Level('../levels/1.tmx')
surf.Render()
player = Player(display,0,0,(100,200),10,0)
while start:
    display.blit(surf.GetSurface(), (0, 0))
    pressedKeys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or  pressedKeys[pg.K_ESCAPE]:
            pg.quit()
    player.Update(gameObject['static'])

    pg.display.update()
    pg.time.Clock().tick(settings.FPS)
