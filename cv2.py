# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 01:17:10 2023

@author: Alejandro
"""

import cv2

# Crear el objeto VideoCapture para acceder a la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame por frame
    ret, frame = cap.read()

    # Mostrar el frame en una ventana
    cv2.imshow("Video en tiempo real", frame)

    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar el objeto VideoCapture y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
