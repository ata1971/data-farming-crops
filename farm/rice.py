from farm.crop import Crop

class Rice(Crop):
    # YOUR CODE HERE
    def water(self):
        self.grains += 5
  
    def transplant(self):
        self.grains += 10