_base_ = [
  'queryinst_r50_fpn_1x_coco.py', 
  '../_base_/datasets/autokary2022.py'
]

load_from = 'https://download.openmmlab.com/mmdetection/v2.0/queryinst/queryinst_r50_fpn_1x_coco/queryinst_r50_fpn_1x_coco_20210907_084916-5a8f1998.pth'

mlflow_tags = {
        "model_type": "QueryInst",
        "dataset": "AutoKary 2022",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="QueryInst" , params=mlflow_tags)
]
