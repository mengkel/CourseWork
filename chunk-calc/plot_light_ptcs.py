import wnutils.xml as wx
import matplotlib.pyplot as plt

xml1 = wx.Xml('with-thermo-no-sdot.xml')
xml2 = wx.Xml('with-thermo-with-sdot.xml')

props = xml1.get_properties_as_floats(['time'])['time']
props2 = xml2.get_properties_as_floats(['time'])['time']

nuclides_list = ['n']
fractions = xml1.get_mass_fractions(nuclides_list)
fractions2 = xml2.get_mass_fractions(nuclides_list)

for i, sp in enumerate(fractions):
    line1, = plt.plot(props, fractions[sp],label = sp)
plt.yscale('log')
plt.xlim(0,8)
plt.title(r'$\dot s=0 $')

for i, sp in enumerate(fractions2):
    line2, = plt.plot(props2, fractions2[sp], label = sp)

plt.yscale('log')
plt.xlim(0,12)
#plt.title('Mass Fraction' )
plt.ylabel('Mass fracttion of n')
plt.xlabel('time (s)')
plt.legend((line1,line2),(r'$\dot s = 0$', r'$\dot s \neq 0$'))

plt.show()

