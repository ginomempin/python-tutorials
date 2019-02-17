
import cv2
import numpy


def main():
    print("READ the img as a pixel array")
    img = cv2.imread("small_4x6.png", cv2.IMREAD_COLOR)
    print("SIZE: {}".format(img.shape))
    row_idx = 0
    for row in img:
        print("ROW: {}".format(row_idx))
        for pixel in row:
            blue, green, red = pixel
            print("  B={},G={},R={}".format(blue, green, red))
        row_idx += 1

    print("ACCESS the pixel at 0,2 (BLUE)")
    p02 = img[0, 2]
    print(p02)

    print("ACCESS the pixels of the last row (all BLACK)")
    plr = img[3, :]
    print(plr)

    print("STACK horizontally")
    img_x2_horz = numpy.hstack((img, img))
    print(img_x2_horz.shape)
    print("SAVE to a 4x12 image")
    ret = cv2.imwrite("small_4x12.png", img_x2_horz)
    print(ret)

    print("STACK vertically")
    img_x2_vert = numpy.vstack((img, img))
    print(img_x2_vert.shape)
    print("SAVE to a 8x6 image")
    ret = cv2.imwrite("small_8x6.png", img_x2_vert)
    print(ret)

    print("SPLIT horizontally")
    subs = numpy.hsplit(img, 2)
    print(subs[0].shape)
    print("SAVE to a 4x3 image")
    ret = cv2.imwrite("small_4x3.png", subs[0])
    print(ret)

    print("SPLIT vertically")
    subs = numpy.vsplit(img, 2)
    print(subs[0].shape)
    print("SAVE to a 2x6 image")
    ret = cv2.imwrite("small_2x6.png", subs[0])
    print(ret)


main()
