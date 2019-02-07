from entities.carsimulator.Track import Track
from entities.carsimulator.Car import Car
from entities.geometry.CollisionDetection import *
from entities.neuralnetwork.Network import Network
from OpenGL.GL import *
import numpy


class Race(object):
    def __init__(self,n,k,m):
        self._track = Track(n)
        self._cars = []
        self.__n=n
        self.__k=k
        self.__number_cars = m
        self.__total_time = 0
        self.__alives = self.__number_cars


        #Cotxo que duc jo
        car = Car(self._track, 2, 1, Point2D(-1, 0), 0,n)
        start_position, angle, start_segment = self._track.get_start_position()
        car.bounds.position = start_position
        car.bounds.rotation_in_radians = angle
        car.current_segment = start_segment
        car.distance = 0
        car.number = 0   + self.__k
        self._cars.append(car)
        #Els altres
        for x in range(1, self.__number_cars):
            car = Car(self._track, 2, 1, Point2D(-1, 0),1,n)
            start_position, angle, start_segment = self._track.get_start_position()
            car.bounds.position = start_position
            car.bounds.rotation_in_radians = angle
            car.current_segment = start_segment
            car.distance = 0
            car.number = x  + self.__k

            self._cars.append(car)

    def reset(self):
        self.__total_time = 0

        weights = [max(c.get_weight(), 0) for c in self._cars]
        total_weight = 0
        sum_weights = []
        for w in weights:
            total_weight = total_weight + w
            sum_weights.append(total_weight)

        previous_cars = self._cars

        self.__alives = self.__number_cars
        self._cars = []




        # jo
        car = Car(self._track, 2, 1, Point2D(-1, 0), 0,self.__n)
        start_position, angle, start_segment = self._track.get_start_position()
        car.bounds.position = start_position
        car.bounds.rotation_in_radians = angle
        car.current_segment = start_segment
        car.distance = 0
        car.number = 0   + self.__k
        car.current_speed = 5
        car.steer = 0
        self._cars.append(car)



        for x in range(1, self.__number_cars):
            car = Car(self._track, 2, 1, Point2D(-1, 0),1,self.__n)
            start_position, angle, start_segment = self._track.get_start_position()
            car.bounds.position = start_position
            car.bounds.rotation_in_radians = angle
            car.current_segment = start_segment
            car.distance = 0
            car.current_speed = 5
            car.steer = 0
            car.number = x  + self.__k

            w = numpy.random.uniform(0, total_weight)
            index = 0
            i = 0
            while i < len(sum_weights):
                if sum_weights[i] >= w:
                    index = i
                    break;
                i = i + 1

            if index >= len(previous_cars):
                index = 0

            if x > 5:
                car.net = previous_cars[index].net.copy()
                car.net.apply_noise()

            self._cars.append(car)

    def get_first_car(self) -> Car:
        max_distance = None
        first_car = None
        for c in self._cars:
            distance = c.get_total_distance()
            if (max_distance is None) or (distance > max_distance):
                max_distance = distance
                first_car = c
        return first_car

    def render(self):


        c = self._cars[0]
        if not c.collision:
            for i in range(len(c.collision_points)):

                if i == 5:
                    glBegin(GL_LINES)
                    glColor3f(1, 1, 1)
                    glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y - 1, 0)
                    glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y + 1, 0)
                    glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y + 1, 0)
                    glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y - 1, 0)
                    glEnd()
                else:
                    glBegin(GL_LINES)
                    glColor3f(1, 0.3, 0)
                    glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y - 1, 0)
                    glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y + 1, 0)
                    glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y + 1, 0)
                    glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y - 1, 0)
                    glEnd()



        self._track.render()

        for x in range(1, self.__number_cars):
           c=self._cars[x]
           if not c.collision:
                 for i in range(len(c.collision_points)):

                     if i==5:
                         glBegin(GL_LINES)
                         glColor3f(1, 1, 1)
                         glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y - 1, 0)
                         glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y + 1, 0)
                         glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y + 1, 0)
                         glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y - 1, 0)
                         glEnd()
                     else:
                        glBegin(GL_LINES)
                        glColor3f(0, 1, 1)
                        glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y - 1, 0)
                        glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y + 1, 0)
                        glVertex3f(c.collision_points[i].x - 1, c.collision_points[i].y + 1, 0)
                        glVertex3f(c.collision_points[i].x + 1, c.collision_points[i].y - 1, 0)
                        glEnd()

           self._track.render()



        self._cars[0].render(0)
        for x in range(1, self.__number_cars):
            self._cars[x].render(1)


    def simulate(self, elapsed_time: float):
        self.__total_time = self.__total_time + elapsed_time
        for c in (self._cars):

            if not c.collision:
                c.simulate(elapsed_time)


                for segment in self._track._segments:
                    if segment.collides(c):
                        c.collision = True
                        c.collision_time = self.__total_time

                if c.collision:
                    self.__alives = self.__alives - 1


                ns = self._track.next_segment(c.current_segment)
                if self.track.segments[ns].in_segment(c.bounds.position):
                    c.total_segment_distance = c.total_segment_distance + self.track.segments[c.current_segment].total_distance
                    c.current_segment = ns
                    if ns == 0:
                        c.laps = c.laps + 1
                else:
                    ps = self._track.previous_segment(c.current_segment)
                    if self.track.segments[ps].in_segment(c.bounds.position):
                        if c.current_segment == 0:
                            c.laps = c.laps - 1
                        c.current_segment = ps
                        c.total_segment_distance = c.total_segment_distance - self.track.segments[c.current_segment].total_distance

                # distancia recorreguda en el segment actual
                cs = self.track.segments[c.current_segment]
                c.distance = (cs.point_ini - cs.advanced(c.bounds.position)).length()

        self._cars[0].torna()
        self._cars[0].sensors()

    @property
    def cars(self) -> List[Car]:
        return self._cars

    @property
    def alives(self) -> int:
        return self.__alives

    @property
    def track(self) -> Track:
        return self._track

    @property
    def alives(self) -> int:
        return self.__alives\

    @property
    def total_time(self) -> float:
        return self.__total_time
