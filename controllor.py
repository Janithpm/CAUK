from pynput import *
import serial

v = ""
while True:
	port_name = input("Enter the BT port :")
	confirm = input("confirm ? [y/n] :")

	if confirm.lower() == "y" or port_name.lower() == "yes":
		try:
			seri = serial.Serial(port_name,9600)
			print("\n_________Serial Port Conected !__________\n")
			break
		except:
			print("invalied input !\n")
	else:
		print("\n")
		continue
		
			

def on_press(key):

	if key == keyboard.Key.esc or key == keyboard.KeyCode(char="q") or key == keyboard.KeyCode(char="Q") :
		quit()
	elif key == keyboard.Key.up:
		v = "1"
	elif key == keyboard.Key.down:
		v= "2"

seri.write(v.encode())


with keyboard.Listener(on_press=on_press) as listener:
	listener.join()

