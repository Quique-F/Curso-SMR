# Actividad 7 – Comparación de cadenas

$usuarioLogueado = "Admin_Sistemas"

# 1. Coincidencia exacta (-eq)

if ($usuarioLogueado -eq "Admin_Sistemas") { Write-Host "Usuario reconocido." }



# 2. Contiene subcadena (-like con asteriscos o .Contains())

if ($usuarioLogueado -like "*Admin*") { Write-Host "El usuario tiene perfil de Administrador." }



# 3. Comienza o termina (-match o métodos)

if ($usuarioLogueado.StartsWith("Admin")) { Write-Host "El nombre comienza por 'Admin'." }
if ($usuarioLogueado.EndsWith("Sistemas")) { Write-Host "El nombre termina por 'Sistemas'." }