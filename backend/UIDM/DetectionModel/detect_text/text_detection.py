from .ocr import *
from .Text import Text
import cv2
import json
import numpy as np
from os.path import join as pjoin


def save_detection_json(texts, img_shape):
    
    output = {'img_shape': img_shape, 'texts': []}
    for text in texts:
        c = {'id': text.id, 'content': text.content}
        loc = text.location
        c['column_min'], c['row_min'], c['column_max'], c['row_max'] = loc['left'], loc['top'], loc['right'], loc['bottom']
        c['width'] = text.width
        c['height'] = text.height
        output['texts'].append(c)
    
    return output



def visualize_texts(org_img, texts, shown_resize_height=None, show=False, write_path=None):
    img = org_img.copy()
    for text in texts:
        text.visualize_element(img, line=2)

    img_resize = img
    if shown_resize_height is not None:
        img_resize = cv2.resize(img, (int(shown_resize_height * (img.shape[1]/img.shape[0])), shown_resize_height))

    if show:
        cv2.imshow('texts', img_resize)
        cv2.waitKey(0)
        cv2.destroyWindow('texts')
    if write_path is not None:
        cv2.imwrite(write_path, img)


def text_sentences_recognition(texts):
    '''
    Merge separate words detected by Google ocr into a sentence
    '''
    changed = True
    while changed:
        changed = False
        temp_set = []
        for text_a in texts:
            merged = False
            for text_b in temp_set:
                if text_a.is_on_same_line(text_b, 'h', bias_justify=0.2 * min(text_a.height, text_b.height), bias_gap=2 * max(text_a.word_width, text_b.word_width)):
                    text_b.merge_text(text_a)
                    merged = True
                    changed = True
                    break
            if not merged:
                temp_set.append(text_a)
        texts = temp_set.copy()

    for i, text in enumerate(texts):
        text.id = i
    return texts


def merge_intersected_texts(texts):
    '''
    Merge intersected texts (sentences or words)
    '''
    changed = True
    while changed:
        changed = False
        temp_set = []
        for text_a in texts:
            merged = False
            for text_b in temp_set:
                if text_a.is_intersected(text_b, bias=2):
                    text_b.merge_text(text_a)
                    merged = True
                    changed = True
                    break
            if not merged:
                temp_set.append(text_a)
        texts = temp_set.copy()
    return texts


def text_cvt_orc_format(ocr_result):
    texts = []
    if ocr_result is not None:
        for i, result in enumerate(ocr_result):
            error = False
            x_coordinates = []
            y_coordinates = []
            text_location = result['boundingPoly']['vertices']
            content = result['description']
            for loc in text_location:
                if 'x' not in loc or 'y' not in loc:
                    error = True
                    break
                x_coordinates.append(loc['x'])
                y_coordinates.append(loc['y'])
            if error: continue
            location = {'left': min(x_coordinates), 'top': min(y_coordinates),
                        'right': max(x_coordinates), 'bottom': max(y_coordinates)}
            texts.append(Text(i, content, location))
    return texts


def text_filter_noise(texts):
    valid_texts = []
    for text in texts:
        if len(text.content) <= 1 and text.content.lower() not in ['a', ',', '.', '!', '?', '$', '%', ':', '&', '+']:
            continue
        valid_texts.append(text)
    return valid_texts


def text_detection(input_file, output_file, show=False):

    img = cv2.imread(input_file)

    ocr_result = ocr_detection_google(input_file)
    texts = text_cvt_orc_format(ocr_result)
    texts = merge_intersected_texts(texts)
    texts = text_filter_noise(texts)
    texts = text_sentences_recognition(texts)
    texts = save_detection_json(texts, img.shape)

    return(texts)

def area_calc(col_min, row_min, col_max, row_max):
    width = col_max - col_min
    height = row_max - row_min
    area = width * height
    
    return area


def calc_intersection_area(element_a, element_b, bias=(0, 0)):
    a = element_a
    b = element_b
    
    element_a_area = area_calc(a[0], a[1], a[2], a[3])
    element_b_area = area_calc(b[0], b[1], b[2], b[3])
    
    col_min_s = max(a[0], b[0]) - bias[0]
    row_min_s = max(a[1], b[1]) - bias[1]
    col_max_s = min(a[2], b[2])
    row_max_s = min(a[3], b[3])
    w = np.maximum(0, col_max_s - col_min_s)
    h = np.maximum(0, row_max_s - row_min_s)
    inter = w * h

    iou = inter / (element_a_area + element_b_area - inter)
    ioa = inter / element_a_area
    iob = inter / element_b_area

    return inter, iou, ioa, iob

glob_obj = []
def iterate(obj):
    
    for i in obj:
        if 'Children' in i:
            iterate(i['Children'])
        else:
            glob_obj.append({
                "Text": i['Text'],
                "Bounds": i['Bounds']
            })
    return 0

def meta_json_correction(op, input_file):
    
    with open(input_file, 'r') as f:
        j_data = json.load(f)
        
        iterate(j_data)
        
        for text in op['texts']:
            text['text_meta'] = []
            element_a = [text['column_min'], text['row_min'], text['column_max'], text['row_max']]
            for meta_text in glob_obj:
                element_b = meta_text['Bounds']
                inter, iou, ioa, iob = calc_intersection_area(element_a, element_b)
                
                
                if inter >= 0:
           
                    if iob >= 1:
                        text['text_meta'].append(meta_text['Text'])

        return op