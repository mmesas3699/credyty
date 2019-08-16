
import calendar


def count_sundays():
    """Cuenta el total de ocaciones que un mes empieza en domingo
    por cada año del siglo XX y retorna el resultado"""
    total = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            day = calendar.monthrange(year, month)[0]

            if day == 6:
                total += 1

    print('Total: ', total)
    return total


if __name__ == '__main__':
    count_sundays()
