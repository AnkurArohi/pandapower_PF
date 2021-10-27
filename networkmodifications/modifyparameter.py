import pandapower as pp
from pandapowerTest import runpowerflow
from pandapowerTest.runpowerflow import Run_pf


class UpdateValues(Run_pf):

    #net=runpowerflow.Run_pf("Test-Network",net=None).buildnetwork()
    def trafotap(self):
        iterativetap={}
        net=super().buildnetwork()
        print("original position=",net.trafo.tap_pos.at[pp.get_element_index(net, "trafo", "Trafo")])
        for i in range(-5,5):
            net.trafo.tap_pos.at[pp.get_element_index(net, "trafo", "Trafo")]=i
            pf=pp.runpp(net)
            iterativetap[i]=net.res_bus
            print(iterativetap)


UpdateValues("First modification").trafotap()