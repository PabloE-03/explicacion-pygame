def doomguy_collide(doomguy):
    if(doomguy.rect.x<5):
        doomguy.rect.x = 5

    if(doomguy.rect.x + 85>795):
        doomguy.rect.x = 795 - 85

    if(doomguy.rect.y < 5):
        doomguy.rect.y = 5
    
    if(doomguy.rect.y + 114 > 595):
        doomguy.rect.y = 595 - 114

def imp_collide(imp,derecha_imp,izquierda_imp):
    if(derecha_imp==1 and imp.rect.y + 94>580):
        derecha_imp=0
        izquierda_imp=1
        imp.rect.x = 675 
        imp.rect.y  = 500
    elif(izquierda_imp==1 and imp.rect.y<15):
        izquierda_imp = 0
        derecha_imp = 1
        imp.rect.x = 75
        imp.rect.y = 20
    return derecha_imp,izquierda_imp

def proyectil_collide(fireballs,derecha,izquierda):

    if(fireballs[0].rect.x<0 or fireballs[0].rect.x +96 > 795 and fireballs[0].rect.y<600):
        fireballs[0].rect.x = 900
        fireballs[0].rect.y = 700
        derecha = 0
        izquierda = 0
    if(fireballs[1].rect.x<0 or fireballs[1].rect.x +96 > 795 and fireballs[1].rect.y<600):
        fireballs[1].rect.x = 900
        fireballs[1].rect.y = 700
        derecha = 0
        izquierda = 0
    
    return derecha,izquierda

def bala_collide(bala,imp,fase):
    if((bala.rect.x>imp.rect.x and bala.rect.x+40<imp.rect.x+61) and (bala.rect.y>imp.rect.y and bala.rect.y+40<imp.rect.y+94)):
        fase+=1
        bala.rect.x = 900
        bala.rect.y = 700
    return fase