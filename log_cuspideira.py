# Configure a porta serial
# TROQUE "COM3" pela porta correta:
#   Windows -> COM3, COM4, etc
#   Linux -> /dev/ttyUSB0 ou /dev/ttyACM0
#   Mac -> /dev/tty.usbmodemxxxxx

import serial
import time

PORTA = "COM4"
BAUD = 9600

def main():
    try:
        print("Conectando ao Arduino...")
        arduino = serial.Serial(PORTA, BAUD, timeout=1)
        time.sleep(2)  # espera o Arduino reiniciar
        print("Conectado! Lendo dados...\n")

    except Exception as e:
        print("Erro ao abrir porta serial:", e)
        return

    # Abre o arquivo de log
    with open("log_cuspideira.txt", "a") as log:
        while True:
            try:
                linha = arduino.readline().decode("utf-8").strip()

                if linha:  # apenas se houver texto
                    print(linha)
                    log.write(linha + "\n")
                    log.flush()  # garante gravação imediata

            except KeyboardInterrupt:
                print("\nFinalizado pelo usuario.")
                break
                
            except Exception as e:
                print("Erro ao ler:", e)

    arduino.close()


if __name__ == "__main__":
    main()
