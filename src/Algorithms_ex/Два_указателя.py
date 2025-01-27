"""
Найти максимальное число одинаковых подряд идущих символов в строке.
"""


def max_repeats(s):
    if not s:
        return 0
    result, current_idx = 0, 0
    while current_idx < len(s):
        next_idx = current_idx + 1
        while next_idx < len(s) and s[next_idx] == s[current_idx]:
            next_idx += 1
        result = max(result, next_idx - current_idx)
        current_idx = next_idx
    return result

# Тесты
def test_max_repeats():
    assert max_repeats('aaabb') == 3
    assert max_repeats('abbb') == 3
    assert max_repeats('ababab') == 1
    assert max_repeats('') == 0
    assert max_repeats('a') == 1
    assert max_repeats('aa') == 2
    assert max_repeats('aaa') == 3
    assert max_repeats('ab') == 1
    assert max_repeats('abc') == 1
    assert max_repeats('abbc') == 2
    assert max_repeats('abcc') == 2 

    print("All tests passed successfully.")

test_max_repeats()



