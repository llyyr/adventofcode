def ints(s):
    """
    Extract numbers from a string.

    Examples
    --------
    >>> extract_numbers("Hello4.2this.is random 24 text42")
    [4.2, 24, 42]

    >>> extract_numbers("2.3+45-99")
    [2.3, 45, -99]

    >>> extract_numbers("Avogadro's number, 6.022e23, is greater than 1 million.")
    [6.022e+23, 1]
    """
    numbers = []
    current = ''
    for c in s.lower() + '!':
        if (c.isdigit() or
            (c == 'e' and ('e' not in current) and (current not in ['', '.', '-', '-.'])) or
            (c == '.' and ('e' not in current) and ('.' not in current)) or
            (c == '+' and current.endswith('e')) or
            (c == '-' and ((current == '') or current.endswith('e')))):
            current += c
        else:
            if current not in ['', '.', '-', '-.']:
                if current.endswith('e'):
                    current = current[:-1]
                elif current.endswith('e-') or current.endswith('e+'):
                    current = current[:-2]
                numbers.append(current)
            if c == '.' or c == '-':
                current = c
            else:
                current = ''

    # Convert from strings to actual python numbers.
    numbers = [float(t) if ('.' in t or 'e' in t) else int(t) for t in numbers]

    return numbers
