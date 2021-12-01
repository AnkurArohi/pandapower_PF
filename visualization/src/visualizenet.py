import pandapower.plotting as plot
from pandapowerTest.powerflowstudy.src.powerflow import RunPf
from pandapower.plotting.plotly import pf_res_plotly
from pandapower.plotting.plotly import simple_plotly

class Visaulize(RunPf):
    def __init__(self,name,networkname):
        #for network in networks:
        super().__init__(name,networkname)
        plot.simple_plot(self.net)
        pf_res_plotly(self.net)
        #simple_plotly(self.net,on_map=True)

