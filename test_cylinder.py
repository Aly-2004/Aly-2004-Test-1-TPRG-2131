#TPRG 2131 Fall 2024 Test 1
#October 31st, 2024
#Alyousef Soliman 100883692
#This program is strictly my own work. Any material
#beyond course learning materials that is taken from
#the Web or other sources is properly cited, giving
#credit to the original author(s).

#test_cylinder.py
#The purpose for this program is not to produce an output but to use the pytest module

import pytest  #Import the pytest module to enable testing functionalities.

#Import specific functions from the cylinder.py module that we want to test.
from cylinder1 import (
    volume_cylinder,
    area_cylinder
)

def test_volume_cylinder():
    """Test cases for the volume_cylinder function."""
    
    assert volume_cylinder(1, 2) == 1.5708  #Expected volume is around 1.57 (π * ((1/2) ** 2) * 2)
    
    
    assert volume_cylinder(0.1, 4) == 0.031416   # Expected volume is around 0.0314 (π * ((0.1/2) ** 2) * 4)
    
    
    assert volume_cylinder(2, 1) == 3.1416   # Expected volume is around 3.14 (π * ((2/2) ** 2) * 1)
    
def test_area_cylinder():
    """Test cases for the area_cylinder function."""
    
    assert volume_cylinder(1, 2) == 7.8540  #Expected volume is around 7.85 ((2 * π * (1/2) * 2) + (2 * π* (r ** 2)))
    
    
    assert volume_cylinder(0.1, 4) == 1.2723   # Expected volume is around 1.27 ((2 * π * (0.1/2) * 4) + (2 * π* (r ** 2)))
    
    
    assert volume_cylinder(2, 1) == 12.5664   # Expected volume is around 12.56 ((2 * π * (2/2) * 1) + (2 * π* (r ** 2)))
    
