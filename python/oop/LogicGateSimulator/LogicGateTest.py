from python.oop.LogicGateSimulator.LogicGate import AND
from python.oop.LogicGateSimulator.LogicGate import OR
from python.oop.LogicGateSimulator.LogicGate import NOT

g1 = AND("AND-1")
print(g1.get_output())

g2 = OR("OR-1")
print(g2.get_output())

g3 = NOT("NOT-1")
print(g3.get_output())