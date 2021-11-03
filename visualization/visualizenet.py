import pandapower.plotting as plot
import pandapower.networks
from pandapowerTest.powerflowstudy.powerflow import RunPf


class Visaulize(RunPf):
    def __init__(self,name,networkname):
        #for network in networks:
        super().__init__(name,networkname)
        plot.simple_plot(self.net)


networks = [pandapower.networks.example_multivoltage(),None]
for network in networks:
    vis=Visaulize("visualize",network)