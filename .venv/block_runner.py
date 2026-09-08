import pygame
import sys
import random
import io
import wave

class BlockRunner:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Block Runner")
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.gravity = 0.6
        self.running = True

        self.font = pygame.font.SysFont('Arial', 24)

        self.assets = self.generate_assets()
        self.sounds = self.generate_sounds()

        self.platforms = []
        self.stars = []
        self.init_game()

    def generate_assets(self):
        def create_surface(w, h, color):
            surf = pygame.Surface((w, h))
            surf.fill(color)
            return surf

        return {
            'bg': create_surface(self.WIDTH, self.HEIGHT, (30, 30, 30)),
            'player': create_surface(40, 60, (0, 255, 255)),
            'platform': create_surface(100, 20, (100, 100, 100)),
            'star': create_surface(20, 20, (255, 255, 0)),
            'win': create_surface(self.WIDTH, self.HEIGHT, (10, 100, 10))
        }

    def generate_sounds(self):
        def make_silence_wav():
            buf = io.BytesIO()
            with wave.open(buf, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(44100)
                wf.writeframes(b'\x00\x00' * 44100)
            buf.seek(0)
            return pygame.mixer.Sound(file=buf)

        return {
            'jump': make_silence_wav(),
            'collect': make_silence_wav()
        }

    def init_game(self):
        self.player = pygame.Rect(100, 100, 40, 60)
        self.vel_y = 0
        self.on_ground = False
        self.score = 0

        self.platforms = [pygame.Rect(x, 500, 100, 20) for x in range(0, self.WIDTH, 135)]
        self.platforms.append(pygame.Rect(600, 400, 100, 20))
        self.platforms.append(pygame.Rect(300, 360, 100, 20))
        self.stars = [pygame.Rect(620, 370, 20, 20), pygame.Rect(320, 270, 20, 20)]

        # Simulate reading from 5 files
        self.read_file("config.txt")
        self.read_file("map.txt")
        self.read_file("instructions.txt")
        self.read_file("levels.dat")
        self.read_file("savegame.json")

    def read_file(self, filename):
        print(f"Reading {filename}... (simulated)")

    def save_score(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.score))

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, (x, y))

    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.screen.blit(self.assets['bg'], (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.on_ground:
                        self.vel_y = -12
                        self.sounds['jump'].play()
                    if event.key == pygame.K_q:
                        self.quit_game()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: self.player.x -= 5
            if keys[pygame.K_RIGHT]: self.player.x += 5

            self.vel_y += self.gravity
            self.player.y += self.vel_y
            self.on_ground = False

            # Collisions
            for plat in self.platforms:
                if self.player.colliderect(plat):
                    if self.vel_y > 0 and self.player.bottom <= plat.bottom:
                        self.player.bottom = plat.top
                        self.vel_y = 0
                        self.on_ground = True

            # Collect stars
            collected = [star for star in self.stars if self.player.colliderect(star)]
            for star in collected:
                self.stars.remove(star)
                self.sounds['collect'].play()
                self.score += 1

            # Draw everything
            for plat in self.platforms:
                self.screen.blit(self.assets['platform'], plat.topleft)
            for star in self.stars:
                self.screen.blit(self.assets['star'], star.topleft)
            self.screen.blit(self.assets['player'], self.player.topleft)

            self.draw_text(f"Score: {self.score}", 10, 10)
            self.draw_text("Press Q to quit", 10, 40)

            # Win condition
            if not self.stars:
                self.screen.blit(self.assets['win'], (0, 0))
                self.draw_text("YOU WIN!", 330, 250)
                self.draw_text("Press Q to quit", 310, 300)
                self.save_score()

            pygame.display.flip()

    def quit_game(self):
        print("Saving and exiting...")
        self.save_score()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = BlockRunner()
    game.run()