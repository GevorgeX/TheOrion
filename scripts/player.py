import pygame as pg
from  settings import GRAVITY,OFFSET,HEIGHT,WIDTH

arrImgIdle= [pg.image.load(f"../img/Wizard/idle/{i}.png") for i in range(20)]
arrImgWalk = [pg.image.load(f"../img/Wizard/walk/{i}.png") for i in range(20)]
arrImgJump = [pg.image.load(f"../img/Wizard/jump/{i}.png") for i in range(8)]
class Player:
    def __init__(self ,wid :pg.Surface, posX , posY,size,speed  ,Health  = 100):
        self.wid = wid
        self.__speed = speed
        self.__size = size
        self.__rect = pg.Rect(posX,posY,size[0],size[1])
        self.__left = False
        self.__animCount= 0
        self.__activeAnim = 0
        arrImgIdle = []
        self.__onGround = False
        self.__jumpForce= 15
        self.__isJumping = False
        self.__velocity = [0,0]
    def __Movement(self,colliders):
        colliders = [pg.Rect(OFFSET['x']+i.x,OFFSET['y']+i.y,i.width,i.height) for i in colliders]

        # if (self.__rect.x <WIDTH*0.3 and self.__velocity[0]<0 )or (self.__rect.x >WIDTH*0.7 and self.__velocity[0]>0):
        #     OFFSET['x'] -= self.__velocity[0]
        # else:
        #     self.__rect.x += self.__velocity[0]
        #self.__rect.x += self.__velocity[0]
        OFFSET['x']-= self.__velocity[0]
        self.__CollisionsX(colliders)
        OFFSET['y'] += self.__velocity[1]
        self.__CollisionsY(colliders)
        if not self.__onGround:
            self.__velocity[1]+= GRAVITY
        else:
            self.__isJumping = False
            self.__velocity[1] =0
    def __Input(self):
        pressedKeys = pg.key.get_pressed()
        if pressedKeys[pg.K_w] and self.__onGround:
            self.__velocity[1] =-self.__jumpForce
            self.__isJumping = True
            self.__ChangeAnim(arrImgJump)
        if pressedKeys[pg.K_a] :
             self.__velocity[0] = -self.__speed
             self.__left = True
             if not self.__isJumping: self.__ChangeAnim(arrImgWalk)
        elif pressedKeys[pg.K_d] :
             self.__velocity[0] = self.__speed
             self.__left = False
             if not self.__isJumping: self.__ChangeAnim(arrImgWalk)
        else:
            self.__velocity[0] = 0
            if not self.__isJumping: self.__ChangeAnim(arrImgIdle)
        if self.__isJumping:
            self.__Animation(False)
        else:
            self.__Animation()
    def __CollisionsX(self,colliders):
        for col in colliders:
            if self.__rect.colliderect(col):
                if self.__velocity[0] >0:
                    self.__rect.right = col.left
                elif self.__velocity[0] <0:
                    self.__rect.left = col.right
    def __CollisionsY(self,colliders):
        self.__onGround = False
        for col in colliders:
            if self.__rect.colliderect(col):
                if self.__velocity[1] >0:
                    self.__onGround = True
                    self.__rect.bottom = col.top
                elif self.__velocity[1] <0:
                    self.__rect.top = col.bottom
    def __Animation(self , repeat = True ):
        if   self.__animCount <= len(self.__activeAnim)-1:
             self.__animCount += .5
        elif repeat:
            self.__animCount = 0
        image = pg.transform.scale(pg.transform.flip(self.__activeAnim[int(self.__animCount)],self.__left,False),(self.__rect.w*4,self.__rect.h*2))
        self.wid.blit(image,pg.Rect(self.__rect.x-self.__size[0]*1.5,self.__rect.y-10-self.__size[1]/2,self.__rect.w,self.__rect.h))
    def __ChangeAnim(self,newAnim):
        if self.__activeAnim != newAnim :
            self.__animCount = 0
            self.__activeAnim = newAnim
    def Update(self,cols):
        self.__Input()
        self.__Movement(cols)



