#!/home/johann/catkin_ws/src/tests/Vision-Actuadores-venv/bin/python3

#Vision CamaraPrimesense
import numpy as np
#import cv2
#from primesense import openni2#, nite2
#from primesense import _openni2 as c_api


#ROS y Actuadores librerias
import threading
import os
import sys
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Float32MultiArray
global DisG
global DisO
global X
global Y
global Z
global stop_threads
stop_threads = False
Dis=0
DisG=[0,0,0]
DisO=[0,0,0]
X=0
Y=0
Z=0


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class ActuadorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        ActuadoresGUI = resource_path("ActuadoresGUI.ui")
        uic.loadUi(ActuadoresGUI, self)
        self.Salir.clicked.connect(self.Salido)
        self.RETROCEDERX.clicked.connect(self.RETROCEDERXX)
        self.RETROCEDERY.clicked.connect(self.RETROCEDERYY)
        self.RETROCEDERZ.clicked.connect(self.RETROCEDERZZ)
        self.AVANZARX.clicked.connect(self.AVANZARXX)
        self.AVANZARY.clicked.connect(self.AVANZARYY)
        self.AVANZARZ.clicked.connect(self.AVANZARZZ)
        self.PARADAX.clicked.connect(self.STOPX)
        self.PARADAY.clicked.connect(self.STOPY)
        self.PARADAZ.clicked.connect(self.STOPZ)

    def Salido (self):
        global stop_threads
        stop_threads=True
        # global DisG
        # global DisO
        # UGripper()
        # UObjeto()
        # O=DisO[1]
        # G=DisG[1]
        # print(O-G)
        # ACTUADORZ(O-G)

    def AVANZARXX(self):
        global X
        X=X+1000
        ACTUADORX(X)
    def AVANZARYY(self):
        global Y
        Y = Y + 1000
        ACTUADORY(Y)
    def AVANZARZZ(self):
        global Z
        Z = Z + 1000
        ACTUADORZ(Z)
    def STOPX(self):
        global stop_threads
        stop_threads = False
        global X
        X = 0
        ACTUADORX(X)

    def STOPY(self):
        global stop_threads
        stop_threads = False
        global Y
        Y = 0
        ACTUADORY(Y)

    def STOPZ(self):
        global stop_threads
        stop_threads = False
        global Z
        Z = 0
        ACTUADORZ(Z)


    def RETROCEDERXX(self):
        global X
        X = X - 1000
        ACTUADORX(X)
    def RETROCEDERYY(self):
        global Y
        Y = Y - 1000
        ACTUADORY(Y)
    def RETROCEDERZZ(self):
        global Z
        Z = Z - 1000
        ACTUADORZ(Z)

#Controlador
def Automatico ():
    global stop_threads, DisG, DisO
    while True:
        time.sleep(0.2)
        while stop_threads:
            # t = threading.Thread(target=listener)
            # t.start()
            UGripper()
            UObjeto()
            print(DisO)
            print(DisG)
            O = DisO[1]
            G = DisG[1]
            print((O - G))
            ACTUADORZ(-17*(O - G)) #-17
            O = DisO[0]
            G = DisG[0]
            print(-(O - G))
            ACTUADORY(-4 * (O - G))#-4
            O = DisO[2]
            G = DisG[2]
            print(-(O - G))
            ACTUADORX(-1 * (O - G))
#Enviar al arduino
def ACTUADORX(paquete):
    pub = rospy.Publisher("ACTUADORX", Float32, queue_size=10)
    rospy.init_node("ACTUADORESPY",anonymous=True)#Se inicia el nodo ACTUADORESPY(Actuadores python)
    rate = rospy.Rate(10) #10 Hz
    if not rospy.is_shutdown():
        hello_str = float(paquete)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def ACTUADORY(paquete):
    pub = rospy.Publisher("ACTUADORY", Float32, queue_size=10)
    rospy.init_node("ACTUADORESPY",anonymous=True)
    rate = rospy.Rate(10) #10 Hz
    if not rospy.is_shutdown():
        hello_str = float(paquete)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def ACTUADORZ(paquete):
    pub = rospy.Publisher("ACTUADORZ", Float32, queue_size=10)
    rospy.init_node("ACTUADORESPY",anonymous=True)
    rate = rospy.Rate(10) #10 Hz
    if not rospy.is_shutdown():
        hello_str = float(paquete)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

#Para recibir de la camara
def callback(data):
    rospy.loginfo(data.data)
    global DisG
    DisG=data.data

def callback2(data):
    rospy.loginfo(data.data)
    global DisO
    DisO=data.data

def UObjeto():
    rospy.init_node("ACTUADORESPY", anonymous=True)
    rospy.Subscriber("DistanciaObjeto", Float32MultiArray, callback2)
    rate = rospy.Rate(10)  # 10 Hz
    rate.sleep()
    #rospy.spin()
def UGripper():
    rospy.init_node("ACTUADORESPY", anonymous=True)
    rospy.Subscriber("DistanciaGripper", Float32MultiArray, callback)
    rate = rospy.Rate(10)  # 10 Hz
    rate.sleep()
    #rospy.spin()
'''
def talker(paquete):
    pub = rospy.Publisher("ACTUADORZ", Float32, queue_size=10)
    rospy.init_node("talker",anonymous=True)
    rate = rospy.Rate(10) #10 Hz
    if not rospy.is_shutdown():
        hello_str = float(paquete)
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ActuadorGUI()
    t1 = threading.Thread(target=Automatico, daemon=True)
    t1.start()
    GUI.show()
    sys.exit(app.exec_())

