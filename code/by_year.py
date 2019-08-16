

def count_sundays(year, day, total=0):
    """Cuenta el total de ocaciones que un año empieza en domingo durante
    el siglo XX y retorna el resultado."""

    if year >= 2000:
        return total

    if _check_sunday(day):
        total += 1

    next_day = _check_index_day(day, _leap_year(year))
    year += 1
    count_sundays(year, next_day, total)


def _check_index_day(index_day, value_to_add):
    """ Retorna el indice del día de inicio de año.

        Suma el valor de
            : index_day + value_to_add

        Tiene en cuenta que el indice maximo no puede
        ser mayor a 6 (siendo 6 domingo).

        Si es mayor a seis resta la diferencia entre el valor
        resultante de la suma anterior y 6. A este resultado se le resta
        uno generando el nuevo indice.

    """

    result = index_day + value_to_add

    if result > 6:
        return (result - 6) - 1
    else:
        return result


def _check_sunday(day):
    """ Retorna True si el dia es Domingo."""
    week_days = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]

    if week_days[day] == 'sunday':
        return True
    else:
        return False


def _leap_year(year):
    """ Retorna:
        2, si el año es bisiesto.
        1, si NO lo es."""

    if year % 100 == 0:
        # Inicio de siglo
        if year % 400 == 0:
            return 1
        else:
            return 1
    elif year % 4 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    count_sundays(1900, 0, total=0)
