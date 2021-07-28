from Generation import genPass

from options import options

opt = begin()
GetInfo(opt)
lst = options()

print(genPass(lst))
