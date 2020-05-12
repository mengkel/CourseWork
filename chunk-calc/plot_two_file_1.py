import wnutils.xml as wx
import matplotlib.pyplot as plt

xml1 = wx.Xml('with-thermo-no-sdot.xml')
xml2 = wx.Xml('with-thermo-with-sdot.xml')
#xml3 = wx.Xml('entropy_generation_nobeta.xml')

data1 = xml1.get_properties_as_floats(['t9','time','rho','entropy per nucleon'])
data2 = xml2.get_properties_as_floats(['t9','time','rho','entropy per nucleon'])
#data3 = xml3.get_properties_as_floats(['t9','time','rho','entropy per nucleon'])

l1, = plt.plot(data1['t9'],data1['rho'])
l2, = plt.plot(data2['t9'],data2['rho'])


#l1, = plt.plot(data1['time'],data1['rho'])
#l2, = plt.plot(data2['time'],data2['rho'])
#l3, = plt.plot(data3['time'],data3['rho'])


plt.legend((l1,l2),(r'$\dot s = 0 $',r'$\dot s \neq 0$'))
plt.xlabel(r'$T_9$')
plt.ylabel(r'$\rho$')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e1,1e-3)
#plt.xlim(0,3)
plt.show()
#plt.savefig('compare t9.png')

