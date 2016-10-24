import cv2



def main():
    print "begin vision"
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(1)

    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, frame = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)

        if key == 27:  # exit on ESC
            break
    vc.release()
    cv2.destroyWindow("preview")

if __name__ == "__main__":
    main()

