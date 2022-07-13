import pygame as pg
import pytmx as pt
from settings import OFFSET
class Level:
    def __init__(self,filename):
        self.__gameMap = pt.load_pygame(filename,pixelalpha = True)
    def GetSize(self):
        return (self.__gameMap.tilewidth * self.__gameMap.width,self.__gameMap.tileheight * self.__gameMap.height)
    def Render(self , *layerNames):
        ti = self.__gameMap.get_tile_image_by_gid
        surf = pg.Surface((self.__gameMap.tilewidth * self.__gameMap.width,self.__gameMap.tileheight * self.__gameMap.height))
        for layer in  self.__gameMap.visible_layers:
            if layer.name in layerNames:
                if isinstance(layer, pt.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            surf.blit(tile, (x * self.__gameMap.tilewidth,y * self.__gameMap.tileheight))

        return surf
    def GetCords(self,*layerNames):
        cords = []
        ti = self.__gameMap.get_tile_image_by_gid
        for layer in self.__gameMap.visible_layers:
            if layer.name in layerNames:
                if isinstance(layer, pt.TiledTileLayer):
                    for x, y, gid, in layer:
                        tile = ti(gid)
                        if tile:
                            cords.append(pg.Rect(x * self.__gameMap.tilewidth,y * self.__gameMap.tileheight,self.__gameMap.tilewidth,self.__gameMap.tileheight))
        return  cords

