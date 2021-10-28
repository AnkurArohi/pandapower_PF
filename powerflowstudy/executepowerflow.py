import pandapower.networks

from pandapowerTest.powerflowstudy.powerflow import Run_pf


def executeandpublishresults(networks):
    for key, value in networks.items():
        pf = Run_pf(key, value).execute()
        pf.bus.to_csv("datamodel/bus" + "_" + key + ".csv")
        pf.line.to_csv("datamodel/line" + "_" + key + ".csv")
        pf.trafo.to_csv("datamodel/trafo" + "_" + key + ".csv")
        pf.ext_grid.to_csv("datamodel/slack" + "_" + key + ".csv")
        #
        pf.res_bus.to_csv("output/busVoltages" + "_" + key + ".csv")
        pf.res_line.to_csv("output/line" + "_" + key + ".csv")
        pf.res_trafo.to_csv("output/trafo." + "_" + key + "csv")
        pf.res_ext_grid.to_csv("output/slack" + "_" + key + ".csv")


#
networks = {"example": pandapower.networks.example_simple(), "inbuilt": None}
executeandpublishresults(networks)
