import pandapower as pp
from pandapowerTest.optimalpf.src.opf import Opf


class ExecuteOPF:
    def __init__(self,networks,constraint_i,constraint_lb_v,constraint_ub_v,gen_min_p,gen_max_p):
        for key, value in networks.items():
            self.constraint_i=constraint_i
            self.constraint_lb_v=constraint_lb_v
            self.constraint_ub_v=constraint_ub_v
            self.gen_min_p_mw=gen_min_p
            self.gen_max_p_mw=gen_max_p
            self.permutethroughcostfunc(value)



    def analyzingresults(self,opf):
        print("OPF output Slack: \n", opf.net.res_ext_grid)
        print("OPF output Gen: \n", opf.net.res_gen)
        sum_p_gen = 0.0
        sum_p_load = 0.0
        for p in opf.net.res_gen.get("p_mw"):
            sum_p_gen += p
        for p in opf.net.res_ext_grid.get("p_mw"):
            sum_p_gen += p
        print("Total generation: ", sum_p_gen)
        for p in opf.net.res_load.get("p_mw"):
            sum_p_load += p
        print("Total load: ", sum_p_load)
        print("Total OPF cost :", opf.net.res_cost)

        print("#############-- Loading in trafo --########## \n")
        print("After OPF Trafo Loading : ", opf.net.res_trafo.loading_percent)
        print("#############-- Loading in lines --########## \n")
        print("After OPF line loading: \n", opf.net.res_line.loading_percent)

    def permutethroughcostfunc(self,network):

        print("--------------------- Loss Minimization------------------- \n")
        opf = Opf("Loss minimization", network,self.constraint_i,self.constraint_lb_v,self.constraint_ub_v,
                  self.gen_min_p_mw,self.gen_max_p_mw)
        pp.runopp(opf.net, verbose=True, delta=1000,trafo3w_losses='hv')
        #pp.rundcopp(opf.net, verbose=True, delta=1e-6, trafo3w_losses='hv')
        self.analyzingresults(opf)
        print("--------------------- Slack Cheaper------------------------ \n")
        opf = Opf("Slack cheaper",network,self.constraint_i,self.constraint_lb_v,self.constraint_ub_v,
                  self.gen_min_p_mw,self.gen_max_p_mw)
        pp.runopp(opf.net, verbose=True, delta=1e-16)
        #pp.rundcopp(opf.net, verbose=True, delta=1e-6, trafo3w_losses='hv')
        self.analyzingresults(opf)
        print("--------------------- Slack Minimization------------------- \n")
        opf = Opf("avoid Slack",network,self.constraint_i,self.constraint_lb_v,self.constraint_ub_v,
                  self.gen_min_p_mw,self.gen_max_p_mw)
        pp.runopp(opf.net, verbose=True, delta=1e-16)
        #pp.rundcopp(opf.net, verbose=True, delta=1e-6, trafo3w_losses='hv')
        self.analyzingresults(opf)



#opfpowermodel()





def opfpowermodel():
    #Juia Implementation not used yet
    opf = Opf("Loss minimization")
    pp.runpm_ac_opf(opf.net)