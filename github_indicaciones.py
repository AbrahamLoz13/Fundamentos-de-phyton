# -----------------------------------------------------------------------------
# DESCRIPCIÓN: Pasos para subir mis proyectos a GitHub desde la Terminal
# -----------------------------------------------------------------------------

"""
-------------------------------------------------------------------------
PASO 0: CONFIGURACIÓN INICIAL 
(Solo se hace 1 vez cuando instalas Git en la computadora)
-------------------------------------------------------------------------
"""
# Abre la terminal (Ctrl + ñ) y configura tu usuario:
# git config --global user.name "Tu Nombre"
# git config --global user.email "tucorreo@email.com"


"""
-------------------------------------------------------------------------
PASO 1: SUBIR UN PROYECTO NUEVO POR PRIMERA VEZ
(Cuando creas una carpeta nueva y quieres conectarla a GitHub)
-------------------------------------------------------------------------
1. Ve a GitHub.com -> New Repository -> Ponle nombre -> Create.
2. NO marques 'Add README' ni '.gitignore', déjalo vacío.
3. Copia el link HTTPS que te da.
4. Ejecuta estos comandos en orden en la terminal de VS Code:
"""

# 1. Inicia el repositorio en tu compu
# git init

# 2. Prepara todos los archivos (.) para ser guardados
# git add .

# 3. Guarda la versión en tu computadora (Commit)
# git commit -m "Primer commit: Inicio del proyecto"

# 4. Renombra la rama principal a 'main'
# git branch -M main

# 5. Conecta con la nube (SUSTITUYE EL LINK POR EL TUYO)
# git remote add origin https://github.com/TU_USUARIO/TU_PROYECTO.git

# 6. Sube los archivos (Push)
# git push -u origin main


"""
-------------------------------------------------------------------------
PASO 2: RUTINA DIARIA (LO QUE HARÁS SIEMPRE)
(Cada vez que termines de programar o quieras guardar avance)
-------------------------------------------------------------------------
"""

# 1. Agrega los cambios recientes
# git add .

# 2. Empaquétalos con un mensaje
# git commit -m "Descripción de lo que hice hoy"

# 3. Mándalos a la nube
# git push


"""
-------------------------------------------------------------------------
COMANDOS ÚTILES DE AYUDA
-------------------------------------------------------------------------
"""
# git status    -> Te dice qué archivos modificaste (en rojo) o están listos (verde).
# git log       -> Te muestra el historial de todos tus guardados anteriores.
# clear         -> Limpia el texto de la terminal.