import pandapower as pp

from pandapowerTest import networkcreator
from pandapowerTest.networkelems.bus import Bus
from pandapowerTest.networkelems.line import Line
from pandapowerTest.networkelems.load import Load
from pandapowerTest.networkelems.slack import Slack
from pandapowerTest.networkelems.trafo import Trafo


class BuildNetwork:
    def __init__(self, name, net):
        self.name = name
        self.net = net
        self.bus_list = []
        self.bus_ident = {}
        self.slacks = []
        self.slack_ident = {}
        self.loads = []
        self.loads_ident = {}
        self.trafos = []
        self.trafos_ident = {}
        self.lines = []
        self.lines_ident = {}
        self.state = True

    def start(self):
        if self.net is None:
            self.net = pp.create_empty_network()

            run_pf = networkcreator.CreateDatamodel(self.name)
            self.createbusdata(self.bus_ident, self.bus_list, self.net, run_pf)

            # slack/loads/trafos/lines always after bus

            self.createslackdata(self.bus_ident, self.net, run_pf, self.slacks, self.slack_ident)

            self.createloaddata(self.bus_ident, self.loads, self.net, run_pf, self.loads_ident)

            self.createlinedata(self.bus_ident, self.lines, self.net, run_pf, self.lines_ident)

            self.createtrafodata(self.bus_ident, self.net, run_pf, self.trafos, self.trafos_ident)
            ##Generators defined for OPF
            g0 = pp.create_gen(self.net, self.bus_ident["BUS 4"], p_mw=10, min_p_mw=0, max_p_mw=80, vm_pu=1.01,
                               controllable=True, cos_phi=0.93, vn_kv=110, sn_mva=5, xdss_pu=0.2, rdss_ohm=5)
            g1 = pp.create_gen(self.net, self.bus_ident["BUS 5"], p_mw=10, vm_pu=1.01, sn_mva=5,min_p_mw=0, max_p_mw=80,
                               controllable=True,  vn_kv=110, xdss_pu=0.2,rdss_ohm=5,cos_phi=0.93)
        else:
            print("Example network is provided datamodel is not built")
        # switch after bus and line

        # self.createswitch(self.net,self.bus_ident,self.lines_ident,self.state,run_pf)

        return self

    def createtrafodata(self, bus_ident, net, run_pf, trafos, trafos_ident=None):
        #trafo1 = Trafo(net, bus_ident.get("BUS 1"), bus_ident.get("BUS 2"), "0.4 MVA 20/0.4 kV", "Trafo")
        trafo1 = Trafo(net, bus_ident.get("BUS 1"), bus_ident.get("BUS 2"), "100 MVA 220/110 kV", "Trafo")
        ######more trafos here append them below
        trafos.append(trafo1)
        for trafo in trafos:
            trafo_str = trafo.trafoname
            trafos_ident[trafo_str] = run_pf.createtrafo(trafo.netname, trafo.bus_hv, trafo.bus_lv, trafo.std_type,
                                                         trafo.trafoname)

    def createlinedata(self, bus_ident, lines, net, run_pf, lines_ident):
        line1 = Line(net, bus_ident.get("BUS 2"), bus_ident.get("BUS 3"), "Line", 1, "149-AL1/24-ST1A 110.0")
        lines.append(line1)
        line2 = Line(net, bus_ident.get("BUS 3"), bus_ident.get("BUS 4"), "Line 2", 1,  "149-AL1/24-ST1A 110.0")
        lines.append(line2)
        line3 = Line(net, bus_ident.get("BUS 3"), bus_ident.get("BUS 5"), "Line 3", 5,  "149-AL1/24-ST1A 110.0")
        lines.append(line3)
        line4 = Line(net, bus_ident.get("BUS 4"), bus_ident.get("BUS 5"), "Line 4", 1,  "149-AL1/24-ST1A 110.0")
        lines.append(line4)
        for line in lines:
            line_str = line.linename
            lines_ident[line_str] = run_pf.createlines(line.netname, line.from_bus, line.to_bus, line.length,
                                                       line.std_type, line.linename)

    def createloaddata(self, bus_ident, loads, net, run_pf, loads_ident):
        load1 = Load(net, bus_ident.get("BUS 3"), 50, 0.05, "Load")
        loads.append(load1)
        load2 = Load(net, bus_ident.get("BUS 4"), 10, 5, "Load 2")
        loads.append(load2)
        load3 = Load(net, bus_ident.get("BUS 5"), 70, 5, "Load 2")
        loads.append(load3)
        for load in loads:
            run_pf.createload(load.netname, load.bus, load.p_mw, load.q_mvar, load.name)

    def createslackdata(self, bus_ident, net, run_pf, slacks, slacks_ident):
        slack1 = Slack(net, bus_ident.get("BUS 1"), 1.02, "GridConnnection")
        slacks.append(slack1)
        run_pf.createslack(slack1.netname, slack1.bus, slack1.voltage_pu, slack1.name,-1000,1000)

    def createbusdata(self, bus_ident, bus_list, net, run_pf):
        bus1 = Bus(net, 220., "BUS 1", True, 1.20, 0.80)
        bus_list.append(bus1)
        bus2 = Bus(net, 110., "BUS 2", True, 1.20, 0.8)
        bus_list.append(bus2)
        bus3 = Bus(net, 110., "BUS 3", True, 1.2, 0.8)
        bus_list.append(bus3)
        bus4 = Bus(net, 110.,"BUS 4",True,1.20,0.80)
        bus_list.append(bus4)
        bus5 = Bus(net, 110.,"BUS 5",True,1.20,0.80)
        bus_list.append(bus5)

        for bus in bus_list:
            bus_str = bus.busname
            bus_ident[bus_str] = run_pf.createbus(bus.net, bus.vn, bus.busname)
        return bus_ident

    def createswitch(self, net, bus_ident, lines_ident, state, run_pf):
        run_pf.createswitches(net, bus_ident.get("BUS 3"), lines_ident.get("Line"), state)
