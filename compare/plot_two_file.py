import wnutils.xml as wx
import matplotlib.pyplot as plt

xml1 = wx.Xml('out-cst-s.xml')
xml2 = wx.Xml('out-wind-nobeta.xml')

data1 = xml1.get_properties_as_floats(['t9','time','rho','entropy per nucleon'])
data2 = xml2.get_properties_as_floats(['t9','time','rho','entropy per nucleon'])
l1, = plt.plot(data1['time'],data1['t9'],'b-')
l2, = plt.plot(data2['time'],data2['t9'], 'r.')
plt.legend((l1,l2),('cst entropy','entropy vary no beta decay'))
plt.xlabel('Time (s)')
plt.ylabel(r'$T_9$')
plt.xlim(0,3)
plt.savefig('compare t9.png')


plt.figure(2)
l1, = plt.plot(data1['time'],data1['rho'], 'b-')
l2, = plt.plot(data2['time'],data2['rho'], 'r.')
plt.legend((l1,l2),('cst entropy','entropy vary no beta decay'))
plt.xlabel('Time (s)')
plt.ylabel(r'$\rho$')
plt.xlim(0,3)
plt.ylim(1.e0,1.e7)
plt.yscale('log')
plt.savefig('compare density.png')

plt.figure(3)
l1, = plt.plot(data1['time'],data1['entropy per nucleon'])
l2, = plt.plot(data2['time'],data2['entropy per nucleon'])
plt.legend((l1,l2),('cst entropy','entropy vary no beta decay'))
plt.xlabel('Time (s)')
plt.ylabel('entropy per nucleon')
plt.xlim(0,2)
plt.savefig('compare entropy.png')

plt.show()



