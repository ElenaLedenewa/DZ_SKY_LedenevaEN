from typing import Union
from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_widget: Union[str]) -> str:
    """Функция принимает на вход только один аргумент — строку, которая
    состоит из требуемых частей. Это может быть строка типа
    Visa Platinum 7000 7922 8960 6361,
    или Maestro 7000 7922 8960 6361,
    или Счет 73654108430135874305.
    Возвращает исходную строку с замаскированным номером карты/счета."""

    prefix_widget = ''
    number_widget = ''

#    for sym in card_or_account_widget:
#        if not sym.isdigit():
#           prefix_vidget = prefix_vidget + sym
#        else

    widgets_list = card_or_account_widget.split(" ")
    prefix_widget = ""
    number_widget1 = ""

    if widgets_list[0].lower() == 'счет':
        prefix_widget = 'Счет'
        number_widget = prefix_widget + " " + get_mask_account(widgets_list[1])
    else:
        for widget in widgets_list:
            if widget.isalpha():
                prefix_widget = prefix_widget + widget + " "
            else:
                number_widget1 = number_widget1 + widget
        number_widget = prefix_widget + get_mask_card_number(number_widget1)

    return number_widget


def get_data(str_data: Union[str]) -> str:
    """Функция, которая принимает на вход строку вида
       2018-07-11T02:26:18.671407
       и возвращает строку с датой в виде
       11.07.2018"""

    st_data = str_data[8:10] + "." + str_data[5:7] + "." + str_data[0:4]

    return st_data
