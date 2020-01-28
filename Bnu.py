import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from astropy import units as u

def Bnu( nu, T ):
  T = T * u.K
  nu = nu * u.Hz
  x = const.h.cgs * nu / ( const.k_B.cgs * T )
  return \
    ( 2. * const.h.cgs * np.power( nu, 3 ) / np.power( const.c.cgs, 2 ) ) * \
    np.exp( -x ) / ( 1. - np.exp( -x ) )

def main():

  lnu = np.linspace( 7, 17, 200 )
  nu = np.power( 10., lnu )

  t1 = 100.
  t2 = 1000.
  t3 = 10000.

  b1 = []
  b2 = []
  b3 = []

  plt.rc('text', usetex=True)
  plt.rc('font', family='serif', size=13)

  plt.plot( nu, Bnu(nu, t1), label = 'T = 100 K' )
  plt.plot( nu, Bnu(nu, t2), label = 'T = 1,000 K' )
  plt.plot( nu, Bnu(nu, t3), label = 'T = 10,000 K' )

  plt.xscale( 'log' )
  plt.yscale( 'log' )

  plt.xlim( [1.e7,1.e17] )
  plt.ylim( [1.e-16,1.e2] )


  plt.xlabel( r'$\nu\ (Hz)$' )
  plt.ylabel( r'$B_\nu\ (erg\ cm^{-2}\ s^{-1}\ ster^{-1}\ Hz^{-1})$' )

  plt.legend()
   
  plt.show()

if __name__== "__main__":
  main()

