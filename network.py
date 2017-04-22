import cv2
import numpy as np
import math
import requests
import json
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
