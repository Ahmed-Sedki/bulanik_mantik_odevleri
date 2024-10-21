import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_membership_function(u, a, b, c, d):
    if u < a or u > d:
        return 0
    elif a <= u < b:
        return (u - a) / (b - a)
    elif b <= u <= c:
        return 1
    elif c < u <= d:
        return (d - u) / (d - c)

def plot_trapezoidal_membership(a, b, c, d, u):
    # Define u values for plotting the membership function
    u_values = np.linspace(a - 1, d + 1, 1000)
    membership_values = [trapezoidal_membership_function(value, a, b, c, d) for value in u_values]

    # Plot the trapezoidal membership function
    plt.plot(u_values, membership_values, label='Membership Function')
    plt.xlabel('u')
    plt.ylabel('$\mu_A(u)$')
    plt.title('Yamuk Uyelik Fonksiyonu (Trapezoidal Membership Function)')

    # Plot the user-defined value and its membership value
    mu_u = trapezoidal_membership_function(u, a, b, c, d)
    plt.scatter([u], [mu_u], color='red', zorder=5)
    plt.text(u, mu_u, f'({u}, {mu_u:.2f})', fontsize=10, verticalalignment='bottom')

    plt.legend()
    plt.grid(True)
    plt.show()

a, b, c, d = 1, 30, 70, 100
u = float(input('Enter value for u (between 1 and 100): '))

plot_trapezoidal_membership(a, b, c, d, u)
