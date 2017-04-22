import cv2
import numpy as np
import requests
from robot import Robot
from network import Network
from detection import Detection
from config import Config
import json
from Queue import Queue


class Backbone(object):

    def __init__(self, network_weights, config_file):
        self.robot = Robot()
        self.network = Network(network_weights)
        self.config = Config(config_file)

        self.moves_stack = Queue()
        self.conditions = self.config.get_standard_conditions()
        self.additional_conditions = []

    def move(self, frame):
        detections = self.get_detections(frame)
        move = 3

        if self.moves_stack.empty():
            self.moves_stack, self.additional_conditions = self.get_moves(
                detections)

        pass_conditions = self.can_move(self.conditions, detections)
        pass_add_conditions = self.can_move(
            self.additional_conditions, detections)

        if not pass_conditions or not pass_add_conditions:
            return False

        if not self.moves_stack.empty():
            move = self.moves_stack.get()

        else:
            distances = self.robot.distance()
            move = self.network.move(distances)

        if move is 0:
            self.robot.left()
        elif move is 1:
            self.robot.right()
        elif move is 2:
            self.robot.forward()

        return True

    def get_detections(self, frame):
        encoded = cv2.imencode('.jpg', frame)[1].tostring()
        results = requests.post(
            "http://192.168.1.101:1234/cyclops", data=encoded)
        height, width = frame.shape[:2]
        data = json.loads(results.content)
        detections = []
        zones = self.config.zones()

        for detection in data['objects']:
            det = Detection(detection, height, width, zones)
            det.active = self.config.is_active(det.name)
            detections.append(det)

    def get_moves(self, detections):
        sign = max(detections, key=lambda x: x.area())
        moves = self.config.get_moves(sign.name)
        conditiions = self.config.get_conditions(sign.name)

        return moves, conditiions

    def can_move(self, conditions, detections):
        for condition in conditions:
            for detection in detections:
                if detection.active:
                    if detection.zone == condition:
                        return False

        return True

    def close(self):
        self.robot.close()


def main():
    backbone = Backbone('data.weights', 'config.json')
    cap = cv2.VideoCapture(0)
    while 'pigs' != 'fly':
        ret, frame = cap.read()
        backbone.move(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()
