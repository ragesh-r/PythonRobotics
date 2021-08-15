import math
import pygame

class buildEnvironment():
    def __init__(self,mapDimensions):
        pygame.init()
        self.pointcloud = []
        self.externalMap = pygame.image.load('Floorplan.png')
        self.mapHeight, self.mapWidth = mapDimensions
        self.mapWindowName = 'RRT Planning'
        pygame.display.set_caption(self.mapWindowName)
        self.map = pygame.display.set_mode((self.mapHeight, self.mapWidth))
        self.map.blit(self.externalMap,(0, 0))
        #colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.grey = (70, 70, 70)



    def polar2cartesian(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = -distance * math.sin(angle) + robotPosition[1]
        return (int(x), int(y))

    def dataStorage(self, data):
        print(len(self.pointcloud))
        for element in data:
            point = self.polar2cartesian(element[0] , element[1] , element[2])
            if point not in self.pointcloud:
                self.pointcloud.append(point)

    def show_sensorData(self):
       self.infomap = self.map.copy()
       for point in self.pointcloud:
           self.infomap.set_at((int(point[0]), int(point[1])), self.red)
