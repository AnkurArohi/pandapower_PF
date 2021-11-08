import pandapower as pp


class Bus:
    net = pp.create_empty_network()
    vn = .0
    busname = ""
    in_service = True
    # opf required paras
    max_vm_pu = .0
    min_vm_pu = .0
    #busid

    def __init__(self, net, vn, busname, in_service, max_vm_pu, min_vm_pu):
        self.net = net
        self.vn = vn
        self.busname = busname
        self.in_service = in_service
        self.max_vm_pu = max_vm_pu
        self.min_vm_pu = min_vm_pu


    def __str__(self):
        return "network:" + self.net + " voltage nominal" + self.vn + self.busname
