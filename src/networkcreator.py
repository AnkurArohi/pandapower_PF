import pandapower as pp


class CreateDatamodel:

    def __init__(self, name):
        self.name = name
        # self.createnetwork()

    #
    # # create empty net
    #     def createnetwork(self):
    #         return pp.create_empty_network()

    # create buses
    def createbus(self, netname, voltage, name):
        return pp.create_bus(netname, vn_kv=voltage, name=name)

    # create slack
    def createslack(self, netname, bus, voltagepu, name,min_p_mw, max_p_mw):
        return pp.create_ext_grid(netname, bus=bus, vm_pu=voltagepu, name=name,min_p_mw=-1000, max_p_mw=1000)

    def createload(self, netname, bus, p_mw, q_mvar, name):
        return pp.create_load(netname, bus=bus, p_mw=p_mw, q_mvar=q_mvar, name=name)

    # create branch elements
    def createtrafo(self, netname, bus_hv, bus_lv, std_type, name):
        return pp.create_transformer(netname, hv_bus=bus_hv, lv_bus=bus_lv, std_type=std_type, name=name)

    def createlines(self, netname, from_bus, to_bus, length, std_type, name):
        return pp.create_line(netname, from_bus=from_bus, to_bus=to_bus, length_km=length, std_type=std_type, name=name)

    def createswitches(self, netname, bus, line, closed):
        pp.create_switch(netname, bus, line, et="1",closed=closed)
