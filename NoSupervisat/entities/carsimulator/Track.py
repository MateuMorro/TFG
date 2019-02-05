from typing import List
from entities.geometry.Point2D import Point2D
from entities.carsimulator.Segment import Segment
from entities.carsimulator.ObstaculoCuadrilatero import Obstaculo
from entities.geometry.Polygon import Polygon
from entities.carsimulator.CarregarCircuit import CarregarCircuit
from entities.carsimulator.CarregarObstacle import CarregarObstacle
from OpenGL.GL import *
import csv
import os

class Track(object):
    def __init__(self,n):

            self.__points=CarregarCircuit(n).points()
            widths=CarregarCircuit(n).widths()

            self._segments = []
            parray = []
            for i in range(0, len(self.__points)):
                p0 = self.__points[i]
                j = (i + 1) % len(self.__points)
                p1 = self.__points[j]
                k = (i + 2) % len(self.__points)
                p2 = self.__points[k]
                v0 = (p1 - p0).unitary()
                v1 = (p2 - p1).unitary()
                vf = (v0 + v1).unitary()
                vn = Point2D(vf.y, -vf.x)
                width = widths[i]
                pn1 = p1 + vn.mul_by_value(width)
                pn2 = p1 - vn.mul_by_value(width)
                parray.append((pn1, pn2))

            wall_width = 0.5 # crea los segmentos usando los pares de puntos, usando como ancho de la pared 0.5
            for i in range(0, len(parray)):
                j = (i+1) % len(parray)
                p0 = parray[i][0]
                p1 = parray[i][1]
                p2 = parray[j][0]
                p3 = parray[j][1]
                self._segments.append(Segment(p0, p1, p2, p3, wall_width))

            obstacles = CarregarObstacle(n).lista()
            for i in obstacles:

                self._segments[0].collisionRegions.append(Polygon(i))


            #Obstacles circuit 7
            # if n==7:
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(36, 23), Point2D(30, 23), Point2D(33, 19),Point2D(36, 19)]))
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(60, 20), Point2D(66, 20), Point2D(66, 26), Point2D(60, 26)]))
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(127, 60), Point2D(129, 53), Point2D(131, 56)]))
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(60, 100), Point2D(64, 100), Point2D(64, 103), Point2D(62, 103)]))
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(60, 43), Point2D(64, 44), Point2D(64, 45), Point2D(60, 51)]))
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(82, 106), Point2D(96, 104), Point2D(93, 108)]))
            #


            #Obstacles circuit 10
            # if n==10:
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(38, 102), Point2D(44, 106), Point2D(64, 103)]))
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(72, 75), Point2D(79, 75), Point2D(76, 70)]))
            #     self._segments[0].collisionRegions.append(Polygon([Point2D(106, 20), Point2D(110, 18), Point2D(112, 23), Point2D(109, 27), Point2D(105, 26)]))

            # Obstacles circuit 11

            #if n==11:
            #    self._segments[0].collisionRegions.append(Polygon([Point2D(70, 122), Point2D(85, 120), Point2D(70, 115)]))
            #    self._segments[0].collisionRegions.append(Polygon([Point2D(70, 103), Point2D(85, 103), Point2D(70, 110)]))



    def DistanciaTotalCircuit(self):
        distancia=0

        for i in range(0, len(self.__points)-1):
            distancia=distancia+self.__points[i].distance_to(self.__points[i+1])

        distancia=distancia+self.__points[len(self.__points)-1].distance_to(self.__points[0])

        return distancia





    def render(self):
        for s in self._segments:
            s.render()

    def render2(self):
        for s in self._segments:
            s.render2()

    def next_segment(self, num: int) -> int:
        return (num + 1) % len(self.segments)

    def previous_segment(self, num: int) -> int:
        return (num - 1 + len(self.segments)) % len(self.segments)

    @property
    def segments(self) -> List[Segment]:
        return self._segments

    def get_start_position(self) -> (Point2D, float, int):
        '''
        Compute start position in the track
        :return: Three values: Start Position, Orientation, Starting Segment Index
        '''
        start_segment = 0
        a = self.segments[start_segment].get_start_position()
        return a[0], a[1], start_segment




