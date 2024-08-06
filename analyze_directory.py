import os

def analyze_directory(directory, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            for root, dirs, files in os.walk(directory):
                file.write(f"Directorio: {root}\n")
                file.write("Subdirectorios:\n")
                for dir in dirs:
                    file.write(f"  - {dir}\n")
                file.write("Archivos:\n")
                for file_name in files:
                    file.write(f"  - {file_name}\n")
                file.write("\n")
        print(f"El análisis se ha guardado en {output_file}")
    except Exception as e:
        print(f"Se produjo un error: {e}")

def main():
    # Cambia 'ruta/a/tu/carpeta' por la ruta de la carpeta que deseas analizar
    directory_to_analyze = 'C:/Users/Guaymallen/Documents/Deposito/acomod/python/chatbot/base-js-baileys-postgres'
    output_file_path = 'output.txt'
    analyze_directory(directory_to_analyze, output_file_path)

if __name__ == "__main__":
    main()
