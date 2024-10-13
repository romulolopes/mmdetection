

_base_ = [
  "solo_r50_fpn_1x_coco.py", 
  '../_base_/datasets/autokary2022.py'
]

load_from = 'https://download.openmmlab.com/mmdetection/v2.0/solo/solo_r50_fpn_1x_coco/solo_r50_fpn_1x_coco_20210821_035055-2290a6b8.pth'

mlflow_tags = {
        "model_type": "Solo",
        "dataset": "AutoKary 2022",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="Solo" , params=mlflow_tags)
]
