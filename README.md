# PA2_
### Lessley Herandez
### Spring 21, COSC269

### Purpose of Assingment 
The purpose of this assingment is to introduce ROS, the simulator, and a behavioral based multirobot formation control. 

Modifying the simulation for multirobots 
Implementing flocking behavior through simpler local behavior 

### The task 
1- create a world in Gazebo simulator with 3 robots
2- Assuming that the robot can also get information about the other orientation and position, implement seperation, alignment, and cohesion behavior 
3- The robot should not collide with any obstacle 
4- Create a simulated world in stage, with 10 robots and test the same code in the simulator

### Requirements 
- ROS -- tested on Melodic, but other versions may work.
- colcon -- used for building the application.

### Methods 
How does your program work? What design decisions did you make? 


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