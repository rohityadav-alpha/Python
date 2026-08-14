import gc
x = [1,2,3]
y = x
del x
del y
gc.collect()
