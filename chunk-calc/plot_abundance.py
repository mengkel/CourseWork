import sys
import wnutils.xml as wx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig = plt.figure()

xml = wx.Xml(sys.argv[1])

z = sys.argv[2]

y = xml.get_all_abundances_in_zones()

def updatefig(i):
    p = xml.get_all_properties_for_zone("[position() = " + str(i+1) + "]")
    
    keys = list(dict.keys(p))
    
    u = list(filter(lambda x: x[0] == 'yz_eq' and x[1] == z, keys))

    yn = y[i, int(z), :]

    yneq = np.zeros(y.shape[2])

    for uu in u:
        yneq[int(uu[2]) - int(uu[1])] = float(p[uu])
        
    fig.clear()
    plt.plot(yn,label='Network')
    plt.plot(yneq,label='$(n,\\gamma)-(\\gamma,n)$ equilibrium')
    plt.xlabel('N, Neutron Number')
    plt.ylabel('Abundance')
    plt.title('Z = '+str(z))
    plt.ylim(1.e-10,1)
    plt.xlim(10,60)
    plt.yscale('log')
    plt.legend()
    plt.draw()

anim = animation.FuncAnimation(fig, updatefig, y.shape[0])
anim.save('ng.mp4', fps = 15)
