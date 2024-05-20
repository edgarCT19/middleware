const express = require('express');
const app = express();

// Middleware que imprime un mensaje en la consola para cada solicitud recibida
app.use((req, res, next) => {
  console.log('Se recibió una solicitud HTTP');
  next(); // Llama a la siguiente función en la cadena de middleware
});

// Ruta de ejemplo
app.get('/', (req, res) => {
  res.send('¡Hola, mundo!');
});

// Iniciar el servidor en todas las interfaces de red
const PORT = 3000;
app.listen(PORT, '172.20.10.8', () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});
