from OpenGL.GL import *
import math
from entities.geometry.Point2D import Point2D
from entities.geometry.Rectangle import Rectangle
from entities.geometry.CollisionDetection import *
from entities.neuralnetwork.Network import Network
from entities.neuralnetwork.NetworkAmbSensors import NetworkAmbSensors
from entities.carsimulator.CarLogState import  CarLogState
import csv

class CarUsuari(object):
    """
    wheels_rotation_in_degrees:
        0 -> Wheels are centered
        negative -> Wheels are turned right
        positive -> Wheels are turned left
    """
    @staticmethod
    def get_num_angles() -> int:
        return 11

    def __init__(self, track, width: float, length: float, center: Point2D, tipo: int,n):
        self.__track = track
        self.__bounds = Rectangle(width, length)
        self.__bounds.center = center
        self.speed_in_meters_per_sec = 20


        self.__tipo=tipo # 0 si el duc jo, 1 si el du sa xarxa


        self.steer = 0
        self.__collision = False
        angles = [45, 65, 75, 85, 90, 95, 105, 115, 135]
        angle_ini = 10
        num_angles = self.get_num_angles()

        angles = [angle_ini+(x*(180-angle_ini*2)/(num_angles-1)) for x in range(0, num_angles)]
        self.__collision_distance = 150
        self.__vectors = [Point2D(math.sin(angle/180*math.pi)*self.__collision_distance, math.cos(angle/180*math.pi)*self.__collision_distance) for angle in angles]
        self.__collision_points = [Point2D(0, 0) for v in self.__vectors]
        self.__collision_distances = [0] * len(self.__vectors)
        self.__current_segment = 0
        self.__distance = 0
        self.__total_segment_distance = 0
        #self._net = Network([CarUsuari.get_num_angles(), 25, 2])
        #self._net = NetworkAmbSensors([CarUsuari.get_num_angles(), 25, 2])
        self._net=n
        self.__laps = 0
        self.__current_speed = 5
        self.number = 0



        self.__teclat=0
        self.__guardarTeclat=[]


        self.__tempsCar=0
        self.__SensorCentral=[8] * 10
        self.__memoriaSensorCentral=[]


    def memoriaSensorCentral(self):
        return self.__memoriaSensorCentral

    def SensorCentral(self):
        return self.__SensorCentral

    @property
    def net(self) -> int:
        return self._net

    @net.setter
    def net(self, new_net: float):
        self._net = new_net

    @property
    def current_speed(self) -> float:
        return self.__current_speed

    @current_speed.setter
    def current_speed(self, new_current_speed: float):
        self.__current_speed = new_current_speed

    @property
    def laps(self) -> int:
        return self.__laps

    @laps.setter
    def laps(self, new_laps: float):
        self.__laps = new_laps

    @property
    def current_segment(self) -> int:
        return self.__current_segment

    @current_segment.setter
    def current_segment(self, new_current_segment: float):
        self.__current_segment = new_current_segment

    @property
    def distance(self) -> float:
        return self.__distance

    @distance.setter
    def distance(self, new_distance: float):
        self.__distance = new_distance

    @property
    def total_segment_distance(self) -> float:
        return self.__total_segment_distance

    @total_segment_distance.setter
    def total_segment_distance(self, new_total_segment_distance: float):
        self.__total_segment_distance = new_total_segment_distance

    @property
    def bounds(self) -> Rectangle:
        return self.__bounds

    @property
    def collision_points(self) -> List[Point2D]:
        return self.__collision_points

    @property
    def collision_distances(self) -> List[float]:
        return self.__collision_distances

    @property
    def vectors(self) -> List[Point2D]:
        return self.__vectors

    @property
    def width(self) -> float:
        return self.__bounds.height

    @width.setter
    def width(self, new_width: float):
        self.__bounds.height = new_width

    @property
    def collision(self) -> float:
        return self.__collision

    @collision.setter
    def collision(self, new_collision: float):
        self.__collision = new_collision

    # @property
    # def log(self) -> CarLogState:
    #     return self.__CarLogState

    @property
    def length(self) -> float:
        return self.__bounds.width

    @length.setter
    def length(self, new_length: float):
        self.__bounds.width = new_length

    @property
    def position(self) -> Point2D:
        return self.__bounds.position

    @position.setter
    def position(self, new_position: Point2D):

        self.__bounds.position = new_position

    def render(self,tipo):
        if tipo==1:
            points = self.__bounds.points
            glBegin(GL_QUADS)
            glColor3f(0.2, 0.2, 0.2)
            glVertex3f(points[0].x, points[0].y, 0)
            glColor3f(1, 1, 1)
            if self.__collision:
                glColor3f(0.5, 0.5, 0.5)
            glVertex3f(points[1].x, points[1].y, 0)
            glVertex3f(points[2].x, points[2].y, 0)

            glColor3f(0.2, 0.2, 0.2)
            glVertex3f(points[3].x, points[3].y, 0)
            glEnd()
        else:
            points = self.__bounds.points
            glBegin(GL_QUADS)
            glColor3f(0.2, 0.2, 0.2)
            glVertex3f(points[0].x, points[0].y, 0)
            glColor3f(1, 1, 1)
            if self.__collision:
                glColor3f(0.5, 0.5, 0.5)
            glVertex3f(points[1].x, points[1].y, 0)
            glVertex3f(points[2].x, points[2].y, 0)

            glColor3f(0.2, 0.2, 0.2)
            glVertex3f(points[3].x, points[3].y, 0)
            glEnd()

    def colocar(self,x,y,angle,vel):

        self.__bounds.position = Point2D(x,y)
        self.__bounds.rotation_in_radians=angle
        #print(self.__current_speed)
        if vel==1:
            self.__current_speed=self.__current_speed+5*0.03
        else:
            if vel==0:
                self.__current_speed=self.__current_speed-5*0.03


        self.compute_collision_points()

    # def colocarAmbXarxa(self,sensors,tecla):
    #     r = self._net.feedforward(self.__collision_distances)
    #     steer = r[0]
    #     speed = r[1]
    #     self._steer = steer[0] - 0.5
    #     self.rotate((steer[0] - 0.5) * 10 * (2 * math.pi) / 360)
    #     self._current_speed = 7  # 3 + min(3, speed[0] * 3)
    def tempsCar(self):
        return self.__tempsCar

    def simulate(self, elapsed_time: float):
        # calculamos la nueva posicion
        cos = math.cos(self.__bounds.rotation_in_radians)
        sin = math.sin(self.__bounds.rotation_in_radians)
        mov = Point2D(cos * elapsed_time * self.current_speed, sin * elapsed_time * self.current_speed)

        self.__bounds.position = self.__bounds.position + mov

        #self.__guardarAngles.append(self.__bounds.rotation_in_radians)
        #self.__recorregut.append(self.__bounds.position)

        self.__tempsCar=self.__tempsCar+1


        self.compute_collision_points()

    def compute_collision_points(self):
        '''
        Compute collision points, like the car have distance sensors, and detect the points where will collide
        :return: no returns
        '''

        rot = self.bounds.rotation_in_radians
        self.__collision_points = []
        self.__collision_distances = []
        for vector in self.vectors:
            # para cada sensor calculamos un segmento (p0-p1) que representa el haz para detectar un obstáculo
            vector = vector.rotate(Point2D(0, 0), rot)
            p0 = Point2D(self.bounds.position.x, self.bounds.position.y)
            p1 = Point2D(self.bounds.position.x + vector.x, self.bounds.position.y + vector.y)

            # inicialmente no ha detectado nada
            min_distance = self.__collision_distance+1
            min_point = None


            for s in self.__track.segments:


                for cr in s.collisionRegions:
                    points = cr.points
                    numPoints = len(points)
                    for x in range(0, numPoints):
                        cr1 = points[x]
                        cr2 = points[(x+1)%numPoints]
                        intersection = segment_intersection(p0, p1, cr1, cr2)
                        if intersection is not None:
                            distance = (intersection - self.bounds.position).length()
                            if distance < min_distance:
                                min_distance = distance
                                min_point = intersection

                '''
                # de todas las colisiones nos quedamos con la más cercana
                #  buscamos si colisiona con el borde izquierdo
                intersection = segment_intersection(p0, p1, s.p1, s.p3)
                if intersection is not None:
                    distance = (intersection - self.bounds.position).length()
                    if distance < min_distance:
                        min_distance = distance
                        min_point = intersection
                # buscamos si colisiona con el borde derecho
                intersection = segment_intersection(p0, p1, s.p2, s.p4)
                if intersection is not None:
                    distance = (intersection - self.bounds.position).length()
                    if distance < min_distance:
                        min_distance = distance
                        min_point = intersection
                '''

            if min_point is not None:
                # Ha habido colision
                self.__collision_points.append(min_point)
                self.__collision_distances.append(min_distance)
            else:
                # No ha habido colision, nos quedamos con el punto final del segmento
                self.__collision_points.append(p1)
                self.__collision_distances.append(min_distance)


    def rotate(self, degree: float):
        '''
        Apply rotation to the car
        :param degree: degree en radians
        :return: Nothing
        '''
        self.__bounds.rotate(degree)



    def get_total_distance(self) -> float:
        return self.__total_segment_distance + self.__distance

    def teclat(self,tecla : float):
          self.__teclat=tecla
          return self.__teclat


    def rotacio(self):
        return self.__bounds.rotation_in_radians



