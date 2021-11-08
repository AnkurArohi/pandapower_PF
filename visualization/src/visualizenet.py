import pandapower.plotting as plot
from pandapowerTest.powerflowstudy.src.powerflow import RunPf


class Visaulize(RunPf):
    def __init__(self,name,networkname):
        #for network in networks:
        super().__init__(name,networkname)
        plot.simple_plot(self.net)


