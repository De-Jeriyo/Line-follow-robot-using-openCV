import cv2

cap = cv2.VideoCapture(0)

def getImg(display=False, size=[480, 240]):
    success, img = cap.read()

    if not success:
        print("Failed to grab frame")
        return None

    img = cv2.resize(img, (size[0], size[1]))

    if display:
        cv2.imshow('IMG', img)
    return img


if __name__ == '__main__':
    while True:
        img = getImg(True)

        if img is None:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()