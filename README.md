# expandable_semantic_segmentation
Training using crops, inferring on large image

# Label images
Install steps: https://github.com/wkentaro/labelme \
```cd dataset/train``` and then repeat steps for val\
```labelme --nodata --autosave --labels cats```

# Json to Mask
Convert json to mask via,\
```python json2mask.py```

# Semantic segmentation
```jupyter notebook```\
```semanitc_seg.ipynb```



