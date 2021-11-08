import pandapower.shortcircuit as sc

from pandapowerTest.topology.src.topologicalfeature import Topology


class ShortCircuitCalc(Topology):
    def __init__(self, name,network):
        super().__init__(name,network)
        self.net.ext_grid["s_sc_max_mva"] = 100
        self.net.ext_grid["rx_max"] = 0.1
        sc.calc_sc(self.net, case="max", ip=True, r_fault_ohm=2.)
        var = self.net.res_bus_sc
        print(var)


