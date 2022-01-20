# Simple Pong Game v1.0

import pygame
pygame.init()

# Colors
black = (0,0,0)
white = (255,255,255)
screen_size = (800,600)
player1_x = 30
player1_y = 255
player_width = 15
player_height = 90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


# Player 1 speed and coordinates 
player1_x_coor = 30
player1_y_coor = 300 - (player_height / 2)
player1_y_speed = 0
player2_x_coor = 770 - player_width
player2_y_coor = 300 - (player_height / 2)
player2_y_speed = 0


# Ball coordinates
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3



game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			# Player1
			if event.key == pygame.K_w:
				player1_y_speed = -3
			if event.key == pygame.K_s:
				player1_y_speed = 3

			# Player2
			if event.key == pygame.K_UP:
				player2_y_speed = -3
			if event.key == pygame.K_DOWN:
				player2_y_speed = 3

		if event.type == pygame.KEYUP:
			# Player1
			if event.key == pygame.K_w:
				player1_y_speed = 0
			if event.key == pygame.K_s:
				player1_y_speed = 0

			# Player2
			if event.key == pygame.K_UP:
				player2_y_speed = 0
			if event.key == pygame.K_DOWN:
				player2_y_speed = 0

	# Limit players movement so they stay on screen
	if player1_y_coor > 600-5 - player_height :
		player1_y_coor = 600-5 - player_height
	if player1_y_coor < 5:
		player1_y_coor = 5

	if player2_y_coor > 600-5 - player_height:
		player2_y_coor = 600-5 - player_height
	if player2_y_coor < 5:
		player2_y_coor = 5

	# Check if ball bounces on horizontal side
	if ball_y > 590 or ball_y < 10:
		ball_speed_y *= -1

	# Check if ball goes out the right or left side
	if ball_x > 800 or ball_x <0:
		ball_x = 400
		ball_y = 300
		# If the ball passes, reverse direction
		ball_speed_x *= -1


	# Modify coordinates to give movement to players/ball
	player1_y_coor += player1_y_speed
	player2_y_coor += player2_y_speed

	# Ball movement
	ball_x += ball_speed_x
	ball_y += ball_speed_y



	screen.fill(black)
	# Drawing zone
	player1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
	player2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
	ball = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)

	# Collisions
	if ball.colliderect(player1) or ball.colliderect(player2):
		ball_speed_x *= -1

	pygame.display.flip()
	clock.tick(60)

pygame.quit()