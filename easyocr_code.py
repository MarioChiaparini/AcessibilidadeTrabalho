import cv2
import numpy as np
import easyocr
import matplotlib.pyplot as plt

path = "/home/ABTLUS/mario.neto/Desktop/TrabalhoAcessibilidade/images_examples/perigo2.jpg"
#var_img = cv2.imread(path)

def recognize(image):
    reader = easyocr.Reader(['pt']) 
    return reader.readtext(image)

#result = recognize(var_img)

def overlay_ocr_text(img_path, save_name):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    dpi = 30
    fig_width, fig_height = int(img.shape[0]/dpi), int(img.shape[1]/dpi)
    plt.figure()
    f, axarr = plt.subplots(1,2, figsize=(fig_width, fig_height))
    axarr[0].imshow(img)

    result = recognize(img_path)

    for (bbox, text, prob) in result:
        if prob >= 0.5:
            
            print(f'Detected text: {text} (Probability: {prob:.2f})')

           
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))

            
            cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(255, 0, 0), thickness=10)

            
            cv2.putText(img=img, text=text, org=(top_left[0], top_left[1] - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(10, 203, 23), thickness=8)

    
    axarr[1].imshow(img)
    plt.savefig(f'./output/{save_name}_overlay.jpg', bbox_inches='tight')



#img = cv2.imread(path)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
overlay_ocr_text(path, 'alert1')
