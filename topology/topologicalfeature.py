import pandapower.topology as top
from pandapowerTest.powerflowstudy.powerflow import RunPf


class Topology(RunPf):
    def __init__(self, name):
        super().__init__(name,None)
        #self.detailednet = super().buildnetwork()
        #self.net = self.detailednet.net

    def checksupply(self):
        print("Here unsupplied buses", top.unsupplied_buses(self.net))

    def create_graph(self):
        mg = top.create_nxgraph(self.net, include_trafos=False)
        print(mg)
        print(mg.adjacency())
        for item in mg.adjacency():
            print(item)
        # starts the search from bus 2 and outputs connected buses at BUS 3 which is a load bus
        print("Connected buses to load bus BUS 3 including BUS 3(2) \n",
              list(top.connected_component(mg, self.bus_ident.get("BUS 3"))))
        print("Distance in km from Load Bus BUS 3 to all buses \n",
              top.calc_distance_to_bus(self.net, self.bus_ident.get("BUS 3")))



