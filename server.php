<?php
// Obtener los datos enviados desde la aplicación Python
$data = json_decode(file_get_contents('php://input'), true);

// Mensaje enviado desde Python
$message = $data['message'];

// Crear un array de respuesta
$response = array(
    'status' => 'success',
    'message' => "Mensaje recibido desde Python: $message"
);

// Convertir la respuesta a formato JSON
$json_response = json_encode($response);

// Imprimir la respuesta como JSON
header('Content-Type: application/json');
echo $json_response;
?>
