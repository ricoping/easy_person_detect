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

