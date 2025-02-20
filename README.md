# Brazo robótico de 3 grados de libertad usando Ros2

    | Asignatura  | Programación de robots con Ros |
    | Integrantres | Bastián Almonacid  Darwin Muñoz |
Requerimientos:
`Linix`
`Ros2`
`Gazebo`
`Rviz`

## Simulaciones

A continuación se detallan los pasos para poder correctamente ejecutar las simulaciones tanto del entorno de Rviz y gazebo, todo esto desde la terminal de linux

#### Simulación en Rviz
Para poder ejecutar los comandos correctamente, abriremos la terminal desde la carpeta entorno  y se deberan ejecutar los siguientes comandos:
```
source/opt/ros/iron/setup.bash
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
Si se ejecuta todo de manera correcta nos debería de abrir la siguiente interfaz para poder interactuar con el brazo robot

![](https://github.com/Lightwin22/Brazo_Robotico_Ros2/blob/master/Rviz.jpeg)
En la parte izquiera de la imagen se ve el echo del topico joint_states verificando que la tf es correcta

##### Breve explicación los comandos ejecutados
` source/opt/ros/iron/setup.bash` 

Como se usará la versión Iron de Ros2, lo que hace es configurar el entorno de la terminal para poder ejecutar estos comandos y se establecen las variables de entorno.

`colcon build`
Creará  la compilación de los nuevos archivos generados para su posterior simulación dentro del entorno de Rviz

`ros2 launch paquete_proyecto visualizacion.launch.py`
Esta linea finalmente lanza la simulación de Rviz para poder realizar los movimientos con el brazo.

#### Simulación en Gazebo

Al igual que las simulaciones de Rviz, abriremos la terminal donde estan alojados los archivos pertenecientes al proyecto y se ejecutaran la siguientes lineas de comando:
```
source\opt\ros\iron\setup.bash
```
```
cd entorno
```
```
colcon build
```
```
source install\local_setup.bash
```
```
ros2 launch paquete_proyecto gazebo.launch.py
```
Al igual como se realizarón las simulaciones con Rviz, si se ejecutaron todos los comandos correctamente, nos debería de abrir el entorno de Gazebo con el mundo se creo previamente para poder interacturar con el brazo robótico.

![](https://github.com/Lightwin22/Brazo_Robotico_Ros2/blob/master/Gazebo.jpeg)

Tanto el launch de Gazebo como el de Rviz ejecutan además los nodos de joint_state_publisher_gui y robot_state_publisher.

![](https://github.com/Lightwin22/Brazo_Robotico_Ros2/blob/master/sensor_rviz.jpeg)

Integración de sensor/cámara visualizada desde Rviz
