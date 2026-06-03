import pygame

from field_tiles.tile import Tile
from units.player import Player


class App:
    def __init__(self):
        self._running = True
        self.size = self.weight, self.height = 1366, 768
        self.clock = pygame.time.Clock()
        self.tiles: list[Tile] = []

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.player = Player(200, 200)
        self.tiles.append(Tile(0, 500, 0))
        self.tiles.append(Tile(64, 500, 0))

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

    def on_execute(self) -> None:
        self.on_init()

        while self._running:
            self.player.set_on_floor(self.tiles)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
