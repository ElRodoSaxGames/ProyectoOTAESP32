import time

def loop():
    counter = 0
    while True:
        # aquí leerías sensores y mandarías a la nube
        print("dato:", counter)
        counter += 1
        time.sleep(2)
