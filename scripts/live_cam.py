from ultralytics import YOLO
import cv2

model = YOLO('best.pt')


cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("Kamera başlatıldı. Çıkmak için 'q' tuşuna basın.")

while cap.isOpened():
    
    success, frame = cap.read()
    
    if success:
        results = model(frame, conf=0.25, stream=True)
        
        for r in results:
            annotated_frame = r.plot()
            
    
        cv2.imshow("YOLOv8 Canlı PCB Hata Tespiti", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Kameradan görüntü alınamadı.")
        break

cap.release()
cv2.destroyAllWindows()