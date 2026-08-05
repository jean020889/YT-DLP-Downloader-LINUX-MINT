import subprocess
import sys
import os

def check_update():
    print("[+] Verificando actualizaciones de yt-dlp...")
    try:
        subprocess.run(["yt-dlp", "-U"], check=False)
    except FileNotFoundError:
        print("[!] Error: yt-dlp no está instalado o no está en el PATH.")
        sys.exit(1)
    print("-" * 50)

def get_url():
    url = input("\n[>] Ingresa la URL (video o playlist): ").strip()
    if not url:
        print("[!] URL vacía. Cancelando.")
        sys.exit(1)
    return url

def show_formats(url):
    print("\n[+] Obteniendo formatos y calidades disponibles...\n")
    subprocess.run(["yt-dlp", "--extractor-args", "youtube:player_client=android,web", "-F", url])

def get_native_file_chooser():
    """Llama a Zenity para desplegar el selector de directorios GTK nativo."""
    print("\n[+] Selecciona la carpeta de destino en la ventana del explorador...")
    
    user_home = os.path.expanduser("~")
    downloads_default = os.path.join(user_home, "Descargas")

    try:
        # Comando Zenity con la ruta ~/Descargas como punto de partida por defecto
        cmd = [
            "zenity", 
            "--file-selection", 
            "--directory", 
            f"--filename={downloads_default}/",
            "--title=Selecciona la carpeta de destino para la descarga"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        # Código 0 indica que el usuario seleccionó una carpeta y dio 'Aceptar'
        if result.returncode == 0:
            selected_path = result.stdout.strip()
            if selected_path:
                print(f"[✔] Destino confirmado: {selected_path}")
                return selected_path
        else:
            # Si el usuario presiona 'Cancelar' o cierra la ventana
            print("[!] Selección cancelada en la ventana gráfica. Usando ~/Descargas por defecto.")
            return downloads_default

    except Exception as e:
        print(f"[!] Ocurrió un error al lanzar Zenity: {e}")
        return downloads_default

def main():
    try:
        check_update()

        url = get_url()
        show_formats(url)

        # Invocación del explorador GTK nativo
        output_dir = get_native_file_chooser()

        if not os.path.exists(output_dir):
            print(f"[+] Creando carpeta de destino: {output_dir}")
            os.makedirs(output_dir, exist_ok=True)

        print("\n" + "="*50)
        print("--- OPCIONES DE DESCARGA ---")
        print("1. Descargar Audio MP3 (Mejor calidad + Metadatos)")
        print("2. Descargar Video en Máxima Calidad (Automático - MP4)")
        print("3. Ingresar ID de Calidad Específica (Ej: 399+140 o 137+140)")
        print("4. Descargar Playlist Completa")
        print("0. Salir")

        option = input("\n[>] Selecciona una opción (0-4): ").strip()

        if option == "0":
            print("Saliendo...")
            sys.exit(0)

        output_template = ["-o", os.path.join(output_dir, "%(title)s.%(ext)s")]
        base_flags = [
            "--extractor-args", "youtube:player_client=android,web",
            "--no-mtime"
        ]

        if option == "1":
            cmd = [
                "yt-dlp", "-x", 
                "--audio-format", "mp3", 
                "--audio-quality", "0", 
                "--embed-thumbnail", 
                "--add-metadata"
            ] + base_flags + output_template + [url]

        elif option == "2":
            cmd = [
                "yt-dlp", 
                "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best", 
                "--merge-output-format", "mp4"
            ] + base_flags + output_template + [url]

        elif option == "3":
            format_id = input("\n[>] Ingresa el ID del formato (Si es video-only como 399, usa 399+bestaudio): ").strip()
            if not format_id:
                print("[!] ID no válido.")
                sys.exit(1)
            cmd = [
                "yt-dlp", 
                "-f", format_id, 
                "--merge-output-format", "mp4"
            ] + base_flags + output_template + [url]

        elif option == "4":
            cmd = [
                "yt-dlp", 
                "--yes-playlist"
            ] + base_flags + output_template + [url]

        else:
            print("[!] Opción no válida.")
            sys.exit(1)

        print("\n[+] Iniciando descarga...\n")
        subprocess.run(cmd, check=True)
        print(f"\n[✔] Descarga completada exitosamente en: {output_dir}")

    except KeyboardInterrupt:
        print("\n\n[!] Operación cancelada por el usuario.")
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Error durante la descarga (Código {e.returncode}).")
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()
