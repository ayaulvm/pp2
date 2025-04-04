import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
colors = [RED, GREEN, BLUE, YELLOW]

# Setup screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shape Drawing Tool")
clock = pygame.time.Clock()

# Drawing modes
DRAW_LINE = 0
DRAW_RECTANGLE = 1
DRAW_CIRCLE = 2
ERASER = 3
DRAW_SQUARE = 4
DRAW_RIGHT_TRIANGLE = 5
DRAW_EQUILATERAL_TRIANGLE = 6
DRAW_RHOMBUS = 7

# Initial tool settings
draw_mode = DRAW_LINE
current_color = BLUE
radius = 10
points = []  # Store drawn shapes (optional for undo/redo features)

# Drawing function for all supported modes
def draw_tool(screen, start, end, mode, color, width):
    if mode == DRAW_LINE:
        pygame.draw.line(screen, color, start, end, width)

    elif mode == DRAW_RECTANGLE:
        pygame.draw.rect(screen, color, pygame.Rect(start[0], start[1], end[0] - start[0], end[1] - start[1]), width)

    elif mode == DRAW_CIRCLE:
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, start, radius, width)

    elif mode == DRAW_SQUARE:
        side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect = pygame.Rect(start[0], start[1], side, side)
        pygame.draw.rect(screen, color, rect, width)

    elif mode == DRAW_RIGHT_TRIANGLE:
        x1, y1 = start
        x2, y2 = end
        points = [(x1, y1), (x2, y2), (x1, y2)]  # Right-angle at (x1, y2)
        pygame.draw.polygon(screen, color, points, width)

    elif mode == DRAW_EQUILATERAL_TRIANGLE:
        x1, y1 = start
        x2, y2 = end
        side = abs(x2 - x1)
        height = (3 ** 0.5 / 2) * side
        direction = -1 if y2 < y1 else 1
        points = [
            (x1, y1),
            (x1 + side, y1),
            (x1 + side / 2, y1 + direction * height)
        ]
        pygame.draw.polygon(screen, color, points, width)

    elif mode == DRAW_RHOMBUS:
        x1, y1 = start
        x2, y2 = end
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        points = [
            (cx, y1),     # Top
            (x2, cy),     # Right
            (cx, y2),     # Bottom
            (x1, cy)      # Left
        ]
        pygame.draw.polygon(screen, color, points, width)

    elif mode == ERASER:
        pygame.draw.circle(screen, WHITE, start, width)

# Main application loop
def main():
    global draw_mode, current_color, radius, points

    running = True
    start_pos = None

    while running:
        screen.fill(WHITE)  # Clear screen each frame

        # Get pressed keys (for shortcuts)
        pressed = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keyboard controls for tools and colors
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r: current_color = RED
                elif event.key == pygame.K_g: current_color = GREEN
                elif event.key == pygame.K_b: current_color = BLUE
                elif event.key == pygame.K_y: current_color = YELLOW
                elif event.key == pygame.K_l: draw_mode = DRAW_LINE
                elif event.key == pygame.K_v: draw_mode = DRAW_RECTANGLE
                elif event.key == pygame.K_c: draw_mode = DRAW_CIRCLE
                elif event.key == pygame.K_e: draw_mode = ERASER
                elif event.key == pygame.K_s: draw_mode = DRAW_SQUARE
                elif event.key == pygame.K_t: draw_mode = DRAW_RIGHT_TRIANGLE
                elif event.key == pygame.K_q: draw_mode = DRAW_EQUILATERAL_TRIANGLE
                elif event.key == pygame.K_h: draw_mode = DRAW_RHOMBUS
                elif event.key == pygame.K_UP:
                    radius = min(50, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)

            # Mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos

            # Mouse button up (draw shape)
            if event.type == pygame.MOUSEBUTTONUP:
                if start_pos:
                    end_pos = event.pos
                    draw_tool(screen, start_pos, end_pos, draw_mode, current_color, radius)
                    start_pos = None

            # Mouse movement with button held (for eraser or free draw)
            if event.type == pygame.MOUSEMOTION and start_pos:
                end_pos = event.pos
                draw_tool(screen, start_pos, end_pos, draw_mode, current_color, radius)
                start_pos = end_pos  # Update for continuous stroke

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the app
if __name__ == "__main__":
    main()
