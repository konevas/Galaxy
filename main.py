from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    VLINES_COUNT = 7
    VLINES_SPACING = .1
    vertical_lines = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"w: {self.width} h: {self.height}")
        self.init_vertical_line()

    def on_parent(self, widget, parent):
        # print(f"on_parent: w: {self.width} h: {self.height}")
        pass

    def on_size(self, *args):
        # print(f"on_size: w: {self.width} h: {self.height}")
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()

    def on_perspective_point_x(self, widget, value):
        # print(f"PX: w: {value}")
        pass

    def on_perspective_point_y(self, widget, value):
        # print(f"PY: w: {value}")
        pass

    def init_vertical_line(self):
        with self.canvas:
            Color(1, 1, 1)
            for line in range(0, self.VLINES_COUNT):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        center_x = int(self.width / 2)

        spacing = self.VLINES_SPACING * self.width
        offset = -int(self.VLINES_COUNT / 2)
        for index, line in enumerate(self.vertical_lines):
            line_x = int(center_x + offset * spacing)
            line.points = [
                line_x,
                0,
                line_x,
                self.height
            ]
            offset += 1

    def transform(self, x: float = 0, y: float = 0):
        MainWidget.transform_2d(x, y)

    @staticmethod
    def transform_2d(x, y):
        return x, y

    def transform_perspective(self, x, y):
        pass

class Galaxy(App):
    pass


if __name__ == '__main__':
    Galaxy().run()
