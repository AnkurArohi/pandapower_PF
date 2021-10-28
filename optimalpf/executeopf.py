import pandapower as pp
from pandapowerTest.optimalpf.opf import Opf


opf=Opf("Loss minimization")
pp.runopp(opf.net, delta=1e-16)

print(opf.net.res_ext_grid)
print(opf.net.res_gen)
