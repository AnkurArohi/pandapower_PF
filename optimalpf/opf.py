from pandapowerTest.topology.topologicalfeature import Topology
import pandapower as pp

class Opf(Topology):
    def __init__(self, name):
        super().__init__(name)
        pp.runpp(self.net,init="auto")
        print("Before OPF Slack : ",self.net.res_ext_grid)
        print("Before OPF Gen : ",self.net.res_gen)
        print("Before OPF Load : ", self.net.res_load)

        self.costfunc()

    def costfunc(self):
        costeg = pp.create_poly_cost(self.net, 0, 'ext_grid', cp1_eur_per_mw=10)
        costgen1 = pp.create_poly_cost(self.net, 0, 'gen', cp1_eur_per_mw=10)
        costgen2 = pp.create_poly_cost(self.net, 1, 'gen', cp1_eur_per_mw=10)

