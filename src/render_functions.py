from __future__ import annotations

from typing import TYPE_CHECKING, Tuple

from src import color

if TYPE_CHECKING:
    from tcod import Console

    from src.engine import Engine
    from src.game_map import GameMap


def get_names_at_location(x: int, y: int, game_map: GameMap) -> str:
    if not game_map.in_bounds(x, y) or not game_map.visible[x, y]:
        return ""

    names = ", ".join(entity.name for entity in game_map.entities if entity.x == x and entity.y == y)

    return names.capitalize()


def render_hp_bar(console: Console, current_hp: int, maximum_hp: int, total_width: int, location: Tuple[int, int]) -> None:
    bar_width = int(float(current_hp) / maximum_hp * total_width)
    x, y = location

    console.draw_rect(x=x, y=y, width=total_width, height=1, ch=1, bg=color.hp_bar_empty)

    if bar_width > 0:
        console.draw_rect(x=x, y=y, width=bar_width, height=1, ch=1, bg=color.hp_bar_filled)

    console.print(x=x, y=y, string=f"HP: {current_hp}/{maximum_hp}", fg=color.bar_text)


def render_lvl_bar(console: Console, level: int, current_xp: int, maximum_xp: int, total_width: int, location: Tuple[int, int]) -> None:
    bar_width = int(float(current_xp) / maximum_xp * total_width)
    x, y = location

    console.draw_rect(x=x, y=y, width=total_width, height=1, ch=1, bg=color.lvl_bar_empty)

    if bar_width <= total_width:
        console.draw_rect(x=x, y=y, width=bar_width, height=1, ch=1, bg=color.lvl_bar_filled)

    console.print(x=x, y=y, string=f"LVL: {level} EXP: {current_xp}/{maximum_xp}", fg=color.bar_text)


def render_dungeon_level(console: Console, dungeon_level: int, location: Tuple[int, int]) -> None:
    """
    Render the level the player is currently on, at the given location.
    """
    x, y = location

    console.print(x=x, y=y, string=f"Dungeon level: {dungeon_level}")


def render_names_at_mouse_location(console: Console, x: int, y: int, engine: Engine) -> None:
    mouse_x, mouse_y = engine.mouse_location

    names_at_mouse_location = get_names_at_location(x=mouse_x, y=mouse_y, game_map=engine.game_map)

    console.print(x=x, y=y, string=names_at_mouse_location)
