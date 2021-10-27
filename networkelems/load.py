
import pandapower as pp


class Load:
    netname = pp.create_empty_network()
    p_mw =.0
    q_mvar=.0
    name=""


    def __init__(self, netname,bus,p_mw,q_mvar,name):
        self.netname = netname
        self.bus = bus
        self.p_mw = p_mw
        self.q_mvar = q_mvar
        self.name = name