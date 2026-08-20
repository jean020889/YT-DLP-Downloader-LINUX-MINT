## Para eliminarlo por completo, debes borrar el archivo ejecutable principal y limpiar los accesos directos o archivos de configuración residuales.

### Pasos de desinstalación:

1. **Eliminar el archivo ejecutable:**
```bash
sudo rm /usr/local/bin/ytdlp-gui

```


2. **Eliminar el acceso directo de la interfaz gráfica (.desktop):**
```bash
rm -f ~/.local/share/applications/*ytdlp*.desktop
sudo rm -f /usr/share/applications/*ytdlp*.desktop

```


3. **Purgar directorios de configuración o caché:**
```bash
rm -rf ~/.config/*ytdlp*
rm -rf ~/.cache/*ytdlp*

```



¿El programa utilizaba algún entorno virtual de Python (`venv`) o dependencias globales adicionales que debamos limpiar?
