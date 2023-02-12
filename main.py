import library


def user_deposit():
    summa = library.get_user_numbers()
    hryvna , coins = str(summa).split('.')
    result_hryvna = library.get_national_ua_money(hryvna)
    result_coins = library.get_national_ua_coins(coins)
    hryvna , coins = library.get_user_numbers_for_list(summa)
    return (f'Введенная Вами сумма - {hryvna} {result_hryvna} {coins} {result_coins}')



print(user_deposit())



