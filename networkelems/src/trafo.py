
import pandapower as pp

class Trafo:
    netname = pp.create_empty_network()
    std_type=""
    trafoname=""

    def __init__(self, netname, bus_hv, bus_lv,std_type,trafoname):
        self.netname = netname
        self.bus_hv = bus_hv
        self.bus_lv = bus_lv
        self.trafoname = trafoname
        self.std_type= std_type