import pygame

# Initialize Pygame
pygame.init()

# Define Constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Define Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
colors = [RED, GREEN, BLUE, YELLOW]

# Initialize Screen and Clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define Draw Modes
DRAW_LINE = 0
DRAW_RECTANGLE = 1
DRAW_CIRCLE = 2
ERASER = 3

# Define a variable to hold the current drawing tool
draw_mode = DRAW_LINE
current_color = BLUE
radius = 10
points = []  # Store points for line drawing

# Function to handle drawing based on selected mode
def draw_tool(screen, start, end, mode, color, width):
    if mode == DRAW_LINE:
        pygame.draw.line(screen, color, start, end, width)
    elif mode == DRAW_RECTANGLE:
        pygame.draw.rect(screen, color, pygame.Rect(start[0], start[1], end[0] - start[0], end[1] - start[1]), width)
    elif mode == DRAW_CIRCLE:
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start, radius, width)
    elif mode == ERASER:
        pygame.draw.circle(screen, WHITE, start, width)

def main():
    global draw_mode, current_color, radius, points

    running = True
    start_pos = None  # Start position for drawing
    
    while running:
        screen.fill(WHITE)  # Clear the screen

        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:  # Red color
                    current_color = RED
                elif event.key == pygame.K_g:  # Green color
                    current_color = GREEN
                elif event.key == pygame.K_b:  # Blue color
                    current_color = BLUE
                elif event.key == pygame.K_y:  # Yellow color
                    current_color = YELLOW
                elif event.key == pygame.K_l:  # Line tool
                    draw_mode = DRAW_LINE
                elif event.key == pygame.K_c:  # Circle tool
                    draw_mode = DRAW_CIRCLE
                elif event.key == pygame.K_v:  # Rectangle tool
                    draw_mode = DRAW_RECTANGLE
                elif event.key == pygame.K_e:  # Eraser tool
                    draw_mode = ERASER
                elif event.key == pygame.K_UP:  # Increase radius (line width)
                    radius = min(50, radius + 1)
                elif event.key == pygame.K_DOWN:  # Decrease radius (line width)
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click - start drawing
                    start_pos = event.pos
                elif event.button == 3:  # Right click - erase
                    start_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if start_pos:
                    # Finish drawing the current shape
                    end_pos = event.pos
                    draw_tool(screen, start_pos, end_pos, draw_mode, current_color, radius)
                    if draw_mode != ERASER:
                        points.append((start_pos, end_pos))  # Store the drawing points
                    start_pos = None  # Reset start position after drawing

            if event.type == pygame.MOUSEMOTION:
                if start_pos:
                    # While the mouse moves, keep drawing
                    end_pos = event.pos
                    draw_tool(screen, start_pos, end_pos, draw_mode, current_color, radius)
                    if draw_mode != ERASER:
                        points.append((start_pos, end_pos))  # Store the drawing points
                    start_pos = event.pos

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Maintain the FPS

    pygame.quit()

if __name__ == "__main__":
    main()
