
import pandapower as pp

class Slack:
    netname = pp.create_empty_network()

    voltage_pu=.0
    name=""


    def __init__(self, netname,bus,v_pu,name):
        self.netname = netname
        self.bus = bus
        self.voltage_pu = v_pu
        self.name = name