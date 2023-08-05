#!/usr/bin/python3
"""Defines a function that multiplies matrices using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of 2 matrices.

    Args:
        m_a (list of lists of ints or floats): The first matrix.
        m_b (list of lists of ints or floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
