""" lambeq's drawing module. """

__all__ = [
    'Equation',
    'DrawableDiagram',

    'draw',
    'draw_equation',
    'draw_pregroup',
    'to_gif',

    'COLORS',
    'SHAPES'
]

from lambeq.backend.drawing.drawing import (draw, draw_equation,
                                            draw_pregroup, to_gif)
from lambeq.backend.drawing.drawing_backend import COLORS, SHAPES
from lambeq.backend.drawing.drawable import DrawableDiagram
