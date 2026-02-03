import cv2
import numpy as np

class TemplateMatcher:
    def find_template(self, main_image, template, method=cv2.TM_CCOEFF_NORMED):
        """Şablonu ana görüntü üzerinde arar ve en iyi konumu döner."""
        if len(main_image.shape) == 3:
            main_image = cv2.cvtColor(main_image, cv2.COLOR_BGR2GRAY)
        if len(template.shape) == 3:
            template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(main_image, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # TM_SQDIFF metodu için en iyi sonuç min_loc, diğerleri için max_loc
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            return min_loc, min_val
        else:
            return max_loc, max_val