import numpy as np
import uc480
import pygame
import matplotlib.pyplot as plt
import sys,os,time
of = open('output.tsv','w')
pygame.init()

width,height = 1024,768
cam = uc480.uc480()

screen = pygame.display.set_mode([width,height],pygame.FULLSCREEN)
cut = 10

SLMPix = np.zeros((width,height))

val = [x for x in range(0,256,120)]
lines = [300,700]


phase = []
for a in val:
    SLMPix[:,384:] = a
    draw = np.stack((SLMPix,)*3,axis=2)
    pygame.surfarray.blit_array(screen,draw)
    pygame.display.flip()
    cam = uc480.uc480()
    cam.connect()
    img = cam.acquire()
    cam.disconnect()
    phi=[]
    for b in lines:
        row = img[b,:]
        rowFT = np.fft.fft(row)
        rowFT[:cut] = 0
        rowFT[30:] = 0
        peak = np.argmax(np.abs(rowFT))
        print(peak)
        phiN = np.log(2*rowFT[peak]).imag
        phi.append(phiN)
    dphi = phi[1]-phi[0]
    waveshift = dphi/(2*np.pi)
    phase.append(waveshift)
for a in val:
    of.write(str(a)+'\t'+str(phase[a])+'\n')
of.close()
plt.scatter(val,phase)
plt.show()
