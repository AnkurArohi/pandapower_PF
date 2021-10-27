
import pandapower as pp

class Line:
    netname = pp.create_empty_network()
    length=.0
    #max_i_ka=.0
    std_type=""
    linename=""

    def __init__(self, netname, from_bus, to_bus, linename, length,std_type):
        self.netname = netname
        self.from_bus = from_bus
        self.to_bus = to_bus
        self.linename = linename
        self.length = length
        #self.max_i_ka = max_i_ka
        self.std_type= std_type

    def __str__(self):
        return "network:" + self.netname + " linename" + self.linename