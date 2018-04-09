
class LogicGate(object):

    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA, self.pinB = None, None

    def get_pinA(self):
        return int(input("Enter pin A for gate " + self.get_label() + ":  "))

    def get_pinB(self):
        return int(input("Enter pin B for gate " + self.get_label() + ":  "))


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def get_pin(self):
        return int(input("Enter pin for gate " + self.get_label() + ":  "))


class AND(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()

        return a and b
