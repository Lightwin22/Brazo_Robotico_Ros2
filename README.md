Brazo robótico de 4 grados de libertad usando Ros2

    | Asignatura  | Programación de robots con Ros |
    | Integrantres | Bastián Almonacid  Darwin Muñoz |
Requerimientos:
`Linix`
`Ros2`
`Gazebo`
`Rviz`

##Simulaciones

A continuación se detallan los pasos para poder correctamente las simulaciones tanto del entorno de Rviz y gazebo, todo esto desde la terminal de linux

####Simulación en Rviz
Para pdoer ejecutar los comandos correctamente, abriremos la terminal en la cual tenemos almacenado el proyecto y se deberá ejecutar el siguiente comando:
```
source/opt/ros/iron/setup.bash
```
```
cd entorno
```
```
colcon build
```
```
source install/local_setup.bash
```
```
ros2 launch paquete_proyecto visualizacion.launch.py
```

####Simulación en Gazebo
