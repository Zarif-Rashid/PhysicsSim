import pygame
pygame.init()

WIDTH, HEIGHT = 1500, 800
fps = 165
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

# game constants
wall_thickness = 10
gravity = 0.4  # Gravity constant
bounce_stop = 0.6  # Speed threshold for bouncing to stop

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, y_speed, x_speed, id):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.y_speed = y_speed
        self.x_speed = x_speed  
        self.id = id
        self.cicle = ''

    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

    def check_gravity(self):
        if self.y_pos < HEIGHT - self.radius - (wall_thickness/2):
            self.y_speed += gravity
        else:
            if self.y_speed > bounce_stop:
                self.y_speed = self.y_speed * -1 * self.retention
            else:
                if abs(self.y_speed) <= bounce_stop:
                    self.y_speed = 0

        return self.y_speed
    
    def update_pos(self):
        self.y_pos += self.y_speed
        self.x_pos += self.x_speed

def draw_walls():
    left = pygame.draw.line(screen, "white", (0, 0), (0, HEIGHT), wall_thickness)
    right = pygame.draw.line(screen, "white", (WIDTH, 0), (WIDTH, HEIGHT), wall_thickness)
    top = pygame.draw.line(screen, "white", (0, 0), (WIDTH, 0), wall_thickness)
    bottom = pygame.draw.line(screen, "white", (0, HEIGHT), (WIDTH, HEIGHT), wall_thickness)
    wall_list = [left, right, top, bottom]
    return wall_list

ball1 = Ball(50,50,15,'white', 50, 0.9, 0, 0, 1)
ball2 = Ball(WIDTH/2, HEIGHT/2, 30, 'red', 100, 0.9, 0, 0, 2)


run = True
while run:
    timer.tick(fps)
    screen.fill("black")  # Fill the screen with black
    walls = draw_walls()
    ball1.draw()  # Draw the ball
    ball1.update_pos()
    ball1.y_speed = ball1.check_gravity()  # Check gravity and update ball position
    ball2.draw()  # Draw the second ball


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # Update the display

pygame.quit()  # Quit pygame when the loop ends