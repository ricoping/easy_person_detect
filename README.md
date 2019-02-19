# easy_person_detect
You can roughly classify the image files on the basis of whether there is person in them.

# Requirement
You need to install opencv-python. My version is 4.0.0.21.
~~~
pip install opencv-python
~~~

# How to use
Both *lbpcascade_frontalface_improved.xml* and *opcv.py* need to be on the same directory.

# Example
~~~
import opcv
opcv.isPerson(person.jpg) # True
opcv.isPerson(not_person.jpg) # False
~~~

![person](https://user-images.githubusercontent.com/47266653/53034718-24a58e80-34b7-11e9-919d-18fd40bc2e0b.jpg)
![not_person](https://user-images.githubusercontent.com/47266653/53034723-2707e880-34b7-11e9-95fd-d321f6e34572.jpg)
