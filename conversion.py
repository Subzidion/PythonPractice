from math import pi


convert = {
        'k': {
            'c': lambda k: k - 273.15,
            'f': lambda k: (k - 273.15) * (9/5) + 32,
            'k': lambda k: k
            },
        'f': {
            'c': lambda f: (f - 32) * (5/9),
            'f': lambda f: f,
            'k': lambda f: (f - 32) * (5/9) + 273.15
            },
        'c': {
            'c': lambda c: c,
            'f': lambda c: c * (9/5) + 32,
            'k': lambda c: c + 273.15
            },
        'd': {
            'd': lambda d: d,
            'r': lambda d: r * pi * 180
            },
        'r': {
            'd': lambda r: r * 180/pi,
            'r': lambda r: r
            }
        }

while True:
    value = input()
    try:
        number, current, to = float(value[:-2]), value[-2:-1], value[-1:]
        print(str(convert[current][to](number)) + to)
    except KeyError:
        print("No candidate for conversion")
    except ValueError:
        print("Bad Input")
