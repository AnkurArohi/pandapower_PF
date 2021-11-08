import pandapower.networks
from pandapowerTest.powerflowstudy.src.powerflow import RunPf


def executeandpublishresults(networks):
    for key, value in networks.items():
        pf = RunPf(key, value).execute()
        pf.bus.to_csv("datamodel/bus" + "_" + key + ".csv")
        pf.line.to_csv("datamodel/line" + "_" + key + ".csv")
        pf.trafo.to_csv("datamodel/trafo" + "_" + key + ".csv")
        pf.ext_grid.to_csv("datamodel/slack" + "_" + key + ".csv")
        pf.gen.to_csv("output/gen" + "_" + key + ".csv")
        pf.load.to_csv("datamodel/load" + "_" + key + ".csv")
        #
        pf.res_bus.to_csv("output/busVoltages" + "_" + key + ".csv")
        pf.res_line.to_csv("output/line" + "_" + key + ".csv")
        pf.res_trafo.to_csv("output/trafo." + "_" + key + "csv")
        pf.res_ext_grid.to_csv("output/slack" + "_" + key + ".csv")
        pf.res_gen.to_csv("output/gen" + "_" + key + ".csv")
        pf.res_load.to_csv("output/load" + "_" + key + ".csv")


#
networks = {"MV Oberheim": pandapower.networks.mv_oberrhein(), "example": pandapower.networks.example_simple(),
            "inbuilt": None}
executeandpublishresults(networks)
