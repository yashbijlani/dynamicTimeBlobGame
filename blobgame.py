import pygame, random

screen = pygame.display.set_mode([1024, 768])
height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
pygame.display.set_caption('Window Caption')
clock = pygame.time.Clock()

img=pygame.image.load(r"/home/kaliv1/Pictures/portal.png")
img=pygame.transform.scale(img, (30, 30))
img.convert()
rect=img.get_rect()
rect.center=width//2,height//2

star_field_slow = []
star_field_medium = []
star_field_fast = []

for slow_stars in range(50): 
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_slow.append([star_loc_x, star_loc_y]) 

for medium_stars in range(35):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(15):
    star_loc_x = random.randrange(0, width)
    star_loc_y = random.randrange(0, height)
    star_field_fast.append([star_loc_x, star_loc_y])
            
#create the window
pygame.init()
positions=[]
posx, posy=width//2, 0
game = True
font1 = pygame.font.Font(None, 72)
font2 = pygame.font.Font(None, 36)
raindrops=20
positions=[[0,0] for x in range(raindrops)]
speed=2
score=-1

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game = False 
    screen.fill([0,0,0])
    pos=(rect.x, rect.y)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: rect.y-=1*speed
    if keys[pygame.K_s]: rect.y+=1*speed
    if keys[pygame.K_a]: rect.x-=1*speed
    if keys[pygame.K_d]: rect.x+=1*speed
    if positions[0][1]==0 or positions[0][1]>width:
        for i in range(raindrops):
            positions[i][0]=random.randrange(0,width)
            positions[i][1]=0
        score+=1

    for z in range(raindrops):
        pygame.draw.circle(screen, (255, 0, 0), (positions[z][0],positions[z][1]), 10)
        collide=rect.collidepoint(positions[z][0], positions[z][1])
        if collide:
            text=font1.render("GAME OVER", True, (255, 255, 255))
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            pygame.time.wait(1000)
            game=False
        if abs(rect.x-pos[0])>0 or abs(rect.y-pos[1])>0:
            #positions[z][0]+=1
            positions[z][1]+=3+score*1.1
        else:
            #positions[z][0]+=0.1
            positions[z][1]+=1

    text=font2.render("Score: %d"%score, True, (255, 255, 255))
    screen.blit(text, [width-100, 0])
    for star in star_field_slow:
        star[1] += 1
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, (128, 128, 128), star, 3)

    for star in star_field_medium:
        star[1] += 4
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, (192, 192, 192), star, 2)

    for star in star_field_fast:
        star[1] += 8
        if star[1] > height:
            star[0] = random.randrange(0, width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, (255, 255, 0), star, 1)
    rect.clamp_ip(screen.get_rect()) #setting border    
    screen.blit(img,rect)
    pygame.display.flip()  #redraw everything we've asked pygame to draw
    clock.tick(60)         #set frames per second
pygame.quit()
