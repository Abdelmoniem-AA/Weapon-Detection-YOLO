<h1 align="center" id="title">Weapon Detection YOLO Model</h1>

<p align="center"><img src="https://img.shields.io/badge/python-3.14-blue"></p>

<p id="description">A real-time weapon detection using Ultralytics YOLO11 trained on a custom 3000+ image dataset.</p>

  
  
<h2>Features</h2>

*   Real-time weapon detection using a webcam
*   Detection on images and videos
*   Four weapon classes: Gun, Knife/Machete, Axe, and Grenade
*   Custom dataset with manually annotated images
*   Background (negative) images included to reduce false positives

<h2>Dataset</h2>
<p>The model was trained on a custom dataset that included 3000+ images. The dataset was collected from multiple publically available sources, mostly through scraping. Eventually, these images were manually annotated using CVAT.</p>
<p><b>Note:</b> The dataset is not included in the repository due to its size.</p>

<h2>Technologies Used</h2>

*   Python
*   Ultralytics YOLO11
*   OpenCV
*   Playwright
*   CVAT

## Results

| Metric | Value |
|--------|------:|
| mAP@50 | 0.573 |
| mAP@50-95 | 0.406 |
| Precision | 0.749 |
| Recall | 0.471 |

## Class Performance

| Class | Precision | Recall | mAP@50 | mAP@50-95 |
|-------|----------:|-------:|--------:|----------:|
| Gun | 0.633 | 0.425 | 0.482 | 0.318 |
| Knife/Machete | 0.737 | 0.463 | 0.578 | 0.386 |
| Axe | 0.840 | 0.520 | 0.652 | 0.464 |
| Grenade | 0.789 | 0.476 | 0.582 | 0.457 |
