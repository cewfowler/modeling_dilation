import numpy as np;
import matplotlib.pyplot as plt
from random import random

from kivy.app import App, Widget;
from kivy.clock import Clock;
from kivy.uix.floatlayout import FloatLayout;
from kivy.core.window import Window;
from kivy.uix.label import Label;
from kivy.graphics import Color, Ellipse, Line;
from kivy.graphics.stencil_instructions import StencilPush, StencilPop, StencilUse,StencilUnUse;

from util import calculateMovement, getDistance;

Window.clearcolor = (0.9,0.9,0.9,1)


centerX = Window.size[0]/2;
centerY = Window.size[1]/2;

class Pupil(Widget):
    dilate = None;

    def __init__(self, lightSrc, maxRadius, minRadius, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs);

        self.minRadius = minRadius;
        self.maxRadius = maxRadius;
        self.lightSrc = lightSrc;

        d = getDistance(centerX, centerY, self.lightSrc[0], self.lightSrc[1]);
        t = np.linspace(0, 20, int(20/0.2), endpoint=False);

        # Get how pupil oscillates
        calculateMovement(1.135, 0.05, 1.135, 0.0003, 1250, 0.01, t);
        self.r = maxRadius * calculateMovement(1, self.lightSrc[2]/maxRadius, d/maxRadius, 0.0003, 1250, 0.01, t);
        self.counter = 0;

        self.dilate = Clock.schedule_interval(self.updatePupil, 0.2);

        # plot results
        plt.plot(t, self.r)
        plt.xlabel('time')
        plt.ylabel('y(t)')
        plt.show()

    def updatePupil(self, dt):

        newR = self.r[self.counter] + 8 * (random()-0.6);

        self.counter = self.counter + 1;
        if (self.counter >= len(self.r)):
            self.counter = 0;

        self.canvas.clear();
        with self.canvas:

            # Black
            Color(0, 0, 0, 1);
            Ellipse(pos=(centerX - newR, centerY - newR), size=(2*newR,2*newR));


class Eye(App):

    def build(self):
        self.root = root = FloatLayout();

        #print("Center X: " + str(centerX));
        #print("Center Y: " + str(centerY));

        lightSrc = [centerX-350, centerY, 16]

        with root.canvas:

            # Black
            Color(0, 0, 1, 1);

            # Eye
            r = 600;
            Ellipse(pos=(centerX - r, centerY - r), size=(2*r,2*r));

            # Black
            Color(0, 0, 0, 1);
            # Outer eye outline
            Line(circle=(centerX, centerY, r), width=3);

            # Show Pupil
            Pupil(lightSrc, 350, 100);

            # Gold
            Color(184/255, 212/255, 5/255, 1);

            # Light on edge of pupil
            Ellipse(pos=(lightSrc[0], lightSrc[1]), size=(2*lightSrc[2],2*lightSrc[2]));

        return root;


Eye().run();
