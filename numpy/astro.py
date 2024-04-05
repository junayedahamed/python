# import  astropy.cosmology
import  numpy as np
# value=np.array([1,2,3,6,4])
val=np.array([[4.0,6.0,8.0,11.005],[99.0,44.11,6.0,19.458]])
print(val)


print("dimension",val.ndim)
print("shape of array: ",val.shape)   #returns a tuple of shape of arry row and columns
valmean=np.mean(val,axis=1)
sdVAl=np.std(val,axis=1)
valmode=np.median(val,axis=1)

valexp=np.exp(val)
print(f'exponental:{valexp}')

print("SD val: ",sdVAl)
print("valmean: ",valmean)
print(f'mode :{valmode}')



# sd=np.std(value)
# mex=np.mean(value)
# print("max=",mex)
#
# print(sd)

