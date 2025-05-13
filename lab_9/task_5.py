import numpy as np
from scipy.stats import multivariate_normal
from numpy.linalg import det, inv

def multivariate_normal_my(X, m, C):
    D = len(m)
    diff = X - m
    term1 = -0.5 * D * np.log(2 * np.pi)
    term2 = -0.5 * np.log(det(C))
    term3 = -0.5 * np.sum(diff @ inv(C) * diff, axis=1)
    return term1 + term2 + term3

N, D = 100, 3
X = np.random.randn(N, D)
m = np.zeros(D)
C = np.eye(D)

our_log = multivariate_normal_my(X, m, C)

scipy_log = multivariate_normal(m, C).logpdf(X)

print("Максимальная разница:", np.max(np.abs(our_log - scipy_log)))
print("Средняя разница:", np.mean(np.abs(our_log - scipy_log)))