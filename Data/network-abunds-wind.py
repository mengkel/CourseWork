import wnutils.xml as wx
import matplotlib.pyplot as plt

my_xml = wx.Xml('out-wind-1.xml')
my_xml.make_network_abundances_movie('network_abunds.mp4', colorbar = cb)
cb = {'shrink': 1, 
      'label': 'Abundance', 
      'aspect': 10, 
      'ticks': [1.e-10, 1.e-8, 1.e-6, 1.e-4, 1.e-2, 1.]})
