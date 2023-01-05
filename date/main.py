def is_leap_year(year: str = '') -> bool:
    """
    判断是否是闰年
    普通闰年：公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年等就是闰年）。
    世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是闰年，2000年是闰年）。

    :param year: str 要判断的年份
    :return: bool 返回判断结果
    """
    year = int(year)
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
