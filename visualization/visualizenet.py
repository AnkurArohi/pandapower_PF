import pandapower.plotting as plot
from pandapowerTest.powerflowstudy.powerflow import RunPf


class Visaulize(RunPf):
    def __init__(self,name):
        super().__init__(name,None)
        plot.simple_plot(self.net)


vis=Visaulize("Visualize net")