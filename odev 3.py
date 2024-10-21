import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

# Define the range of x
x = np.arange(1, 100, 1)


def uyelik_hesapla(a, b, c, u, direction='left'):
    """
    Calculates the membership degree for a given u based on the parameters a, b, c.

    Parameters:
    - a, b, c: Parameters defining the membership function.
    - u: Input value or array of input values.
    - direction: 'left' for left shoulder, 'right' for right shoulder.

    Returns:
    - Membership degree(s) as a NumPy array.
    """
    z = np.zeros_like(u, dtype=float)

    if direction == 'left':
        # For left shoulder:
        # 0 for u < a
        # 2 * ((u - a) / (c - a))^2 for a <= u <= b
        # 1 - 2 * ((u - c) / (c - a))^2 for b < u <= c
        # 1 for u > c
        mask1 = (u >= a) & (u < b)
        mask2 = (u >= b) & (u <= c)
        z[mask1] = 2 * (((u[mask1] - a) / (c - a)) ** 2)
        z[mask2] = 1 - 2 * (((u[mask2] - c) / (c - a)) ** 2)
        z[u > c] = 1
    elif direction == 'right':
        # For right shoulder:
        # 0 for u < a
        # 1 - 2 * ((u - a) / (c - a))^2 for a <= u <= b
        # 2 * ((u - c) / (c - a))^2 for b < u <= c
        # 1 for u > c
        mask1 = (u >= a) & (u < b)
        mask2 = (u >= b) & (u <= c)
        z[mask1] = 1 - 2 * (((u[mask1] - a) / (c - a)) ** 2)
        z[mask2] = 2 * (((u[mask2] - c) / (c - a)) ** 2)
        z[u > c] = 1
    else:
        raise ValueError("Direction must be either 'left' or 'right'.")

    return z


# Parameters for the membership functions
b_genislik = 40
c_orta_nokta = 50

# Left Shoulder Parameters
a_sol = c_orta_nokta - b_genislik
b_sol = c_orta_nokta - b_genislik / 2
c_sol = c_orta_nokta

# Right Shoulder Parameters
a_sag = c_orta_nokta
b_sag = c_orta_nokta + b_genislik / 2
c_sag = c_orta_nokta + b_genislik

# Calculate membership values
z_sol = uyelik_hesapla(a_sol, b_sol, c_sol, x, direction='left')
z_sag = uyelik_hesapla(a_sag, b_sag, c_sag, x, direction='right')

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)  # Make space for widgets

# Plot membership functions
line_sol, = ax.plot(x, z_sol, label='Left Shoulder', color='blue')
line_sag, = ax.plot(x, z_sag, label='Right Shoulder', color='red')

ax.set_xlabel('x')
ax.set_ylabel('Membership Value')
ax.set_title('Fuzzy Membership Functions')
ax.legend()
ax.grid(True)

# Initialize lists to keep track of plotted points and annotations
plotted_points_sol = []
plotted_points_sag = []
annotations = []


# Define the callback function for the button
def on_click(event):
    # Retrieve the text from the TextBox
    u_input = text_box.text
    try:
        u = float(u_input)
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")  # "Please enter a valid number."
        return

    # Check if u is within the range
    if u < x.min() or u > x.max():
        print(
            f"Lütfen {x.min()} ile {x.max()} arasında bir u değeri girin.")  # "Please enter a u value between x.min() and x.max()."
        return

    # Calculate membership values for the input u
    u_array = np.array([u])
    mu_sol = uyelik_hesapla(a_sol, b_sol, c_sol, u_array, direction='left')[0]
    mu_sag = uyelik_hesapla(a_sag, b_sag, c_sag, u_array, direction='right')[0]

    # Plot the points
    point_sol, = ax.plot(u, mu_sol, 'bo')  # Blue dot for left shoulder
    point_sag, = ax.plot(u, mu_sag, 'ro')  # Red dot for right shoulder
    plotted_points_sol.append(point_sol)
    plotted_points_sag.append(point_sag)

    # Annotate the points
    annotation_sol = ax.annotate(f"({u}, {mu_sol:.2f})", xy=(u, mu_sol), xytext=(5, 5),
                                 textcoords='offset points', color='blue', fontsize=9)
    annotation_sag = ax.annotate(f"({u}, {mu_sag:.2f})", xy=(u, mu_sag), xytext=(5, -15),
                                 textcoords='offset points', color='red', fontsize=9)
    annotations.extend([annotation_sol, annotation_sag])

    # Redraw the canvas to show the new points and annotations
    plt.draw()


# Define the callback function to clear plotted points
def on_clear(event):
    # Remove all plotted points and annotations
    for point in plotted_points_sol + plotted_points_sag:
        point.remove()
    for annotation in annotations:
        annotation.remove()
    # Clear the lists
    plotted_points_sol.clear()
    plotted_points_sag.clear()
    annotations.clear()
    # Redraw the canvas
    plt.draw()


# Add TextBox for user input
axbox = plt.axes([0.1, 0.1, 0.3, 0.05])  # [left, bottom, width, height]
text_box = TextBox(axbox, 'u Değeri Girin: ', initial="")  # "Enter u value:"

# Add Button for plotting
axbutton = plt.axes([0.5, 0.1, 0.1, 0.05])  # [left, bottom, width, height]
button = Button(axbutton, 'Çiz')  # "Draw"

# Add Button for clearing plotted points
axclear = plt.axes([0.65, 0.1, 0.1, 0.05])
clear_button = Button(axclear, 'Temizle')  # "Clear"

# Connect the button to the callback function
button.on_clicked(on_click)
clear_button.on_clicked(on_clear)

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define the range of x
# x = np.arange(1, 100, 1)
#
#
# def uyelik_hesapla(a, b, c, u, direction='right'):
#     """
#     Calculates the membership degree for a given u based on the parameters a, b, c.
#
#     Parameters:
#     - a, b, c: Parameters defining the membership function.
#     - u: Input value or array of input values.
#     - direction: 'left' for left shoulder, 'right' for right shoulder.
#
#     Returns:
#     - Membership degree(s) as a NumPy array.
#     """
#     z = np.zeros_like(u, dtype=float)
#
#     if direction == 'left':
#         # For left shoulder:
#         # 0 for u < a
#         # 2 * ((u - a) / (c - a))^2 for a <= u <= b
#         # 1 - 2 * ((u - c) / (c - a))^2 for b < u <= c
#         # 1 for u > c
#         mask1 = (u >= a) & (u < b)
#         mask2 = (u >= b) & (u <= c)
#         z[mask1] = 2 * (((u[mask1] - a) / (c - a)) ** 2)
#         z[mask2] = 1 - 2 * (((u[mask2] - c) / (c - a)) ** 2)
#         z[u > c] = 1
#     elif direction == 'right':
#         # For right shoulder:
#         # 0 for u < a
#         # 1 - 2 * ((u - a) / (c - a))^2 for a <= u <= b
#         # 2 * ((u - c) / (c - a))^2 for b < u <= c
#         # 1 for u > c
#         mask1 = (u >= a) & (u < b)
#         mask2 = (u >= b) & (u <= c)
#         z[mask1] = 1 - 2 * (((u[mask1] - a) / (c - a)) ** 2)
#         z[mask2] = 2 * (((u[mask2] - c) / (c - a)) ** 2)
#         z[u > c] = 1
#     else:
#         raise ValueError("Direction must be either 'left' or 'right'.")
#
#     return z
#
#
# # Parameters for the left shoulder
# b_genislik = 40
# c_orta_nokta = 50
# a_sol = c_orta_nokta - b_genislik
# b_sol = c_orta_nokta - b_genislik / 2
# c_sol = c_orta_nokta
#
# # Calculate membership values for the left shoulder
# z_sol = uyelik_hesapla(a_sol, b_sol, c_sol, x, direction='left')
#
# # Parameters for the right shoulder
# a_sag = c_orta_nokta
# b_sag = c_orta_nokta + b_genislik / 2
# c_sag = c_orta_nokta + b_genislik
#
# # Calculate membership values for the right shoulder
# z_sag = uyelik_hesapla(a_sag, b_sag, c_sag, x, direction='right')
#
# # Plotting the membership functions
# plt.figure(figsize=(10, 6))
# plt.plot(x, z_sol, label='Left Shoulder', color='blue')
# plt.plot(x, z_sag, label='Right Shoulder', color='red')
# plt.xlabel('x')
# plt.ylabel('Membership Value')
# plt.title('Optimized Fuzzy Membership Functions')
# plt.legend()
# plt.grid(True)
# plt.show()
