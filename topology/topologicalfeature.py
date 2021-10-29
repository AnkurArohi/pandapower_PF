import pandapower.topology as top
from pandapowerTest.powerflowstudy.powerflow import RunPf
import networkx as nx


class Topology(RunPf):
    def __init__(self, name):
        super().__init__(name,None)
        self.mg = top.create_nxgraph(self.net, include_trafos=True)
        #self.detailednet = super().buildnetwork()
        #self.net = self.detailednet.net

    def checksupply(self):
        print("Here unsupplied buses", top.unsupplied_buses(self.net))

    def create_graph(self):

        print(self.mg)
        print(self.mg.adjacency())
        for item in self.mg.adjacency():
            print(item)
        # starts the search from bus 2 and outputs connected buses at BUS 3 which is a load bus
        print("Connected buses to load bus BUS 3 including BUS 3(2) \n",
              list(top.connected_component(self.mg, self.bus_ident.get("BUS 3"))))
        print("Distance in km from Load Bus BUS 3 to all buses \n",
              top.calc_distance_to_bus(self.net, self.bus_ident.get("BUS 3")))
        return self.mg

    def shortestdistance(self):
        #wrt length of line if weight para removed counts no. of buses to determine this
        path=nx.shortest_path(self.mg,self.bus_ident.get("BUS 1"),self.bus_ident.get("BUS 4"),weight="weight")
        print(path)
        print(self.net.bus.loc[path])
        print(self.net.line.loc[top.elements_on_path(self.mg, path, "line")])
        print(self.net.trafo.loc[top.elements_on_path(self.mg, path, "trafo")])

    def determinerings(self):
        mg_undirected= top.create_nxgraph(self.net, multi=False)
        print(nx.cycle_basis(mg_undirected))

    def tryingpandasanalysis(self):
        for idx,row in self.net.bus.iterrows():
            print(idx)
            print(row["vn_kv"])

        for ind in self.net.bus.itertuples():
            print(ind)
            print(ind.vn_kv)

        print(self.net.bus["vn_kv"])