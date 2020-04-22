from scipy.integrate import odeint
from math import pi, acos, sqrt;

# r_lightSrc = radius of lightSrc
# r_pupil = radius of pupil
# d = distance between centers of pupil and lightSrc
# Q = illuminance of ambient light
# k = oscillation constant
# E = illuminance of point source
# t = time points
def calculateMovement(r_pupil_0, r_lightSrc, d, Q, k, E, t):

    print('Params: ');
    print('r_pupil: ' + str(r_pupil_0))
    print('r_lightSrc: ' + str(r_lightSrc))
    print('d: ' + str(d))
    print('Q: ' + str(Q))
    print('k: ' + str(k))
    print('E: ' + str(E))

    def drdt(r_pupil, t):
        if (d - r_lightSrc > r_pupil):
            area = 0;
        elif (d + r_lightSrc > r_pupil):
            # area of light src
            a_lightSrc = r_lightSrc**2 * acos( (d**2 + r_lightSrc**2 - r_pupil**2) / (2 * d * r_lightSrc) );

            # area of pupil
            a_pupil = r_pupil**2 * acos( (d**2 + r_pupil**2 - r_lightSrc**2) / (2 * d * r_pupil) );

            # area of pupil and lightSrc not overlapping
            not_a = 0.5 * sqrt( (-d+r_lightSrc+r_pupil) * (d+r_lightSrc-r_pupil) * (d-r_lightSrc+r_pupil) * (d+r_lightSrc+r_pupil) );

            area = a_lightSrc + a_pupil - not_a;
        else:
            area = pi * r_lightSrc**2

        # value of luminous flux in ambient light
        lum_flux_ambient = Q * pi * d**2

        # luminous flux entering pupil
        lum_flux = Q * pi * r_pupil**2 + E * area


        return (-k * (lum_flux - lum_flux_ambient));

    r = odeint(drdt, r_pupil_0, t);
    return r;


def simpleCalc(r_pupil, r_lightSrc, d, k):
    return -k * (r_pupil - (d-r_lightSrc));

def getDistance(x1, y1, x2, y2):
    return sqrt( (x1-x2)**2 + (y1-y2)**2 );
