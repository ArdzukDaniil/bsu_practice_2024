def month(month_number, lang):
    if lang == "ru":
        months_ru = [
            'Январь', 'Февраль', 'Март', 'Апрель',
            'Май', 'Июнь', 'Июль', 'Август',
            'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ]
        return months_ru[month_number - 1]
    elif lang == "en":
        months_en = [
            'January', 'February', 'March', 'April',
            'May', 'June', 'July', 'August',
            'September', 'October', 'November', 'December'
        ]
        return months_en[month_number - 1]
    else:
        return "Unsupported language"
