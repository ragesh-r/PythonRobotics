import pygame
import math
import numpy as np






def add_noise(distance, angle, sigma):
    mean = np.array([distance, angle])
    covariance = np.diag(sigma**2)
    distance, angle = np.random.multivariate_normal(mean, covariance)
    distance = max(0, distance)
    angle = max(0,angle)
    return [distance, angle]








class LaserSensor2D:
    def __init__(self, Range, map, noise):
        self.Range = Range
        self.speed = 4 #rounds per sec
        self.sigma = np.array([noise[0], noise[1]])
        self.position = (0, 0)
        self.map = map
        self.width, self.height = pygame.display.get_surface().get_size()
        self.sensedObstacles = []

    def euclideanDistance(self, obstaclePosition):
        return math.sqrt((obstaclePosition[0]-self.position[0])**2+(obstaclePosition[1]-self.position[1])**2)


    def sense_Obstacles(self):
        data = []
        x1, y1 =self.position[0], self.position[1]
        for angle in np.linspace(0, 2*np.pi, 60, False):
            x2, y2 = (x1 + self.Range * math.cos(angle), y1 - self.Range * math.sin(angle))

            for i in range(0, 100):
                u = i/100
                x = int(x2 * u + x1 * (1 - u))
                y = int(y2 * u + y1 * (1 - u))
                if 0<x<self.width and 0<y<self.height:
                    color = self.map.get_at((x, y))
                    if (color[0], color[1], color[2]) == (0, 0, 0):
                        distance = self.euclideanDistance((x, y))
                        output = add_noise(distance, angle, self.sigma)
                        output.append(self.position)
                        data.append(output)
                        break
        if len(data)>0:
            return data
        else:
            return False






()






