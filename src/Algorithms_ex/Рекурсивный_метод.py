# написать функцию, которая принимает целое число и возвращает n-ное число Фибоначчи
def nth_fibonacci(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


nth_fibonacci(7)


def generate(n):
    result = []

    def generate_(left_open, left_closed, accum):
        if not left_open and not left_closed:
            result.append(''.join(accum))
            return
        if left_open:
            accum.append('(')
            generate_(left_open - 1, left_closed, accum)
            accum.pop()
        if left_closed > left_open:
            accum.append(')')
            generate_(left_open, left_closed - 1, accum)
            accum.pop()

    generate_(n, n, [])
    return result

generate()