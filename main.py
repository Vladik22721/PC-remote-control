import time
import serial
import pyautogui as pg
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

allserial = QSerialPort()
allserial.setBaudRate(115200)
portlist = []
ports = QSerialPortInfo().availablePorts()
for port in ports:
    portlist.append(port.portName())


port_user = pg.prompt(text=f'ports: {portlist}', title='app' , default='')

ser = serial.Serial(port_user, 9600)
ser.reset_input_buffer()

decoded_bytes = None

print("HELLO USER :)")
previous_value = None

step = 10
previous_time = time.time()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = int(ser_bytes.strip().decode("utf-8"))
        print(decoded_bytes)

        if decoded_bytes == previous_value:
            current_time = time.time()
            if current_time - previous_time <= 0.2:
                step += 10
            else:
                step = 10
            previous_time = current_time
        else:
            step = 10
            previous_value = decoded_bytes

        if decoded_bytes == 1785:
            pg.move(0, -step)

        if decoded_bytes == -31111:
            pg.move(0, step)

        if decoded_bytes == 18105:
            pg.move(step, 0)

        if decoded_bytes == -22951:
            pg.move(-step, 0)

        if decoded_bytes == 5865:
            pg.leftClick(pg.position())

        if decoded_bytes == -19381:
            pg.rightClick(pg.position())

        if decoded_bytes == 2295:
            pg.scroll(-100)
        if decoded_bytes == 18615:
            pg.scroll(100)
        if decoded_bytes == 16575:
            pg.alert(text='Bye', title='app')
            break

    except Exception as e:
        print(f'Error: {e}')
