import pygame

from src.units.unit import Unit


class Player(Unit):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "assets/sprites/units/robinHood_.png")

        self.running_speed = 200

        self.gravity = 8
        self.jump_power = 400
        self.is_jumping = True
        self.on_floor = False
        self.vertical_velocity = 0
        self.start_fall_speed = 180

        self.frame_timer = 0
        self.frame_index = 0
        self.image = self.get_frame(self.frame_index)

    def update(self, delta_time: float) -> None:
        self.movement(delta_time)
        self.frame_timer += delta_time

        if self.frame_timer >= self.frame_speed:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % 4
            self.image = pygame.transform.scale(self.get_frame(self.frame_index), (64, 64))
            self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

        if self.on_floor and not self.is_jumping:
            self.vertical_velocity = 0
        else:
            self.vertical_velocity += self.gravity
            self.rect.y += int(self.vertical_velocity * delta_time)

    def movement(self, delta_time: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= int(self.running_speed * delta_time)
        if keys[pygame.K_RIGHT]:
            self.rect.x += int(self.running_speed * delta_time)
        if keys[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.on_floor = False
            self.vertical_velocity = -self.jump_power

    def get_frame(self, index) -> pygame.Surface:
        frame = pygame.Surface((self.frame_w, self.frame_h), pygame.SRCALPHA)

        frame.blit(
            self.sheet,
            (0, 0),
            (index * self.frame_w, 0, self.frame_w, self.frame_h)
        )

        return frame

    def set_on_floor(self, tiles: list) -> None:
        self.on_floor = False

        for tile in tiles:
            if tile.on_floor(self.rect):
                self.on_floor = True
                self.is_jumping = False
                self.vertical_velocity = 0
                self.rect.bottom = tile.rect.top
                return
