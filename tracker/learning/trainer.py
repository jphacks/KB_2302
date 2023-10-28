from ultralytics import YOLO

from ControlPath import BEST_FILE, YOLO_ORI_FILE

def train_model(): 
    
    model = YOLO(YOLO_ORI_FILE)  # load a pretrained model (recommended for training)
    
    print(model.names)
    # Train the model
    results = model.train(
        data="data.yaml", 
        epochs=100, 
        imgsz=640, 
        batch=12, 
        device=0
    )

    # Export the model
    model.export(format="torchscript")

def predict():
    # load a pretrained model (recommended for training)
    model = YOLO(BEST_FILE)  
    
    print(model.names)
    
    results = model.track(
        source="IMG_6559.mp4",
        conf=0.3, 
        iou=0.5, 
        show=True
    )
    
if __name__ == "__main__":
    # train_model()
    predict()