# -*- coding: utf-8 -*-
# @Time    : 2023/4/30 11:07 AM
# @Author  : Patrick
# @Email   : firechecking@gmail.com
# @File    : problem_01.py
# @Software: GeometryAnimation
# @Description: problem_01

import sys

sys.path.append('../../')
from manimlib import *
from common.common import TextTitle, Comment


class Solution(Scene):
    def _draw_problem(self):
        color = BLACK
        s = '命题01：在一段给定的有限直线上，作一个等边三角形'
        text = TextTitle(s, color=color, font='STKaiti', font_size=40).to_edge(UP, buff=0.25)
        line = Line(color=color)

        dot_A = Dot(line.start, color=color)
        label_A = Text("A", color=color)
        label_A.next_to(dot_A, DOWN)
        dot_B = Dot(line.end, color=color)
        label_B = Text("B", color=color)
        label_B.next_to(dot_B, DOWN)

        self.play(Write(text))
        self.wait()

        self.add(dot_A)
        self.add(label_A)
        self.play(ShowCreation(line))
        self.add(dot_B)
        self.add(label_B)
        self.wait()
        return line

    def _draw_solution(self, line):
        color = BLUE

        with Comment(self, "【公设3】以任意点为心，以任意距离，可以画圆", text_style={"画圆": RED}):
            circle_1 = Circle(arc_center=line.start, radius=line.get_length(), color=color)
            circle_2 = Arc(-PI, TAU, arc_center=line.end, radius=line.get_length(), color=color)

            self.play(ShowCreation(circle_1))
            self.wait()
            self.play(ShowCreation(circle_2))
            self.wait()

        with Comment(self, "【公设1】由任意一点到另外任意一点，可以画直线", text_style={"画直线": RED}):
            dot_C = Dot(circle_1.point_from_proportion(1 / 6), color=color)
            label_C = Text("C", color=color)
            label_C.next_to(dot_C, UP)

            self.add(dot_C)
            self.add(label_C)

            self.play(ShowCreation(Line(start=dot_C.get_center(), end=line.start, color=color)))
            self.wait()
            self.play(ShowCreation(Line(start=dot_C.get_center(), end=line.end, color=color)))
            self.wait()
        return dot_C

    def _draw_result(self, line, dot):
        color = RED
        with Comment(self,
                     "【定义15】圆是由一条线围成的平面图形，其内有一点与这条线上的点连成的所有线段都相等\n【公理1】等于同量的量彼此相等",
                     disappear=False):
            self.play(ShowCreation(Line(start=dot.get_center(), end=line.start, color=color, stroke_width=10)))
            self.play(ShowCreation(Line(start=line.start, end=line.end, color=color, stroke_width=10)))
            self.play(ShowCreation(Line(start=line.end, end=dot.get_center(), color=color, stroke_width=10)))
            self.wait(3)

    def construct(self):
        line = self._draw_problem()
        dot = self._draw_solution(line)
        self._draw_result(line, dot)


if __name__ == "__main__":
    solution = Solution()
    solution.construct()
