import json
import os

import pygame

from src.creator.unit_spawner import UnitSpawner
from src.field_tiles.tile import Tile


class Creator:
    def __init__(self):
        self._running = True
        self.size = self.weight, self.height = 1366, 768
        self.clock = pygame.time.Clock()
        self.tiles: list[Tile] = []
        self.mouse_tile = None
        self.selected_number = 1
        self.unit_spawner = UnitSpawner(self)

    def on_init(self, level: int):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.selected_level = level
        if not os.path.exists(f"levels/{level}.json"):
            with open(f"levels/{level}.json", "w") as f:
                json.dump([], f)
        with open(f"levels/{level}.json") as f:
            for tile_data in json.load(f):
                self.tiles.append(Tile.from_json(tile_data))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        delta_time = self.clock.tick(60) / 1000.0  # Convert milliseconds to seconds
        self.unit_spawner.on_loop()

    def on_render(self) -> None:
        self._display_surf.fill((30, 30, 30))  # background color

        self.unit_spawner.on_render()
        # draw tiles
        for tile in self.tiles:
            self._display_surf.blit(tile.image, tile.rect)
        if self.mouse_tile:
            self._display_surf.blit(self.mouse_tile.image, self.mouse_tile.rect)
        pygame.display.flip()

    @staticmethod
    def on_cleanup() -> None:
        pygame.quit()

    def on_execute(self, level: int) -> None:
        self.on_init(level)

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def save(self) -> None:
        with open(f"levels/{self.selected_level}.json", "w") as f:
            json.dump([tile.to_json() for tile in self.tiles], f)
