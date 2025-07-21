import os

reset_every =  "\033[0m"

wm_black_text = "\033[30m"
wm_red_text = "\033[31m"
wm_green_text = "\033[32m"
wm_yellow_text = "\033[33m"
wm_blue_text = "\033[34m"
wm_white_text = "\033[37m"

wm_black_text_bg = "\033[40m"
wm_red_text_bg = "\033[41m"
wm_green_text_bg = "\033[42m"
wm_yellow_text_bg = "\033[43m"
wm_blue_text_bg = "\033[44m"
wm_white_text_bg = "\033[47m"

wm_reset_text_style = "\033[0m"
wm_bold_text_style = "\033[1m"
wm_italic_text_style = "\033[3m"
wm_underline_text_style = "\033[4m"

class RainbowTerminalText:
    info = "ITS PROJECT #0003 - OF Saddam Muslim || WE WANT TO HELP YOU"
    author = 'Saddam Muslim'

    def __init__(self):
        if os.name == 'nt':
            os.system("")
    def wm_print(self , *args , wm_text = wm_white_text , wm_bg = wm_black_text_bg , wm_style = wm_reset_text_style , space = ' ' , end = '\n'):
        wm_outtup_text = space.join(str(arg) for arg in args)
        self . reset_every =  "\033[0m"

        self .wm_outtup_end_test = f"{wm_style}{wm_text}{wm_bg}{wm_outtup_text}{self . reset_every}{end}"
        print(self . wm_outtup_end_test )
        
    def ghost_message(self):
        print('-ㅤㅤㅤ-')

    def endless_terminal(self):
        print("Work started successfully")

        while True:
            try:
                wait = input(">_$ㅤ")
                exec(wait)
            except NameError:
                print('Error - Error Type ^NameError / Python does not process free text.')
                print(NameError)
            except TypeError:
                print('Error - Error Type ^TypeError / Python does not process free text.')
                print(TypeError)
            except SyntaxError:
                print('Error - Error Type ^SyntaxError / Python does not process free text.')
                print(SyntaxError)
            except AttributeError:
                print('Error - Error Type ^AttributeError / Python does not process free text.')
                print(AttributeError)