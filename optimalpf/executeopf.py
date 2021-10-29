import pandapower as pp
from pandapowerTest.optimalpf.opf import Opf


def analyzingresults(opf):
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

def permutethroughcostfunc():

    print("--------------------- Loss Minimization------------------- \n")
    opf = Opf("Loss minimization")
    pp.runopp(opf.net, verbose=True, delta=1e-16)
    analyzingresults(opf)
    print("--------------------- Slack Cheaper------------------------ \n")
    opf = Opf("Slack cheaper")
    pp.runopp(opf.net, verbose=True, delta=1e-16)
    analyzingresults(opf)
    print("--------------------- Slack Minimization------------------- \n")
    opf = Opf("avoid Slack")
    pp.runopp(opf.net, verbose=True, delta=1e-16)
    analyzingresults(opf)

def opfpowermodel():
    #Julia implementation not used
    opf = Opf("Loss minimization")
    pp.runpm_ac_opf(opf.net)


permutethroughcostfunc()
#opfpowermodel()