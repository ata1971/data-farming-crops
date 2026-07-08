# corn.py
class Corn:
    # YOUR CODE HERE
    #grains = 0
    def __init__(self):
        self.grains = 0

    def water(self):
        self.grains += 10
      
    def ripe(self):
        return True if self.grains >= 15 else False
