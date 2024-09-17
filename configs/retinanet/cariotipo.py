_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/cariotipo.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py',
    './retinanet_tta.py'
]

# optimizer
optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001))


    
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/retinanet/retinanet_r50_fpn_1x_coco/retinanet_r50_fpn_1x_coco_20200130-c2398f9e.pth'

mlflow_tags = {
        "model_type": "Retina Net",
        "dataset": "Cariotipo",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="Retina Net" , params=mlflow_tags)
]