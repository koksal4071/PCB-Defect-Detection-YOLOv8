from ultralytics import YOLO
import cv2

model = YOLO('best.pt')

gorsel_adi = 'kart2.jpg'  
results = model.predict(source=gorsel_adi, conf=0.25, save=True, show=True)

print("İşlem tamamlandı!")
cv2.waitKey(0)
cv2.destroyAllWindows()