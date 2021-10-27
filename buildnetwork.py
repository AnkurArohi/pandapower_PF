import pandapower as pp

from pandapowerTest import networkcreator
from pandapowerTest.networkelems.bus import Bus
from pandapowerTest.networkelems.line import Line
from pandapowerTest.networkelems.load import Load
from pandapowerTest.networkelems.slack import Slack
from pandapowerTest.networkelems.trafo import Trafo



class BuildNetwork:
    def __init__(self,name):
        self.name=name

    def start(self):
        bus_list=[]
        bus_ident = {}
        slacks=[]
        loads=[]
        trafos=[]
        lines=[]

        net=pp.create_empty_network()
        run_pf= networkcreator.RunningPowerF(self.name)
        self.createbusdata(bus_ident, bus_list, net, run_pf)

        #slack/loads/trafos/lines always after bus

        self.createslackdata(bus_ident, net, run_pf, slacks)

        self.createloaddata(bus_ident, loads, net, run_pf)

        self.createlinedata(bus_ident, lines, net, run_pf)

        self.createtrafodata(bus_ident, net, run_pf, trafos)

        return net


    def createtrafodata(self,bus_ident, net, run_pf, trafos):
        trafo1 = Trafo(net, bus_ident.get("BUS 1"), bus_ident.get("BUS 2"), "0.4 MVA 20/0.4 kV", "Trafo")
        trafos.append(trafo1)
        run_pf.createtrafo(trafo1.netname, trafo1.bus_hv, trafo1.bus_lv, trafo1.std_type, trafo1.trafoname)


    def createlinedata(self,bus_ident, lines, net, run_pf):
        line1 = Line(net, bus_ident.get("BUS 2"), bus_ident.get("BUS 3"), "Line", 0.1, "NAYY 4x50 SE")
        lines.append(line1)
        run_pf.createlines(line1.netname, line1.from_bus, line1.to_bus, line1.length, line1.std_type, line1.linename)


    def createloaddata(self,bus_ident, loads, net, run_pf):
        load1 = Load(net, bus_ident.get("BUS 3"), 0.1, 0.05, "Load")
        loads.append(load1)
        run_pf.createload(load1.netname, load1.bus, load1.p_mw, load1.q_mvar, load1.name)


    def createslackdata(self,bus_ident, net, run_pf, slacks):
        slack1 = Slack(net, bus_ident.get("BUS 1"), 1.02, "GridConnnection")
        slacks.append(slack1)
        run_pf.createslack(slack1.netname, slack1.bus, slack1.voltage_pu, slack1.name)


    def createbusdata(self,bus_ident, bus_list, net, run_pf):
        bus1 = Bus(net, 20., "BUS 1", True, 1.20, 0.80)
        bus_list.append(bus1)
        bus2 = Bus(net, 0.4, "BUS 2", True, 1.20, 0.8)
        bus_list.append(bus2)
        bus3 = Bus(net, 0.4, "BUS 3", True, 1.2, 0.8)
        bus_list.append(bus3)
        for bus in bus_list:
            bus_str = bus.busname
            bus_ident[bus_str] = run_pf.createbus(bus.net, bus.vn, bus.busname)
        return bus_ident


