import serial, sys, time, commands, re 
import logging

device = None
baud = 9600

if not device:
    devicelist = commands.getoutput("ls /dev/ttyAMA*")
    if devicelist[0] == '/':
        device = devicelist
    if not device: 
        print "Fatal: Can't find usb serial device."
        sys.exit(0);
    else:
        print "Success: device = %s"% device

ser = serial.Serial(
    port=device,
    baudrate=baud,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

#https://stackoverflow.com/a/27628622
def readline(a_serial, eol=b'\r\n'):
    leneol = len(eol)
    line = bytearray()
    while True:
        c = a_serial.read(1)
        if c:
            line += c
            if line[-leneol:] == eol:
                break
        else:
            break
    return bytes(line)


while True:
    try:
        line = readline(ser)
        print "len = %d\r\n" % len(line)
        print " ".join(hex(ord(n)) for n in line)
    except Exception as e:
        print e
    except KeyboardInterrupt:
        print "closing serial port..."
        ser.close()
        sys.exit()
    finally:
        pass

