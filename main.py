# File name:main.py

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRoundFlatButton
from math import sqrt


class CustomButton(MDRoundFlatButton):
    pass


class CustomOpButton(MDRoundFlatButton):
    pass


class CalcScreen(MDScreen):

    def on_power_press(self):
        if self.ids.calc_screen.text == "":
            self.ids.calc_screen.text = "0"
            self.ids.calc_screen.background_color = "#e5e5e5"  # couleur blanc-sale
            self.ids.btn_power.icon_color = "lime"
        else:
            self.ids.calc_screen.text = ""
            self.ids.calc_screen.background_color = "#0a0908"  # couleur noir
            self.ids.btn_power.icon_color = "white"

    def button_press(self, button):

        screen_value = self.ids.calc_screen.text
        if "Error" in screen_value:
            screen_value = ""
        if screen_value == "0":
            self.ids.calc_screen.text = ""
            self.ids.calc_screen.text = f"{button}"
        else:
            self.ids.calc_screen.text = ""
            self.ids.calc_screen.text = f"{screen_value}{button}"

    def on_clear(self):
        self.ids.calc_screen.text = "0"

    def on_correction(self):
        screen_value = self.ids.calc_screen.text
        self.ids.calc_screen.text = screen_value[:-1]

    def on_Equal_press(self):
        newOp = True
        if newOp == True:
            screen_value = self.ids.calc_screen.text

            try:
                valeurs = eval(screen_value)
                self.ids.calc_screen.text = str(valeurs)
            except:
                self.ids.calc_screen.text = "Error"

    def on_exp_press(self, base, exp):
        screen_value = self.ids.calc_screen.text
        base = (screen_value)
        return base ** exp

    def on_operator_sign(self, sign):
        screen_value = self.ids.calc_screen.text
        self.ids.calc_screen.text = f"{screen_value}{sign}"

    def on_dot_press(self):
        screen_value = self.ids.calc_screen.text
        numberList = screen_value.split("+")
        if "+" in screen_value and "." not in numberList[-1]:
            screen_value = f"{screen_value}."
            self.ids.calc_screen.text = screen_value
        elif "." in screen_value:
            pass
        else:
            screen_value = f"{screen_value}."
            self.ids.calc_screen.text = screen_value

    def on_plus_moins_press(self):
        screen_value = self.ids.calc_screen.text
        sign = "-"
        if sign in screen_value:
            screen_value = f'{screen_value.replace(sign, "")}'

            self.ids.calc_screen.text = f"{screen_value}"
        else:
            self.ids.calc_screen.text = f"{sign}{screen_value}"

    def on_percent_press(self, screen_value, const_k=0.01):
        screen_value = self.ids.calc_screen.text
        val_in_percent = eval(screen_value) * const_k
        valeur_rond = round(val_in_percent, 10)
        self.ids.calc_screen.text = f"{valeur_rond}"

    def on_racine_press(self):
        screen_value = self.ids.calc_screen.text
        racine = sqrt(float(screen_value))
        self.ids.calc_screen.text = f"{racine}"


class CalculatriceApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen = Builder.load_file('main.kv')
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

    def build(self):
        return self.screen


if __name__ == '__main__':
    CalculatriceApp().run()
