import gspread
from datetime import date

import const


def create_date(date_str):
    if len(date_str) == const.DATE_LEN:
        date_str = "0" + date_str
    return date_str


def category_one_and_two_today(list_of_lists, title, values_list_date, today):
    res = ""
    for i in range(len(values_list_date)):
        # первая строка - это заголовок
        # первый столбец - дата начала, второй столбец - дата окончания
        #
        if i != 0:
            str_date_start = create_date(list_of_lists[i][0])
            str_date_finish = create_date(list_of_lists[i][1])

            day_start = int(str_date_start[0] + str_date_start[1])
            month_start = int(str_date_start[3] + str_date_start[4])
            year_start = int(str_date_start[6] + str_date_start[7] + str_date_start[8] + str_date_start[9])

            day_finish = int(str_date_finish[0] + str_date_finish[1])
            month_finish = int(str_date_finish[3] + str_date_finish[4])
            year_finish = int(str_date_finish[6] + str_date_finish[7] + str_date_finish[8] + str_date_finish[9])
            if ((day_start <= today.day) or (month_start <= today.month and year_start <= today.year)) and \
                     ((day_finish >= today.day and month_finish == today.month) or month_finish >= today.month or year_finish >= today.year):
                for j in range(len(title)):
                    res += "%s: %s \n" % (title[j], list_of_lists[i][j])
                res += '\n'
    return res


def parse_table_today():
    res = ""
    gc = gspread.service_account(filename='grantbot-356509-75d5aeebc133.json')
    # Открываем тестовую таблицу
    sh = gc.open("Гранты")

    # лист 1 - конкурсы
    # лист 2 - гранты
    # лист 3 - обучение
    # лист 4 - мероприятия
    worksheet = sh.get_worksheet(const.CATEGORY - 1)
    values_list_date = worksheet.col_values(1)
    today = date.today()
    if today.month < 10:
        today_str = "%d.0%d.%d" % (today.day, today.month, today.year)
    else:
        today_str = "%d.%d.%d" % (today.day, today.month, today.year)

    # Здесь мы получаем для каждой категории информацию
    # сегодня (если дата совпадает с сегодняшей)
    # в этом месяце (если месяц совпадает)
    # скоро (остальные, у которых месяц больше текущего, либо месяц меньше, но год больше)
    #

    # получим всю инфу с листа и выведем тольку ту, что нам нужна
    list_of_lists = worksheet.get_all_values()
    title = list_of_lists[0]  # заголовки нашей информации, будут жирными

    if const.CATEGORY == 1 or const.CATEGORY == 2:
        res = category_one_and_two_today(list_of_lists, title, values_list_date, today)
    else:
        for i in range(len(values_list_date)):
            # первая строка - это заголовок
            if i != 0 and list_of_lists[i][0] == today_str:
                for j in range(len(title)):
                    str = "%s: %s \n" % (title[j], list_of_lists[i][j])
                    res += str
                res += '\n'

    if len(res) == 0:
        res = "На сегодя событий не обнаружено"
    return res


def category_one_and_two_month(list_of_lists, title, values_list_date, today):
    res = ""
    for i in range(len(values_list_date)):
        # первая строка - это заголовок
        # первый столбец - дата начала, второй столбец - дата окончания
        if i != 0:
            str_date_start = create_date(list_of_lists[i][0])
            day_start = int(str_date_start[0] + str_date_start[1])
            month_start = int(str_date_start[3] + str_date_start[4])
            if month_start == today.month and day_start > today.day:
                for j in range(len(title)):
                    res += "%s: %s \n" % (title[j], list_of_lists[i][j])
                res += '\n'
    return res


def parse_table_month():
    res = ""
    gc = gspread.service_account(filename='grantbot-356509-75d5aeebc133.json')
    # Открываем тестовую таблицу
    sh = gc.open("Гранты")

    # лист 1 - конкурсы
    # лист 2 - гранты
    # лист 3 - обучение
    # лист 4 - мероприятия
    worksheet = sh.get_worksheet(const.CATEGORY - 1)
    values_list_date = worksheet.col_values(1)
    today = date.today()
    if today.month < 10:
        today_month_str = "0%d" % today.month
    else:
        today_month_str = "%d" % today.month
    # Здесь мы получаем для каждой категории информацию
    # сегодня (если дата совпадает с сегодняшей)
    # в этом месяце (если месяц совпадает)
    # скоро (остальные, у которых месяц больше текущего, либо месяц меньше, но год больше)
    #

    # получим всю инфу с листа и выведем тольку ту, что нам нужна
    list_of_lists = worksheet.get_all_values()
    title = list_of_lists[0]  # заголовки нашей информации, будут жирными

    if const.CATEGORY == 1 or const.CATEGORY == 2:
        res = category_one_and_two_month(list_of_lists, title, values_list_date, today)
    else:
        for i in range(len(values_list_date)):
            # первая строка - это заголовок
            if i != 0:
                str_month = create_date(list_of_lists[i][0])
                month = str_month[3] + str_month[4]
                if month == today_month_str:
                    for j in range(len(title)):
                        res += "%s: %s \n" % (title[j], list_of_lists[i][j])
                    res += '\n'

    if len(res) == 0:
        res = "В этом месяце событий не обнаружено"
    return res


def category_one_and_two_soon(list_of_lists, title, values_list_date, today):
    res = ""
    for i in range(len(values_list_date)):
        # первая строка - это заголовок
        # первый столбец - дата начала, второй столбец - дата окончания
        if i != 0:
            str_date_start = create_date(list_of_lists[i][0])

            month_start = int(str_date_start[3] + str_date_start[4])
            year_start = int(str_date_start[6] + str_date_start[7] + str_date_start[8] + str_date_start[9])
            if month_start > today.month or (month_start <= today.month and year_start > today.year):
                for j in range(len(title)):
                    res += "%s: %s \n" % (title[j], list_of_lists[i][j])
                res += '\n'
    return res


def parse_table_soon():
    res = ""
    gc = gspread.service_account(filename='grantbot-356509-75d5aeebc133.json')
    # Открываем тестовую таблицу
    sh = gc.open("Гранты")

    # лист 1 - конкурсы
    # лист 2 - гранты
    # лист 3 - обучение
    # лист 4 - мероприятия
    worksheet = sh.get_worksheet(const.CATEGORY - 1)
    values_list_date = worksheet.col_values(1)
    today = date.today()

    # получим всю инфу с листа и выведем тольку ту, что нам нужна
    list_of_lists = worksheet.get_all_values()
    title = list_of_lists[0]  # заголовки нашей информации, будут жирными

    if const.CATEGORY == 1 or const.CATEGORY == 2:
        res = category_one_and_two_soon(list_of_lists, title, values_list_date, today)
    else:
        for i in range(len(values_list_date)):
            # первая строка - это заголовок
            if i != 0:
                str_month = create_date(list_of_lists[i][0])
                if len(str_month) == 9:
                    str_month = "0" + str_month
                month = int(str_month[3] + str_month[4])
                year = int(str_month[6] + str_month[7] + str_month[8] + str_month[9])
                if (month > today.month) or (month < today.month and year > today.year):
                    for j in range(len(title)):
                        res += "%s: %s \n" % (title[j], list_of_lists[i][j])
                    res += '\n'

    if len(res) == 0:
        res = "Все события уже прошли"
    return res
