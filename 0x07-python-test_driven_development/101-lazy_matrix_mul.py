#!/usr/bin/python3
"""
This module contains the definition for the lazy_matrix_mul method which
returns the product of the two matrices passed. It utilizes the numpy module
for the computation hence the lazy added to the function name
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies and returns the product of two matrices created
    using the numpy module.

    Paramete(s)
    -----------
    m_a (list): First matrix
    m_b (list): Second matrix

    Returns:
        m_a * m_b
    """
    return (np.matmul(m_a, m_b))
