""" resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 2024 Test 1
By Alyousef Soliman 100883692
This program is strictly my own work. Any material
beyond course learning materials that is taken from
the Web or other sources is properly cited, giving
credit to the original author(s).
"""
class Resistor(object):
    """Model a fixed resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res

    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)


### DEFINE class VariableResistor HERE ###
#I couldn't figure out how to make the self.actual_resistance work without errors
class VariableResistor(Resistor):
    def __init__1(self, res):
        self.resistance = res
    
    def set_resistance(self, percent):
        return percent
        
    def current(self, voltage):
        return voltage / self.resistance 
    
    def __str__(self):
        return "R=" + str(self.resistance)

if __name__ == "__main__":
    r1 = Resistor(1000.0)
    print("R1:", r1)
    print("R1: voltage=12.0, current=", r1.current(12.0))

    ## UNCOMMENT THIS BLOCK TO TEST VariableResistor
    r2 = VariableResistor(1000.0)
    print("R2:", r2)
    print("R2 100%: voltage=12.0, current=", r2.current(12.0))
    r2.set_resistance(50.0)
    print("R2 50%: voltage=12.0, current=", r2.current(12.0))
