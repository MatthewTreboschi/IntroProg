from Generation import genPass
from login import *
from options import options

opt = begin()
GetInfo(opt)
lst = options()

print(genPass(lst))
