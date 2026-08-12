"""
hud.py — the Siri-style liquid-glass waveform HUD.

Drawing functions are factored out so main.py can `from hud import draw_hud,
init_hud` instead of duplicating this ~150 lines of pygame code (your
original main.py had a full copy-paste of this file inline — now there's
one copy).

Run this file directly to test the HUD on its own with keyboard shortcuts:
  1 = toggle ELIX | 2 = fake detections | 3 = fake notification | Q = quit
"""

import pygame
import math
import time
import random
from datetime import datetime

WIDTH, HEIGHT = 480, 320

DARK = (8, 8, 12)
CYAN = (0, 255, 255)
CYAN_DIM = (0, 80, 100)
GREEN = (0, 255, 100)
RED = (255, 60, 60)
GRAY = (40, 40, 40)

WAVE_COLORS = [
    (120, 60, 255),
    (0, 120, 255),
    (0, 220, 255),
    (255, 80, 120),
    (255, 140, 60),
]
_wave_offsets = [random.uniform(0, math.pi * 2) for _ in WAVE_COLORS]
_wave_speeds = [0.8, 1.1, 0.6, 1.3, 0.9]
_wave_amps = [18, 22, 15, 20, 16]

_fonts = {}


def init_hud():
    """Call once after pygame.init(). Returns (screen, clock)."""
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("XonFrame - E.L.I.X")
    _fonts["large"] = pygame.font.SysFont("consolas", 28, bold=True)
    _fonts["medium"] = pygame.font.SysFont("consolas", 16, bold=True)
    _fonts["small"] = pygame.font.SysFont("consolas", 12)
    _fonts["tiny"] = pygame.font.SysFont("consolas", 10)
    return screen, pygame.time.Clock()


def draw_corner_brackets(surface, x, y, w, h, color, size=14):
    pygame.draw.line(surface, color, (x, y), (x + size, y), 1)
    pygame.draw.line(surface, color, (x, y), (x, y + size), 1)
    pygame.draw.line(surface, color, (x + w, y), (x + w - size, y), 1)
    pygame.draw.line(surface, color, (x + w, y), (x + w, y + size), 1)
    pygame.draw.line(surface, color, (x, y + h), (x + size, y + h), 1)
    pygame.draw.line(surface, color, (x, y + h), (x, y + h - size), 1)
    pygame.draw.line(surface, color, (x + w, y + h), (x + w - size, y + h), 1)
    pygame.draw.line(surface, color, (x + w, y + h), (x + w, y + h - size), 1)


def draw_glass_orb(surface, cx, cy, radius, t, active):
    glow_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    if active:
        for i in range(8):
            alpha = int(15 - i * 1.5)
            r = radius + i * 6
            for color in [(120, 60, 255), (0, 120, 255), (255, 80, 120)]:
                pygame.draw.circle(glow_surf, (*color, max(0, alpha)), (cx, cy), r, 2)
    surface.blit(glow_surf, (0, 0))

    if active:
        wave_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        num_points = 120
        for wave_idx, color in enumerate(WAVE_COLORS):
            points_top, points_bottom = [], []
            speed = _wave_speeds[wave_idx]
            amp = _wave_amps[wave_idx]
            offset = _wave_offsets[wave_idx]
            for i in range(num_points + 1):
                angle = (i / num_points) * math.pi * 2
                x = cx + radius * math.cos(angle)
                y_base = cy + radius * 0.15 * math.sin(angle * 2 + t * 0.5)
                wave = amp * math.sin(angle * 3 + t * speed + offset)
                wave += (amp * 0.5) * math.sin(angle * 5 + t * speed * 1.4 + offset)
                dist = math.sqrt((x - cx) ** 2 + (y_base - cy) ** 2)
                if dist < radius - 4:
                    points_top.append((x, y_base + wave))
                    points_bottom.append((x, y_base - wave * 0.6))
            if len(points_top) > 2:
                alpha = 180 if wave_idx == 0 else 120 - wave_idx * 15
                pygame.draw.lines(wave_surf, (*color, alpha), False, points_top, 2)
            if len(points_bottom) > 2:
                alpha = 100 if wave_idx == 0 else 80 - wave_idx * 10
                pygame.draw.lines(wave_surf, (*color, alpha), False, points_bottom, 1)
        surface.blit(wave_surf, (0, 0))

    orb_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    pygame.draw.circle(orb_surf, (200, 200, 255, 50), (cx, cy), radius, 2)
    hx, hy = cx - int(radius * 0.3), cy - int(radius * 0.3)
    pygame.draw.circle(orb_surf, (255, 255, 255, 15), (hx, hy), int(radius * 0.15), 0)
    surface.blit(orb_surf, (0, 0))

    if not active:
        pulse = 0.3 + 0.1 * math.sin(t * 1.5)
        idle_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.circle(idle_surf, (0, 180, 220, int(60 * pulse)), (cx, cy), int(radius * 0.5), 2)
        surface.blit(idle_surf, (0, 0))


def draw_hud(screen, clock, t, state):
    font_large, font_medium = _fonts["large"], _fonts["medium"]
    font_small, font_tiny = _fonts["small"], _fonts["tiny"]

    screen.fill(DARK)
    for x in range(0, WIDTH, 40):
        pygame.draw.line(screen, (15, 15, 20), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 40):
        pygame.draw.line(screen, (15, 15, 20), (0, y), (WIDTH, y))

    orb_cx, orb_cy, orb_r = 130, 185, 75
    draw_glass_orb(screen, orb_cx, orb_cy, orb_r, t, state["elix_active"])
    draw_corner_brackets(screen, 45, 100, 170, 170, CYAN_DIM)

    pygame.draw.line(screen, CYAN_DIM, (0, 68), (WIDTH, 68), 1)
    now = datetime.now()
    screen.blit(font_large.render(now.strftime("%H:%M"), True, CYAN), (20, 15))
    screen.blit(font_tiny.render(now.strftime("%A  %B %d"), True, (80, 80, 100)), (22, 50))

    batt = state["battery_percent"]
    bc = GREEN if batt > 30 else RED
    screen.blit(font_tiny.render(f"PWR  {batt}%", True, bc), (WIDTH - 95, 18))
    pygame.draw.rect(screen, bc, (WIDTH - 95, 33, 36, 7), 1)
    pygame.draw.rect(screen, bc, (WIDTH - 94, 34, int(34 * batt / 100), 5))
    conn = "● LINKED" if state["connected"] else "● OFFLINE"
    screen.blit(font_tiny.render(conn, True, GREEN if state["connected"] else RED), (WIDTH - 95, 48))

    if state["elix_active"]:
        blink = int(t * 2) % 2 == 0
        label, color = ("LISTENING" if blink else "E.L.I.X"), CYAN
    else:
        label, color = "E.L.I.X  READY", CYAN_DIM
    label_surf = font_small.render(label, True, color)
    screen.blit(label_surf, (orb_cx - label_surf.get_width() // 2, 270))

    panel_x = 240
    pygame.draw.line(screen, CYAN_DIM, (panel_x - 15, 80), (panel_x - 15, HEIGHT - 40), 1)
    screen.blit(font_small.render("[ VISUAL SCAN ]", True, CYAN_DIM), (panel_x, 85))
    pygame.draw.line(screen, CYAN_DIM, (panel_x, 102), (WIDTH - 20, 102), 1)

    if state["detections"]:
        for i, obj in enumerate(state["detections"][:4]):
            bar_w = int(140 * (0.95 - i * 0.1))
            pygame.draw.rect(screen, (0, 60, 30), (panel_x, 112 + i * 28, bar_w, 18))
            pygame.draw.rect(screen, GREEN, (panel_x, 112 + i * 28, bar_w, 18), 1)
            screen.blit(font_tiny.render(obj.upper(), True, GREEN), (panel_x + 5, 116 + i * 28))
    else:
        screen.blit(font_tiny.render("NO TARGETS", True, GRAY), (panel_x, 115))
        screen.blit(font_tiny.render("MOTION WATCH ON", True, GRAY), (panel_x, 132))

    pygame.draw.line(screen, CYAN_DIM, (0, HEIGHT - 38), (WIDTH, HEIGHT - 38), 1)
    if state["notification"]:
        blink = int(time.time() * 2) % 2 == 0
        notif_color = CYAN if blink else CYAN_DIM
        pygame.draw.rect(screen, (0, 20, 30), (0, HEIGHT - 38, WIDTH, 38))
        screen.blit(font_tiny.render(f">> {state['notification'][:55]}", True, notif_color), (15, HEIGHT - 25))
    else:
        screen.blit(font_tiny.render("XONFRAME v0.1  //  ELIX ONLINE", True, (50, 50, 70)), (15, HEIGHT - 25))

    draw_corner_brackets(screen, 4, 4, WIDTH - 8, HEIGHT - 8, CYAN_DIM, size=18)
    screen.blit(font_tiny.render(f"{int(clock.get_fps())}fps", True, GRAY), (WIDTH - 40, HEIGHT - 25))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    screen, clock = init_hud()
    state = {
        "battery_percent": 82, "connected": True, "detections": [],
        "elix_active": False, "notification": "",
    }
    start_time = time.time()
    running = True
    print("E.L.I.X HUD test mode — 1=toggle elix 2=fake detections 3=fake notif Q=quit")
    while running:
        t = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    state["elix_active"] = not state["elix_active"]
                if event.key == pygame.K_2:
                    state["detections"] = ["person", "laptop", "bottle", "phone"]
                if event.key == pygame.K_3:
                    state["notification"] = "ALERT: Motion detected in frame"
                if event.key == pygame.K_q:
                    running = False
        draw_hud(screen, clock, t, state)
        clock.tick(30)
    pygame.quit()
