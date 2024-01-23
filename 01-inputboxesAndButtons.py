import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

"""
Every GUI element called widget and imported from kivy.uix."widget_module" and the call the widget class capitalize

# GridLayout
Here we define our grid class derivered from gridlayout, like other object oriented approach we call the
  parent constractor first with infinit keywords parameter (**kwargs).
GridLayout object hast cols property that define the number of columns.
Each widget have to attach to to ther each cell with add_widget(Object) method.
Because we define gridlayout as the root widget and define other widgets inside them, we sould return
  an instance of MyGridLayout() within build method.

# TextBox
Textbox can be multiline or singleline if provide boolean parameter multiline = False/True
Since we need the value of textbox use self.blahblah property as holder for textbox object to use its value,
  otherwise it can used like *Label* that just used to show a fixed text
To set and get text we use .text property
To set the font size use .font_size argument/(property if used in class)

# Button
Obviousley, used to interact with software.
It has text and font_size property too.
Specific method is bind() that used to callback to an event, like "on_press" event .bind(on_"event"=method)
  when define bind method we have to specify an extra argument for
  event instance or called object instance IDK exactly?
We can call add_widget with new widget as argument and it create will be created when user press the button,

"""


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout construct
        super().__init__(**kwargs)

        # set columns
        self.cols = 2

        # Add widgets
        # everything is widgets
        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Fav Pizza: "))
        self.pizza = TextInput(multiline=False,
                               font_size=32)
        self.add_widget(self.pizza)

        self.add_widget(Label(text="Fav Color: "))
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        # Create a submit button
        # Next lesson span on grid layout
        self.submit = Button(text="Submit",
                             font_size=32)
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
