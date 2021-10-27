from pandapowerTest.buildnetwork import BuildNetwork
import pandapower as pp

class Run_pf:
    def __init__(self,name):
        self.name=name
        # pf = BuildNetwork(name).start()
        # print(pf.res_bus)
        # print(pf.bus)
        # print(pf.line)
        # print(pf.trafo)
        # print(pf.load)
        # print(pf.res_line)
        # print(pf.res_trafo)
        # type(net.res_trafo)

    def execute(self):
        net=BuildNetwork(self.name).start()
        pp.runpp(net)
        return net




pf=Run_pf("Test-Network").execute()
print(pf.res_bus)
