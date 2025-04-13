import random

class ReplayBuffer:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.buffer = []

    def add(self, image_path, comment):
        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)
        self.buffer.append((image_path, comment))

    def sample(self, batch_size=4):
        return random.sample(self.buffer, min(len(self.buffer), batch_size))

    def get_all(self):
        return self.buffer
