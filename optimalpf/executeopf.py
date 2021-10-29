import pandapower as pp
from pandapowerTest.optimalpf.opf import Opf


opf=Opf("Loss minimization")
pp.runopp(opf.net, delta=1e-16)

print("OPF output Slack: \n",opf.net.res_ext_grid)
print("OPF output Gen: \n",opf.net.res_gen)

sum_p_gen=0.0
sum_p_load=0.0
for p in opf.net.res_gen.get("p_mw"):
    sum_p_gen += p
for p in opf.net.res_ext_grid.get("p_mw"):
    sum_p_gen += p

print("Total generation: ",sum_p_gen)

for p in opf.net.res_load.get("p_mw"):
    sum_p_load += p

print("Total load: ",sum_p_load)