from pandapowerTest.buildnetwork import BuildNetwork
import pandapower as pp
import os


##Definition of powerflow call method
#Bus type :- Flat start = PV(angle =0°, V=provided covert to pu)
#Flat start = PQ(angle =0°, V=1pu)
#Flat start = UDEL/REF/Slack(angle =0°, V=provided convert to p.u (if not provided take 1 pu))
#DC->before AC do DC power flow -> calculates angles at PQ,PV,REF , voltage magnitudes are flat started(as above)
#########################################################################
#pandapower
# “auto” - init defaults to “dc” if calculate_voltage_angles is True or “flat” otherwise
#
# “flat”- flat start with voltage of 1.0pu and angle of 0° at all PQ-buses and 0° for PV buses as initial solution, the
# slack bus is initialized with the values provided in net[“ext_grid”]
#
# “dc” - initial DC loadflow before the AC loadflow. The results of the DC loadflow are used as initial solution for
#     the AC loadflow. Note that the DC loadflow only calculates voltage angles at PQ and PV buses, voltage magnitudes are still flat started.
#
# “results” - voltage vector of last loadflow from net.res_bus is used as initial solution.
# This can be useful to accelerate convergence in iterative loadflows like time series calculations.
# Considering the voltage angles might lead to non-convergence of the power flow in flat start.
# That is why in “auto” mode, init defaults to “dc” if calculate_voltage_angles is True or “flat” otherwise
# ##


def createoutputfolder():
    path= 'output'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)


def datamodelfolder():
    path_dm= 'datamodel'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path_dm)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path_dm)
    return path_dm

class RunPf(object):
    def __init__(self, name, net):
        self.name = name
        self.net = net
        self.buildnet = BuildNetwork(self.name, self.net).start()
        self.net = self.buildnet.net
        self.lines_ident = self.buildnet.lines_ident
        self.bus_ident = self.buildnet.bus_ident
        # pf = BuildNetwork(name).start()
        # print(pf.res_bus)
        # print(pf.bus)
        # print(self.net.line)
        # print(pf.trafo)
        # print(pf.load)
        # print(pf.res_line)
        # print(pf.res_trafo)
        # type(net.res_trafo)

    def buildnetwork(self):
        return self

    def execute(self):
        pp.runpp(self.net,calculate_voltage_angles=True , init="auto")
        #pp.runpp(self.net)
        print(self.net)
        pp.diagnostic(self.net, report_style="compact", warnings_only=True)
        # use only while debugging
        # self.traversedm()
        createoutputfolder()
        path_dm=datamodelfolder()
        #pp.to_excel(self.net, path_dm+self.name+".xlsx")
        return self.net

    def traversedm(self):
        print("get_element_index for line  ", pp.get_element_index(self.net, "line", "Line"))
        print("get_element_index for bus  ", pp.get_element_index(self.net, "bus", "BUS 3"))


