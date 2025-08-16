
def cal_z_score(x,mean,std,z=None):
    if x is None:
        return z * std + mean
    if mean is None:
        return x - z * std
    if std is None:
        return (x- mean)/z
    return (x-mean)/std

print(cal_z_score(23,27,3))
print(cal_z_score(15,11,None,2))
print(cal_z_score(97,None,5,-1.2))
print(cal_z_score(None,19,1.2,3))