from python.oop.LogicGateSimulator.LogicGate import AND
from python.oop.LogicGateSimulator.LogicGate import OR
from python.oop.LogicGateSimulator.LogicGate import NOT
from python.oop.LogicGateSimulator.LogicGate import Connector

g1 = AND("AND-1")
g2 = AND("AND-2")
g3 = OR("OR-1")
g4 = NOT("NOT-1")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

print(g4.get_output())
