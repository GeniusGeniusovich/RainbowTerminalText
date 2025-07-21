from RainbowTerminalText import*

""" 
    Это официальный инстуркционный документ для взаимодействия и работы с библиотекой RainbowTerminalText.
    Разработчик библиотеки : Саддам Муслим 
    Для обратной свзяи напишите на наш телеграмм: @SaddaMusliM
    YouTube : @ZlodeyBobr

    Библиотека несет в себе задачу упростить и облегчить пользователям возможность преминения / вывода текстов различных цветов 
    в терминале вашего текстового редактора / терминала


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

"""
wm_terminal = RainbowTerminalText()
wm_terminal .  wm_print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ' , wm_text= wm_white_text , wm_style= wm_bold_text_style , wm_bg = wm_white_text_bg , end = '')
wm_terminal .  wm_print('ㅤㅤㅤㅤㅤㅤㅤWaterMelon RainbowTerminalText ㅤㅤㅤㅤ' , wm_text= wm_blue_text , wm_style= wm_bold_text_style , wm_bg = wm_blue_text_bg , end = '')
wm_terminal .  wm_print('ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ' , wm_text= wm_red_text , wm_style= wm_bold_text_style , wm_bg = wm_red_text_bg , end = '')
wm_terminal .  wm_print('if you need emptry message - use . ghost_message()' , wm_text= wm_red_text , wm_style= wm_bold_text_style , wm_bg = wm_red_text_bg , end = '')

wm_terminal . endless_terminal()