import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

# Define the distance range
mesafe = np.linspace(-500, 500, 1000)

# Compute the YAKIN fuzzy set
yakın = np.piecewise(mesafe,
                     [mesafe < 200,
                      (mesafe >= 200) & (mesafe <= 500),
                      mesafe > 500],
                     [1,
                      lambda x: (500 - x) / 300,
                      0])

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Plot the fuzzy set
line, = ax.plot(mesafe, yakın, label='YAKIN Bulanık Kümesi', color='b')

# Plot the vertical lines at x=200 and x=500
ax.axvline(x=200, color='r', linestyle='--', label='200')
ax.axvline(x=500, color='g', linestyle='--', label='500')
ax.axvline(x=0, color='black', linestyle='--')

# Add title and labels
ax.set_title('YAKIN Bulanık Kümesi')
ax.set_xlabel('Mesafe')
ax.set_ylabel('Üyelik Derecesi')
ax.grid(True)
ax.legend()

# Create a TextBox widget for user input
axbox = plt.axes([0.1, 0.05, 0.3, 0.075])  # x, y, width, height
text_box = TextBox(axbox, 'Mesafe Değeri: ')

# Create a Button widget
axbutton = plt.axes([0.5, 0.05, 0.1, 0.075])
button = Button(axbutton, 'Çiz')

# Initialize an empty scatter plot for the point
scatter_point = ax.scatter([], [], color='r', zorder=5)

# Initialize empty text for annotation
annotation = ax.text(0, 0, '', fontsize=12, color='red')


# Define the function to update the plot when the button is pressed
def submit(event):
    try:
        kullanıcı_mesafe = float(text_box.text)
        # Calculate the membership degree
        if kullanıcı_mesafe < 200:
            uyelik_derecesi = 1
        elif 200 <= kullanıcı_mesafe <= 500:
            uyelik_derecesi = (500 - kullanıcı_mesafe) / 300
        else:
            uyelik_derecesi = 0

        # Update the scatter point
        scatter_point.set_offsets([[kullanıcı_mesafe, uyelik_derecesi]])

        # Update the annotation
        annotation.set_position((kullanıcı_mesafe, uyelik_derecesi))
        annotation.set_text(f'({kullanıcı_mesafe}, {uyelik_derecesi:.2f})')

        # Redraw the figure
        fig.canvas.draw_idle()
    except ValueError:
        # If the input is not a valid float, do nothing or show an error
        pass


# Connect the button press event to the function
button.on_clicked(submit)

plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# # Mesafe aralığını tanımla
# mesafe = np.linspace(-500, 500, 1000)
#
# # YAKIN bulanık kümesini hesapla
# yakın = np.piecewise(mesafe,
#                      [mesafe < 200,
#                       (mesafe >= 200) & (mesafe <= 500),
#                       mesafe > 500],
#                      [1,
#                       lambda x: (500 - x) / 300,
#                       0])
#
# # Kullanıcıdan bir mesafe değeri al
# kullanıcı_mesafe = float(input("Bir mesafe değeri giriniz: "))
#
# # Girilen mesafenin üyelik derecesini hesapla
# if kullanıcı_mesafe < 200:
#     uyelik_derecesi = 1
# elif 200 <= kullanıcı_mesafe <= 500:
#     uyelik_derecesi = (500 - kullanıcı_mesafe) / 300
# else:
#     uyelik_derecesi = 0
#
# # Grafiği çiz
# plt.figure(figsize=(10, 6))
# plt.plot(mesafe, yakın, label='YAKIN Bulanık Kümesi', color='b')
# plt.scatter(kullanıcı_mesafe, uyelik_derecesi, color='r', label=f'Girilen Değer: {kullanıcı_mesafe}\nÜyelik Derecesi: {uyelik_derecesi:.2f}', zorder=5)
# plt.title('YAKIN Bulanık Kümesi')
# plt.xlabel('Mesafe')
# plt.ylabel('Üyelik Derecesi')
# plt.grid(True)
# plt.axvline(x=200, color='r', linestyle='--', label='200')
# plt.axvline(x=500, color='g', linestyle='--', label='500')
# plt.legend()
# plt.show()
