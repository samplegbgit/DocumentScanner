import cv2
import numpy as np

def reorder(points):
    points = points.reshape((4, 2))

    new_points = np.zeros((4, 1, 2), dtype=np.int32)

    add = points.sum(1)
    diff = np.diff(points, axis=1)

    new_points[0] = points[np.argmin(add)]  
    new_points[3] = points[np.argmax(add)]   
    new_points[1] = points[np.argmin(diff)] 
    new_points[2] = points[np.argmax(diff)]  

    return new_points

img = cv2.imread("document.jpg")

if img is None:
    print("Image not found!")
    exit()

original = img.copy()


img = cv2.resize(img, (800, 800))
original = cv2.resize(original, (800, 800))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 1)

edges = cv2.Canny(blur, 50, 150)


contours, _ = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

biggest = np.array([])
max_area = 0


for c in contours:
    area = cv2.contourArea(c)

    if area > 5000:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4 and area > max_area:
            biggest = approx
            max_area = area


if biggest.size != 0:

    
    cv2.drawContours(img, [biggest], -1, (0, 255, 0), 3)

  
    biggest = reorder(biggest)

    pts1 = np.float32(biggest)

    pts2 = np.float32([
        [0, 0],
        [800, 0],
        [0, 800],
        [800, 800]
    ])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    warped = cv2.warpPerspective(original, matrix, (800, 800))

  
    gray_scan = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)

    scanned = cv2.adaptiveThreshold(
        gray_scan,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )


    cv2.imwrite("scanned_document.jpg", scanned)

    
    cv2.imshow("Original", original)
    cv2.imshow("Detected", img)
    cv2.imshow("Scanned", scanned)

else:
    print("No document detected!")

cv2.waitKey(0)
cv2.destroyAllWindows()