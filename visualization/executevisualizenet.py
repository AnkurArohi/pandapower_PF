import pandapower.networks

from pandapowerTest.visualization.src.visualizenet import Visaulize

networks = [pandapower.networks.example_multivoltage(),None]
for network in networks:
    vis=Visaulize("visualize",network)