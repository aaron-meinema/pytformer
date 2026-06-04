import pygame


class Tile:
    def __init__(self, x, y, image_number: int):
        self.full_image = pygame.image.load(
            "assets/sprites/tiles/midground_/summer_.png").convert_alpha()
        self.image = pygame.Surface((8, 8), pygame.SRCALPHA)
        self.image.blit(self.full_image, (0, 0), (image_number * 8, 8, 8, 8))
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))

    def get_width(self) -> int:
        return self.rect.width

    def get_height(self) -> int:
        return self.rect.height

    def get_position(self) -> tuple:
        return self.rect.topleft

    def on_floor(self, unit_rect: pygame.Rect) -> bool:
        if not self.rect.colliderect(unit_rect):
            return False

        overlap = min(unit_rect.right, self.rect.right) - max(unit_rect.left, self.rect.left) - 20
        if overlap <= 0:
            return False
        print(f'self top: {self.rect.top}, unit bottom: {unit_rect.bottom}')
        return (unit_rect.bottom - 8) <= self.rect.top

    def on_wall(self, unit_rect: pygame.Rect) -> bool:
        return self.rect.colliderect(unit_rect) and (unit_rect.right >= self.rect.left - 10 and
                                                     unit_rect.left <= self.rect.right + 10)
