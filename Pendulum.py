import pygame
import math

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Arial', 20)

WIDTH, HEIGHT = 1920, 1000
fps = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

# game constants
gravity = 9.81*0.01  # Gravitational field strength 

# Pendulum parameters
origin = (WIDTH // 2, HEIGHT // 4)
length = 300
angle = math.pi / 4  # Initial angle (45 degrees)
angle_vel = 0
angle_acc = 0
bob_radius = 30

def draw_pendulum(origin, bob_pos):
    pygame.draw.line(screen, "white", origin, bob_pos, 4)
    pygame.draw.circle(screen, "red", bob_pos, bob_radius)

# class Ball:
#     def __init__(self, x_pos, y_pos, radius, color, mass, retention, x_speed, y_speed, id):
#         self.x_pos = x_pos
#         self.y_pos = y_pos
#         self.radius = radius
#         self.color = color
#         self.mass = mass
#         self.retention = retention
#         self.y_speed = y_speed
#         self.x_speed = x_speed  
#         self.id = id
#         self.cicle = ''
#         self.selected = False

#     def draw(self):
#         self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)

#     def check_gravity(self):
#         if self.y_pos < HEIGHT - self.radius - (wall_thickness/2):
#             self.y_speed += gravity
#         else:
#             if self.y_speed > bounce_stop:
#                 self.y_speed = self.y_speed * -1 * self.retention
#             else:
#                 if abs(self.y_speed) <= bounce_stop:
#                     self.y_speed = 0

#         return self.y_speed
    
#     def gravity_pull(self, other_ball):
#         dist = math.sqrt((self.x_pos - other_ball.x_pos) ** 2 + (self.y_pos - other_ball.y_pos) ** 2)
#         min_dist = 1  # Prevent division by zero and huge forces
#         max_acc = 3   # Maximum allowed acceleration
#         max_speed = 27 # Maximum allowed speed
#         # clamping produces odd orbits but prevents instability

#         # Clamp distance to avoid huge forces
#         dist = max(dist, min_dist)

#         acc = (G * other_ball.mass) / (dist)**2  
#         acc = min(acc, max_acc)  # Clamp acceleration

#         acc_y = acc * (other_ball.y_pos - self.y_pos) / dist
#         acc_x = acc * (other_ball.x_pos - self.x_pos) / dist
#         self.y_speed += acc_y
#         self.x_speed += acc_x

#         # Clamp speeds
#         self.y_speed = max(-max_speed, min(self.y_speed, max_speed))
#         self.x_speed = max(-max_speed, min(self.x_speed, max_speed))

#         return [self.y_speed, self.x_speed, acc, dist]
    
#     def update_pos(self, mouse):
#         if not self.selected:
#             self.y_pos += self.y_speed
#             self.x_pos += self.x_speed
#         else:
#             self.x_pos = mouse[0]
#             self.y_pos = mouse[1]

#     def check_select(self, pos):
#         self.selected = False
#         if self.circle.collidepoint(pos):
#             self.selected = True
#         return self.selected
        



run = True
while run:
    timer.tick(fps)
    screen.fill("black")

    # Pendulum physics
    angle_acc = -gravity / length * math.sin(angle)
    angle_vel += angle_acc
    angle_vel *= 0.999  # Damping
    angle += angle_vel

    # Calculate bob position
    bob_x = origin[0] + length * math.sin(angle)
    bob_y = origin[1] + length * math.cos(angle)
    bob_pos = (int(bob_x), int(bob_y))

    draw_pendulum(origin, bob_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()  # Quit pygame when the loop ends