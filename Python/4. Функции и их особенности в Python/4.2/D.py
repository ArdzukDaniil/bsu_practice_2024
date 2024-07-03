def month(month_number, language="ru"):
    months_ru = [
        "январь", "февраль", "март", "апрель",
        "май", "июнь", "июль", "август",
        "сентябрь", "октябрь", "ноябрь", "декабрь"
    ]
    months_en = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    if language.lower() == "ru":
        return months_ru[month_number - 1].capitalize()
    elif language.lower() == "en":
        return months_en[month_number - 1]
