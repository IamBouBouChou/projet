import pygame as p

p.init()

# on décide de la taille de la fenêtre de jeu
SCREEN_HEIGHT=600
SCREEN_WIDTH=800

screen=p.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

p.display.set_caption('Main Menu')

# On définit les images pour créer les boutons après
start_img=p.image.load('start_button.png').convert_alpha()
exit_img=p.image.load('exit_button.png').convert_alpha()
compte_img=p.image.load('compte_button.png').convert_alpha()
classement_img=p.image.load('classement_button.png').convert_alpha()

start_hover_img=p.image.load('start_button_shadow.png').convert_alpha()
exit_hover_img=p.image.load('exit_button_shadow.png').convert_alpha()
compte_hover_img=p.image.load('compte_button_shadow.png').convert_alpha()
classement_hover_img=p.image.load('classement_button_shadow.png').convert_alpha()


#classe Button
class Button():
    def __init__(self,x,y,image,hover_image,scale):# on prend en entrée des coordonées pour pouvoir placer le bouton, ainsi que l'image du bouton et de son ombre
        width=image.get_width()# pour faire un bouton un peu plus intéractif, et aussi une échelle pour pouvoir dimensioner notre bouton
        height=image.get_height()
        self.image=p.transform.scale(image,(int(width*scale),int(height*scale)))
        self.hover_image=p.transform.scale(hover_image,(int(width*scale),int(height*scale)))
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.clicked=False # pour savoir plus tard si une action est réalisé sur la souris, on l'initialise ici
    
    def draw(self):
        action=False
        pos=p.mouse.get_pos() #position de la souris en temps réel
        
        if self.rect.collidepoint(pos): #si le curseur est en collision avec le bouton
            image_to_display=self.hover_image #l'image change pour son ombre
            if p.mouse.get_pressed()[0]==1 and self.clicked==False: #si le bouton de la souris est cliqué
                self.clicked=True
                action=True
        else:
            image_to_display=self.image #l'image reste celle de base
        if p.mouse.get_pressed()[0]==0: #si le bouton de la souris n'est pas cliqué
            self.clicked=False  #il n'y a pas d'action
        
        screen.blit(image_to_display,(self.rect.x,self.rect.y)) #on affiche l'image adéquate
        
        return action

#On créer les boutons
start_button=Button(400,140,start_img,start_hover_img,1)
exit_button=Button(400,440,exit_img,exit_hover_img,1)
compte_button=Button(400,240,compte_img,compte_hover_img,1)
classement_button=Button(400,340,classement_img,classement_hover_img,1)

#Le programme principale
run=True
while run:
    
    screen.fill((218,239,252))
    
    if start_button.draw()==True:
        print('start')
    
    if exit_button.draw()==True:
        run=False
    
    if compte_button.draw()==True:
        print("compte")
    
    if classement_button.draw()==True:
        print('classement')
    
    for event in p.event.get():
        if event.type==p.QUIT:
            run = False
    p.display.update()
p.quit()