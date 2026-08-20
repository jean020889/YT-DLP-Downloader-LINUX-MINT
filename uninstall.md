## This program was manually installed as a binary or executable script and does not belong to any package manager (such as APT or Flatpak).

## To completely remove it, you must delete the main executable file and clean up shortcuts or residual configuration files.

### Uninstallation Steps:

1. **Delete the executable file:**

```bash
sudo rm /usr/local/bin/ytdlp-gui

```

2. **Delete the graphical interface shortcut (.desktop):**

```bash
rm -f ~/.local/share/applications/*ytdlp*.desktop
sudo rm -f /usr/share/applications/*ytdlp*.desktop

```

3. **Purge configuration or cache directories:**

```bash
rm -rf ~/.config/*ytdlp*
rm -rf ~/.cache/*ytdlp*

```



-------------------------------------------------------------------------------------------------------------------------------------



## Este programa fue instalado manualmente como un binario o script ejecutable y no pertenece a ningún gestor de paquetes (como APT o Flatpak).

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

