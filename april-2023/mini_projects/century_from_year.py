def century(year):
    if (int(year) % 100) == 0:
        return (year / 100)
    else: return round((int(year) / 100) + 0.5)

    century(1705)
century(1900)
century(1601)
century(2000)
century(356)
century(89)
