"""
Module: 2
Week: 2
Topic: Background Subtraction
"""

import numpy as np
import cv2

bg1_image = cv2.imread("assets/bg1.png", 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread("assets/ob1.png", 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread("assets/bg2.jpg", 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_diff(image1, image2):
    diff = cv2.absdiff(image1, image2)
    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    return diff


def compute_binary_mask(diff):
    _, mask = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)
    return mask


def replace_background(bg1, bg2, ob):
    diff_single = compute_diff(bg1, ob)
    mask = compute_binary_mask(diff_single)

    output = np.where(mask == 255, bg2, ob)

    return output
