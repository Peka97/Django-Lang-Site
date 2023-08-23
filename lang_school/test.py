from datetime import datetime
from calendar import monthrange
from pytz import timezone


def generate_calendar(lessons: list):
    tzname = 'Europe/Moscow'
    current_cell = 0
    day_idx = 0

    result = '<tr class="table-row"></tr>'
    today = datetime.now(timezone(tzname))
    weekday_start_month = datetime(today.year, today.month, 1).weekday()
    days = monthrange(today.year, today.month)

    result += '<tr class="table-row"></tr>'

    for _ in range(weekday_start_month):
        result += '<td class="table-date nil"></td>'
        current_cell += 1

    while True:
        if current_cell == 7:
            current_cell = 0
            result += '</tr><tr class="table-row">'
        try:
            current_day = days[day_idx]
        except IndexError:
            result += '</tr>'
            break
        class_name = 'table-date'

        if current_day == today.day:
            class_name += ' active-date'

        for lesson in lessons:
            lesson_day = datetime.strptime(
                lesson.time, 'YYYY-MM-DD HH:MM'
            ).day()

            if lesson_day == current_day:
                class_name += ' event day'

        result += f'<td class="{class_name}">{current_day}</td>'

        current_cell += 1

    return result


if __name__ == '__main__':
    generate_calendar([])
