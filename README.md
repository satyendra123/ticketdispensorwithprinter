# ticketdispensorwithprinter
in this i have making the esp32 with uartprinter by using the Tprinter.h library
name=ThermalPrinter library by BinaryWorlds
version=1.2
author=BinaryWorlds
maintainer=<BinaryWorlds.contact@gmail.com>
sentence=ThermalPrinter library for arduino and esp32
paragraph=ThermalPrinter library for arduino and esp32
category=Device Control
url=https://github.com/BinaryWorlds/ThermalPrinter
architectures=*




made by BinaryWorlds
Not for commercial use, in other case by free to use it.
Just copy this text and link to oryginal repository: https://github.com/BinaryWorlds/ThermalPrinter

I am not responsible for errors in the library. I deliver it "as it is".
I will be grateful for all suggestions.

Tested on firmware 2.69 and JP-QR701
Some features may not work on the older firmware.


#include "TPrinter.h"
#include <HardwareSerial.h>

const int printerBaudrate = 9600;  // or 19200 usually
const byte rxPin = 16;   // check datasheet of your board
const byte txPin = 17;   // check datasheet of your board
const byte dtrPin = 27;  // optional
const byte rsePin = 4;   // direction of transmission, max3485

HardwareSerial mySerial(1);
Tprinter myPrinter(&mySerial, printerBaudrate);

void setup() {
  micros();
  mySerial.begin(printerBaudrate, SERIAL_8N1, rxPin, txPin);  // must be 8N1 mode
  pinMode(rsePin, OUTPUT);     // optional
  digitalWrite(rsePin, HIGH);  // optional

  // myPrinter.enableDtr(dtrPin, LOW); // optional
  myPrinter.begin();
}
