import cv2
import numpy as np
import time
import serial

ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

def make_command(cmd,left_speed,right_speed):
	cmd_to_arduino = cmd + chr(int(left_speed)) + chr(int(right_speed))
	return cmd_to_arduino

def nothing(x):
	pass

cam = cv2.VideoCapture(0)
move = False
cmd = 'S'
left_speed = 0
right_speed = 0
zero_str = 'S' + chr(0) + chr(0)

try:
	while True:
		ret, frame = cam.read()

		#start = time.time()    #to measure time taken to process one frame

		#frame = cv2.resize(frame,(320,240))
		frame = cv2.resize(frame,(960,720))
		#frame = cv2.resize(frame,(1440,1080))

		#cv2.imshow('piCam',frame)
		#cv2.moveWindow('piCam',0,0)

		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		#cv2.imshow('HSV',hsv)
		#cv2.moveWindow('HSV',0,260)

		hue_l = 4
		hue_h = 17

		sat_l = 168
		sat_h = 229

		val_l = 189
		val_h = 255

		hue2_l = 10
		hue2_h = 15

		lower_bnd = np.array([hue_l,sat_l,val_l])
		upper_bnd = np.array([hue_h,sat_h,val_h])
		lower2_bnd = np.array([hue2_l,sat_l,val_l])
		upper2_bnd = np.array([hue2_h,sat_h,val_h])

		FGMask = cv2.inRange(hsv,lower_bnd,upper_bnd)
		#cv2.imshow('FG mask', FGMask)
		#cv2.moveWindow('FG mask',0,260)

		FG2Mask = cv2.inRange(hsv,lower2_bnd,upper2_bnd)

		FG = cv2.bitwise_and(frame,frame,mask = FGMask)
		#cv2.imshow('FG', FG)
		#cv2.moveWindow('FG',330,0)

		FG2 = cv2.bitwise_and(frame,frame,mask = FG2Mask)

		FGmaskComp = cv2.add(FGMask,FG2Mask)

		BGMask = cv2.bitwise_not(FGMask)
		#cv2.imshow('BG mask', BGMask)
		#cv2.moveWindow('BG mask',330,260)

		BG_mask = cv2.cvtColor(BGMask,cv2.COLOR_GRAY2BGR)

		final1 = cv2.add(FG,BG_mask)
		final = cv2.add(final1,FG2)
		#cv2.imshow('Final', final)
		#cv2.moveWindow('Final',660,0)

		#_,contours,_=cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		contours,_ =cv2.findContours(FGmaskComp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
		for cnt in contours:
			area=cv2.contourArea(cnt)
			(x,y,w,h)=cv2.boundingRect(cnt)
			if area >= 300:
				x_cord = x + w/2
				move = True
				#cv2.drawContours(frame,[cnt],0,(255,0,0),3)
				cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
				print("Object detected at " + str(x_cord))

			else:
				x_cord = 720/2
				move = False


		if(move):
			if(x_cord < 320):       #let there be 40px deadband each side of center of screen
				left_speed = (x_cord/360)*62 + 64
				right_speed = 126

			elif(x_cord > 400):
				left_speed = 126
				right_speed = ((720 - x_cord)/360)*62 + 64

			else:
				left_speed = 126
				right_speed = 126

		else:
			left_speed = 95
			right_speed = 95

		command = make_command(cmd, left_speed, right_speed)
		ser.write(command.encode())


		#cv2.imshow('piCam',frame)
		#cv2.moveWindow('piCam',0,0)

		#fps = cam.get(cv2.CAP_PROP_FPS)
		#print(format(fps))

		#time.sleep(0.1)
		#end = time.time()

		#print(end-start)
		#time.sleep(0.25)

		if cv2.waitKey(1) == ord('q'):
			ser.write(zero_str.encode())
			break

except KeyboardInterrupt:
	ser.write(zero_str.encode())

cam.release()
cv2.destroyAllWindows()
