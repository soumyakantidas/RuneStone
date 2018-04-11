
class LogicGate(object):

    def __init__(self, label):
        self.label = label
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        print("Output of " + self.get_label() + " : " + str(self.output))
        return self.output

    def perform_gate_logic(self):
        pass

    def set_next_pin(self, source):
        pass


class BinaryGate(LogicGate):

    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pinA, self.pinB = None, None

    def get_pinA(self):
        if self.pinA is None:
            return int(input("Enter pin A for gate " + self.get_label() + ":  "))
        else:
            return self.pinA.get_output()

    def get_pinB(self):
        if self.pinB is None:
            return int(input("Enter pin B for gate " + self.get_label() + ":  "))
        else:
            return self.pinB.get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError("No Empty Pins")


class UnaryGate(LogicGate):
    def __init__(self, label):
        LogicGate.__init__(self, label)
        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter pin for gate " + self.get_label() + ":  "))
        else:
            return self.pin.get_output()

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError("No Empty Pin")


class AND(BinaryGate):

    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()

        return a and b


class OR(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)

    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        print("PinA of " + self.get_label() + " : " + str(a))
        print("PinB of " + self.get_label() + " : " + str(b))

        return a or b


class NOT(UnaryGate):
    def __init__(self, label):
        UnaryGate.__init__(self, label)

    def perform_gate_logic(self):
        pin = self.get_pin()
        print("Pin of " + self.get_label() + " : " + str(pin))
        return 0 if pin == 1 else 1


class NAND(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)
        self.and_gate = AND("NAND-INTERNAL-AND")
        self.not_gate = NOT("NAND-INTERNAL-NOT")
        self.connector = Connector(self.and_gate, self.not_gate)

    def perform_gate_logic(self):
        return self.not_gate.get_output()


class NOR(BinaryGate):
    def __init__(self, label):
        BinaryGate.__init__(self, label)
        self.or_gate = OR("NOR-INTERNAL-OR")
        self.not_gate = NOT("NOR-INTERNAL-NOT")
        self.connector = Connector(self.or_gate, self.not_gate)

    def perform_gate_logic(self):
        return self.not_gate.get_output()


class Connector:

    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate
        tgate.set_next_pin(self.fgate)

    def get_fgate(self):
        return self.fgate

    def get_tgate(self):
        return self.tgate
