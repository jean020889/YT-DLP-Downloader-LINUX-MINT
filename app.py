
#!/usr/bin/env python3
import sys
import os
import subprocess
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QProgressBar,
    QFileDialog, QTextEdit, QMessageBox, QCheckBox
)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QFont

class UpdateYtDlpWorker(QThread):
    log = pyqtSignal(str)
    finished = pyqtSignal(bool, str)  # éxito, mensaje

    def run(self):
        self.log.emit("[INFO] Verificando actualizaciones de yt-dlp...")
        try:
            # Ejecutar yt-dlp -U para auto-actualización
            process = subprocess.Popen(
                ["yt-dlp", "-U"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            for line in process.stdout:
                self.log.emit(line.strip())
            process.wait()
            if process.returncode == 0:
                self.finished.emit(True, "yt-dlp actualizado correctamente (si había nueva versión).")
            else:
                self.finished.emit(False, f"La actualización falló con código {process.returncode}. Continuando con la versión actual.")
        except Exception as e:
            self.finished.emit(False, f"Error al actualizar: {str(e)}")

class DownloadWorker(QThread):
    progress = pyqtSignal(float, str)
    log = pyqtSignal(str)
    finished = pyqtSignal(bool, str)

    def __init__(self, url, output_dir, option, custom_format="", use_cookies=True, browser="firefox"):
        super().__init__()
        self.url = url
        self.output_dir = output_dir
        self.option = option
        self.custom_format = custom_format
        self.use_cookies = use_cookies
        self.browser = browser

    def run(self):
        output_template = os.path.join(self.output_dir, "%(title)s.%(ext)s")
        cmd = [
            "yt-dlp",
            "--force-ipv4",
            "--extractor-args", "youtube:player_client=android,web",
            "--no-mtime",
            "-o", output_template
        ]

        if self.use_cookies:
            cmd += ["--cookies-from-browser", self.browser]
            self.log.emit(f"[INFO] Usando cookies del navegador: {self.browser}")

        if self.option == "audio":
            cmd += ["-x", "--audio-format", "mp3", "--audio-quality", "0", "--embed-thumbnail", "--add-metadata"]
        elif self.option == "video_max":
            cmd += ["-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", "--merge-output-format", "mp4"]
        elif self.option == "custom":
            fmt = self.custom_format if self.custom_format else "best"
            cmd += ["-f", fmt, "--merge-output-format", "mp4"]
        elif self.option == "playlist":
            cmd += ["--yes-playlist"]

        cmd.append(self.url)

        self.log.emit(f"[COMANDO] {' '.join(cmd)}")

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )

            for line in process.stdout:
                line_clean = line.strip()
                if line_clean:
                    self.log.emit(line_clean)
                    if "[download]" in line_clean and "%" in line_clean:
                        try:
                            parts = line_clean.split()
                            for part in parts:
                                if "%" in part:
                                    pct_str = part.replace("%", "")
                                    pct = float(pct_str)
                                    self.progress.emit(pct, line_clean)
                                    break
                        except ValueError:
                            pass

            process.wait()
            if process.returncode == 0:
                self.finished.emit(True, "Descarga completada exitosamente.")
            else:
                self.finished.emit(False, f"Error en la descarga (Código {process.returncode}).")

        except Exception as e:
            self.finished.emit(False, f"Error de ejecución: {str(e)}")

class YtdlpApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YT-DLP Downloader - Linux Mint")
        self.resize(720, 650)
        self.init_ui()
        self.check_version()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # URL
        main_layout.addWidget(QLabel("<b>URL del Video o Playlist:</b>"))
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://www.youtube.com/watch?v=...")
        main_layout.addWidget(self.url_input)

        # Carpeta destino
        main_layout.addWidget(QLabel("<b>Carpeta de Destino:</b>"))
        path_layout = QHBoxLayout()
        default_dir = os.path.join(os.path.expanduser("~"), "Descargas")
        self.path_input = QLineEdit(default_dir)
        self.btn_browse = QPushButton("Explorar...")
        self.btn_browse.clicked.connect(self.browse_directory)
        path_layout.addWidget(self.path_input)
        path_layout.addWidget(self.btn_browse)
        main_layout.addLayout(path_layout)

        # Calidad
        main_layout.addWidget(QLabel("<b>Calidad / Formato:</b>"))
        self.combo_option = QComboBox()
        self.combo_option.addItem("Audio MP3 (Mejor Calidad + Metadatos)", "audio")
        self.combo_option.addItem("Video MP4 (Máxima Calidad Automática)", "video_max")
        self.combo_option.addItem("Playlist Completa", "playlist")
        self.combo_option.addItem("Formato Personalizado (ID de yt-dlp)", "custom")
        self.combo_option.currentIndexChanged.connect(self.on_combo_change)
        main_layout.addWidget(self.combo_option)

        self.custom_format_input = QLineEdit()
        self.custom_format_input.setPlaceholderText("Ej: 399+140 o bestvideo+bestaudio")
        self.custom_format_input.setVisible(False)
        main_layout.addWidget(self.custom_format_input)

        # Opciones de cookies
        cookies_layout = QHBoxLayout()
        cookies_layout.addWidget(QLabel("<b>Cookies:</b>"))
        self.cookies_check = QCheckBox("Usar cookies del navegador")
        self.cookies_check.setChecked(True)
        self.cookies_check.toggled.connect(self.on_cookies_toggle)
        cookies_layout.addWidget(self.cookies_check)

        self.browser_combo = QComboBox()
        self.browser_combo.addItems(["firefox", "chrome", "brave", "chromium", "edge", "opera"])
        self.browser_combo.setToolTip("Selecciona el navegador del que extraer las cookies")
        cookies_layout.addWidget(self.browser_combo)
        cookies_layout.addStretch()
        main_layout.addLayout(cookies_layout)

        # Opción de actualización automática
        update_layout = QHBoxLayout()
        self.update_check = QCheckBox("Actualizar yt-dlp antes de descargar (recomendado)")
        self.update_check.setChecked(True)
        update_layout.addWidget(self.update_check)
        update_layout.addStretch()
        main_layout.addLayout(update_layout)

        # Estado y progreso
        self.lbl_status = QLabel("Estado: Listo")
        main_layout.addWidget(self.lbl_status)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

        # Log
        main_layout.addWidget(QLabel("<b>Registro de Salida:</b>"))
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFont(QFont("Monospace", 9))
        main_layout.addWidget(self.log_text)

        # Botón descargar
        self.btn_download = QPushButton("Iniciar Descarga")
        self.btn_download.setStyleSheet("padding: 10px; font-weight: bold; font-size: 14px;")
        self.btn_download.clicked.connect(self.start_download)
        main_layout.addWidget(self.btn_download)

    def browse_directory(self):
        folder = QFileDialog.getExistingDirectory(self, "Seleccionar Carpeta de Destino", self.path_input.text())
        if folder:
            self.path_input.setText(folder)

    def on_combo_change(self):
        is_custom = self.combo_option.currentData() == "custom"
        self.custom_format_input.setVisible(is_custom)

    def on_cookies_toggle(self, checked):
        self.browser_combo.setEnabled(checked)

    def check_version(self):
        # Solo muestra la versión actual al iniciar
        self.log_text.append("[+] Verificando versión de yt-dlp...")
        try:
            res = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True, timeout=5)
            version = res.stdout.strip()
            self.log_text.append(f"[+] Versión instalada: {version}")
        except Exception as e:
            self.log_text.append(f"[!] No se pudo obtener la versión: {e}")
        self.log_text.append("-" * 50)

    def start_download(self):
        url = self.url_input.text().strip()
        output_dir = self.path_input.text().strip()
        option = self.combo_option.currentData()
        custom_fmt = self.custom_format_input.text().strip()
        use_cookies = self.cookies_check.isChecked()
        browser = self.browser_combo.currentText()
        do_update = self.update_check.isChecked()

        if not url:
            QMessageBox.warning(self, "Atención", "Debes ingresar una URL válida.")
            return

        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        # Deshabilitar botón durante todo el proceso
        self.btn_download.setEnabled(False)
        self.progress_bar.setValue(0)
        self.lbl_status.setText("Estado: Preparando...")
        self.log_text.append(f"\n[+] Iniciando descarga en: {output_dir}")

        # Si se requiere actualización, lanzamos el worker de actualización
        if do_update:
            self.update_worker = UpdateYtDlpWorker()
            self.update_worker.log.connect(self.log_text.append)
            self.update_worker.finished.connect(
                lambda success, msg: self.after_update(success, msg, url, output_dir, option, custom_fmt, use_cookies, browser)
            )
            self.update_worker.start()
        else:
            # Directo a descarga
            self.start_download_worker(url, output_dir, option, custom_fmt, use_cookies, browser)

    def after_update(self, success, msg, url, output_dir, option, custom_fmt, use_cookies, browser):
        self.log_text.append(f"[ACTUALIZACIÓN] {msg}")
        # Continuamos con la descarga independientemente de si la actualización falló o no
        self.start_download_worker(url, output_dir, option, custom_fmt, use_cookies, browser)

    def start_download_worker(self, url, output_dir, option, custom_fmt, use_cookies, browser):
        self.lbl_status.setText("Estado: Descargando...")
        self.worker = DownloadWorker(url, output_dir, option, custom_fmt, use_cookies, browser)
        self.worker.progress.connect(self.update_progress)
        self.worker.log.connect(self.log_text.append)
        self.worker.finished.connect(self.download_finished)
        self.worker.start()

    def update_progress(self, pct, status_text):
        self.progress_bar.setValue(int(pct))
        self.lbl_status.setText(f"Estado: {status_text}")

    def download_finished(self, success, message):
        self.btn_download.setEnabled(True)
        if success:
            self.progress_bar.setValue(100)
            self.lbl_status.setText("Estado: Descarga completada")
            QMessageBox.information(self, "Éxito", message)
        else:
            self.lbl_status.setText("Estado: Error")
            QMessageBox.critical(self, "Error", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YtdlpApp()
    window.show()
    sys.exit(app.exec())
