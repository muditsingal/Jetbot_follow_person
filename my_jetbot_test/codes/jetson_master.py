#!/usr/bin/python3
import time
import serial

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")

data_to_arduino = "S"

def make_command(cmd, left_wheel, right_wheel):
    data_to_arduino = cmd + cmd + chr(left_wheel) + chr(right_wheel) + "\n"

serial_port = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
# Wait a second to let the port initialize
time.sleep(1)

try:
    # Send a simple header
    #serial_port.write("UART Demonstration Program\r\n".encode())
    #serial_port.write("NVIDIA Jetson Nano Developer Kit\r\n".encode())
    while True:
        make_command('S',180,180)
        serial_port.write(data_to_arduino.encode())
        time.sleep(1.5)

        make_command('S',160,127-(160-127))
        serial_port.write(data_to_arduino.encode())
        time.sleep(1)


        make_command('S',180,180)
        serial_port.write(data_to_arduino.encode())
        time.sleep(1.5)

        make_command('S',160,127-(160-127))
        serial_port.write(data_to_arduino.encode())
        time.sleep(1)


        make_command('S',180,180)
        serial_port.write(data_to_arduino.encode())
        time.sleep(1.5)

        make_command('S',160,127-(160-127))
        serial_port.write(data_to_arduino.encode())
        time.sleep(1)


        make_command('S',180,180)
        serial_port.write(data_to_arduino.encode())
        time.sleep(1.5)

        make_command('S',160,127-(160-127))
        serial_port.write(data_to_arduino.encode())
        time.sleep(1)


        #if serial_port.inWaiting() > 0:
            #data = serial_port.readline()
            #print(data)
            #serial_port.write(data_to_arduino.encode())
            #serial_port.write("\n".encode())
            # if we get a carriage return, add a line feed too
            # \r is a carriage return; \n is a line feed
            # This is to help the tty program on the other end 
            # Windows is \r\n for carriage return, line feed
            # Macintosh and Linux use \n

            #if data == "\r".encode():
                # For Windows boxen on the other end
                #serial_port.write("\n".encode())


except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
