from os.path import join as pjoin
import cv2
import os
import numpy as np


def resize_height_by_longest_edge(img_path, resize_length=800):
    org = cv2.imread(img_path)
    height, width = org.shape[:2]
    if height > width:
        return resize_length
    else:
        return int(resize_length * (height / width))


def CheckComponent(input_path_img):

    '''
        ele:min-grad: gradient threshold to produce binary map         
        ele:ffl-block: fill-flood threshold
        ele:min-ele-area: minimum area for selected elements 
        ele:merge-contained-ele: if True, merge elements contained in others
        text:max-word-inline-gap: words with smaller distance than the gap are counted as a line
        text:max-line-gap: lines with smaller distance than the gap are counted as a paragraph
        Tips:
        1. Larger *min-grad* produces fine-grained binary-map while prone to over-segment element to small pieces
        2. Smaller *min-ele-area* leaves tiny elements while prone to produce noises
        3. If not *merge-contained-ele*, the elements inside others will be recognized, while prone to produce noises
        4. The *max-word-inline-gap* and *max-line-gap* should be dependent on the input image size and resolution
        mobile: {'min-grad':4, 'ffl-block':5, 'min-ele-area':50, 'max-word-inline-gap':6, 'max-line-gap':1}
        web   : {'min-grad':3, 'ffl-block':5, 'min-ele-area':25, 'max-word-inline-gap':4, 'max-line-gap':4}
    '''
    
    
    key_params = {
        'min-grad':10, 
        'ffl-block':5, 
        'min-ele-area':50,
        'merge-contained-ele':True, 
        'merge-line-to-paragraph':False, 
        'remove-bar':True
    }

    # set input image path
    output_root = './'
    results = {}
    finalresults = {}

    resized_height = resize_height_by_longest_edge(input_path_img, resize_length=800)

    is_ip = True
    is_ocr = True
    is_merge = True

    if is_ocr:
        from .detect_text import text_detection as text
        op = text.text_detection(
            input_path_img, 
            output_root, 
            show=False
        )
        
        results['textjson'] = op

    if is_ip:
        from .lib_ip import ip_region_proposal as ip
        op = ip.compo_detection(
            input_path_img, 
            output_root, 
            key_params, 
            show=False
        )
        
        results['imagejson'] = op[0]
        results['image'] = op[1]
        
    if is_merge:
        from .detect_merge import merge as merge
        compo_json = results['imagejson']
        ocr_json = results['textjson']
        
        op = merge.merge(
            input_path_img, 
            compo_json, 
            ocr_json, 
            is_remove_bar=key_params['remove-bar'], 
            is_paragraph=key_params['merge-line-to-paragraph'], 
            show=False
        )
    
        finalresults['combinedimage'] = op[0]
        finalresults['combinedjson'] = op[1]
    
    return finalresults