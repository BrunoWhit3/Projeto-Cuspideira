# Troque "COM3" no Windows ou "/dev/ttyUSB0" / "/dev/ttyACM0" no Linux
import serial
import time

def conectar_arduino(porta="COM3", baud=9600):
    while True:
        try:
            print(f"Tentando conectar ao Arduino em {porta}...")
            arduino = serial.Serial(porta, baud, timeout=1)
            time.sleep(2)
            print("Arduino conectado!")
            return arduino
        except:
            print("Arduino nao encontrado. Tentando novamente em 2s...")
            time.sleep(2)

def loop_principal():
    arduino = conectar_arduino()

    with open("log_cuspideira.txt", "a") as log:
        while True:
            try:
                if arduino.in_waiting > 0:
                    linha = arduino.readline().decode(errors="ignore").strip()
                    print("Arduino -> ", linha)
                    log.write(linha + "/n")
                    log.flush()
            
            except KeyboardInterrupt:
                print("\nFinalizado pelo usuario.")
                break
            
            except serial.SerialException:
                print("Arduino foi desconectado!")
                print("Aguardando reconexao...")
                arduino = conectar_arduino()
            
            except Exception as e:
                print("Erro inesperado:", e)
                time.sleep(1)


    arduino.close()



if __name__ == "__main__":
    loop_principal()
