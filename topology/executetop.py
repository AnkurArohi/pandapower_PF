import pandapower.networks
from pandapowerTest.topology.src.topologicalfeature import Topology

networks = {"MV Oberheim": pandapower.networks.mv_oberrhein(), "example": pandapower.networks.example_simple(),
            "inbuilt": None}

for key, value in networks.items():
    # Top cass calls itself(PosConstruct) the other functions
    print("-------------------------- Currently analysing TOPOLOGICAL Features for this network",key)
    top_obj = Topology("first top analysis", value)
    top_obj.checksupply()
    top_obj.create_graph(value)
    top_obj.determinerings()
    if key == "inbuilt":
        top_obj.shortestdistance()
