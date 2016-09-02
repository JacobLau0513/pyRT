from abc import abstractmethod
from ..math.ray import *
import uuid

class Shape():
    def __init__(self, name: str):
        self.name = name
        self.id = str(uuid.uuid4())

    @abstractmethod
    def hit(self, ray: Ray, hitrecord: HitRecord) -> bool:
        '''
        :param ray: the ray to check hit
        :param tmin: tmin to test intersection
        :param tmax: tmax to test intersection
        :param hitrecord: the hitrecord which is only valid if there is a hit
        :return: True if there is a hit
        '''
        pass

    @abstractmethod
    def hitShadow(self, ray: Ray) -> bool:
        '''
        :param ray:
        :param tmin:
        :param tmax:
        :return:
        '''
        pass

    #####################
    # TODO: BOUNDING BOX
    #       implement abstract method to retrieve bounding box
    ####################

    ####################
    # TODO: MATERIAL
    #       handle shape material (color, textures, ...)
    ####################


