
# ArturAlertBatteryWindous

## Install Program

---
--> ArturAlertBattery.exe  

## Ejemlpo de prueva
### Icono del Programa
<div style="text-align:center;">
  <img src="https://github.com/user-attachments/assets/7a8cb347-35c0-4998-b00e-51e2952035ed" width="300"/>
</div>


---

## Notificación de la Batería Baja
<div style="text-align:center;">
  <img src="https://github.com/user-attachments/assets/4984ea4a-9345-4be1-a3b7-80dbafa2a3af" width="300"/>
</div>

Este es el **icono de notificación** cuando la batería está baja.

---

## Notificación de la Batería Alta
<div style="text-align:center;">
  <img src="https://github.com/user-attachments/assets/c903b88d-d457-4d51-98d2-e1bd38ffa692" width="300"/>
</div>

Este es el **icono de notificación** cuando la batería está alta, por encima del porcentaje máximo que se ha configurado.



# ArturAlertBattery - Alerta de Batería con Notificaciones Personalizadas

Este proyecto está diseñado para alertarte sobre el estado de tu batería, notificándote cuando la carga es demasiado alta (para desconectar el cargador) o demasiado baja (para conectar el cargador). Además, incluye una interfaz gráfica donde puedes configurar los límites de alerta.

## Características

- Notificaciones personalizadas cuando la batería supera el límite superior (80%) o cae por debajo del límite inferior (5%).
- Ventanas emergentes con sonido de alerta.
- Interfaz gráfica para actualizar los límites de porcentaje de batería.
- La alerta se muestra en la esquina inferior derecha de la pantalla, encima de todas las ventanas.

## Librerías Utilizadas

Para que el proyecto funcione correctamente, hemos utilizado varias bibliotecas. A continuación se detalla lo que hemos instalado:

1. **psutil**: Utilizado para obtener el estado de la batería (porcentaje de carga, si está conectada o no al cargador).
   - Instalación:
     ```bash
     pip install psutil
     ```

2. **tkinter**: Utilizado para crear la interfaz gráfica de usuario (GUI).
   - Tkinter es una biblioteca estándar de Python, por lo que generalmente no necesitas instalarla por separado. Si no la tienes, puedes instalarla de la siguiente manera:
     ```bash
     pip install tk
     ```

3. **winsound**: Utilizado para reproducir sonidos de alerta de manera sencilla.
   - Esta biblioteca es parte de la biblioteca estándar de Python en sistemas Windows, por lo que no es necesario instalarla.

## Requisitos

Para ejecutar este proyecto, necesitas tener Python instalado en tu sistema. Se recomienda Python 3.6 o superior.

### Instalación

1. Asegúrate de tener Python instalado en tu sistema. Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. Instala las dependencias utilizando pip:
   ```bash
   pip install psutil
   pip install tk
