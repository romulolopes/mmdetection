# The new config inherits a base config to highlight the necessary modification
_base_ = '../mask_rcnn/mask-rcnn_r50-caffe_fpn_ms-poly-1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=25), mask_head=dict(num_classes=25)))

# Modify dataset related settings
data_root = '../dataset/'
metainfo = {
    'classes': ( '0', '1','2', '3', '4', '5' , '6' , '7',
    '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
    '19', '20', '21', '22', '23', '24'),
    'palette': [
        (220, 20, 60),
    ]
}
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='train/_annotations.coco.json',
        data_prefix=dict(img='train/')))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='val/_annotations.coco.json',
        data_prefix=dict(img='val/')))
test_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='test/_annotations.coco.json',
        data_prefix=dict(img='test/')))
 

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'val/_annotations.coco.json')
test_evaluator = dict(ann_file=data_root + 'test/_annotations.coco.json')


# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'