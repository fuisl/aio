"""
Module: 2
Week: 2
Topic: Basic Vector Operations
"""

import numpy as np


def compute_vector_length(v):
    """
    Compute the length of a vector
    """
    return np.sqrt(np.sum(v**2))


def compute_dot_product(v1, v2):
    """
    Compute the dot product of two vectors
    """
    return np.dot(v1, v2)


def matrix_multi_vector(matrix, vector):
    """
    Multiply vector by a matrix
    """
    return np.matmul(matrix, vector)


def matrix_multi_matrix(matrix1, matrix2):
    """
    Multiply two matrices
    """
    return np.matmul(matrix1, matrix2)


def inverse_matrix(matrix):
    """
    Compute the inverse of a matrix
    """
    return np.linalg.inv(matrix)

def compute_eigenvalues_eigenvectors(matrix):
    """
    Compute the eigenvalues and eigenvectors of a matrix
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors