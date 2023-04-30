# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 6:07 PM
# @Author  : Patrick
# @Email   : firechecking@gmail.com
# @File    : common.py
# @Software: GeometryAnimation
# @Description: common

from manimlib import *


class TextTitle(MarkupText):
    def __init__(self, *args, **kwargs):
        super(TextTitle, self).__init__(*args, **kwargs)

        underline = Line(LEFT, RIGHT, color=kwargs['color'])
        underline.next_to(self, DOWN, buff=0.25)
        underline.set_width(FRAME_WIDTH - 2)
        self.add(underline)
        self.underline = underline


class Comment():
    def __init__(self, scene, text, color=BLACK, text_style=None, disappear=True):
        self.scene = scene
        self.text = text
        self.color = color
        self.text_style = text_style if text_style else {}
        self.disappear = disappear

    def __enter__(self):
        self.comment = Text(self.text,
                            color=self.color,
                            font='STKaiti',
                            font_size=30,
                            ).to_edge(DOWN, buff=0.25)
        if self.text_style:
            self.comment.set_color_by_text_to_color_map(self.text_style)
        self.scene.play(Write(self.comment))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.disappear:
            self.scene.play(FadeOut(self.comment))
