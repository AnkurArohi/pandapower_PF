from pandapowerTest.topology.src.topologicalfeature import Topology
import pandapower as pp


class Opf(Topology):
    def __init__(self, name, network, constraint_i, constraint_lb_v, constraint_ub_v,gen_p_min, gen_p_max):
        super().__init__(name, network)
        #pp.runpp(self.net, calculate_voltage_angles=True, init="auto")
        print("Before OPF Slack : ", self.net.res_ext_grid)
        print("Before OPF Gen : ", self.net.res_gen)
        print("Before OPF Load : ", self.net.res_load)
        print("Before OPF Trafo Loading : \n", self.net.res_trafo.loading_percent)
        print("Before OPF line loading: \n", self.net.res_line.loading_percent)
        self.costfunc(name)
        self.modifypara(gen_p_min,gen_p_max)
        self.modifyconstraints(constraint_i, constraint_lb_v, constraint_ub_v)

    def costfunc(self, name):
        if (name == "Loss minimization"):
            print("In Loss Minimization cost poly")
            costeg = pp.create_poly_cost(self.net, 0, 'ext_grid', cp1_eur_per_mw=1)
            costgen1 = pp.create_poly_cost(self.net, 0, 'gen', cp1_eur_per_mw=1)
            costgen2 = pp.create_poly_cost(self.net, 1, 'gen', cp1_eur_per_mw=1)
            costgen3 = pp.create_poly_cost(self.net, 2, 'gen', cp1_eur_per_mw=1)
            costgen4 = pp.create_poly_cost(self.net, 3, 'gen', cp1_eur_per_mw=1)
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

    def modifyconstraints(self, constraint_i, constraint_lb_v, constraint_ub_v):
        self.net.trafo["max_loading_percent"] = constraint_i
        self.net.line["max_loading_percent"] = constraint_i
        self.net.bus.max_vm_pu = constraint_ub_v
        self.net.bus.min_vm_pu = constraint_lb_v

    def modifypara(self,gen_p_min,gen_p_max):
        self.net.gen["min_p_mw"]=gen_p_min
        self.net.gen["max_p_mw"]=gen_p_max
        self.net.gen["controllable"]=True
        self.net.sgen['min_p_mw']=-1000
        self.net.sgen['max_p_mw'] = 1000
        self.net.sgen['min_q_mvar'] = -1000
        self.net.sgen['max_q_mvar'] = 1000
        self.net.sgen["controllable"]=True
        self.net.load['min_p_mw']=-1000
        self.net.load['max_p_mw'] = 1000
        self.net.load['min_q_mvar'] = -1000
        self.net.load['max_q_mvar'] = 1000
        self.net.load["controllable"]=True
