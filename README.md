# --------------------------------- ENGLISH -------------------------------------

# 📥 YT-DLP Downloader for Linux Mint (PyQt6 GUI)

![Linux Mint](https://img.shields.io/badge/Linux_Mint-22.x-green?logo=linuxmint&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![PyQt6](https://img.shields.io/badge/GUI-PyQt6-41CD52?logo=qt&logoColor=white)
![yt-dlp](https://img.shields.io/badge/Backend-yt--dlp-red)

A high-performance, cross-platform media downloader optimized for **Linux Mint (Cinnamon / MATE / XFCE)**. Powered by `yt-dlp` in the backend, it integrates a native graphical user interface built with `PyQt6`, implementing multithreading (`QThread`) to prevent interface freezes, alongside real-time progress monitoring.

---

A lightweight graphical user interface (GUI) developed in Python and PyQt6 acting as a frontend wrapper for `yt-dlp`, optimized for Linux Mint and Ubuntu/Debian-based distributions.

## Features

* Simple PyQt6-based interface featuring a real-time progress bar.
* Direct extraction to **MP3 Audio** including embedded metadata and cover art.
* **MP4 Video** downloading at the highest available quality.
* Support for downloading **Full Playlists**.
* Support for **Custom Formats** (native `yt-dlp` format IDs).
* Asynchronous version check for the installed `yt-dlp` binary.

## System Requirements

The system must have the `yt-dlp` binary and core system tools installed (such as `ffmpeg` for audio conversion):

```bash
sudo apt update
sudo apt install python3 python3-pip ffmpeg yt-dlp -y

-------------------------------------------------------------------------------------------------------
```

# --------------------------------- ESPAÑOL -------------------------------------

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
