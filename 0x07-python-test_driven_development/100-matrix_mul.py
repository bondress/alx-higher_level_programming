#!/usr/bin/python3

"""Defines a function that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints or floats): The first matrix.
        m_b (list of lists of ints or floats): The second matrix.
    Raises:
        TypeError: If m_a or m_b is not a list of lists of ints or floats.
        TypeError: If m_a or m_b is empty.
        TypeError: If m_a or m_b has rows of different sizes.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix showing the result of m_a multiplied by m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(elemnt, int) or isinstance(elemnt, float))
               for elemnt in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(elemnt, int) or isinstance(elemnt, float))
               for elemnt in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix_one = []
    for x in range(len(m_b[0])):
        n_row = []
        for y in range(len(m_b)):
            n_row.append(m_b[y][x])
        matrix_one.append(n_row)

    matrix_two = []
    for row in m_a:
        n_row = []
        for col in matrix_one:
            prodct = 0
            for x in range(len(matrix_one[0])):
                prodct += row[x] * col[x]
            n_row.append(prodct)
        matrix_two.append(n_row)

    return matrix_two
