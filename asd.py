import math
from PIL import Image

def collisione(q,p,z):
    Qx=q[0];Qy=q[1]
    Px=p[0];Py=p[1]
    Zx=z[0];Zy=z[1]
    return (Py-Qy)*Zx+(Qx-Px)*Zy+(Px*Qy-Qx*Py) >= 0

def verificaintersezioni(lista3punti,Z):
    A = lista3punti[0]
    B = lista3punti[1]
    C = lista3punti[2]
    Avalid = collisione(A,B,Z)
    Bvalid = collisione(B,C,Z)
    Cvalid = collisione(C,A,Z)
    return Avalid and Bvalid and Cvalid

def controllotriangoli(triangolo1,triangolo2):
    A = triangolo2[0]
    B = triangolo2[1]
    C = triangolo2[2]
    verifica1 = verificaintersezioni(triangolo1,A)
    verifica2 = verificaintersezioni(triangolo1,B)
    verifica3 = verificaintersezioni(triangolo1,C)
    D = triangolo1[0]
    E = triangolo1[1]
    F = triangolo1[2]
    verifica4 = verificaintersezioni(triangolo2,D)
    verifica5 = verificaintersezioni(triangolo2,E)
    verifica6 = verificaintersezioni(triangolo2,F)
    return verifica1 or verifica2 or verifica3 or verifica4 or verifica5 or verifica6
    
#-----------------------------------------------------------------------------
done = False
x=360
y=0
jpg = Image.new("RGB",(360,360))

try:
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        for y in range(360):
            for x in range(360):
                if controllotriangoli(triangolo,triangolo1):
                    jpg.putpixel((x,y),(255,255,255))
            
        grafico()
        pygame.display.update()
        clock.tick(60)
        
finally:
    pygame.quit()
    jpg.show()
