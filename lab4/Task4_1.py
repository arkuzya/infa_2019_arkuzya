from graph import *

#�������
penColor(0, 0, 0)
brushColor(0, 0, 0)
rectangle(0, 0, 500, 500)

#����
penColor(255, 233, 210)
brushColor(255, 233, 210)
polygon([(30, 80), (130, 370), (150, 370), (50, 80)])
polygon([(470, 80), (370, 370), (350, 370), (450, 80)])

#�����
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(45, 80, 25)
circle(455, 80, 25)

#������ �������������
penColor(0, 0, 0)
brushColor(0, 255, 0)
rectangle(10, 20, 490, 80)

#����
penColor("#cd5700")
brushColor("#cd5700")
circle(250, 480, 150)

#������������
penColor(0, 0, 0)
brushColor(0, 0, 0)
rectangle(0, 460, 500, 800)

#������
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(250, 250, 120)

#���������
penColor(0, 0, 0)
brushColor(114, 190, 255)
circle(215, 225, 25)
circle(285, 225, 25)

#������
penColor(0, 0, 0)
brushColor(0, 0, 0)
circle(215, 230, 7)
circle(285, 230, 7)

#���
penColor(0, 0, 0)
brushColor("#8d4100")
polygon([(250, 270), (240, 254), (260, 254)])

#���
penColor(0, 0, 0)
brushColor("#ff1a1a")
polygon([(250, 320), (190, 280), (310, 280)])

#������
penColor(0, 0, 0)
brushColor("#cd5700")
polygon([(150, 400), (110, 390), (105, 350), (150, 325), (175, 355)])
polygon([(350, 400), (390, 390), (395, 350), (350, 325), (325, 355)])

#������
penColor(0, 0, 0)
brushColor(255, 0, 255)
polygon([(145, 192), (165, 165), (132, 157)])
polygon([(160, 171), (182, 151), (152, 136)])
polygon([(176, 156), (200, 141), (174, 121)])
polygon([(193, 144), (224, 132), (195, 110)])
polygon([(218, 134), (252, 130), (230, 101)])
polygon([(500-145, 192), (500-165, 165), (500-132, 157)])
polygon([(500-160, 171), (500-182, 151), (500-152, 136)])
polygon([(500-176, 156), (500-200, 141), (500-174, 121)])
polygon([(500-193, 144), (500-224, 132), (500-195, 110)])
polygon([(500-218, 134), (500-252, 130), (500-230, 101)])

#�������
button("PYTHON is AMAZING", 10, 15, font = ("Arial", 24, "bold"), background="#00ff00", justify = CENTER, width = 25, height = 0)



run()