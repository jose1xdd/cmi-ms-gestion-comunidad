PASSWORD_RECOVERY_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Recuperación de Contraseña</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f6f9;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 600px;
      margin: 40px auto;
      background-color: #ffffff;
      border-radius: 8px;
      box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
      padding: 40px;
    }
    h2 {
      color: #333333;
    }
    p {
      color: #555555;
      line-height: 1.6;
    }
    .code-box {
      background-color: #f0f0f0;
      padding: 20px;
      border-radius: 8px;
      text-align: center;
      font-size: 24px;
      font-weight: bold;
      color: #007bff;
      letter-spacing: 2px;
      margin: 20px 0;
    }
    .footer {
      margin-top: 30px;
      font-size: 12px;
      color: #999999;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Recuperación de contraseña</h2>
    <p>Hola,</p>
    <p>Recibimos una solicitud para restablecer tu contraseña. Usa el siguiente código para continuar con el proceso:</p>

    <div class="code-box">{{codigo}}</div>

    <p>Si no solicitaste este cambio, puedes ignorar este mensaje.</p>

    <p>Gracias.</p>

    <div class="footer">
      © 2025 Comunidad Indigena Quillancinga del municipio de Consaca . Todos los derechos reservados.
    </div>
  </div>
</body>
</html>
 
"""

TEMPORARY_PASSWORD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Contraseña Provisional</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f6f9;
      margin: 0;
      padding: 0;
    }
    .container {
      max-width: 600px;
      margin: 40px auto;
      background-color: #ffffff;
      border-radius: 8px;
      box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.1);
      padding: 40px;
    }
    h2 {
      color: #333333;
    }
    p {
      color: #555555;
      line-height: 1.6;
    }
    .code-box {
      background-color: #f0f0f0;
      padding: 20px;
      border-radius: 8px;
      text-align: center;
      font-size: 24px;
      font-weight: bold;
      color: #28a745;
      letter-spacing: 2px;
      margin: 20px 0;
    }
    .footer {
      margin-top: 30px;
      font-size: 12px;
      color: #999999;
      text-align: center;
    }
  </style>
</head>
<body>
  <div class="container">
    <h2>Contraseña Provisional</h2>
    <p>Hola,</p>
    <p>Se ha generado una contraseña provisional para que puedas acceder temporalmente a tu cuenta. Por favor, utiliza la siguiente contraseña:</p>

    <div class="code-box">{{password}}</div>

    <p>Te recomendamos cambiar esta contraseña una vez inicies sesión.</p>

    <p>Si no solicitaste este acceso, ignora este mensaje.</p>

    <p>Gracias.</p>

    <div class="footer">
      © 2025 Comunidad Indígena Quillacinga del municipio de Consacá. Todos los derechos reservados.
    </div>
  </div>
</body>
</html>
"""


