from pandapowerTest.buildnetwork import BuildNetwork
import pandapower as pp
import os


def createoutputfolder():
    path = 'output'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)


def datamodelfolder():
    path = 'datamodel'
    # Check whether the specified path exists or not
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)


class Run_pf(object):
    def __init__(self, name, net=None):
        self.name = name
        self.buildnet = BuildNetwork(self.name).start()
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

        pp.runpp(self.net)
        print(self.net)
        pp.diagnostic(self.net, report_style="compact", warnings_only=True)
        self.traversedm()
        createoutputfolder()
        datamodelfolder()
        return self.net

    def traversedm(self):
        print("get_element_index for line  ", pp.get_element_index(self.net, "line", "Line"))
        print("get_element_index for bus  ", pp.get_element_index(self.net, "bus", "BUS 3"))





def executeandpublishresults():
    pf = Run_pf("Test-Network", net=None).execute()
    pf.bus.to_csv("datamodel/bus.csv")
    pf.line.to_csv("datamodel/line.csv")
    pf.trafo.to_csv("datamodel/trafo.csv")
    pf.ext_grid.to_csv("datamodel/slack.csv")
    #
    pf.res_bus.to_csv("output/busVoltages.csv")
    pf.res_line.to_csv("output/line.csv")
    pf.res_trafo.to_csv("output/trafo.csv")
    pf.res_ext_grid.to_csv("output/slack.csv")


#
#executeandpublishresults()
