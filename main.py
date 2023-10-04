from equation import Equation
from time import sleep
from Print_color import print_Color

def run_balance():
    """
    Runs the chemical equation balance algorithm
    """
    print_Color('Insert chemical equation with elements in\nparentheses followed by the number of atoms:', ['yellow'])
    print_Color('~*Example: ~*(H)2 ~*+ ~*(O)2~* = ~*(H)2(O)1', ['cyan', 'magenta', 'yellow', 'magenta', 'yellow', 'magenta'], advanced_mode=True)
    print_Color('>>> ', ['green'], print_END='') 
    user_input = input('')
    try:
        equation = Equation(user_input)
        print_Color('Balanced equation: ' + equation.balance(), ['yellow', 'green'], advanced_mode=True) # made by artinnavidgoli
        sleep(3)
        run_balance()
    except IndexError:
        print_Color('Invalid input...', ['red'])
        sleep(3)
        run_balance()

run_balance()
