import base64

# Mensaje codificado en Base64
encoded_message = "494a55574b3354574d565847535a44504c354255535243544a465054454d425347493d3d3d3d3d3d"

# Decodificar el mensaje
decoded_message = base64.b64decode(encoded_message).decode('utf-8')
print(decoded_message)
