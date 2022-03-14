from distutils.log import error
from re import L
from tkinter import RIGHT
from venv import main
import pygame
from random import randint
import math
import time
import os
import numpy

class text:
    def show(self,text:str,text_size:int,color:tuple=(255,255,255))-> None:
        self.print_text = pygame.font.SysFont(None,text_size).render(text,True,color)

    def get_size(self):
        return self.print_text.get_size()

    def blit(self,ps):
        screen.blit(self.print_text,ps)

class object:
    def __init__(self,ps:tuple,car=False,sum=False):
        self.error = False
        self.img_nombor = 0
        self.image=0
        self.x_ps = ps[0]
        self.y_ps = ps[1]
        self.car = car
        self.sum = sum
    def set_ps(self,x,y):
        self.x_ps = x
        self.y_ps = y

    def move_set(self,x,y):
        self.x_ps += x
        self.y_ps += y

    def point_print(self):
        if self.car:
            pygame.draw.circle(screen,(255,0,0),[self.x_ps,self.y_ps],5)
        elif self.sum:
            pygame.draw.circle(screen,(0,0,255),[self.x_ps,self.y_ps],5)
        else:
            pygame.draw.circle(screen,(255,255,255),[self.x_ps,self.y_ps],5)
class size:
        def __init__(self,x,y):
            self.current_w=x
            self.current_h=y

def sum_list_func(i):
    global sum_list,sum_count
    for o in sum_list:
        if not sum_list[i-sum_count]==o:
            if round(((sum_list[i-sum_count].x_ps-o.x_ps)**2+(sum_list[i-sum_count].y_ps-o.y_ps)**2)**0.5,5)<100.0:
                sum_list.remove(o)
                sum_list.remove(sum_list[i-sum_count])
                sum_count+=1
                return True
            return False
def shrm(key:list,m:dict):
    sum_list = list()
    key = sort(key)
    for i in key:
        sum_list.append({})
pygame.init()
intro_text = text()
# size = pygame.display.Info()
size = size(1920,1080)
screen = pygame.display.set_mode((size.current_w, size.current_h))
title = '자율주행 시뮬레이션'
pygame.display.set_caption(title)
clock = pygame.time.Clock()
st_time = pygame.time.get_ticks()
walkcount = 0
fps = 240
particle_list=list()
UP_go = False
DOWN_go = False
LEFT_go = False
RIGHT_go = False
sum_count=0
car=object((23,500),True)
point1=object((400,270))
point2=object((380,770))
point3=object((730,230))
point4=object((680,810))
point5=object((1010,830))
point6=object((1250,770))
point7=object((1530,720))
point8=object((1620,170))
point9=object((1184,440))
point10=object((500,500))
point_list=[point1,point2,point3,point4,point5,point6,point7,point8,point9,point10]
main_loop = True
sum_list = []
while main_loop:
    clock.tick(fps)
    sum_list=[]
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                UP_go = True
            if event.key == pygame.K_DOWN:
                DOWN_go = True
            if event.key == pygame.K_LEFT:
                LEFT_go = True
            if event.key == pygame.K_RIGHT:
                RIGHT_go = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                UP_go = False
            if event.key == pygame.K_DOWN:
                DOWN_go = False
            if event.key == pygame.K_LEFT:
                LEFT_go = False
            if event.key == pygame.K_RIGHT:
                RIGHT_go = False
        
    for i in point_list:
        for o in point_list:
            if not i==o:
                if i.x_ps<o.x_ps:
                    x_standard=i.x_ps
                    x_sum=(o.x_ps-i.x_ps)/2+x_standard
                else:
                    x_standard=o.x_ps
                    x_sum=(i.x_ps-o.x_ps)/2+x_standard
                if i.y_ps<o.y_ps:
                    y_standard=i.y_ps
                    y_sum=(o.y_ps-i.y_ps)/2+y_standard
                else:
                    y_standard=o.y_ps
                    y_sum=(i.y_ps-o.y_ps)/2+y_standard
                sum_list.append(object((x_sum,y_sum),sum=True))
    for i in range(len(sum_list)):
        if sum_list_func(i):
            continue
    if UP_go:
        point10.move_set(0,-2)
    if DOWN_go:
        point10.move_set(0,2)
    if LEFT_go:
        point10.move_set(-2,0)
    if RIGHT_go:
        point10.move_set(2,0)
    car.point_print()
    for i in point_list:
        i.point_print()
    for i in sum_list:
        i.point_print()
    pygame.display.flip()
