# Notas del curso de Programación Avanzada ene-jun 2024

## Temas

1. Programación Orientada a Objetos (POO)
2. Interfaces Gráficas de Usuario (GUI)
3. Comunicación serial
4. Hilos
5. Manejo de archivos de texto

## Librerias necesarias

* numpy
* matplotlib
* tkinter
* pyserial
* threaded
* seaborn
* ipykernel

### Instalar librerias con requirements.txt y venv
Entrar a la carpeta del proyecto y crear un entorno virtual con venv.
```bash
python -m venv .venv
```
  
Activar el entorno virtual. El comando siguiente funciona para **Git Bash**, para activar el entorno desde la **PowerShell** o la **cmd** se tiene que omitir la parte de _source_.
```bash
source .venv/Scripts/activate
```

Instalar las librerias del requirements.txt con la siguiente instrucción.
```bash
pip install -r requirements.txt
```
