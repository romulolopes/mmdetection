_base_ = [ '../_base_/datasets/autokary2022.py','./boxinst_r50_fpn_ms-90k_coco.py']

# model settings
model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',
                      checkpoint='torchvision://resnet101')))



load_from = 'https://download.openmmlab.com/mmdetection/v3.0/boxinst/boxinst_r101_fpn_ms-90k_coco/boxinst_r101_fpn_ms-90k_coco_20221229_145106-facf375b.pth'

mlflow_tags = {
        "model_type": "Box inst",
        "dataset": "AutoKary 2022",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="Box inst" , params=mlflow_tags)
]
