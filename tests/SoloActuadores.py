#!/home/johann/catkin_ws/src/tests/Vision-Actuadores-venv/bin/python3
import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import rospy
from std_msgs.msg import Float32
global X
global Y
global Z
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
        print(1)
        sys.exit(app.exec_())
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
        global X
        X = 0
        ACTUADORX(X)
    def STOPY(self):
        global Y
        Y = 0
        ACTUADORY(Y)
    def STOPZ(self):
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

def ACTUADORX(paquete):
    pub = rospy.Publisher("ACTUADORX", Float32, queue_size=10)
    rospy.init_node("ACTUADORESPY",anonymous=True)
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
    GUI.show()
    sys.exit(app.exec_())

