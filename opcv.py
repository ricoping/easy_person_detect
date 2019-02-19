import cv2, os


def isPerson(image_path):
	mode_xml = "haarcascade_frontalface_alt.xml"
	mode_xml = "haarcascade_eye.xml"
	mode_xml = "lbpcascade_frontalface_improved.xml"
	script_path = os.path.dirname(__file__)
	#cascade_path = os.path.join(script_path, "opencv", "opencv", "data", "lbpcascades", mode_xml)
	cascade_path = os.path.join(script_path, mode_xml)

	color = (255,255,255)

	image = cv2.imread(image_path)

	image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cascade = cv2.CascadeClassifier(cascade_path)

	facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

	print(facerect)

	if len(facerect) > 0:
		return True
	else:
		return False

print(isPerson("data_3.jpg"))