from pathlib import Path

import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Addaing Image in Pygame")

ASSET_DIR = Path(__file__).resolve().parent


def create_penguin_image(size):
    image = pygame.Surface(size, pygame.SRCALPHA)

    width, height = size

    center_x = width // 2

    pygame.draw.ellipse(image, (25, 35, 50), (35, 10, width - 70, height - 20))

    pygame.draw.ellipse(image, (245, 245, 235), (55, 70, width - 110, height - 45))

    pygame.draw.ellipse(image, (255, 255, 255), (68, 40, 22, 28))

    pygame.draw.ellipse(image, (255, 255, 255), (110, 40, 22, 28))

    pygame.draw.circle(image, (10, 10, 15), (79, 54), 6)

    pygame.draw.circle(image, (10, 10, 15), (121, 54), 6)

    pygame.draw.polygon(image, (245, 150, 35), ((center_x, 62), (center_x - 14, 75), (center_x + 14, 75)))

    pygame.draw.ellipse(image, (245, 150, 35), (45, height - 28, 55, 22))

    pygame.draw.ellipse(image, (245, 150, 35), (100, height - 28, 55, 22))

    return image


def load_image(filename, size, fallback_colour):
    image_path = ASSET_DIR / filename
    if image_path.exists():
        return pygame.transform.scale(
            pygame.image.load(str(image_path)).convert_alpha(),
            size,
        )
    if filename == "penguin.png":
        return create_penguin_image(size)

    image = pygame.Surface(size, pygame.SRCALPHA)
    image.fill(fallback_colour)
    return image


background_image = load_image(
    "background.png",
    (SCREEN_WIDTH, SCREEN_HEIGHT),
    (180, 220, 255, 255),
)

penguin_image = load_image("penguin.png", (200, 200), (40, 40, 60, 255))

penguin_rect = penguin_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))


def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
