import wnutils.xml as wx
import matplotlib.pyplot as plt

my_xml1 = wx.Xml('out-cst-s.xml')
my_xml2 = wx.Xml('out-wind-nobeta.xml')

y1 = my_xml1.get_abundances_vs_nucleon_number(nucleon = 'a', zone_xpath="[last()]")
y2 = my_xml2.get_abundances_vs_nucleon_number(nucleon = 'a', zone_xpath="[last()]")

line1, = plt.plot(y1[0,:])
line2, = plt.plot(y2[0,:])
plt.xlabel('Mass Number, A')
plt.ylabel('Abundance per nucleon, Y(A)')
plt.xlim(120,250)
plt.ylim(1.e-6,1.e-2)
plt.yscale('log')
plt.legend((line1,line2),('cst entropy','entropy vary no beta decay'))
plt.show()




