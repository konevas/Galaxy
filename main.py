from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        # print(f"w: {self.width} h: {self.height}")

    def on_parent(self, widget, parent):
        # print(f"on_parent: w: {self.width} h: {self.height}")
        pass

    def on_size(self, *args):
        # print(f"on_size: w: {self.width} h: {self.height}")
        # self.perspective_point_x = self.width / 2
        # self.perspective_point_y = self.height * 0.75

    def on_perspective_point_x(self, widget, value):
        # print(f"PX: w: {value}")
        pass

    def on_perspective_point_y(self, widget, value):
        # print(f"PY: w: {value}")
        pass

class Galaxy(App):
    pass


if __name__ == '__main__':
    Galaxy().run()
