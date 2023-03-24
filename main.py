#Muhammed Emin Ay @eminimki - 20120205038
import math
from OpenGL.GLUT import *
from OpenGL.GL import *
import sys
import random as rn
cam_boyasi = [0.1, 1, 1]
kapi_boyasi = [1,0,0]

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)

    # Kapi Boyasi
    r = kapi_boyasi[0]
    g = kapi_boyasi[1]
    b = kapi_boyasi[2]
    glColor3f(r, g, b)

    glBegin(GL_POLYGON)
    glVertex2f(0.5, 0)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 0)
    glVertex2f(-0.5, 0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 0)
    glEnd()

    #Cam Boyasi
    r = cam_boyasi[0]
    g = cam_boyasi[1]
    b = cam_boyasi[2]
    glColor3f(r, g, b)

    glBegin(GL_POLYGON)
    glVertex2f(-0.25, 0)
    glVertex2f(-0.25, 0.5)
    glVertex2f(0.25, 0.5)
    glVertex2f(0.25, 0)
    glEnd()

    #Arka Kapi Cerceve
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.5, 0)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0,0)
    glEnd()

    #On Kapi Cerceve
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0.5, 0)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.0, -0.5)
    glVertex2f(0.0, 0)
    glEnd()

    # Cam Cerceve
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-0.25, 0)
    glVertex2f(-0.25, 0.5)
    glVertex2f(0.25, 0.5)
    glVertex2f(0.25, 0)
    glEnd()




    #Arka Teker
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertex in range(0, 720):
        angle = float(vertex) * 1 * math.pi / 360
        glVertex3f(-0.35 + math.cos(angle) * 0.1, -0.6 + math.sin(angle) * 0.1, 0.0)
    glEnd()

    # On Teker
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    for vertex in range(0, 720):
        angle = float(vertex) * 1 * math.pi / 360
        glVertex3f(0.35 + math.cos(angle) * 0.1, -0.6 + math.sin(angle) * 0.1, 0.0)
    glEnd()
    glFlush()

def keyPressed(*args):
    #Escape code=\x1b
    if args[0] == b"\x1b" or args[0] == bytes('q', 'utf-8'):
        sys.exit()
    elif args[0] == bytes('r', 'utf-8'):
        kapi_boyasi[0] = rn.random()
        kapi_boyasi[1] = rn.random()
        kapi_boyasi[2] = rn.random()
        print("arabanin rengi degisti.")
        glutPostRedisplay()
    else:
        print("bilinmeyen bir tusa basildi.")




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Plot Points")
    glutDisplayFunc(plotpoints)
    glutKeyboardFunc(keyPressed)
    init()
    glutMainLoop()


main()
