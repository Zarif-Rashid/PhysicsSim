import pygame
import math
pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Arial', 20)

WIDTH, HEIGHT = 1600, 1000
fps = 165
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

# game constants
wall_thickness = 10
gravity = 9.81*0.01  # Gravitational field strength 
G = 6.67e1*1.5  # Gravitational constant
bounce_stop = 0.6  # Speed threshold for bouncing to stop

class Ball:
    def __init__(self, x_pos, y_pos, radius, color, mass, retention, x_speed, y_speed, id):
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
    
    def gravity_pull(self, other_ball):
        dist = math.sqrt((self.x_pos - other_ball.x_pos) ** 2 + (self.y_pos - other_ball.y_pos) ** 2)
        acc = (G * other_ball.mass) / (dist)**2  
        acc_y = acc * (other_ball.y_pos - self.y_pos) / dist
        acc_x = acc * (other_ball.x_pos - self.x_pos) / dist
        self.y_speed += acc_y
        self.x_speed += acc_x

        return [self.y_speed, self.x_speed, acc]
    
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

ball1 = Ball(WIDTH/4,HEIGHT/4 + 100,5,'white', 50, 1, 0, 4.6, 1)    
ball2 = Ball(WIDTH/2+200, HEIGHT/4 + 100, 5, 'blue', 50, 1, 0, -5, 2)

ball_main = Ball(WIDTH/2, HEIGHT/2, 10, 'red', 80, 0.9, 0, 0, 3)
tracer1_points = []
tracer2_points = []


run = True
while run:
    timer.tick(fps)
    screen.fill("black")  # Fill the screen with black
    walls = draw_walls()
    ball1.draw()  # Draw the ball
    ball1.update_pos()
    ball2.draw()  # Draw the second ball
    ball2.update_pos()
    # ball1.y_speed = ball1.check_gravity()  # Check gravity and update ball position
    ball1.y_speed = ball1.gravity_pull(ball_main)[0]  # Apply gravity pull from the second ball
    ball1.x_speed = ball1.gravity_pull(ball_main)[1]  # Apply gravity pull from the second ball
    ball2.y_speed = ball2.gravity_pull(ball_main)[0]  # Apply gravity pull from the second ball
    ball2.x_speed = ball2.gravity_pull(ball_main)[1]  # Apply gravity pull from the second ball
    print(f"Ball 1 Position: ({ball1.x_pos}, {ball1.y_pos}), Speed: ({ball1.x_speed}, {ball1.y_speed})")
    ball_main.draw()  # Draw the second ball

    tracer1_points.append((int(ball1.x_pos), int(ball1.y_pos)))
    tracer2_points.append((int(ball2.x_pos), int(ball2.y_pos)))

    for point in tracer1_points:
        pygame.draw.circle(screen, "yellow", point, 2)  # Small yellow dot
    for point in tracer2_points:
        pygame.draw.circle(screen, "blue", point, 2)  # Small blue dot  

    text_surface = font.render(f"x_speed: {ball1.x_speed:.2f}, y_speed: {ball1.y_speed:.2f}, acc: {ball1.gravity_pull(ball_main)[2]:.2f}, Force: {ball1.mass*ball1.gravity_pull(ball_main)[2]:.2f}", True, "aqua")
    screen.blit(text_surface, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # Update the display

pygame.quit()  # Quit pygame when the loop ends