
class Rice():
    # YOUR CODE HERE
    def __init__(self):
        self.grains = 0
    
    def water(self):
        self.grains += 5
          
    def ripe(self):
        return True if self.grains >= 15 else False
    
    def transplant(self):
        self.grains += 10