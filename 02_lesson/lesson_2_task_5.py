def month_to_season(month):
    if month == 12 or month == 1 or month == 2:
        return "Зима"
    if month == 3 or month == 4 or month == 5:
        return "Весна"
    if month == 6 or month == 7 or month == 8:
        return "Лето"
    if month == 9 or month == 10 or month == 11:
        return "Лето"


month = 2
season = month_to_season(month)

print(season)
