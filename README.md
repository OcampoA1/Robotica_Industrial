<div id="header" align = "center">
  <h1 align = "center">Visión Computacional Aplicada a Dobot Magician</h1>
  <img src = "https://media.giphy.com/media/PlLanl8Bzcvr14IfjJ/giphy.gif" width="400"/>  
</div>

<div id = "exp" align = "center"> 
  <p align = "justify">La visión computacional es un campo de estudio que busca desarrollar sistemas capaces de interpretar y comprender información visual a partir    de imágenes o videos. Su objetivo es simular la visión humana y utilizarla para diversos propósitos, como reconocimiento de objetos, seguimiento de movimiento,       detección de rostros, entre otros.</p>
  <p align = "justify">Uno de los avances más significativos en la visión computacional ha sido la detección y seguimiento de manos. Esto permite a las máquinas        reconocer la posición y los movimientos de las manos humanas en tiempo real. Un marco de trabajo popular para esta tarea es Mediapipe, una biblioteca desarrollada    por Google que proporciona modelos y herramientas para el procesamiento de imágenes y video.</p>
  <p align = "justify">El Dobot Magician es un robot manipulador de escritorio versátil y preciso que se puede controlar de forma programática. Combina                 características como la precisión, la capacidad de carga útil y la facilidad de uso para una amplia gama de aplicaciones.</p>
  <p align = "justify">La integración de la visión computacional mediante Mediapipe con el Dobot Magician permite aprovechar la capacidad de reconocimiento de manos    para controlar el robot de manera intuitiva. Mediante el análisis en tiempo real de la posición y los movimientos de los nodos de la mano, el sistema puede         interpretar gestos y comandos para controlar el robot de manera precisa y fluida.</p>  
  <p align = "justify">La implementación objetivo es a partir de Mediapipe detectar y rastrear los puntos clave de la mano, como las puntas de los dedos y la base de la palma. Estos puntos se van a utilizar para calcular la posición y la orientación de la mano en el espacio tridimensional. A partir de esta información, se pueden definir gestos y movimientos específicos que correspondan a comandos para el robot, en este caso en particular, se podrá mover el robot en cruz.</p>
</div>
<div id = "tutorial" align = "center">
  <h1 align = "center">TUTORIAL</h1>
  <ol align = "justify">
    <li><a href="#anaconda">Anaconda</a></li>
    <li><a href="#librerias">Librerías</a></li>
    <li><a href="#API">API Dobot Magician</a></li>
    <li><a href="#mediapipe">MediaPipe</a></li>
    <li><a href="#cv2">OpenCV</a></li>
    <li><a href="#camara">Algortimo OpenCV</a></li>
    <li><a href="#manos">Algoritmo MediaPipe + OpenCV</a></li>
    <li><a href="#final">Algoritmo API + MediaPipe + OpenCV</a></li>
    <li><a href="#video">Video</a></li>
    <li><a href="#recomendacion">Recomendaciones</a></li>
  </ol>
  
</div>

<div id = "1" align = "center">
  <h1 id="anaconda" align = "center">Anaconda</h1>
<ol align = "justify">
  <li><strong>Descargar Anaconda:</strong> Visita el <a href="https://www.anaconda.com/products/individual">sitio web oficial de Anaconda</a> y descarga la versión adecuada para tu sistema operativo (Windows, macOS o Linux).</li>
  
  <li><strong>Instalar Anaconda:</strong> Ejecuta el archivo de instalación que descargaste y sigue las instrucciones proporcionadas por el instalador. Asegúrate de marcar la opción "Agregar Anaconda al PATH" durante la instalación para poder acceder a los comandos de Anaconda desde la línea de comandos.</li>
  
  <li><strong>Abrir Spyder:</strong> Una vez instalado Anaconda, puedes abrir el IDE Spyder. En Windows, ve al menú Inicio y busca "Spyder" en la lista de aplicaciones instaladas. En macOS y Linux, puedes abrir una terminal y ejecutar el comando <code>spyder</code>.</li>
</ol>

<p align = "justify">Con estos pasos, tendrás instalado Anaconda y podrás utilizar Spyder como tu entorno de desarrollo para programar en Python y realizar tareas de análisis de datos.</p>

<p align = "justify">Recuerda que esta es una guía básica y puede haber variaciones dependiendo de tu sistema operativo y la versión de Anaconda que estés utilizando. Si deseas obtener más información detallada o encuentras algún problema durante la instalación, te recomiendo consultar la documentación oficial de Anaconda y Spyder.</p>

</div>

<div id = "2" align = "center">
  <h1 id = "librerias" align = "center">Librerías</h1>
  <p align = "justify">En el desarrollo del software que permite la manipulación del robot Dobot Magician a través de gestos de las manos, se utilizan varias bibliotecas y APIs clave. Estas herramientas incluyen Mediapipe, OpenCV y la API DobotDllType. Su integración es fundamental para lograr un control preciso y efectivo del robot.</p>
  <p align = "justify">Mediapipe, OpenCV y la API DobotDllType se combinan para crear un software poderoso y versátil. Estas librerías se utilizan específicamente en el contexto del desarrollo del software diseñado para reconocer y rastrear los gestos de las manos. Mediante el análisis y seguimiento de los nodos clave de la mano, como los dedos y la palma, se puede capturar la información necesaria para controlar el robot Dobot Magician.</p>
  <p align = "justify">Mediapipe desempeña un papel central al proporcionar modelos de aprendizaje automático preentrenados y una estructura para el procesamiento de datos en tiempo real. Esto permite detectar y rastrear los nodos de la mano, proporcionando información crucial para el control del robot.</p>
  <p align = "justify">OpenCV, por su parte, es una biblioteca ampliamente utilizada en visión por computadora. Se utiliza para la captura y procesamiento de imágenes y videos en tiempo real, lo que resulta esencial para la adquisición de imágenes de la cámara y el procesamiento de los datos obtenidos a través de Mediapipe.</p>
  <p align = "justify">La API DobotDllType proporciona la interfaz de programación necesaria para interactuar con el robot Dobot Magician. A través de esta API, se pueden enviar comandos programáticos para controlar el movimiento, la sujeción, la velocidad y otras funciones del robot. Al integrar la API DobotDllType con Mediapipe y OpenCV, se traducen los gestos y movimientos detectados en comandos precisos para el robot Dobot Magician.</p>
</div>

<div id = "3" align = "center">
  <h1 id = "API" align = "center">API</h1>


<ol align = "justify">
  <li><strong>Descargar la API DobotDllType:</strong> Dirígete al <a href="https://www.dobot.cc/">sitio web oficial de Dobot</a> o al repositorio de <a href="https://github.com/DobotRobotics/DobotMagician">GitHub de Dobot</a> y descarga el paquete de la API DobotDllType. Asegúrate de seleccionar la versión adecuada de la API según tu sistema operativo y arquitectura (32 o 64 bits).</li>
  
  <li><strong>Descomprimir el archivo:</strong> Descomprime el archivo ZIP de la API DobotDllType en una ubicación conveniente de tu sistema.</li>
  
  <li><strong>Configurar el entorno de desarrollo:</strong> Abre tu entorno de desarrollo preferido para escribir tu código. Asegúrate de tener Python instalado en tu sistema antes de continuar.</li>
  
  <li><strong>Crear un proyecto de Python:</strong> Crea un nuevo proyecto de Python en tu entorno de desarrollo Spyder</li>
  
  <li><strong>Copiar los archivos de la API:</strong> Dentro del directorio descomprimido de la API DobotDllType, encontrarás varios archivos. Copia el archivo <code>DobotDllType.py</code> en la ubicación de tu proyecto de Python.</li>
  
  <li><strong>Instalar las dependencias:</strong> Verifica si la API DobotDllType tiene dependencias adicionales que debes instalar. Consulta la documentación de la API y sigue las instrucciones proporcionadas para instalar las dependencias necesarias.</li>
  
  <li><strong>Importar y utilizar la API:</strong> Ahora estás listo para importar y utilizar la API DobotDllType en tu proyecto de Python. Agrega la siguiente línea de código al principio de tu archivo Python para importar la API:</li>
</ol>

<pre aling = "center"><code class="language-python">
from dobotdll import DobotDllType
</code></pre>

<p align = "justify">A partir de este punto, puedes utilizar los métodos y funciones proporcionados por la API DobotDllType para controlar el robot Dobot Magician. Consulta la documentación de la API y los ejemplos de código disponibles para aprender cómo utilizar los comandos específicos de la API.</p>

<p align = "justify">Recuerda seguir las instrucciones proporcionadas en la documentación de la API y en el repositorio de Dobot para asegurarte de realizar una instalación correcta y completa de la API DobotDllType.</p>
</div>

<div id = "4" align = "center">
  <h1 id = "mediapipe" align = "center">MediaPipe</h1>
  <ol align = "justify">
  <li><strong>Crear un entorno virtual:</strong> Abre Anaconda Navigator o una terminal y crea un nuevo entorno virtual. Puedes nombrar tu entorno como desees. Por ejemplo, utiliza el siguiente comando en la terminal para crear un entorno llamado "mediapipe-env":</li>
</ol>
<pre align = "center"><code class="language-bash">
conda create --name mediapipe-env
</code></pre>
<ol start="2" align = "justify">
  <li><strong>Activar el entorno virtual:</strong> Una vez creado el entorno virtual, actívalo ejecutando el siguiente comando en la terminal:</li>
</ol>
<pre align = "center"><code class="language-bash">
conda activate mediapipe-env
</code></pre>
<ol start="3" align = "justify">
  <li><strong>Instalar Mediapipe:</strong> Con el entorno virtual activado, puedes instalar Mediapipe utilizando el administrador de paquetes de Anaconda. Ejecuta el siguiente comando en la terminal:</li>
</ol>
<pre align = "center"><code class="language-bash">
conda install -c conda-forge mediapipe
</code></pre>
<ol start="4" align = "justify">
  <li><strong>Verificar la instalación:</strong> Para asegurarte de que Mediapipe se ha instalado correctamente, puedes ejecutar un código de prueba en Python. Abre tu editor de código preferido y crea un nuevo archivo Python. Copia y pega el siguiente código en el archivo:</li>
</ol>
<pre align = "center"><code class="language-python">
import mediapipe as mp
print(mp.__version__)
</code></pre>
<p align = "justify">Guarda el archivo con un nombre descriptivo, por ejemplo, "test_mediapipe.py". Luego, ejecuta el archivo y verifica que se imprima la versión de Mediapipe en la salida de la terminal.</p>

</div>
<div id = "5" align = "center">
  <h1 id = "cv2">OpenCV</h1>
  <ol align = "justify">
  <li><strong>Activar el entorno virtual:</strong> Abre Anaconda Navigator o una terminal y activa el entorno virtual "mediapipe-env" que creaste previamente. Puedes utilizar el siguiente comando en la terminal para activarlo:</li>
</ol>
<pre align = "center"><code class="language-bash">
conda activate mediapipe-env
</code></pre>
<ol start="2">
  <li><strong>Instalar OpenCV:</strong> Con el entorno virtual activado, puedes instalar OpenCV utilizando el administrador de paquetes de Anaconda. Ejecuta el siguiente comando en la terminal:</li>
</ol>
<pre align = "center"><code class="language-bash">
conda install -c conda-forge opencv
</code></pre>
<ol start="3">
  <li><strong>Verificar la instalación:</strong> Para asegurarte de que OpenCV se ha instalado correctamente, puedes ejecutar un código de prueba en Python. Abre tu editor de código preferido y crea un nuevo archivo Python. Copia y pega el siguiente código en el archivo:</li>
</ol>
<pre align = "center"><code class="language-python">
import cv2
print(cv2.__version__)
</code></pre>
<p align = "justify">Guarda el archivo con un nombre descriptivo, por ejemplo, "test_opencv.py". Luego, ejecuta el archivo y verifica que se imprima la versión de OpenCV en la salida de la terminal.</p>
<p align = "justify">Recuerda que al haber creado el entorno virtual "mediapipe-env" previamente, debes asegurarte de activarlo antes de instalar OpenCV. De esta manera, OpenCV se instalará en ese entorno específico y podrás utilizarlo junto con Mediapipe.</p>
</div>

<div id = "6" align = "center">
  <h1 id = "camara">Algortimo OpenCV</h1>
  <p align = "justify">En este tutorial aprenderás cómo utilizar OpenCV para capturar video en tiempo real desde la cámara de tu computadora y mostrarlo en una ventana.</p>
<ol align = "justify">
  <li>Importa la biblioteca OpenCV:</li>
</ol>
<pre align = "center"><code class="language-python">
import cv2
</code></pre>
<ol start="2" align = "justify">
  <li>Crea el objeto <code>VideoCapture</code>:</li>
</ol>
<pre align = "center"><code class="language-python">
cap = cv2.VideoCapture(0)
</code></pre>
<ol start="3" align = "justify">
  <li>Captura y muestra los frames:</li>
</ol>
<pre align = "center"><code class="language-python">
while True:
    ret, frame = cap.read()
    cv2.imshow("Video en tiempo real", frame)
</code></pre>
<ol start="4" align = "justify">
  <li>Finaliza la captura y cierra la ventana:</li>
</ol>
<pre align = "center"><code class="language-python">
if cv2.waitKey(1) &amp; 0xFF == ord('q'):
    break
</code></pre>
<p align = "justify">¡Ahora puedes capturar y mostrar video en tiempo real utilizando OpenCV en tu computadora!. Este codigo se encuentra en la parte superior como 'cv2.py'.</p>
<div id = "7" aling = "center">
  <h1 id = "manos" align = "center">Algoritmo MediaPipe</h1>
  <p align = "justify">En este tutorial, aprenderemos cómo utilizar OpenCV y Mediapipe para detectar y dibujar marcas de las manos en tiempo real utilizando la cámara web de tu computadora.</p>
<ol align = "justify">
  <li><strong>Importar las bibliotecas necesarias:</strong> Importamos las bibliotecas `cv2` y `mediapipe` para acceder a las funciones y clases necesarias.</li>
</ol>
<pre align = "center"><code class="language-python">
import cv2
import mediapipe as mp
</code></pre>
<ol start="2" align = "justify">
  <li><strong>Inicializar el objeto de detección de manos:</strong> Creamos un objeto `Hands` para detectar las manos en la imagen. Configuramos el modo de imagen estática como falso, permitiendo la detección en tiempo real.</li>
</ol>
<pre align = "center"><code class="language-python">
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
</code></pre>
<ol start="3" align = "justify">
  <li><strong>Inicializar la cámara web:</strong> Creamos un objeto `VideoCapture` para acceder a la cámara web de la computadora.</li>
</ol>
<pre align = "center"><code class="language-python">
cap = cv2.VideoCapture(0)
</code></pre>
<ol start="4" align = "justify">
  <li><strong>Procesar los frames de la cámara:</strong> Utilizamos un bucle `while` para capturar continuamente los frames de la cámara y procesarlos.</li>
</ol>
<pre align = "center"><code class="language-python">
while cap.isOpened():
    success, image = cap.read()
</code></pre>
<ol start="5" align = "justify">
  <li><strong>Convertir la imagen a RGB:</strong> Convertimos la imagen capturada de BGR a RGB para ser compatible con la detección de manos de Mediapipe.</li>
</ol>
<pre align = "center"><code class="language-python">
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
</code></pre>
<ol start="6" align = "justify">
  <li><strong>Detectar manos en la imagen:</strong> Utilizamos el objeto `Hands` para procesar la imagen y detectar las manos en ella.</li>
</ol>
<pre align = "center"><code class="language-python">
results = hands.process(image_rgb)
</code></pre>
<ol start="7" align = "justify">
  <li><strong>Dibujar marcas de la mano en la imagen:</strong> Si se detectan manos en la imagen, utilizamos la función `draw_landmarks` de `drawing_utils` para dibujar las marcas de la mano en la imagen.</li>
</ol>
<pre align = "center"><code class="language-python">
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
</code></pre>
<ol start="8" align = "justify">
  <li><strong>Mostrar la imagen con las marcas de la mano:</strong> Mostramos la imagen con las marcas de la mano en una ventana utilizando la función `imshow` de OpenCV.</li>
</ol>
<pre align = "center"><code class="language-python">
cv2.imshow('Hand Detection', image)
</code></pre>
<ol start="9" align = "justify">
  <li><strong>Finalizar la captura y cerrar la ventana:</strong> Si se presiona la tecla 'q', salimos del bucle y liberamos los recursos.</li>
</ol>
<pre align = "center"><code class="language-python">
if cv2.waitKey(1) &amp; 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
</code></pre>
<p>¡Ahora puedes detectar y dibujar marcas de las manos en tiempo real utilizando OpenCV y Mediapipe en tu cámara web!. Cabe resaltar que el codigo explicado se encuentra en mediapipe.py</p>
  </div>
  




