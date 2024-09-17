_base_ = [
    '../_base_/models/faster-rcnn_r50-caffe-dc5.py',
    '../_base_/datasets/cariotipo.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]


load_from = 'https://cdn-model.openxlab.org.cn/models%2Fweight%2Fmmdetection%2FFaster+R-CNN%2Ffaster_rcnn_r50_caffe_dc5_1x_coco_20201030_151909-531f0f43.pth?Expires=1726599141&OSSAccessKeyId=LTAI5tCdKkrGqdpR7PDyejq7&Signature=JlEGhYKgFV4h6%2Fj%2B4UFK%2F47Mz4A%3D&response-content-disposition=attachment%3B%20filename%3Dfaster_rcnn_r50_caffe_dc5_1x_coco_20201030_151909-531f0f43.pth'

mlflow_tags = {
        "model_type": "Faster RCNN",
        "dataset": "Cariotipo",
}
custom_hooks = [
    dict(type='MlflowLoggerHook',  exp_name="Faster RCNN" , params=mlflow_tags)
]
