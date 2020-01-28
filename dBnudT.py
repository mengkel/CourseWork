import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from astropy import units as u

def dBnudT( nu, T ):
  T = T * u.K
  nu = nu * u.Hz
  x = const.h.cgs * nu / ( const.k_B.cgs * T )
  y = const.k_B.cgs * T / ( const.h.cgs * const.c.cgs )
  return \
    2. * const.k_B.cgs * np.power( y, 2 ) * \
    np.power( x, 4 ) * np.exp( -x ) / np.power( 1. - np.exp( -x ), 2 )

def main():

  lnu = np.linspace( 2, 17, 200 )
  nu = np.power( 10., lnu )

  t1 = 100.
  t2 = 1000.
  t3 = 10000.

  plt.rc('text', usetex=True)
  plt.rc('font', family='serif', size=12)

  plt.plot( nu, dBnudT(nu, t1), label = 'T = 100 K' )
  plt.plot( nu, dBnudT(nu, t2), label = 'T = 1,000 K' )
  plt.plot( nu, dBnudT(nu, t3), label = 'T = 10,000 K' )

  plt.xscale( 'log' )
  plt.yscale( 'log' )

  plt.xlim( [1.e2,1.e17] )
  plt.ylim( [1.e-26,1.] )

  plt.xlabel( r'$\nu\ (Hz)$' )
  plt.ylabel( r'$\frac{\partial B_\nu}{\partial T}\ (erg\ cm^{-2}\ s^{-1}\ ster^{-1}\ Hz^{-1} K^{-1})$' )

  plt.legend()
   
  plt.show()

if __name__== "__main__":
  main()

