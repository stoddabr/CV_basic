import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def crop_into_zones(filename, vertical, horizontal, show=False, wait=500):
    field_img = cv.imread(filename)
    row, col, _ = field_img.shape
    print(row, col)
    x_borders = calculate_rectangle_edges(row, vertical)
    y_borders = calculate_rectangle_edges(col, horizontal)
    # split into small sections
    print(x_borders, y_borders)
    x_prev, y_prev = x_borders[0], y_borders[0]
    imgs = []
    i, j = 0, 0
    for x in x_borders[1:]:
        for y in y_borders[1:]:
            if show:
                cv.imshow('image',
                          field_img[x_prev:x, y_prev:y])
                cv.waitKey(wait)
            imgs.append(field_img[x_prev:x, y_prev:y])
            y_prev = y
        x_prev = x
        y_prev = y_borders[0]
    return imgs


def draw_lines(img_draw, vertical, horizontal):
    row, col, _ = img_draw.shape
    x_ = calculate_rectangle_edges(row, vertical)
    y_ = calculate_rectangle_edges(col, horizontal)
    for x in x_[1:]:
        cv.line(img_draw, (y_[0], x), (y_[-1], x), (0, 255, 0), 2)
    for y in y_[1:]:
        cv.line(img_draw, (y, x_[0]), (y, x_[-1]), (0, 0, 255), 2)
    return img_draw


def calculate_rectangle_edges(length, number):
    return [int(length / number * i) for i in range(number + 1)]


img = cv.imread('messi.JPG')
cv.imshow('image', img)
cv.waitKey(500)

list_of_crops = crop_into_zones('messi.JPG', 2, 10, show=False, wait=0)
img = draw_lines(img, 2, 10)
cv.imshow('image', img)
cv.waitKey(0)
print(len(list_of_crops))


for i, v in enumerate(range(2*10)):
    v = v+1
    ax1 = plt.subplot(2*10,2,v)
    ax1.hist(list_of_crops[i].ravel(), 256, [0, 255])

plt.show()
