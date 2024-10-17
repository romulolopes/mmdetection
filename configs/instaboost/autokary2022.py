#editado o arquivo mmdetection/configs/cascade_rcnn/cascade-mask-rcnn_r50_fpn_1x_coco.py para incluir autokary2022.py como dataset

_base_ = [
  'mask-rcnn_r50_fpn_instaboost-4x_coco.py'
]

load_from = 'https://download.openmmlab.com/mmdetection/v2.0/instaboost/mask_rcnn_r50_fpn_instaboost_4x_coco/mask_rcnn_r50_fpn_instaboost_4x_coco_20200307-d025f83a.pth'

mlflow_tags = {
        "model_type": "Insta boost",
        "dataset": "AutoKary 2022",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="Insta boost" , params=mlflow_tags)
]
