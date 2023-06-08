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
  
  <li><strong>Crear un proyecto de Python:</strong> Crea un nuevo proyecto de Python en tu entorno de desarrollo. Puedes utilizar un IDE como PyCharm, Visual Studio Code u otro de tu elección.</li>
  
  <li><strong>Copiar los archivos de la API:</strong> Dentro del directorio descomprimido de la API DobotDllType, encontrarás varios archivos. Copia el archivo <code>DobotDllType.py</code> en la ubicación de tu proyecto de Python.</li>
  
  <li><strong>Instalar las dependencias:</strong> Verifica si la API DobotDllType tiene dependencias adicionales que debes instalar. Consulta la documentación de la API y sigue las instrucciones proporcionadas para instalar las dependencias necesarias.</li>
  
  <li><strong>Importar y utilizar la API:</strong> Ahora estás listo para importar y utilizar la API DobotDllType en tu proyecto de Python. Agrega la siguiente línea de código al principio de tu archivo Python para importar la API:</li>
</ol>

<pre><code class="language-python">
from dobotdll import DobotDllType
</code></pre>

<p align = "justify">A partir de este punto, puedes utilizar los métodos y funciones proporcionados por la API DobotDllType para controlar el robot Dobot Magician. Consulta la documentación de la API y los ejemplos de código disponibles para aprender cómo utilizar los comandos específicos de la API.</p>

<p align = "justify">Recuerda seguir las instrucciones proporcionadas en la documentación de la API y en el repositorio de Dobot para asegurarte de realizar una instalación correcta y completa de la API DobotDllType.</p>




</div>


