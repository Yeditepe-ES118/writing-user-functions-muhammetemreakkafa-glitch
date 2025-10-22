import numpy as np

def throw_rock(m,v0,theta):
    g=9.81 
    theta=theta*np.pi/180 # now it is in radians
    tf= 2*v0*np.sin(theta)/g
    R=v0**2*np.sin(2*theta)/g
    hm=v0**2*np.sin(theta)**2/(2*g)
    vh=v0*np.cos(theta)
    kh=(m*vh*hm**2)/2 # in joule (J)
    
    #eğer return burada olsaydı returnden sonra hiçbir şey değerlendirilmediği için tüm işlemşeri returnden önce yaparız
    print("For a rock with %5.3f kg mass thrown with %5.3f m/s at an angle of %6.2f degrees:\n"\
          "Time of flight is %10.1e s\nThe range in x-direction is %10.1e m\n"\
          "Maximum height is %10.1e m\nThe speed at maximum height is %10.1e m/s\n"\
          "Kinetic energy at the maximum height is %8.2e J" % (m,v0,theta*180/np.pi,tf,R,hm,vh,kh))
    return tf, R, hm, vh, kh
