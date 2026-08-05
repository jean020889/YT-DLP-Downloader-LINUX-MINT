# 📥 YT-DLP Downloader for Linux Mint (PyQt6 GUI)

![Linux Mint](https://img.shields.io/badge/Linux_Mint-22.x-green?logo=linuxmint&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-41CD52?logo=qt&logoColor=white)
![yt-dlp](https://img.shields.io/badge/Backend-yt--dlp-red)

Un descargador de medios multiplataforma y de alto rendimiento optimizado para **Linux Mint (Cinnamon / MATE / XFCE)**. Utiliza `yt-dlp` en el backend e integra una interfaz gráfica nativa construida con `PyQt6`, implementando multihilo (`QThread`) para evitar bloqueos en la interfaz y monitoreo de progreso en tiempo real.

---

Una interfaz gráfica (GUI) ligera desarrollada en Python y PyQt6 como wrapper frontend para `yt-dlp`, optimizada para Linux Mint y distribuciones basadas en Ubuntu/Debian.

## Características

* Interfaz simple basada en PyQt6 con barra de progreso en tiempo real.
* Extracción directa a **Audio MP3** con metadatos y carátula integrada.
* Descarga de **Video MP4** a máxima calidad disponible.
* Soporte para descarga de **Playlists completas**.
* Soporte para **Formato Personalizado** (IDs de formato nativos de `yt-dlp`).
* Verificación asíncrona de la versión instalada de `yt-dlp`.

## Requisitos del Sistema

Es necesario tener instalado en el sistema el binario `yt-dlp` y las herramientas del sistema (como `ffmpeg` para la conversión de audio):

```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg yt-dlp -y
