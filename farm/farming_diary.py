"""
Module: farming_diary
This script simulates a farming diary where different crops (corn and rice) are grown, watered,
and checked for ripeness.
"""

from farm.corn import Corn
from farm.rice import Rice

print("\n\n📝 Day One: Corn")

# 1. Instantiate a corn crop
# YOUR CODE HERE
corn = Corn()
# 2. Water the corn crop
# YOUR CODE HERE
corn.water()
# 3. Print "The corn crop produced ## grains"
# YOUR CODE HERE
print(f"The corn crop produced {corn.grains()}")
# 4. Print "The corn crop is ripe" or "The corn crop is not ripe"
# YOUR CODE HERE
print(f"\nThe corn crop is {corn.ripe()}")

print("\n\n📝 Day Two: Rice")

# 1. Instantiate a rice crop
# YOUR CODE HERE
rice = Rice()
# 2. Water the rice crop
# YOUR CODE HERE
rice.water()
# 3. Transplant the rice crop
# YOUR CODE HERE
rice.transplant()
# 4. Print "The rice crop produced ## grains"
# YOUR CODE HERE
print(f"The corn crop produced {rice.grains()}")
# 5. Print "The rice crop is ripe" or "The rice crop is not ripe"
# YOUR CODE HERE
print(f"\nThe corn crop is {rice.ripe()}")