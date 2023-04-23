def my_cubic_spline(x, y, X):
    # Step 1: Compute the second derivatives of the cubic spline
    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]
    alpha = [3 * (y[i + 1] - y[i]) / h[i] - 3 * (y[i] - y[i - 1]) / h[i - 1] for i in range(1, n - 1)]
    l = [1] * (n - 2)
    mu = [0] * (n - 2)
    z = [0] * n
    for i in range(1, n - 2):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]
    l[n - 3] = x[n - 1] - x[n - 3] - h[n - 3] * mu[n - 3]
    z[n - 2] = (alpha[n - 3] - h[n - 3] * z[n - 3]) / l[n - 3]
    z[n - 1] = 0

    # Step 2: Compute the cubic spline interpolation at each point in X
    Y = []
    j = 0
    for i in range(len(X)):
        while j < n - 1 and X[i] > x[j + 1]:
            j += 1
        if j == n - 1:
            Y.append(y[n - 1])
        else:
            t = (X[i] - x[j]) / h[j]
            a = z[j + 1] - z[j]
            b = -h[j] * (z[j + 1] + 2 * z[j]) / 3 + (y[j + 1] - y[j]) / h[j]
            c = z[j] / 2
            d = (z[j + 1] - z[j]) / (3 * h[j])
            Y.append(a * t * t * t + b * t * t + c * t + d)
    return Y
