Brazo robótico de 3 grados de libertad usando Ros2

    | Asignatura  | Programación de robots con Ros |
    | Integrantres | Bastián Almonacid  Darwin Muñoz |
Requerimientos:
`Linix`
`Ros2`
`Gazebo`
`Rviz`

## Simulaciones

A continuación se detallan los pasos para poder correctamente las simulaciones tanto del entorno de Rviz y gazebo, todo esto desde la terminal de linux

#### Simulación en Rviz
Para poder ejecutar los comandos correctamente, abriremos la terminal en la cual tenemos almacenado el proyecto y se deberán ejecutar las siguientes lineas de comando:
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
Si se ejecuta todo de manera correcta nos debería de abrir la siguiente interfaz para poder interactuar con el brazo

##### Breve explicación los comandos ejecutados
` source/opt/ros/iron/setup.bash` 

Como se usará la versión Iron de Ros2, lo que hace es configurar el entorno de la terminal para poder ejecutar estos comandosy se establecen las variables de entorno.

`colcon build`





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





