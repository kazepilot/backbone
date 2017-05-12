import cv2
import numpy as np
import math
#import requests
#import json
import time

class Neuron(object):

    def __init__(self, weights):
        splitted = weights.replace('\n', '').split(' ')
        self.weights = [float(x) for x in splitted]

    def forward(self, x):
        if len(self.weights) != len(x):
            raise Exception('neuron weights with input does not match')
        add = 0.0
        for i in range(0, len(x)):
            add += self.weights[i] * x[i]

        return max(0.0, add)

class Network(object):

    def __init__(self, filename):
        self.neurons = []

        with open(filename, 'r') as f:
            lines = f.readlines()

            for line in lines:
                self.neurons.append(Neuron(line))

    def move(self, distances):
        results = []

        distances.append(1.0)
        max_val = 0.0
        index = 0

        for idx, neuron in enumerate(self.neurons):
            result = math.exp(neuron.forward(distances))
            if result > max_val:
                max_val = result
                index = idx

        return index

<<<<<<< HEAD
=======
class Detection(object):
    
    def __init__(self, json_data, height, width):
        self.left = int(json_data['left'] * height)
        self.right = int(json_data['right'] * height)
        self.top = int(json_data['top'] * width)
        self.bottom = int(json_data['bottom'] * width)
        self.name = json_data['name']

    def topD(self):
        return (self.top, self.left)

    def bottomD(self):
        return (self.bottom, self.right)
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da

def main():
    from robot import Robot
    network = Network('data.weights')
    robot = Robot()

    while 'pigs' != 'fly':
        distances = robot.distance()
        if distances[0] > 0.95 and distances[1] > 0.95 and distances[2] > 0.95:
	    continue
        print distances	
	move = network.move(distances)
        print move	
	if move is 0:
            robot.left()
            #robot.left()
        elif move is 1:
            robot.right()
            #robot.right()
        else:
            robot.forward()

    robot.close()


<<<<<<< HEAD

=======
>>>>>>> b0179825d8e79cf846283a781dc08070ff4450da
if __name__ == '__main__':
    main()
