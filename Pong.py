import pygame as pg
import os
import random
pg.font.init()
pg.init()


WIDTH, HEIGHT = 1280, 720
WINDOW = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Pong")

SCORE_FONT = pg.font.SysFont("Minecraft",80)
WINNER_FONT = pg.font.SysFont("arial",100)

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 100

FPS = 60
VEL = 8

#Ball
BALL_Vel = 7
ball_image = pg.Surface([20,20])
ball_rect = ball_image.get_rect(topleft=(100,100))
pg.draw.circle(ball_image,"white", (10,10),10)
ball_vec = [8,8]


#players Rect
player1 = pg.Rect(100,HEIGHT/2 - PLAYER_HEIGHT/2 ,PLAYER_WIDTH,PLAYER_HEIGHT)
player2 = pg.Rect(1180,HEIGHT/2 - PLAYER_HEIGHT/2, PLAYER_WIDTH, PLAYER_HEIGHT)

player1_score = 0
player2_score = 0

#Border
boder_top_rect = ((0,0),(1280,20))
boder_down_rect = ((0,700),(1280,20))





def draw_window():
    WINDOW.fill("black")

    #Middle line
    y = 0
    for i in range(35):
        pg.draw.rect(WINDOW,"white",((WIDTH/2-5,y),(10,10)))
        y += 20

    #Draw Score
    player1_score_text = SCORE_FONT.render(str(player1_score),1,"white")
    player2_score_text = SCORE_FONT.render(str(player2_score),1,"white")
    WINDOW.blit(player1_score_text,(WIDTH/2 - player1_score_text.get_width() - 10 ,30))
    WINDOW.blit(player2_score_text,(WIDTH/2 +10  ,30))
    #Draw Ball
    WINDOW.blit(ball_image,ball_rect)
    #Draw Border
    pg.draw.rect(WINDOW,"white",boder_top_rect)
    pg.draw.rect(WINDOW,"white",boder_down_rect)
    #Draw Players
    pg.draw.rect(WINDOW,"white",player1)
    pg.draw.rect(WINDOW,"white", player2)
    

def player1_handle_movement(keys_pressed):
    if keys_pressed[pg.K_w] and player1.y > 20:
        player1.y -= VEL
    if keys_pressed[pg.K_s] and player1.y < 700-PLAYER_HEIGHT:
        player1.y += VEL

def player2_handle_movement(keys_pressed):
    if keys_pressed[pg.K_UP] and player2.y > 20:
        player2.y -= VEL
    if keys_pressed[pg.K_DOWN] and player2.y < 700-PLAYER_HEIGHT:
        player2.y += VEL
     
    pg.display.update()



def reset_game():
    global ball_rect,ball_vec
    h_rand = random.randint(40,680)
    ball_rect = pg.Rect(WIDTH/2,h_rand,20,20)
    ball_vec[0] = -ball_vec[0]
    ball_vec[1] = -ball_vec[1]




def main():
    


    clock = pg.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            
        
        #Input
        keys_pressed = pg.key.get_pressed()
        if keys_pressed:
            player1_handle_movement(keys_pressed)
            player2_handle_movement(keys_pressed)
        
        pg.Rect.move_ip(ball_rect,ball_vec)
        if ball_rect.top <20 or ball_rect.bottom > HEIGHT - 20:
            ball_vec[1] = -ball_vec[1]
        if player2.colliderect(ball_rect):
            ball_vec[0] = -ball_vec[0]

        if player1.colliderect(ball_rect):
            ball_vec[0] = -ball_vec[0]


        global player1_score,player2_score
        if ball_rect.left > WIDTH:
            player1_score +=1
            reset_game()
        if ball_rect.right <0:
            player2_score +=1
            reset_game()



            
        
        
        
        draw_window()
        

    pg.quit()

if __name__ == "__main__":
    main()