## Command Line Args Reference

```bash
save_model.py:
  --weights: path to weights file
    (default: './data/yolov4.weights')
    (for tiny version: './data/yolov4-tiny.weights')
  --output: path to output
    (default: './checkpoints/yolov4-416')
    (for tiny version : './checkpoints/yolov4-tiny-416')
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'False')
  --input_size: define input size of export model
    (default: 416)
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
    
 object_tracker.py:
  --video: path to input video 
    (default: './data/video/cars.mp4')
    (u can input url as well , for example: 'https://verkehrsservice.hessen.de/syncdata/video/k5370.mp4')
    (for inputing a webcam , use 'dev/video0' ,'dev/video1', ...)
  --output: path to output video (remember to set right codec for given format. e.g. XVID for .avi)
    (default: None)
  --output_format: codec used in VideoWriter when saving video to file
    (default: 'XVID')
  --[no]tiny: yolov4 or yolov4-tiny
    (default: 'false')
    (if you specify this flag, remember to use tiny weights in the --weights flag)
  --weights: path to weights file
    (default: './checkpoints/yolov4-416')
    (for tiny version : './checkpoints/yolov4-tiny-416')
  --framework: what framework to use (tf, trt, tflite)
    (default: tf)
  --model: yolov3 or yolov4
    (default: yolov4)
  --size: resize images to
    (default: 416)
  --iou: iou threshold
    (default: 0.45)
  --score: confidence threshold
    (default: 0.50)
  --dont_show: dont show video output
    (default: False)
    (please specific this flag when running on Colab or AWS instance)
  --info: print detailed info about tracked objects
    (default: False)
```

### References  
  * [tensorflow-yolov4-tflite](https://github.com/hunglc007/tensorflow-yolov4-tflite)
  * [Deep SORT Repository](https://github.com/nwojke/deep_sort)
