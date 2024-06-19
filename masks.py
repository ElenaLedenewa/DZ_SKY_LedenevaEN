from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция маскировки номера карты. Функция принимает на вход номер карты и возвращает
    ее маску.  Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX .
    Т. е. видны первые 6 цифр и последние 4, номер разбит по блокам по 4 цифры,
    разделенным пробелами.
     Пример работы функции, возвращающей маску карты
        7000792289606361     # входной аргумент
        7000 79** **** 6361  # выход функции
    """

    card_number_work = card_number

    if card_number_work.isdigit() and len(card_number_work) == 16:
        mask_card_number = card_number_work.replace(card_number_work[6:12], "** **** ")
        card_number_work = mask_card_number
        mask_card_number = card_number_work[0:4] + " " + card_number_work[4:]
    else:
        mask_card_number = "некорректный номер карты"

    return mask_card_number


def get_mask_account(bank_account_number: Union[str]) -> str:
    """Функция маскировки номера счета. Функция принимает на вход номер счета
    и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX. Т. е. видны только последние 4 цифры.
    Пример работы функции, возвращающей маску счета
      73654108430135874305  # входной аргумент
      **4305  # выход функции
    """

    account_number_work = bank_account_number

    if account_number_work.isdigit() and len(account_number_work) == 20:
        mask_account = "**" + account_number_work[16:]
    else:
        mask_account = "некорректный номер счета"

    return mask_account
