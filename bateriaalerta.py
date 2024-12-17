# vercion 0.1
# import psutil
# import time
# from tkinter import messagebox, Toplevel, Label, Button
# import tkinter as tk
# import winsound  # Para sonido de alerta

# # Variables globales
# upper_limit = 80  # Porcentaje máximo por defecto
# lower_limit = 5   # Porcentaje mínimo por defecto
# notification_shown = False  # Controla la repetición de notificaciones

# # Función principal para verificar la batería
# def check_battery():
#     global notification_shown
#     battery = psutil.sensors_battery()
#     percent = battery.percent
#     charging = battery.power_plugged

#     # Notificación si la batería supera el límite superior
#     if charging and percent >= upper_limit and not notification_shown:
#         show_alert_window(f"¡Batería al {percent}%! \nDesconecta el cargador.", "red")
#         notification_shown = True

#     # Notificación si la batería baja del límite inferior
#     elif not charging and percent <= lower_limit and not notification_shown:
#         show_alert_window(f"¡Batería al {percent}%! \nConecta el cargador.", "green")
#         notification_shown = True

#     # Resetear notificación si cambia el estado de carga
#     elif (charging and percent < upper_limit) or (not charging and percent > lower_limit):
#         notification_shown = False

#     # Repite la verificación cada 5 segundos
#     root.after(5000, check_battery)

# # Ventana emergente de alerta personalizada en la esquina inferior derecha
# def show_alert_window(message, color):
#     # Ventana de alerta
#     alert = Toplevel(root)
#     alert.title("⚡ Alerta de Batería ⚡")
#     alert.configure(bg=color)

#     # Bloquear redimensionamiento
#     alert.resizable(False, False)

#     # Calcular la posición en la parte inferior derecha
#     window_width = 400
#     window_height = 200
#     screen_width = root.winfo_screenwidth()  # Ancho de la pantalla
#     screen_height = root.winfo_screenheight()  # Alto de la pantalla

#     # Posición en la esquina inferior derecha
#     x_position = screen_width - window_width - 10  # Un margen de 10 píxeles
#     y_position = screen_height - window_height - 50  # Un margen de 50 píxeles

#     # Establecer la geometría de la ventana
#     alert.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

#     # Hacer que la ventana siempre esté encima de otras
#     alert.attributes('-topmost', 1)

#     # Texto grande y llamativo
#     Label(alert, text=message, font=("Helvetica", 20, "bold"), bg=color, fg="white").pack(expand=True)

#     # Botón para cerrar la alerta
#     Button(alert, text="Entendido", command=alert.destroy, bg="white", fg=color).pack(pady=10)

#     # Sonido de alerta
#     winsound.MessageBeep(winsound.MB_ICONHAND)

# # Función para actualizar los límites desde la interfaz
# def update_limits():
#     global upper_limit, lower_limit
#     try:
#         # Obtiene los nuevos límites desde el panel
#         upper_limit = int(entry_upper.get())
#         lower_limit = int(entry_lower.get())
#         messagebox.showinfo("Actualizado", f"Límites actualizados:\nMáximo: {upper_limit}%\nMínimo: {lower_limit}%")
#     except ValueError:
#         messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# # Crear la interfaz gráfica
# root = tk.Tk()
# root.title("ArturAlertBattery ALP")
# root.geometry("300x200")
# root.resizable(False, False)  # Bloquear redimensionamiento

# # Etiquetas y entradas
# tk.Label(root, text="Porcentaje Máximo (%):").pack(pady=5)
# entry_upper = tk.Entry(root)
# entry_upper.insert(0, str(upper_limit))  # Valor predeterminado de 80%
# entry_upper.pack()

# tk.Label(root, text="Porcentaje Mínimo (%):").pack(pady=5)
# entry_lower = tk.Entry(root)
# entry_lower.insert(0, str(lower_limit))  # Valor predeterminado de 5%
# entry_lower.pack()

# # Botón para actualizar límites
# tk.Button(root, text="Actualizar Límites", command=update_limits).pack(pady=10)

# # Iniciar la verificación de batería
# check_battery()

# # Ejecutar la interfaz
# root.mainloop()

#:::::::::::::::::: vercion 0.2::::::::::::::::
import psutil
import threading
from tkinter import messagebox, Toplevel, Label, Button
import tkinter as tk
import winsound

# Variables globales
upper_limit = 80  
lower_limit = 10  
notification_shown = False 
charger_still_connected = False 

# Función principal para verificar la batería
def check_battery():
    global notification_shown, charger_still_connected
    battery = psutil.sensors_battery()
    percent = battery.percent
    charging = battery.power_plugged

    # Si el cargador está conectado y el porcentaje supera el límite superior
    if charging and percent >= upper_limit:
        if not notification_shown:  # Primera notificación
            threading.Thread(target=play_alert_sound).start()
            show_alert_window(f"¡Batería al {percent}% 🫡! \nDesconecta el cargador.", "#e73f3f")
            notification_shown = True
            charger_still_connected = True  
        elif charger_still_connected:  # Verificación cada 10 segundos
            threading.Thread(target=play_alert_sound).start()
            show_alert_window(f"¡Sigue conectado 😠!\n esta al {percent}%!\nDesconéctar...", "red")

    # Si el cargador está desconectado, reiniciar las banderas
    elif not charging and percent <= lower_limit:
        if not notification_shown:  
            threading.Thread(target=play_alert_sound).start()
            show_alert_window(f"¡Batería al {percent}%!\n 🥱Conecta el cargador.", "green")
            notification_shown = True
            charger_still_connected = False 

    # Resetear notificación si cambia el estado de carga
    elif not charging or (charging and percent < upper_limit):
        notification_shown = False
        charger_still_connected = False

    # Repite la verificación cada 10 segundos
    root.after(10000, check_battery)

# Función para reproducir el sonido de alerta (3 veces)
def play_alert_sound():
    for _ in range(3):
        winsound.Beep(1000, 500)  

# Ventana emergente de alerta personalizada
def show_alert_window(message, color):
    # Ventana de alerta
    alert = Toplevel(root)
    alert.title("⚡ Alerta de Batería ⚡")
    alert.configure(bg=color)

    # Calcular la posición en la parte inferior derecha
    window_width = 400
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = screen_width - window_width - 10
    y_position = screen_height - window_height - 50
    alert.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Hacer que la ventana siempre esté encima
    alert.attributes('-topmost', 1)

    # Texto grande y llamativo
    Label(alert, text=message, font=("Helvetica", 20, "bold"), bg=color, fg="white").pack(expand=True)

    # Botón para cerrar la alerta
    Button(alert, text="Entendido", command=alert.destroy, bg="white", fg=color).pack(pady=10)

# Función para actualizar los límites desde la interfaz
def update_limits():
    global upper_limit, lower_limit
    try:
        upper_limit = int(entry_upper.get())
        lower_limit = int(entry_lower.get())
        messagebox.showinfo("Actualizado", f"Límites actualizados:\nMáximo: {upper_limit}%\nMínimo: {lower_limit}%")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("ArturAlertBattery ALP")
root.geometry("300x200")
root.resizable(False, False)  # Bloquear redimensionamiento

# Etiquetas y entradas
tk.Label(root, text="Porcentaje Máximo (%):").pack(pady=5)
entry_upper = tk.Entry(root)
entry_upper.insert(0, str(upper_limit))  
entry_upper.pack()

tk.Label(root, text="Porcentaje Mínimo (%):").pack(pady=5)
entry_lower = tk.Entry(root)
entry_lower.insert(0, str(lower_limit))  
entry_lower.pack()

# Botón para actualizar límites
tk.Button(root, text="Actualizar Límites", command=update_limits).pack(pady=10)

# Iniciar la verificación de batería
check_battery()

# Ejecutar la interfaz
root.mainloop()

