from pandapowerTest.shortcircuit.src.executeSC import ShortCircuitCalc
import pandapower.networks

networks = {"inbuilt": None}

for key, value in networks.items():
    # Top cass calls itself(PosConstruct) the other functions
    print("-------------------------- Currently analysing SHORT CIRCUIT CALCULATIONS for this network",key)
    ShortCircuitCalc(key,value)
