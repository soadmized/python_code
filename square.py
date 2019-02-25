def square(length):
    perimeter = 4 * length
    square = pow(length, 2)
    dia = pow(2 * pow(length, 2), 0.5)
    return perimeter, square, dia
