#base point-rend_r50-caffe_fpn_ms-3x_coco.py

_base_ = [ '../_base_/datasets/autokary2022.py','./point-rend_r50-caffe_fpn_ms-1x_coco.py' ]

max_epochs = 36

# learning policy
param_scheduler = [
    dict(
        type='LinearLR', start_factor=0.001, by_epoch=False, begin=0, end=500),
    dict(
        type='MultiStepLR',
        begin=0,
        end=max_epochs,
        by_epoch=True,
        milestones=[28, 34],
        gamma=0.1)
]

train_cfg = dict(max_epochs=max_epochs)


load_from = 'https://download.openmmlab.com/mmdetection/v2.0/point_rend/point_rend_r50_caffe_fpn_mstrain_3x_coco/point_rend_r50_caffe_fpn_mstrain_3x_coco-e0ebb6b7.pth'

mlflow_tags = {
        "model_type": "Point Rend",
        "dataset": "AutoKary 2022",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="Point Rend" , params=mlflow_tags)
]
