from pandapowerTest.topology.topologicalfeature import Topology

top_obj = Topology("first top analysis")
top_obj.checksupply()
top_obj.create_graph()
top_obj.shortestdistance()
top_obj.determinerings()

top_obj.tryingpandasanalysis()
