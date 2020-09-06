# PennFudanPed-dataset-for-yolo
Added two python scripts to transform the PennFudanPed pedestrian dataset for train in yolo (first transformed to OIDv4_ToolKit datafomat), then use the OIDv4 to transform to yolov4 ready format 

1. put the <strong>png2jpg.py</strong> into the \PennFudanPed\PNGImages folder. Then run it to transform the PNG images to jpg
2. put <strong>convert_annotation2OIDv4</strong> into \PennFudanPed folder. Run it to converted the label into the OIDv4 format
