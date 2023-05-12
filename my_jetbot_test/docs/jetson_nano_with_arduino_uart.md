# Guide to using UART between Jetson Nano and Arduino Uno

For my home-made jetbot built using parts lying around, I used Arduino Uno for low level control (controlling the motors). I chose arduino as I had it with me. 
In various blogs, I have read that it is convenient to use a servo driver (PCA9685 - 16 Channel 12-Bit PWM Servo Motor Driver I2C Module For Arduino). Also, there are various guides available online to use them.

However, for the scope of this guide, lets talk about UART interface between Jetson nano and arduino uno.

I tried to communicate between the 2 devices using the GPIO pins on Jetson nano (aka J41 header). 
Also, I used a 5V to 3.3V level converter to ensure proper handling of voltages as Jetson Nano works on 3.3V logic level and Arduino works on 5V.

Following is the pinout:
```
Jetson Nano Pin 8 (Tx) -> Rx of Arduino
Jetson Nano Pin 10(Rx) -> Tx of Arduino
Jetson Nano Pin 6 (GND) -> GND of Arduino
```

I tried a lot of online resources and guides, including the guide by [Jetson hacks](https://jetsonhacks.com/2019/10/10/jetson-nano-uart/), but I was not able to communicate reliably between the 2 devices.
I could read the data from arduino to jetson nano but when I tried to send data from jetson nano to arduino, arduino read gibberish data.
Even with different baud rates and different encoding schemes (UTF-8 and ASCII) the result was same.


Finally, I gave UART communication using USB a shot. And guess what? using exactly the same settings and encoding schemes I was easily able to communicate between the 2 devices.
The following code was used. Credits - Jetson Hacks.

### Jetson Nano side code:

```
#!/usr/bin/python3
import time
import serial		#please ensure that serial for python3 is installed in your jetson nano

print("UART Demonstration Program")
print("NVIDIA Jetson Nano Developer Kit")


serial_port = serial.Serial(
    port="/dev/ttyUSB0",	#please check port by command~ ls /dev/tty* ; for me it was ttyUSB0
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)

try:
    while True:
        if serial_port.inWaiting() > 0:
            #data = serial_port.read()
            print(data)
            serial_port.write('H'.encode())
            
		time.sleep(2)	#time in seconds


except KeyboardInterrupt:
    print("Exiting Program")

except Exception as exception_error:
    print("Error occurred. Exiting Program")
    print("Error: " + str(exception_error))

finally:
    serial_port.close()
    pass
```

### Arduino side code:

```
void setup()
{
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
}

char data_from_nano;

void loop()
{
  Serial.write("Hello Jetson!\n");
  data_from_nano = Serial.read();
  digitalWrite(LED_BUILTIN, LOW);
  delay(500); 
  if(data_from_nano == 'H')
  {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);  
  }
}
```


Other links that may be useful:
https://github.com/JetsonHacksNano/UARTDemo
[A good step by step guide](http://blog.rareschool.com/2019/05/five-steps-to-connect-jetson-nano-and.html)
https://www.seeedstudio.com/blog/2020/06/18/arduino-jeston-nano-xavier-nx-communication-using-python-via-usb-m/#:~:text=Firstly%2C%20connect%20your%20Arduino%20with,Type%20in%20the%20following%20command.&text=If%20you%20get%20%2Fdev%2FttyACM0,are%20connected%20to%20each%20other.
https://forums.developer.nvidia.com/t/serial-communication-between-jetson-nano-and-arduino-through-gpio/153941/7
https://blog.hubspot.com/website/what-is-utf-8
https://stackoverflow.com/questions/18534494/convert-from-utf-8-to-unicode-c
