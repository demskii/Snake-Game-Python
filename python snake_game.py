import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Warna yang akan digunakan
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Ukuran layar
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Ukuran ular
SNAKE_SIZE = 20

# Kecepatan ular
SNAKE_SPEED = 12

# Membuat layar
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Ular")

# Inisialisasi posisi awal ular
snake_x = SCREEN_WIDTH // 2
snake_y = SCREEN_HEIGHT // 2

# Inisialisasi panjang ular dan tubuh ular
snake_length = 1
snake_body = [(snake_x, snake_y)]

# Inisialisasi posisi makanan
food_x = random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) //
                        SNAKE_SIZE) * SNAKE_SIZE
food_y = random.randint(
    0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

# Inisialisasi arah awal ular
direction = "UP"

# Fungsi untuk menggambar ular dan makanan


def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(
            screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))


def draw_food(food_x, food_y):
    pygame.draw.rect(screen, WHITE, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Perbarui posisi ular berdasarkan arahnya
    if direction == "UP":
        snake_y -= SNAKE_SIZE
    elif direction == "DOWN":
        snake_y += SNAKE_SIZE
    elif direction == "LEFT":
        snake_x -= SNAKE_SIZE
    elif direction == "RIGHT":
        snake_x += SNAKE_SIZE

    # Tambahkan posisi baru ke kepala ular
    snake_head = (snake_x, snake_y)
    snake_body.insert(0, snake_head)

    # Cek jika ular makan makanan
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(
            0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        food_y = random.randint(
            0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    else:
        # Hapus ekor ular jika tidak makan makanan
        snake_body.pop()

    # Cek tabrakan dengan dinding
    if (
        snake_x < 0
        or snake_x >= SCREEN_WIDTH
        or snake_y < 0
        or snake_y >= SCREEN_HEIGHT
    ):
        running = False

    # Cek tabrakan dengan tubuh ular sendiri
    if len(snake_body) > 1 and snake_head in snake_body[1:]:
        running = False

    # Bersihkan layar
    screen.fill((0, 0, 0))

    # Gambar ular dan makanan
    draw_snake(snake_body)
    draw_food(food_x, food_y)

    # Perbarui layar
    pygame.display.update()

    # Atur kecepatan ular
    pygame.time.Clock().tick(SNAKE_SPEED)

# Akhiri Pygame
pygame.quit()
