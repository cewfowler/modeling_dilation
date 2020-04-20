from kivy.app import App, Widget;
from kivy.clock import Clock;
from kivy.uix.floatlayout import FloatLayout;
from kivy.core.window import Window;
from kivy.uix.label import Label;
from kivy.graphics import Color, Ellipse, Line;
from kivy.graphics.stencil_instructions import StencilPush, StencilPop, StencilUse,StencilUnUse;

Window.clearcolor = (0.9,0.9,0.9,1)


centerX = Window.size[0]/2;
centerY = Window.size[1]/2;

class Pupil(Widget):
    dilate = None;

    def __init__(self, lightSrc, maxRadius, minRadius, *args, **kwargs):
        Widget.__init__(self, *args, **kwargs);

        self.minRadius = minRadius;
        self.maxRadius = maxRadius;

        self.dilate = Clock.schedule_interval(self.update, 0.01);

    def update(self, dt):
        r = 100;
        with self.canvas:
            # Black
            Color(0, 0, 0, 1);
            Ellipse(pos=(centerX - r, centerY - r), size=(2*r,2*r));


class Eye(App):

    def build(self):
        self.root = root = FloatLayout();

        print("Center X: " + str(centerX));
        print("Center Y: " + str(centerY));

        lightSrc = [centerX-50, centerY+50]

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
            Pupil(lightSrc, 500, 300);

            # Gold
            Color(184/255, 212/255, 5/255, 1);

            # Light on edge of pupil
            r = 10;
            Ellipse(pos=(lightSrc[0], lightSrc[1]), size=(2*r,2*r));

        return root;


Eye().run();
