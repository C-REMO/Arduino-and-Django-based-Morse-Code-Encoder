import serial
from django.shortcuts import render


def index(request):
    return render(request, 'base.html', {})


def encode(request):
    if request.method == 'POST':
        msg_to_encode = request.POST.get('msg', '')
        try:
            '''Create serial connection, encode and send the message.
               My serial con. PORT is /dev/ttyACM0, yours may differ.'''
            serial_connection = serial.Serial('/dev/ttyACM0', 9600)
            CODE = {
                # English alphabet
                'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
                'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
                'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
                'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
                'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
                'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
                'Y': '-.--',   'Z': '--..',
                # Numbers
                '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
                '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
                '8': '---..',  '9': '----.',
                # Extended
                ' ': '/',       '.': '.-.-.-', ',': '--..--',   ':': '---...',
                '?': '..--..', "'": '.----.',  '-': '-....-',   '/': '-..-.',
                '@': '.--.-.', '=': '-...-',   '(': '-.--.',    ')': '-.--.-',
                '+': '.-.-.'
            }
            encoded_msg = ' '.join(CODE.get(char.upper())
                                   for char in msg_to_encode)
            serial_connection.write(encoded_msg.encode())
            serial_connection.close()
            serial_error = False
        except serial.SerialException:
            serial_error = True
    return render(request, 'base.html', {'serial_error': serial_error})
