pip install pyscreenshot



import pyscreenshot 
image = pyscreenshot.grab()
#To display the captured screenshot
image.show()
#To save the screenshot
image.save("simon.png")



#program for partial screenshot
import pyscreenshot
#image=pyscreenshot.grab(bbox(x1,x2,y1,y2))
image = pyscreenshot.grab(bbox(10, 10, 500, 500))
#To view screenshot
image.show()
#To save the screenshot
image.save("simon.png")
