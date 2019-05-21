import numpy as np
from scipy.integrate import odeint

def dx(u, g, h, b3, m, x, y, d1, q1, mm, dd1):
    return u*g*h - b3*m*(x/(x+y)) - d1*x - q1*mm*x - dd1*x

def dy(u, g, h, b3, m, x, y, d2, q2, mm, dd3):
    return b3*m*(x/(x+y)) - d2*y - q2*mm*y - dd3*x
