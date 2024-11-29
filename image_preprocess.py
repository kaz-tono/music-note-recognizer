# 入力画像にたいしてエッジ検出を行う
# 出力はエッジ画像

import cv2
import numpy as np
import matplotlib.pyplot as plt

def edge_detection(img):
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # エッジ検出
    edge = cv2.Canny(gray, 100, 200)
    return edge

if __name__ == '__main__':
    img = cv2.imread('resources/sample01.jpg')
    edge = edge_detection(img)
    cv2.imshow('edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('edge.jpg', edge)
    plt.imshow(edge, cmap='gray')
    plt.show()
