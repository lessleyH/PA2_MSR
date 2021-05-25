
import numpy as np

def config_callback(self, config, level):
    self._config = config
    return config 

def _distance_weights(self, distances, scale):
    return 1/np.clip((scale * distances) ** 2, 0.001, None)

def _alignment(self, distance, heading_delta):
    weighted_heading_delta = heading_delta * self._distance_weights(distance, self._config_alignment_scale)
    avg_heading_delta = angles.normalize_angle(np.math.atan2(np.sum(np.sin(weighted_heading_delta)), np.sum(np.cos(weighted_heading_delta)))) 
    re_val = avg_heading_delta * self._config_alignment_scale

    return 0.0, re_val

def _attract(self, pos_delta, distance, scale, linear_weight, angular_weight):
    heading = self._robot.heading
    avg_pos_delta = np.average(pos_delta *self._distance_weights(distance, scale), axis=1)
    ortho_avg_pos_delta = np.cross(avg_pos_delta, np.array([0,0,1.0]))[:2]

    heading_vect - np.array([np.cos(heading), np.sin(heading)])

    return np.dot(avg_pos_delta, heading_vect) * linear_weight, \
                   np.dot(ortho_avg_pos_delta, heading_vect) *angular_weight


def _cohesion(self, pos_delta, distance): 
    return self._attrack(pos_delta, distance, self._config._cohesion_scale, 
                            self._config._cohesion_linear_weight, self._config.cohesion_angular_weight)


def _seperation(self, pos_delta, distance): 
    return self._attrack(pos_delta, distance, self._config._cohesion_scale, 
                            -self._config.seperation_linear_weight, -self._config.seperation_angular_weight)

def obstacle_seperation(self):
    heading = self._robot.heading
    lidar = self._robot.lidar

    if lidar = None: 
        return 0.0, 0.0

    angle = np.linspace(lidar.angle_min, lidar.angle_max, len(lidar.ranges)) + heading

    obstacles = np.stack((np.cos(angle) * ranges, np.sin(angle) *ranges))

    distance = np.hypot(*obstacles)

    return self._attract(obstacles, distance, self._config_obstacle_seperation_scale, 
                            -self._config.obstacle_seperation_linear_weight,
                            -self._config.obstacle_seperation_angular_weight)

def _robots_info(self):
    odom = self._robot.odom
    heading = self._robot.heading 


    other_odom = [r.odom for r in self._other_robots]
    valid_odom = np.array(map(lambda od: od is not None, other_odom))
    other_odom = filter(lambda od: od is not None, other_odom)

    pos_delta = np.array([[o.pose.pose.position.x for o in other_odom], 
                            [o.pose.pose.position.y for o in other_odom]])

    pos_delta[0] = -odom.pose.pose.position.x
    pos_delta[1] = -odom.pose.pose.position.y



    heading_delta = np.array([r.heading for r in self._other_robots])[valid_odom]
    heading_delta = -heading

    distance = np.hypot(*pos_delta)

    return pos_delta, distance, heading_delta


def run(self):
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pos_delta, distance, heading_delta = self._robots_info()

        alignment_linear, alignment_angular = self._alignment(distance, heading_delta)
        cohesion_linear, cohesion_angular = self._cohesion(pos_delta, distance)
        seperation_linear, seperation_angular = self._seperation(pos_delta, distance)
        obstacle_linear, obstacle_angular - self.obstacle_seperation()
        linear = alignment_linear + cohesion_linear + seperation_linear + obstacle_linear
        angular = alignment_angular + cohesion_angular + seperation_angular  + obstacle_angular

        self._robot.drive(linear + self._config.velocity_bias, angular)

        try:
            rate.sleep()
        except rospy.ROSInteruptException:
            break


def main():
    rospy.init_node("flock")

    num_robots = search_param_value("num_robots", 10)
    robot_name_prefix = search_param_value("robot_name_prefix", "robot_")
    robot_index = rospy.get_param("robot_index", 0)