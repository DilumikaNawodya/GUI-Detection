import numpy as np
import cv2


class Element:
    def __init__(self, id, corner, category, text_content=None, text_meta=None):
        self.id = id
        self.category = category
        self.col_min, self.row_min, self.col_max, self.row_max = corner
        self.width = self.col_max - self.col_min
        self.height = self.row_max - self.row_min
        self.area = self.width * self.height

        self.text_content = text_content
        self.text_meta = text_meta
        
        self.parent_id = None
        self.text_children = [] 
        self.compo_children = [] 

    def init_bound(self):
        self.width = self.col_max - self.col_min
        self.height = self.row_max - self.row_min
        self.area = self.width * self.height

    def put_bbox(self):
        return self.col_min, self.row_min, self.col_max, self.row_max

    def wrap_info(self):
        info = {
            'id':self.id, 
            'class': self.category, 
            'height': self.height, 
            'width': self.width,
            'position': {
                'column_min': self.col_min, 
                'row_min': self.row_min, 
                'column_max': self.col_max,
                'row_max': self.row_max
            }
        }
        
        if self.text_content is not None:
            info['text_content'] = self.text_content
        if self.text_meta is not None:    
            info['text_meta'] = self.text_meta
        if len(self.text_children) > 0:
            info['embeddedtext'] = []
            for child in self.text_children:
                info['embeddedtext'].append(child.wrap_info())
        if len(self.compo_children) > 0:
            info['embeddedcompos'] = []
            for child in self.compo_children:
                info['embeddedcompos'].append(child.wrap_info())
        if self.parent_id is not None:
            info['parent'] = self.parent_id
        return info

    def resize(self, resize_ratio):
        self.col_min = int(self.col_min * resize_ratio)
        self.row_min = int(self.row_min * resize_ratio)
        self.col_max = int(self.col_max * resize_ratio)
        self.row_max = int(self.row_max * resize_ratio)
        self.init_bound()

    def element_merge(self, element_b, new_element=False, new_category=None, new_id=None):
        col_min_a, row_min_a, col_max_a, row_max_a = self.put_bbox()
        col_min_b, row_min_b, col_max_b, row_max_b = element_b.put_bbox()
        new_corner = (min(col_min_a, col_min_b), min(row_min_a, row_min_b), max(col_max_a, col_max_b), max(row_max_a, row_max_b))
        if element_b.text_content is not None:
            self.text_content = element_b.text_content if self.text_content is None else self.text_content + '\n' + element_b.text_content
        if new_element:
            return Element(new_id, new_corner, new_category)
        else:
            self.col_min, self.row_min, self.col_max, self.row_max = new_corner
            self.init_bound()

    def calc_intersection_area(self, element_b, bias=(0, 0)):
        a = self.put_bbox()
        b = element_b.put_bbox()
        col_min_s = max(a[0], b[0]) - bias[0]
        row_min_s = max(a[1], b[1]) - bias[1]
        col_max_s = min(a[2], b[2])
        row_max_s = min(a[3], b[3])
        w = np.maximum(0, col_max_s - col_min_s)
        h = np.maximum(0, row_max_s - row_min_s)
        inter = w * h

        iou = inter / (self.area + element_b.area - inter)
        ioa = inter / self.area
        iob = inter / element_b.area

        return inter, iou, ioa, iob
    
    def cal_text_within_compo(self, element_b, bias=(0, 0)):
        
        #self.col_min, self.row_min, self.col_max, self.row_max
        
        a = self.put_bbox()
        b = element_b.put_bbox()
        
        if a[0] <= b[0] and b[2] <= a[2] and a[1] <= b[1] and b[3] <= a[3]: 
            return True
        else:
            return False
        

    def element_relation(self, element_b, bias=(0, 0)):
        """
        @bias: (horizontal bias, vertical bias)
        :return: -1 : a in b
                 0  : a, b are not intersected
                 1  : b in a
                 2  : a, b are identical or intersected
        """
        inter, iou, ioa, iob = self.calc_intersection_area(element_b, bias)

        # area of intersection is 0
        if ioa == 0:
            return 0
        # a in b
        if ioa >= 1:
            return -1
        # b in a
        if iob >= 1:
            return 1
        return 2

    def visualize_element(self, img, color=(0, 255, 0), line=1, show=False):
        loc = self.put_bbox()
        cv2.rectangle(img, loc[:2], loc[2:], color, line)
        
        font = cv2.FONT_HERSHEY_COMPLEX
        if self.category != "Text":
            
            if self.category == "Compo":
                cv2.putText(img,str(self.id),(loc[0]+5,loc[1]+5),font,0.69,(255,255,255),2, cv2.LINE_AA)
                cv2.putText(img,str(self.id),(loc[0]+5,loc[1]+5),font,0.69,(0,0,0),1, cv2.LINE_AA)
                
            elif self.category == "Block":
                cv2.putText(img,str(self.id),(loc[0], self.height//2),font,0.69,(255,0,0),2, cv2.LINE_AA)
                cv2.putText(img,str(self.id),(loc[0], self.height//2),font,0.69,(0,0,0),1, cv2.LINE_AA)
            
            else:
                cv2.putText(img,str(self.id),(loc[0],loc[1]+5),font,0.65,(255,255,255),2, cv2.LINE_AA)
                cv2.putText(img,str(self.id),(loc[0],loc[1]+5),font,0.65,(0,0,0),1, cv2.LINE_AA)
                
        if show:
            cv2.imshow('element', img)
            cv2.waitKey(0)
            cv2.destroyWindow('element')
