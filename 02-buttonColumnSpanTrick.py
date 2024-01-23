import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


"""
# Span Column Trick for GridLayout
Gridlayout use guess approach to fill the grid with widgets (and defined cols)
Question is in this situation when elements is odd, all cell does not filled so one element filled part of
  screen, and result is ugliness
Solution is use the *Nested* gridlayout, the parent gridlayout has one column and the nested ha n-columnt
  so the last element fill the bottom of the screen
  Note that nested gridlayout has to be added to parent widget with call add_widget method with nested widget
    as parameter
"""

# Fix the gap in 2 cols by
#  embedding a 2 cols grid into 1 col grid layout
#  its trick.

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout construct
        super().__init__(**kwargs)

        # set columns
        self.cols = 1

        # Create a second gridlayout

        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets
        # everything is widgets
        self.top_grid.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        self.top_grid.add_widget(Label(text="Fav Pizza: "))
        self.pizza = TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)

        self.top_grid.add_widget(Label(text="Fav Color: "))
        self.color = TextInput(multiline=False)
        self.top_grid.add_widget(self.color)

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)

        # Create a submit button
        # Next lesson span on grid layout
        self.submit = Button(text="Submit", font_size = 32)
        # To do someting, bind to function
        # when press left button called self.press *method*
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, event):
        # When define a callback method we send the instase of calling object
        # Calling object or Event instance ????
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        print(f"Hello \"{name}\", you like Pizze \"{pizza}\""
              f"and your favorite color is \"{color}\"!")

        # Print it to the screen
        self.add_widget(Label(text=f"Hello \"{name}\", you like Pizze \"{pizza}\""
                                   f"and your favorite color is \"{color}\"!"))

        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        # return Label(text="Hello World", font_size=18)
        return MyGridLayout()


if __name__ == "__main__":
    MyApp().run()
