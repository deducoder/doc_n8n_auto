# Guía Rápida: Entornos Virtuales de Python

Este documento te muestra los comandos esenciales para gestionar tus entornos virtuales de Python de forma concisa, usando la sintaxis literal de Markdown para que veas los "símbolos" que lo componen.

---

### Eliminar Entorno Existente (Opcional)

- **Comando:** `rm -rf .venv`
- **Qué hace:** Elimina la carpeta `.venv` (tu entorno virtual actual). Útil para empezar de cero o solucionar errores.
- **Nota:** En **Windows PowerShell**, usa `Remove-Item -Recurse -Force .venv`.

---

### Crear Nuevo Entorno Virtual

- **Comando:** `python -m venv .venv`
- **Qué hace:** Crea una nueva carpeta `.venv` con una instalación aislada de Python y `pip` para tu proyecto.

---

### Activar Entorno Virtual

- **Comando (Windows PowerShell):** `..venv\Scripts\Activate`
- **Comando (Linux/macOS/Git Bash):** `source .venv/bin/activate`
- **Qué hace:** Activa el entorno virtual. Verás `(.venv)` al inicio de tu terminal, indicando que está activo.

---

### Instalar Dependencias

- **Comando:** `pip install -r requirements.txt`
- **Qué hace:** Instala todas las librerías listadas en tu archivo `requirements.txt` dentro del entorno virtual activo.
- **Alternativa:** Para instalar una librería específica: `pip install nombre_de_la_libreria`.

---

### Guardar Dependencias (Opcional pero Recomendado)

- **Comando:** `pip freeze > requirements.txt`
- **Qué hace:** Genera un archivo `requirements.txt` que lista todas las librerías instaladas en tu entorno virtual. Esto es crucial para que otros desarrolladores o tú mismo puedan replicar el entorno exacto de tu proyecto.

---

### Desactivar Entorno Virtual

- **Comando:** `deactivate`
- **Qué hace:** Desactiva el entorno virtual, volviendo a usar la instalación global de Python de tu sistema. El `(.venv)` desaparecerá de tu terminal.

---
