"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon
from campy.graphics.gwindow import GWindow, pause

WIDTH = 700
HEIGHT = 1000


def main():
    """
    TODO:
    """
    window = GWindow(WIDTH, HEIGHT)

    # The outline includes (1) background color (2) Batman (3) Mouth outline

    background = GRect(WIDTH, HEIGHT, x=0, y=0)
    background.filled = True
    background.fill_color = '#3D797F'
    background.color = '#3D797F'
    window.add(background)

    batman = GPolygon()
    batman.add_vertex((208, 66))
    batman.add_vertex((240, 175))
    batman.add_vertex((350, 150))
    batman.add_vertex((460, 175))
    batman.add_vertex((492, 66))
    batman.add_vertex((565, 310))
    batman.add_vertex((585, 590))
    batman.add_vertex((700, 635))
    batman.add_vertex((700, 1000))
    batman.add_vertex((0, 1000))
    batman.add_vertex((0, 635))
    batman.add_vertex((115, 590))
    batman.add_vertex((135, 310))
    batman.filled = True
    batman.fill_color = '#010101'
    batman.color = '#010101'
    window.add(batman)

    mouth = GPolygon()
    mouth.add_vertex((220, 745))
    mouth.add_vertex((270, 745))
    mouth.add_vertex((285, 755))
    mouth.add_vertex((335, 790))
    mouth.add_vertex((345, 800))
    mouth.add_vertex((375, 785))
    mouth.add_vertex((440, 795))
    mouth.add_vertex((460, 835))
    mouth.add_vertex((435, 885))
    mouth.add_vertex((410, 910))
    mouth.add_vertex((370, 930))
    mouth.add_vertex((325, 930))
    mouth.add_vertex((285, 910))
    mouth.add_vertex((240, 860))
    mouth.add_vertex((220, 835))
    mouth.add_vertex((200, 780))
    mouth.filled = True
    mouth.fill_color = '#EDAD87'
    mouth.color = '#010101'
    window.add(mouth)

    # Face shadows: (1) Nose (2) Left eyebrow (3) Right eyebrow (4) lower eye shadow

    nose = GPolygon()
    nose.add_vertex((330, 635))
    nose.add_vertex((340, 630))
    nose.add_vertex((345, 800))
    nose.add_vertex((335, 790))
    nose.filled = True
    nose.fill_color = '#3B6C79'
    nose.color = '#3B6C79'
    window.add(nose)

    left_eyebrow = GPolygon()
    left_eyebrow.add_vertex((200, 370))
    left_eyebrow.add_vertex((305, 615))
    left_eyebrow.add_vertex((190, 545))
    left_eyebrow.filled = True
    left_eyebrow.fill_color = '#3B6C79'
    left_eyebrow.color = '#3B6C79'
    window.add(left_eyebrow)

    right_eyebrow = GPolygon()
    right_eyebrow.add_vertex((390, 510))
    right_eyebrow.add_vertex((395, 545))
    right_eyebrow.add_vertex((365, 615))
    right_eyebrow.add_vertex((360, 580))
    right_eyebrow.filled = True
    right_eyebrow.fill_color = '#3B6C79'
    right_eyebrow.color = '#3B6C79'
    window.add(right_eyebrow)

    lower_eyeshadow = GPolygon()
    lower_eyeshadow.add_vertex((180, 610))
    lower_eyeshadow.add_vertex((205, 670))
    lower_eyeshadow.add_vertex((190, 600))
    lower_eyeshadow.add_vertex((210, 650))
    lower_eyeshadow.add_vertex((245, 665))
    lower_eyeshadow.add_vertex((300, 635))
    lower_eyeshadow.add_vertex((275, 720))
    lower_eyeshadow.add_vertex((190, 680))
    lower_eyeshadow.filled = True
    lower_eyeshadow.fill_color = '#3B6C79'
    lower_eyeshadow.color = '#3B6C79'
    window.add(lower_eyeshadow)

    # Eyes: (1) Eye_white (2) eye_black (3) eye_brown (4) eye_soul (5) eye_shadow

    eye_white = GPolygon()
    eye_white.add_vertex((225, 600))
    eye_white.add_vertex((276, 618))
    eye_white.add_vertex((278, 622))
    eye_white.add_vertex((275, 625))
    eye_white.add_vertex((258, 627))
    eye_white.add_vertex((242, 624))
    eye_white.add_vertex((227, 617))
    eye_white.add_vertex((220, 610))
    eye_white.filled = True
    eye_white.fill_color = '#F4F5F5'
    eye_white.color = '#F4F5F5'
    window.add(eye_white)

    eye_black = GOval(23, 23)
    eye_black.filled = True
    eye_black.fill_color = '#010001'
    eye_black.color = '#010001'
    window.add(eye_black, x=240, y=600)

    eye_brown = GOval(18, 18)
    eye_brown.filled = True
    eye_brown.fill_color = '#251D1B'
    eye_brown.color = '#251D1B'
    window.add(eye_brown, x=243, y=600)

    eye_soul = GOval(5, 5)
    eye_soul.filled = True
    eye_soul.fill_color = '#F4F5F5'
    eye_soul.color = '#F4F5F5'
    window.add(eye_soul, x=245, y=608)

    eye_cover = GPolygon()
    eye_cover.add_vertex((225, 600))
    eye_cover.add_vertex((276, 618))
    eye_cover.add_vertex((255, 600))
    eye_cover.filled = True
    eye_cover.fill_color = '#010101'
    eye_cover.color = '#010101'
    window.add(eye_cover)

    eye_shadow_1 = GPolygon()
    eye_shadow_1.add_vertex((220, 610))
    eye_shadow_1.add_vertex((227, 617))
    eye_shadow_1.add_vertex((242, 624))
    eye_shadow_1.add_vertex((239, 640))
    eye_shadow_1.add_vertex((250, 650))
    eye_shadow_1.add_vertex((225, 650))
    eye_shadow_1.add_vertex((215, 640))
    eye_shadow_1.add_vertex((210, 625))
    eye_shadow_1.filled = True
    eye_shadow_1.fill_color = '#49586D'
    eye_shadow_1.color = '#49586D'
    window.add(eye_shadow_1)

    eye_shadow_2 = GPolygon()
    eye_shadow_2.add_vertex((242, 624))
    eye_shadow_2.add_vertex((239, 640))
    eye_shadow_2.add_vertex((260, 640))
    eye_shadow_2.add_vertex((258, 627))
    eye_shadow_2.filled = True
    eye_shadow_2.fill_color = '#313C65'
    eye_shadow_2.color = '#313C65'
    window.add(eye_shadow_2)

    eye_shadow_3 = GPolygon()
    eye_shadow_3.add_vertex((219, 632))
    eye_shadow_3.add_vertex((239, 640))
    eye_shadow_3.add_vertex((215, 633))
    eye_shadow_3.add_vertex((210, 625))
    eye_shadow_3.filled = True
    eye_shadow_3.fill_color = '#313C65'
    eye_shadow_3.color = '#313C65'
    window.add(eye_shadow_3)

    # Mouth details
    md_1 = GPolygon()
    md_1.add_vertex((270, 745))
    md_1.add_vertex((220, 835))
    md_1.add_vertex((200, 780))
    md_1.filled = True
    md_1.fill_color = '#AD6B63'
    md_1.color = '#AD6B63'
    window.add(md_1)

    md_2 = GPolygon()
    md_2.add_vertex((420, 810))
    md_2.add_vertex((445, 810))
    md_2.add_vertex((440, 825))
    md_2.add_vertex((460, 835))
    md_2.add_vertex((435, 885))
    md_2.add_vertex((410, 910))
    md_2.add_vertex((370, 930))
    md_2.add_vertex((405, 885))
    md_2.add_vertex((325, 855))
    md_2.add_vertex((320, 850))
    md_2.add_vertex((350, 830))
    md_2.add_vertex((348, 820))
    md_2.add_vertex((370, 815))
    md_2.add_vertex((415, 815))
    md_2.filled = True
    md_2.fill_color = '#000100'
    md_2.color = '#000100'
    window.add(md_2)

    md_3 = GPolygon()
    md_3.add_vertex((435, 885))
    md_3.add_vertex((410, 910))
    md_3.add_vertex((370, 930))
    md_3.add_vertex((405, 885))
    md_3.filled = True
    md_3.fill_color = '#7A4751'
    md_3.color = '#7A4751'
    window.add(md_3)

    md_4 = GPolygon()
    md_4.add_vertex((410, 825))
    md_4.add_vertex((410, 835))
    md_4.add_vertex((385, 850))
    md_4.add_vertex((320, 850))
    md_4.add_vertex((320, 850))
    md_4.add_vertex((290, 830))
    md_4.add_vertex((295, 820))
    md_4.add_vertex((350, 830))
    md_4.add_vertex((380, 820))
    md_4.filled = True
    md_4.fill_color = '#430E12'
    md_4.color = '#430E12'
    window.add(md_4)

    md_5 = GPolygon()
    md_5.add_vertex((380, 820))
    md_5.add_vertex((410, 825))
    md_5.add_vertex((372, 844))
    md_5.add_vertex((350, 842))
    md_5.add_vertex((305, 840))
    md_5.add_vertex((290, 830))
    md_5.add_vertex((295, 820))
    md_5.add_vertex((350, 830))
    md_5.filled = True
    md_5.fill_color = '#9B5353'
    md_5.color = '#9B5353'
    window.add(md_5)

    md_6 = GPolygon()
    md_6.add_vertex((380, 820))
    md_6.add_vertex((386, 828))
    md_6.add_vertex((367, 838))
    md_6.add_vertex((316, 835))
    md_6.add_vertex((295, 820))
    md_6.add_vertex((350, 830))
    md_6.filled = True
    md_6.fill_color = '#EB8A73'
    md_6.color = '#EB8A73'
    window.add(md_6)

    md_7 = GPolygon()
    md_7.add_vertex((330, 815))
    md_7.add_vertex((348, 820))
    md_7.add_vertex((350, 830))
    md_7.add_vertex((295, 820))
    md_7.add_vertex((290, 830))
    md_7.add_vertex((282, 827))
    md_7.add_vertex((279, 822))
    md_7.add_vertex((293, 817))
    md_7.filled = True
    md_7.fill_color = '#390F11'
    md_7.color = '#390F11'
    window.add(md_7)

    md_8 = GPolygon()
    md_8.add_vertex((330, 815))
    md_8.add_vertex((348, 820))
    md_8.add_vertex((345, 800))
    md_8.add_vertex((335, 790))
    md_8.filled = True
    md_8.fill_color = '#714850'
    md_8.color = '#714850'
    window.add(md_8)

    md_9 = GPolygon()
    md_9.add_vertex((375, 785))
    md_9.add_vertex((418, 790))
    md_9.add_vertex((445, 810))
    md_9.add_vertex((420, 810))
    md_9.add_vertex((415, 815))
    md_9.add_vertex((370, 815))
    md_9.filled = True
    md_9.fill_color = '#4F2A3B'
    md_9.color = '#4F2A3B'
    window.add(md_9)

    md_10 = GPolygon()
    md_10.add_vertex((405, 885))
    md_10.add_vertex((370, 855))
    md_10.add_vertex((325, 855))
    md_10.add_vertex((295, 866))
    md_10.add_vertex((297, 875))
    md_10.add_vertex((285, 910))
    md_10.add_vertex((325, 930))
    md_10.filled = True
    md_10.fill_color = '#4F2A39'
    md_10.color = '#4F2A39'
    window.add(md_10)

    md_11 = GPolygon()
    md_11.add_vertex((367, 867))
    md_11.add_vertex((362, 910))
    md_11.add_vertex((330, 910))
    md_11.add_vertex((285, 910))
    md_11.add_vertex((297, 875))
    md_11.add_vertex((325, 865))
    md_11.filled = True
    md_11.fill_color = '#EAAB8F'
    md_11.color = '#EAAB8F'
    window.add(md_11)

    md_12 = GPolygon()
    md_12.add_vertex((405, 885))
    md_12.add_vertex((370, 930))
    md_12.add_vertex((325, 930))
    md_12.filled = True
    md_12.fill_color = '#3E1312'
    md_12.color = '#3E1312'
    window.add(md_12)

    md_13 = GPolygon()
    md_13.add_vertex((297, 875))
    md_13.add_vertex((325, 865))
    md_13.add_vertex((285, 910))
    md_13.filled = True
    md_13.fill_color = '#ECB583'
    md_13.color = '#ECB583'
    window.add(md_13)

    md_14 = GPolygon()
    md_14.add_vertex((305, 795))
    md_14.add_vertex((332, 802))
    md_14.add_vertex((330, 815))
    md_14.add_vertex((293, 817))
    md_14.add_vertex((279, 822))
    md_14.add_vertex((270, 800))
    md_14.filled = True
    md_14.fill_color = '#EECC9A'
    md_14.color = '#EECC9A'
    window.add(md_14)

    md_15 = GPolygon()
    md_15.add_vertex((305, 795))
    md_15.add_vertex((270, 800))
    md_15.add_vertex((246, 790))
    md_15.add_vertex((270, 745))
    md_15.filled = True
    md_15.fill_color = '#E49377'
    md_15.color = '#E49377'
    window.add(md_15)

    md_16 = GPolygon()
    md_16.add_vertex((262, 883))
    md_16.add_vertex((270, 800))
    md_16.add_vertex((246, 790))
    md_16.add_vertex((220, 835))
    md_16.filled = True
    md_16.fill_color = '#EFB5A3'
    md_16.color = '#EFB5A3'
    window.add(md_16)

    md_17 = GPolygon()
    md_17.add_vertex((270, 800))
    md_17.add_vertex((279, 822))
    md_17.add_vertex((282, 827))
    md_17.add_vertex((320, 850))
    md_17.add_vertex((325, 855))
    md_17.add_vertex((295, 866))
    md_17.add_vertex((267, 840))
    md_17.filled = True
    md_17.fill_color = '#B58383'
    md_17.color = '#B58383'
    window.add(md_17)

    x_0 = 0
    y_0 = 0
    x_1 = 110
    y_1 = 110
    while x_1 <= window.width:
        line1 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line1.color = '#7BAFAC'
        window.add(line1)

        x_0 += 50
        x_1 += 50

    x_0 = 30
    y_0 = 30
    x_1 = 140
    y_1 = 140
    while x_1 <= window.width + 50:
        line2 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line2.color = '#7BAFAC'
        window.add(line2)

        x_0 += 75
        x_1 += 75

    x_0 = 10
    y_0 = 90
    x_1 = 120
    y_1 = 200
    while x_1 <= window.width:
        line3 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line3.color = '#7BAFAC'
        window.add(line3)

        x_0 += 100
        x_1 += 100

    x_0 = 30
    y_0 = 180
    x_1 = 105
    y_1 = 255

    while x_1 <= window.width / 4:
        line4 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line4.color = '#7BAFAC'
        window.add(line4)

        x_0 += 50
        x_1 += 50

    x_0 = 550
    y_0 = 180
    x_1 = 625
    y_1 = 255

    while x_1 < window.width + 10:
        line5 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line5.color = '#7BAFAC'
        window.add(line5)

        x_0 += 75
        x_1 += 75

    x_0 = 10
    y_0 = 280
    x_1 = 100
    y_1 = 370

    while x_1 <= window.width / 4:
        line6 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line6.color = '#7BAFAC'
        window.add(line6)

        x_0 += 60
        x_1 += 60

    x_0 = 530
    y_0 = 280
    x_1 = 620
    y_1 = 370

    while x_1 < window.width + 100:
        line7 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line7.color = '#7BAFAC'
        window.add(line7)

        x_0 += 60
        x_1 += 60

    x_0 = 0
    y_0 = 350
    x_1 = 50
    y_1 = 400

    while x_1 <= window.width / 4:
        line8 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line8.color = '#7BAFAC'
        window.add(line8)

        x_0 += 100
        x_1 += 100

    x_0 = 540
    y_0 = 350
    x_1 = 590
    y_1 = 400

    while x_1 < window.width + 100:
        line8 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line8.color = '#7BAFAC'
        window.add(line8)

        x_0 += 75
        x_1 += 75

    x_0 = 20
    y_0 = 420
    x_1 = 90
    y_1 = 490

    while x_1 <= window.width / 4:
        line9 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line9.color = '#7BAFAC'
        window.add(line9)

        x_0 += 65
        x_1 += 65

    x_0 = 560
    y_0 = 420
    x_1 = 630
    y_1 = 490

    while x_1 < window.width + 100:
        line10 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line10.color = '#7BAFAC'
        window.add(line10)

        x_0 += 55
        x_1 += 55

    x_0 = 5
    y_0 = 470
    x_1 = 75
    y_1 = 540

    while x_1 <= window.width / 4:
        line11 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line11.color = '#7BAFAC'
        window.add(line11)

        x_0 += 90
        x_1 += 90

    x_0 = 580
    y_0 = 470
    x_1 = 650
    y_1 = 540

    while x_1 < window.width + 100:
        line12 = GLine(x0=x_0, y0=y_0, x1=x_1, y1=y_1)
        line12.color = '#7BAFAC'
        window.add(line12)

        x_0 += 65
        x_1 += 65

    title = GLabel('Batman', x=520, y=950)
    title.color = '#FFD302'
    title.font = '-40'
    window.add(title)

    circle_1 = GOval(160, 70, x=503, y=895)
    circle_1.filled = False
    circle_1.color = '#FFD302'
    window.add(circle_1)

    circle_2 = GOval(159, 69, x=503, y=895)
    circle_2.filled = False
    circle_2.color = '#FFD302'
    window.add(circle_2)

    circle_3 = GOval(161, 71, x=502, y=895)
    circle_3.filled = False
    circle_3.color = '#FFD302'
    window.add(circle_3)

    circle_4 = GOval(161, 71, x=502, y=894)
    circle_4.filled = False
    circle_4.color = '#FFD302'
    window.add(circle_4)

    circle_5 = GOval(162, 72, x=502, y=894)
    circle_5.filled = False
    circle_5.color = '#FFD302'
    window.add(circle_5)

    circle_6 = GOval(163, 73, x=502, y=893)
    circle_6.filled = False
    circle_6.color = '#FFD302'
    window.add(circle_6)

    circle_7 = GOval(163, 73, x=500, y=893)
    circle_7.filled = False
    circle_7.color = '#FFD302'
    window.add(circle_7)


if __name__ == '__main__':
    main()
