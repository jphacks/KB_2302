import cv2
import numpy as np
import os

# 画像の特徴量を計算する関数
def calc_hist(img_path):
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist, hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    return hist.flatten()

# 画像の特徴量を比較する関数
def compare_hist(hist1, hist2):
    return cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

# 類似画像を検索する関数
def search_similar_images(query_path, dataset_path):
    query_hist = calc_hist(query_path)
    results = []
    for root, dirs, files in os.walk(dataset_path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                file_path = os.path.join(root, file)
                hist = calc_hist(file_path)
                similarity = compare_hist(query_hist, hist)
                results.append((file_path, similarity))
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# 類似画像を検索する
results = search_similar_images(
        r'/Users/kuroiwashuntarou/Workspace/KB_2302/FigSearch/figures/pencil case/target.jpg', 
        r'/Users/kuroiwashuntarou/Workspace/KB_2302/FigSearch/figures/'
    )

for result in results[:10]:
    print(result[0], result[1])
