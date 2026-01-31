def measurements(measure):
    def area(measure_area):
        if len(measure_area) == 1:
            return measure_area[0] * measure_area[0]
        elif len(measure_area) == 2:
            rec_area = measure_area[0] * measure_area[1]
            return rec_area
        else:
            raise IndexError
    def perimeter(measure_perimeter):
        if len(measure_perimeter) == 1:
            return measure_perimeter[0] * 4
        elif len(measure_perimeter) == 2:
            rec_per = measure_perimeter[0] * 2 + measure_perimeter[1] * 2
            return rec_per
        else:
            raise IndexError
    try:
        area_mes = area(measure)
        perimeter_mes = perimeter(measure)

    except IndexError:
        return "Input 1 or 2 measurements!"
    return "Perimeter = {} Area = {}".format(perimeter_mes, area_mes)
    `
if __name__ == '__main__':
    try:
        measurements([4,5])
    except IndexError:
        raise IndexError


