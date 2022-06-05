import pygame as pg
import pytmx as pt
from settings import OFFSET
class Level:
    def __init__(self,filename):
        self.gameMap = pt.load_pygame(filename,pixelalpha = True)
    def Render(self , *layerNames):
        ti = self.gameMap.get_tile_image_by_gid
        surf = pg.Surface((self.gameMap.tilewidth * self.gameMap.width,self.gameMap.tileheight * self.gameMap.height))
        for layer in  self.gameMap.visible_layers:
            if layer.name in layerNames:
                if isinstance(layer, pt.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surf.blit(tile, (x * self.gameMap.tilewidth,y * self.gameMap.tileheight))

        return surf
    def GetCords(self,*layerNames):
        cords = []
        ti = self.gameMap.get_tile_image_by_gid
        for layer in self.gameMap.visible_layers:
            if layer.name in layerNames:
                if isinstance(layer, pt.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            cords.append(pg.Rect(OFFSET['x']+x * self.gameMap.tilewidth,OFFSET['y']+y * self.gameMap.tileheight,self.gameMap.tilewidth,self.gameMap.tileheight))
        return  cords

