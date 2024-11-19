import pygame
pygame.init()

window=pygame.display.set_mode((400,400))


window.fill((255,80,20))
pink=(255,192,203)
pygame.draw.circle(window,pink,(300,300),50)

pygame.display.update()
running=True
while running :
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        running=False
pygame.display.flip()
pygame.quit()