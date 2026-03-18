# 🐍 Instalación de Python y Visual Studio Code

---

## 🪟 Windows

### Paso 1 — Instalar Python

1. Abre tu navegador y ve a [python.org/downloads](https://www.python.org/downloads)
2. Haz clic en el botón amarillo **"Download Python 3.x.x"**
3. Abre el archivo `.exe` que se descargó
4. **MUY IMPORTANTE:** Antes de hacer clic en instalar, marca la casilla que dice **"Add Python to PATH"** en la parte inferior de la ventana
5. Haz clic en **"Install Now"**
6. Espera a que termine y haz clic en **"Close"**

**Verificar que se instaló correctamente:**
1. Presiona `Windows + R`, escribe `cmd` y presiona Enter
2. Escribe el siguiente comando y presiona Enter:
```
python --version
```
3. Deberías ver algo como `Python 3.x.x`. Si lo ves, la instalación fue exitosa.

---

### Paso 2 — Instalar Visual Studio Code

1. Abre tu navegador y ve a [code.visualstudio.com](https://code.visualstudio.com)
2. Haz clic en el botón azul **"Download for Windows"**
3. Abre el archivo `.exe` que se descargó
4. Acepta los términos y haz clic en **"Next"** hasta llegar a las opciones adicionales
5. Marca las siguientes casillas:
   - **"Add 'Open with Code' action to Windows Explorer file context menu"**
   - **"Add 'Open with Code' action to Windows Explorer directory context menu"**
   - **"Register Code as an editor for supported file types"**
   - **"Add to PATH"**
6. Haz clic en **"Next"** y luego en **"Install"**
7. Cuando termine, haz clic en **"Finish"**

---

### Paso 3 — Instalar la extensión de Python en VS Code

1. Abre Visual Studio Code
2. Haz clic en el ícono de extensiones en la barra izquierda (parece cuatro cuadros)
3. En el buscador escribe `Python`
4. Instala la extensión que dice **Python** publicada por **Microsoft**
5. Haz clic en **"Install"**

---

### Paso 4 — Verificar que todo funciona

1. En VS Code, abre el menú **Terminal → New Terminal**
2. En la terminal que se abre abajo, escribe:
```
python --version
```
3. Si ves la versión de Python, todo está listo.
4. Crea un archivo nuevo con el nombre `hola.py` y escribe:
```python
print("Hola, mundo!")
```
5. Presiona `F5` o haz clic derecho y selecciona **"Run Python File"**
6. Deberías ver `Hola, mundo!` en la terminal

---
---

## 🐧 Linux

### Paso 1 — Instalar Python

En la mayoría de distribuciones de Linux, Python 3 ya viene instalado. Para verificarlo, abre la terminal y escribe:
```bash
python3 --version
```

Si ves la versión, ya lo tienes instalado y puedes pasar al Paso 2.

Si no está instalado, ejecuta los siguientes comandos según tu distribución:

**Ubuntu / Debian / Linux Mint:**
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

**Fedora:**
```bash
sudo dnf install python3 -y
```

**Arch Linux:**
```bash
sudo pacman -S python
```

**Verificar la instalación:**
```bash
python3 --version
```

---

### Paso 2 — Instalar Visual Studio Code

**Ubuntu / Debian / Linux Mint:**
```bash
sudo apt update
sudo apt install wget gpg -y
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code -y
```

**Fedora:**
```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
sudo dnf install code -y
```

**Arch Linux:**
```bash
sudo pacman -S code
```

**Alternativa para cualquier distribución (descarga manual):**
1. Ve a [code.visualstudio.com](https://code.visualstudio.com)
2. Descarga el archivo `.deb` (Ubuntu/Debian) o `.rpm` (Fedora)
3. Abre la terminal en la carpeta de descarga y ejecuta:

Para `.deb`:
```bash
sudo dpkg -i code_*.deb
```

Para `.rpm`:
```bash
sudo rpm -i code_*.rpm
```

---

### Paso 3 — Instalar la extensión de Python en VS Code

1. Abre Visual Studio Code escribiendo `code` en la terminal o buscándolo en el menú de aplicaciones
2. Haz clic en el ícono de extensiones en la barra izquierda (parece cuatro cuadros)
3. En el buscador escribe `Python`
4. Instala la extensión que dice **Python** publicada por **Microsoft**
5. Haz clic en **"Install"**

---

### Paso 4 — Verificar que todo funciona

1. En VS Code, abre el menú **Terminal → New Terminal**
2. En la terminal que aparece abajo, escribe:
```bash
python3 --version
```
3. Si ves la versión de Python, todo está listo.
4. Crea un archivo nuevo con el nombre `hola.py` y escribe:
```python
print("Hola, mundo!")
```
5. Presiona `F5` o haz clic derecho y selecciona **"Run Python File"**
6. Deberías ver `Hola, mundo!` en la terminal

> **Nota:** En Linux el comando es `python3`, no `python`. Si quieres usar solo `python`, puedes crear un alias ejecutando `alias python=python3` en la terminal.