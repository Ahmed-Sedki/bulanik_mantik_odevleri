import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, StringVar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Üyelik fonksiyonunu tanımlıyoruz
def membership_function(x):
    return 1 / (1 + 10 * (x - 5) ** 2)


# Grafikte çizim ve hesaplama yapmak için bir işlev
def draw_membership(x_given):
    membership_value_given_x = membership_function(float(x_given))

    # Grafikteki eski noktaları temizleyelim
    ax.cla()

    # Grafiği yeniden çizelim
    ax.plot(x_values, membership_values, label='Membership Function')
    ax.set_xlabel('X kesin sayı uzayı')
    ax.set_ylabel('Üyelik Derecesi, μ(x)')
    ax.set_title('Bulanık Küme Üyelik Fonksiyonu')
    ax.grid(True)
    ax.legend()

    # Seçilen X noktası için işaretleme yapalım
    ax.scatter(float(x_given), membership_value_given_x, color='red', zorder=5)
    ax.text(float(x_given), membership_value_given_x, f'({float(x_given):.2f}, {membership_value_given_x:.2f})',
            fontsize=12, color='red')

    # X değerine karşılık gelen dikey çizgiyi çizelim
    ax.axvline(x=float(x_given), color='red', linestyle='--')

    # Grafiği güncelle
    canvas.draw()


# Tkinter arayüzünü oluşturuyoruz
root = Tk()
root.title("Üyelik Fonksiyonu Hesaplama")

# Kullanıcıdan giriş almak için bir label ve input kutusu ekleyelim
label = Label(root, text="Bir X değeri girin (0 ile 10 arasında):")
label.pack()

x_input = StringVar()  # Giriş değerini almak için StringVar kullanıyoruz
entry = Entry(root, textvariable=x_input)
entry.pack()

# "Çiz" butonu
button = Button(root, text="Çiz", command=lambda: draw_membership(x_input.get()))
button.pack()

# Matplotlib grafiği oluşturma
fig, ax = plt.subplots()
x_values = np.linspace(0, 10, 1000)
membership_values = membership_function(x_values)

ax.plot(x_values, membership_values, label='Membership Function')
ax.set_xlabel('X kesin sayı uzayı')
ax.set_ylabel('Üyelik Derecesi, μ(x)')
ax.set_title('Bulanık Küme Üyelik Fonksiyonu')
ax.grid(True)
ax.legend()

# Tkinter penceresine Matplotlib grafiğini yerleştirelim
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Uygulamayı çalıştır
root.mainloop()
