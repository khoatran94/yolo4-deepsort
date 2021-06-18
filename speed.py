import math



"""
calc_distance_between_two_points based on euclidean distance.
   :param number x1: x of first point
   :param number y1: y of first point
   :param number z1: z of first point
   :param number x2: x of second point
   :param number y2: y of second point
   :param number z2: z of second point
   :return: distance in meter
"""
def calc_distance_between_two_points_kart(x1, y1, x2, y2):
    dis = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    dis = dis 
    return dis


"""
Calculate based on two coordinates , start & endframe and fps (frame per second) 
speed in km/h 
   :param number x1: x of first point
   :param number y1: y of first point
   :param number z1: z of first point
   :param number start_frame: number of first frame where object is detected
   :param number x2: x of second point
   :param number y2: y of second point
   :param number z2: z of second point
   :param number end_frame: number of second frame where object is detected
   :param number fps: current frame rate of the video
   :return: speed in km h 
"""
def calc_speed(x1, y1, start_frame, x2, y2, end_frame, fps):
    time = (end_frame - start_frame) * (1 / fps)
    # print(time)
    distance = calc_distance_between_two_points_kart(x1, y1, z1, x2, y2, z2)
    # print(distance)
    speed = distance / time
    speed = abs(speed) * 3.6
    return speed


"""
khoa not finish fixing this
This class store all detected objects and give the functionality to
get their speed. Update() function is working with cartesian coordinates 
"""
class Speedtracker(object):
    def __init__(self):
        self.track_obj = []
    """
    update position information
    :param number id: id of detected object 
    :param number x: x position of detected object
    :param number y: y position of detected object
    :param number z: z position of detected object
    :param number frame: frame where object is detected
    :param number fps: current frame rate of the video
    :return: speed in km h 
    """
    def update(self, id, x, y, z, frame, fps):
        contains = False
        for i in range(len(self.track_obj)):
            if (self.track_obj[i][0] == id):
                contains = True

        if contains:
            for i in range(len(self.track_obj)):
                if (self.track_obj[i][0] == id):
                    self.track_obj[i][6] = x
                    self.track_obj[i][7] = y
                    self.track_obj[i][8] = z
                    self.track_obj[i][9] = frame
        else:
            self.track_obj.append([id, x, y, frame, fps, 0, frame, 0])

    def get_speedtracker(self, id):
        for i in range(len(self.track_obj)):
            if (self.track_obj[i][0] == id):
                return self.track_obj[i]
        return None

    def get_speed(self, id):
        obj = self.get_speedtracker(id)
        if (obj != None):
            speed = calc_speed(obj[1], obj[2], obj[3], obj[4], obj[6], obj[7], obj[8], obj[9], obj[5])
            return speed
        else:
            return None

    # Clean Speedtracker List
    def cleanup(self):
        self.track_obj.clear()
