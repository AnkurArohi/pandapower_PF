import pandapower as pp
from pandapowerTest.powerflowstudy.powerflow import RunPf


class UpdateValues(RunPf):
    def __init__(self, name):
        super().__init__(name,None)
        self.detailednet=super().buildnetwork()
        self.net=self.detailednet.net
        self.lines_ident=self.detailednet.lines_ident
        self.bus_ident=self.detailednet.bus_ident

        #print(self.net.line)
    #net=runpowerflow.Run_pf("Test-Network",net=None).buildnetwork()
    def trafotap(self):
        iterativetap={}

        print("original position=",self.net.trafo.tap_pos.at[pp.get_element_index(self.net, "trafo", "Trafo")])
        for i in range(-5,5):
            self.net.trafo.tap_pos.at[pp.get_element_index(self.net, "trafo", "Trafo")]=i
            pf=pp.runpp(self.net)
            iterativetap[i]=self.net.res_bus
            print(iterativetap)

    def switch(self):
        print(self.bus_ident)
        print(self.lines_ident)
        pp.create_switch(self.net,bus=self.bus_ident["BUS 2"], element=self.lines_ident["Line"],et="1",
                         closed=False)
        pp.runpp(self.net)
        print(self.net.res_bus)

UpdateValues("First modification").trafotap()
#UpdateValues("First modification").switch()