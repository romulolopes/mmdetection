_base_ = [
    '../_base_/datasets/autokary2022.py',
    './scnet_r50_fpn_1x_coco.py'
]

load_from = 'https://download.openmmlab.com/mmdetection/v2.0/scnet/scnet_r50_fpn_1x_coco/scnet_r50_fpn_1x_coco-c3f09857.pth'

mlflow_tags = {
        "model_type": "SCNET",
        "dataset": "AutoKary 2022",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="SCNET" , params=mlflow_tags)
]
