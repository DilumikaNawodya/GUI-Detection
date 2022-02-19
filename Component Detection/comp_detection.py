# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 21:41:41 2022

@author: dncna
"""

import cv2
import numpy as np
import pandas as pd
import os

# Image read and binarizarion

def read_img(img_path, height=None):
    
    try:
        img = cv2.imread(img_path)
        
        if height is not None:
            
            w_h_ratio = img.shape[0] / img.shape[1]
            width = height / w_h_ratio
            img = cv2.resize(img, (int(width), int(height)))
            
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        return img, gray
            
    except Exception as e:
        print(e)
        print("Image reading failed")
        
        return None, None
  
def bin_image(img, grad_min):
    
    
    img_f = np.copy(img)
    img_f = img_f.astype("float")

    kernel_h = np.array([[0,0,0], [0,-1.,1.], [0,0,0]])
    kernel_v = np.array([[0,0,0], [0,-1.,0], [0,1.,0]])
    
    dst1 = abs(cv2.filter2D(img_f, -1, kernel_h))
    dst2 = abs(cv2.filter2D(img_f, -1, kernel_v))
    
    gradient = (dst1 + dst2).astype('uint8')

    rec, binary = cv2.threshold(gradient, grad_min, 255, cv2.THRESH_BINARY)
    morph = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, (3, 3))

    cv2.imshow('binary', morph)
    cv2.waitKey(0)
        
    return morph



# Detect lines

def rm_line(binary, max_line_thickness=8, min_line_length_ratio=0.95):
    
    def is_valid_line(line):
        line_length = 0
        line_gap = 0
        for j in line:
            if j > 0:
                if line_gap > 5:
                    return False
                line_length += 1
                line_gap = 0
            elif line_length > 0:
                line_gap += 1
        if line_length / width > 0.95:
            return True
        return False

    height, width = binary.shape[:2]
    board = np.zeros(binary.shape[:2], dtype=np.uint8)

    start_row, end_row = -1, -1
    check_line = False
    check_gap = False
    for i, row in enumerate(binary):

        if is_valid_line(row):
            # new start: if it is checking a new line, mark this row as start
            if not check_line:
                start_row = i
                check_line = True
        else:
            # end the line
            if check_line:
                # thin enough to be a line, then start checking gap
                if i - start_row < max_line_thickness:
                    end_row = i
                    check_gap = True
                else:
                    start_row, end_row = -1, -1
                check_line = False
        # check gap
        if check_gap and i - end_row > max_line_thickness:
            binary[start_row: end_row] = 0
            start_row, end_row = -1, -1
            check_line = False
            check_gap = False

    if (check_line and (height - start_row) < max_line_thickness) or check_gap:
        binary[start_row: end_row] = 0

    cv2.imshow('no-line binary', binary)
    cv2.waitKey(0)


# Detect components

def component_detection(binary, min_obj_area,
                        line_thickness=8,
                        min_rec_evenness=0.7,
                        max_dent_ratio=0.25,
                        step_h = 5, step_v = 2,
                        rec_detect=False, show=False, test=False):
    """
    :param binary: Binary image from pre-processing
    :param min_obj_area: If not pass then ignore the small object
    :param min_obj_perimeter: If not pass then ignore the small object
    :param line_thickness: If not pass then ignore the slim object
    :param min_rec_evenness: If not pass then this object cannot be rectangular
    :param max_dent_ratio: If not pass then this object cannot be rectangular
    :return: boundary: [top, bottom, left, right]
                        -> up, bottom: list of (column_index, min/max row border)
                        -> left, right: list of (row_index, min/max column border) detect range of each row
    """
    
    mask = np.zeros((binary.shape[0] + 2, binary.shape[1] + 2), dtype=np.uint8)
    compos_all = []
    compos_rec = []
    compos_nonrec = []
    row, column = binary.shape[0], binary.shape[1]
    
    
    cv2.imshow("mask", mask)
    cv2.waitKey(0)
    
    
    for i in range(0, row, step_h):
        for j in range(i % 2, column, step_v):
            if binary[i, j] == 255 and mask[i, j] == 0:

                mask_copy = mask.copy()
                ff = cv2.floodFill(binary, mask, (j, i), None, 0, 0, cv2.FLOODFILL_MASK_ONLY)
                
                if ff[0] < min_obj_area: 
                    continue
                

                
                mask_copy = mask - mask_copy
                region = np.reshape(cv2.findNonZero(mask_copy[1:-1, 1:-1]), (-1, 2))
                region = [(p[1], p[0]) for p in region]

                print(region)

                '''

                # filter out some compos
                component = Component(region, binary.shape)
                
                # calculate the boundary of the connected area
                # ignore small area
                if component.width <= 3 or component.height <= 3:
                    continue
                # check if it is line by checking the length of edges
                # if component.compo_is_line(line_thickness):
                #     continue

                if test:
                    print('Area:%d' % (len(region)))
                    draw.draw_boundary([component], binary.shape, show=True)

                compos_all.append(component)

                if rec_detect:
                    # rectangle check
                    if component.compo_is_rectangle(min_rec_evenness, max_dent_ratio):
                        component.rect_ = True
                        compos_rec.append(component)
                    else:
                        component.rect_ = False
                        compos_nonrec.append(component)

                if show:
                    print('Area:%d' % (len(region)))
                    draw.draw_boundary(compos_all, binary.shape, show=True)

    # draw.draw_boundary(compos_all, binary.shape, show=True)
    if rec_detect:
        return compos_rec, compos_nonrec
    else:
        return compos_all
    '''

img, gray = read_img('C:\Education\Projects\Client Projects\Chavika\ML_Module\GUI Detection model\Component Detection/sample.jpeg')
morph = bin_image(gray, 10)

rm_line(morph)
component_detection(morph, 50)


cv2.destroyAllWindows()
