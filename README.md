# PA2_
### Lessley Herandez
### Spring 21, COSC269

### Purpose of Assingment 


### Requirements 
- ROS -- tested on Melodic, but other versions may work.
- colcon -- used for building the application.

### Methods 
How does your program work? What design decisions did you make? 

It can ba assumed that the robot starts at one of the vertices, following one of the edges, complete it either clockwise or counte-clockwise 

the node should publish at each of the vertices of the polygon the error message using ```std_msgs/Float32``` between the current position and the expected polygon vertice location

To test the code:  
``` 
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```
In a browser window run: http://localhost:8080/vnc.html 

### Evaluation
Does your program actually work? How well? If it doesn't work can you tell why not? 

Well...I thought it worked,but it didn't 

### How to execute the file
In your workspace run:
```
docker-compose up --build
```
Once the  terminal shows this as output:  

```
Starting mac-ros_novnc_1 ... done
Starting mac-ros_ros_1   ... done
```
In a new terminal: 

``` 
cd ros_workspace
docker-compose exec ros bash

roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

in another another terminal 
docker-compose exec ros bash
roslaunch simple_poly simple_poly.launch
```


## Sources/ Inspiration 
Adapted from the 