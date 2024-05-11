import matplotlib.pyplot as plt
import numpy as np


def _filter_step(k, k_max, meas, dt, x_prev, V_prev):
    if (x_prev is None) and (V_prev is None):  # first step of initialization
        return meas, None

    if V_prev is None:  # second step of initialization
        return meas, (meas - x_prev) / dt

    if k > k_max:
        k = k_max

    a = 2. * (2. * k - 1.) / (k * (k + 1.))
    b = 6. / (k * (k + 1.))

    x_pred = x_prev + (V_prev * dt)
    V_pred = V_prev

    x = x_pred + (a * (meas - x_pred))
    V = V_pred + ((b / dt) * (meas - x_pred))

    return x, V

def alpha_beta_filter(noised_values, dt, steps):
    filtered_values = []
    V_arr = []
    x_prev = None
    V_prev = None
    for i in range(steps):
        x, V = _filter_step(i, 10, noised_values[i], dt, x_prev, V_prev)

        filtered_values.append(x)
        V_arr.append(V)

        x_prev = x
        V_prev = V
    return filtered_values


if __name__ == '__main__':
    # gen values
    number_steps = 150
    x0 = 50.
    V0 = 25.
    dt = 1.
    mid_val = 0.
    deviation = 200.
    true_values = []
    noised_values = []

    for i in range(number_steps):
        t = i * dt
        true = x0 + (V0 * t)
        meas = true + np.random.normal(mid_val, deviation)

        true_values.append(true)
        noised_values.append(meas)


    # filter
    filtered_values_ = alpha_beta_filter(noised_values, dt, number_steps)

    # draw
    plt.figure(figsize=(16, 8))
    plt.xlabel('t [secs]')
    plt.ylabel('x [m]')
    plt.plot(true_values, color='green', label='real value')
    plt.plot(noised_values, color='red', label='value with noise')
    plt.plot(filtered_values_, color='blue', label='denoised (filtered) values')
    plt.legend(loc='upper left')
    plt.show()