import json

import pygame

from src.field_tiles.tile import Tile
from src.units.player import Player


class Game:
    def __init__(self):
        self._running = True
        self.size = self.weight, self.height = 1366, 768
        self.clock = pygame.time.Clock()
        self.tiles: list[Tile] = []

    def on_init(self, level: int):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.player = Player(200, 200)
        with open(f"levels/{level}.json") as f:
            for tile_data in json.load(f):
                self.tiles.append(Tile.from_json(tile_data))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        delta_time = self.clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        self.player.update(delta_time)
        self.player.set_on_floor(self.tiles)

    def on_render(self) -> None:
        self._display_surf.fill((30, 30, 30))  # background color

        # draw tiles
        for tile in self.tiles:
            self._display_surf.blit(tile.image, tile.rect)

        # draw sprite
        self._display_surf.blit(self.player.image, self.player.rect)

        pygame.display.flip()

    @staticmethod
    def on_cleanup() -> None:
        pygame.quit()

    def on_execute(self, level: int) -> None:
        self.on_init(level)

        while self._running:
            self.player.set_on_floor(self.tiles)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()
