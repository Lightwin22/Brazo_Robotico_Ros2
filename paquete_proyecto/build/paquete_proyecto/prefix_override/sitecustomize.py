import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vboxuser/Escritorio/ROS/entorno/paquete_proyecto/install/paquete_proyecto'
