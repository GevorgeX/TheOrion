import pygame as pg
import pytmx as pt
class Level:
    def __init__(self,filename):
        self.gameMap = pt.load_pygame(filename,pixelalpha = True )
        self.surface:pg.surface = pg.Surface((self.gameMap.tilewidth * self.gameMap.width,self.gameMap.tileheight * self.gameMap.height))

    def Render(self , *layerNames):
        ti = self.gameMap.get_tile_image_by_gid
        for layerName in layerNames:
            for layer in self.gameMap.get_layer_by_name(layerName):
                if isinstance(layer, pt.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            self.surface.blit(tile, (x * self.gameMap.tilewidth,y * self.gameMap.tileheight))
    def GetCords(self,*layerNames):
        cords = []
        ti = self.gameMap.get_tile_image_by_gid
        for layerName in layerNames:
            for layer in self.gameMap.get_layer_by_name(layerName):
                if isinstance(layer, pt.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            cords.append(pg.Rect(x * self.gameMap.tilewidth,y * self.gameMap.tileheight,self.gameMap.tilewidth,self.gameMap.tileheight))
        return  cords
    def GetSurface(self):
        return self.surface
