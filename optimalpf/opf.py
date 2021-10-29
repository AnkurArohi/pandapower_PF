from pandapowerTest.topology.topologicalfeature import Topology
import pandapower as pp


class Opf(Topology):
    def __init__(self, name):
        super().__init__(name)
        pp.runpp(self.net, init="auto")
        print("Before OPF Slack : ", self.net.res_ext_grid)
        print("Before OPF Gen : ", self.net.res_gen)
        print("Before OPF Load : ", self.net.res_load)
        print("Before OPF Trafo Loading : \n", self.net.res_trafo.loading_percent)
        print("Before OPF line loading: \n",self.net.res_line.loading_percent)
        self.costfunc(name)
        self.modifyconstraints(80, 80)

    def costfunc(self, name):
        if (name == "Loss minimization"):
            costeg = pp.create_poly_cost(self.net, 0, 'ext_grid', cp1_eur_per_mw=10)
            costgen1 = pp.create_poly_cost(self.net, 0, 'gen', cp1_eur_per_mw=10)
            costgen2 = pp.create_poly_cost(self.net, 1, 'gen', cp1_eur_per_mw=10)
        elif (name == "Slack cheaper"):
            costeg = pp.create_poly_cost(self.net, 0, 'ext_grid', cp1_eur_per_mw=1)
            costgen1 = pp.create_poly_cost(self.net, 0, 'gen', cp1_eur_per_mw=10)
            costgen2 = pp.create_poly_cost(self.net, 1, 'gen', cp1_eur_per_mw=10)
        elif (name == "avoid Slack"):
            costeg = pp.create_poly_cost(self.net, 0, 'ext_grid', cp1_eur_per_mw=10, cp2_eur_per_mw2=1)
            costgen1 = pp.create_poly_cost(self.net, 0, 'gen', cp1_eur_per_mw=1)
            costgen2 = pp.create_poly_cost(self.net, 1, 'gen', cp1_eur_per_mw=1)
        else:
            print("Select a optimizing cost poly type")

    def modifyconstraints(self, trafo, line):
        self.net.trafo["max_loading_percent"] = trafo
        self.net.line["max_loading_percent"] = line
