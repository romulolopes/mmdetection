_base_ = [
  'mask-rcnn_r50_fpn_instaboost-4x_coco.py', 
  '../_base_/datasets/autokary2022.py'
]

load_from = 'https://download.openmmlab.com/mmdetection/v2.0/instaboost/mask_rcnn_r50_fpn_instaboost_4x_coco/mask_rcnn_r50_fpn_instaboost_4x_coco_20200307-d025f83a.pth'

mlflow_tags = {
        "model_type": "Insta boost",
        "dataset": "AutoKary 2022",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="Insta boost" , params=mlflow_tags)
]
