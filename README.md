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



