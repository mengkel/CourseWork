import wnutils.xml as wx
import matplotlib.pyplot as plt

xml = wx.Xml('out-wind-nobeta.xml')
xml.make_abundances_vs_nucleon_number_movie('abunda-wind-nobeta.mp4', xlim = [0,300],
#xml.plot_abundances_vs_nucleon_number(xlim = [0,300],  
        ylim = [1.e-10,1.e1], 
        yscale = 'log',
        xlabel = 'Mass Number, A',
        ylabel = 'Y(A)')
#plt.savefig('abunds_wind.png')
plt.show()

