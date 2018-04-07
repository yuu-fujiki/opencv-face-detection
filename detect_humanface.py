import cv2

# イメージファイルの読み込み
img = cv2.imread('kinya.png')

# グレースケール変換
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Haar-like特徴分類器の読み込み
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

facerect = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

# 顔を検知
# faces = face_cascade.detectMultiScale(gray)
# for (x,y,w,h) in faces:
#     # 検知した顔を矩形で囲む
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     # 顔画像（グレースケール）
#     roi_gray = gray[y:y+h, x:x+w]
#     # 顔画像（カラースケール）
#     roi_color = img[y:y+h, x:x+w]
#     # 顔の中から目を検知
#     # eyes = eye_cascade.detectMultiScale(roi_gray)
#     # for (ex,ey,ew,eh) in eyes:
#     #     # 検知した目を矩形で囲む
#     #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

if len(facerect) > 0:
    for rect in facerect:
        img = img[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
#顔が検出されなかった時
else:
    print("no face")

# 画像表示
cv2.imshow('img',img)
cv2.imwrite('./cascadedface.png', img)

# 何かキーを押したら終了
cv2.waitKey(0)
cv2.destroyAllWindows()
