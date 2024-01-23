import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

"""
# Height and Width of Widgets
Question when use GridLayout as saied its filled the screen with predefined width and height to fill the screen
  but what should we do if we want to widgets have smaller or bigger height and width?
Answer We have to disable this GridLayout behaviour (Auto size widget i mean) by set size_hint_(x or y) to None value
  And then specify width(disable size_hint_x) and height(disable size_hint_y)
  But we have to do this for all widgets, its boreing right! we can use the row_force and col_force _defualt
    and set the default value for widgets inside the GridLayout with row_default_hight and col_default_width

 R   |      Col 1     |      Col 2      H g
 o 1 |                |                 e h 1
 w   |                |                 i t
---> | <- - - - - - > | <- - - - - ->
 R   |                |                 H g
 o 2 |                |                 e h 2
 w   |                |                 i t
            Width 1   |      Width2

مجبورش میکنی از مقدار گریدلیاوت رو که از مقدار پیش فرضش استفاده کنه بعدش میای مقدار
پیش فرض برای ارتفاع سطرها و عرض ستون ها انتخاب میکنیم وسلام

"""

class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout construct
        super().__init__(**kwargs)

        self.row_force_default = True
        self.row_default_height = 120
        self.col_force_default = True
        self.col_default_width = 100

        # set columns
        self.cols = 1

        # Create a second gridlayout

        self.top_grid = GridLayout(row_force_default = True,
                                   row_default_height = 40,
                                   col_force_default = True,
                                   col_default_width = 100)
        self.top_grid.cols = 2

        # NEW: Instead pass size_hint and height and width to all the widget we can ues
        #  Use col force default and row force default

        # Add widgets
        # everything is widgets
        self.top_grid.add_widget(Label(text="Name: ",
                                       size_hint_y=None,
                                       height=40,
                                       size_hint_x=None,
                                       width=100))
        self.name = TextInput(multiline=False,
                              size_hint_y=None,
                              height=40,
                              size_hint_x=None,
                              width=100)
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
        # NEW: Change size_hint_y to None means dont guess the heith of button
        #  And then Change it to 50
        self.submit = Button(text="Submit",
                             font_size=32,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=400)
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
