import cv2
import mediapipe as mp
from dobotdll import DobotDllType

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicializar el objeto de detección de manos
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Inicializar la API DobotDllType
api = DobotDllType()

# Conectar al Dobot Magician
portName = "COMX"  # Reemplaza "COMX" con el puerto correcto del Dobot
baudrate = 115200
api.ConnectDobot(portName, baudrate)

# Inicializar la cámara web
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Error al leer el cuadro de video")
        break

    # Convertir la imagen a RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Detectar manos en la imagen
    results = hands.process(image_rgb)

    # Obtener la posición de la mano
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        x = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
        y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y

        # Convertir las coordenadas normalizadas a coordenadas del Dobot
        x_dobot = x * 300  # Ajusta el factor de escala según tus necesidades
        y_dobot = (1 - y) * 300  # Ajusta el factor de escala según tus necesidades

        # Mover el Dobot a la posición de la mano
        api.SetPTPCmd(api, 1, x_dobot, y_dobot, 0, 1)

    # Mostrar la imagen con las marcas de la mano
    cv2.imshow('Hand Detection', image)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Desconectar el Dobot
api.DisconnectDobot(api)

# Liberar recursos
cap.release()
cv2.destroyAllWindows()