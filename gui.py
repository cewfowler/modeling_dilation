from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line;

Window.clearcolor = (0.9,0.9,0.9,1)

class PupilVisual(App):

    def build(self):
        self.root = root = FloatLayout();
        centerX = Window.size[0]/2;
        centerY = Window.size[1]/2;

        minRadius = 300;
        maxRadius = 500;
        print("Center X: " + str(centerX));
        print("Center Y: " + str(centerY));

        with root.canvas:
            # Blue
            Color(0, 0, 1, 1);

            # Pupil Center
            r = 100;
            Ellipse(pos=(centerX - r, centerY - r), size=(2*r,2*r));

            # Black
            Color(0, 0, 0, 1);

            # Pupil Center Outline
            Line(circle=(centerX, centerY, r), width=1.5);

            # Outer pupil
            r = maxRadius;
            Line(circle=(centerX, centerY, r), width=1.5);

            # Gold
            Color(184/255, 212/255, 5/255, 1);

            # Light entering pupil
            r = 10;
            Ellipse(pos=(centerX-300, centerY+150), size=(2*r,2*r));

        return root;


PupilVisual().run();
