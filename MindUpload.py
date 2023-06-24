'''
A machine learning model which can use the video camera,microphone and data inputs from the user to make a replica of themselves,
essentially uploading their mind into the computer systems becoming immortal.    
'''

'''
Step1.Capturing Images through webcam and storing it.
'''
import cv2
cam=cv2.VideoCapture(0)

cv2.namedWindow("Python Camera")

img_counter =0

while True:
    ret,frame=cam.read()
    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("test",frame)

    k =cv2.waitKey(1)
    if k%256==27: #Esc is pressed
        print("Escape hit, closing the app")
        break

    elif k%256 ==32: #Space is hit
        img_name ='photo{}.png'.format(img_counter)
        cv2.imwrite(img_name,frame)
        print("photo taken")
        img_counter=+1
cam.release()
cam.destroyAllWindows()
'''
Step2.Using the captured images to write a 3D model
'''

'''
Step3. Taking voice input from user.
'''
import pyaudio
import wave

audio=pyaudio.PyAudio()

stream =audio.open(format=pyaudio.pyInt16, channels=1, rate=44100,input=True, frames_per_buffer=1024)

frames=[]

try:
    while True:
        data=stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()

sound_file=wave.open("record.wav","wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.writeframes(b''.join(frames))
sound_file.close()