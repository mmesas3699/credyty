# credyty
Código para las purebas de Credyty

En el repositorio se encuentran dos archivos:
  - by_year.py: que genera el resultado por año.
  - by_month.py: que genera el resultado por mes.
  
## En el modulo: by_month.py:

  - Uso el modulo de la libreria estandar de Python: calendar (https://docs.python.org/3/library/calendar.html).
  - La función count_sundays() itera a través de cada mes de cada año del siglo XX.
  - Luego con la función calendar.monthrange(), que retorna el dia de inicio de cada mes más el número total de dias del mes
    , verifica que el día inicial del mes sea domingo.
  - Si el día es domingo suma uno a la variable total y continua con el mes siguiente, si no es domingo no suma y continua el   
    mes siguiente.
  - Cuando termina la iteración retorna total obtenido.
