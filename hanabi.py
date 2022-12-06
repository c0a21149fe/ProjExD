#! /usr/bin/env python
# -*- coding: shift_jis -*-
"""
hanabi.py

July 08, 2005
"""
import tkinter as Tk
import random as R
import math as M



HANABI_COLORS = ['red', 'lightcyan',  '#FF33FF', '#FF99FF', '#FFFFCC', '#FFCC00', 
                 'magenta', 'blueviolet', 'white', '#FF99FF']
NIGHT_COLOR = '#000033'
G = 1
HR = 1
NHANA = 20
N_COLORS = len(HANABI_COLORS)-1


def rand_angle(n):
    """ +- x degree, where x is degree of radius of children """
    return M.pi * R.randint(-10,10)/(float(n)*10.0)

class Hanabi:
    canvas = None
    list = None


    def __init__(self, **p):
        x = p['x']
        y = p['y']
        self.vx = p['vx']
        self.vy = p['vy']
        self.lifetime = p['lifetime']
        self.id = Hanabi.canvas.create_oval(x-HR, y-HR, x+HR, y+HR, fill=p['color'], width=0)
        self.counter=0


    def moving(self):
        if(self.counter<self.lifetime):
            Hanabi.canvas.move(self.id, self.vx, self.vy)
            self.counter += 1
            self.vy += G
        else:
            self.disappear()


    def disappear(self):
        Hanabi.canvas.delete(self.id)
        self.id = None



class Mother(Hanabi):
    
    def disappear(self):
        r0 = R.randint(13,17)
        v0 = R.randint(18, 22)
        nc0 = R.randint(0,N_COLORS)
        nc1 = R.randint(1, N_COLORS-1)
        x1,y1,x2,y2 = Hanabi.canvas.coords(self.id)
        x, y = (x1+x2)/2, (y1+y2)/2
        self.make_sphere(NHANA, x, y, r0, v0, HANABI_COLORS[nc0], self.vx, self.vy)
        self.make_sphere(NHANA/2, x, y, r0/3, v0/3, HANABI_COLORS[(nc0+nc1)%(N_COLORS+1)], self.vx, self.vy)
        Hanabi.disappear(self)


    def make_sphere(self, nh, x, y, r, v, c, vx0, vy0):
        d_eta = 2.0 * M.pi / float(NHANA)
        eta = rand_angle(NHANA) 
        for i in range(int(NHANA/2)):
            dxy = M.sin(eta)
            n = M.floor(dxy * nh)
            d_theta = n and 2 * M.pi/n or 2* M.pi
            theta = rand_angle(NHANA)
            
            if i%2:
                theta += d_theta*0.5
                
            for j in range(int(n)):
                dx = M.cos(theta) * dxy 
                dy = M.sin(theta) * dxy
                Hanabi.list.append(Hanabi(x=r*dx+x, y=r*dy+y, color=c, 
                                   vx=v*dx+vx0, vy=v*dy+vy0,  lifetime=R.randint(8,15)))
                theta += d_theta
            eta +=d_eta




class Frame (Tk.Frame):       
    
    def __init__(self, master=None):
        Tk.Frame.__init__(self, master)
        self.master.title("Hanabi")
        self.master.geometry("+20+20")
        Hanabi.canvas = Tk.Canvas(self, width=500, height=700,
                                   relief=Tk.SUNKEN, borderwidth=2, bg=NIGHT_COLOR)
                                   
        Hanabi.canvas.pack(fill=Tk.BOTH, expand=1)

        Hanabi.list = []
        self.rep()

    def rep(self):
        # delete disappeared items
        n = len(Hanabi.list)
        i=0
        while(i<n):
            if(Hanabi.list[i].id):
                i += 1
            else:
                del Hanabi.list[i]
                n -= 1

        # move items
        for p in Hanabi.list:
            p.moving()

        # launch another hanabi, one every second in average
        if R.randint(0,100)>90:
            self.create_hanabi()

        # repeat
        self.after(100, self.rep)


    def create_hanabi(self):
        vy0 = R.randint(-33,-31)
        Hanabi.list.append(Mother(x=R.randint(150, 350), y=695, vx=R.randint(-1,1), vy=vy0,
                                  color='#CC6600', lifetime=vy0*(-1)-R.randint(3,5)))
        

##-----------------------------------------------------
if __name__ == '__main__':
    f = Frame()
    f.pack(fill=Tk.BOTH, expand=1)
    f.mainloop()

