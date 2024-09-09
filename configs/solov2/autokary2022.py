_base_ = './solov2_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=25), mask_head=dict(num_classes=25)))

# Modify dataset related settings
data_root = 'data/autokary2022/'
metainfo = {
    'classes': ( '0', '1','2', '3', '4', '5' , '6' , '7',
    '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
    '19', '20', '21', '22', '23', '24'),
    'palette': [
        (220, 20, 60),
    ]
}

max_epochs = 36
train_cfg = dict(max_epochs=max_epochs)

# learning rate
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=1.0 / 3,
        by_epoch=False,
        begin=0,
        end=500),
    dict(
        type='MultiStepLR',
        begin=0,
        end=36,
        by_epoch=True,
        milestones=[27, 33],
        gamma=0.1)
]

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
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/solov2/solov2_r50_fpn_3x_coco/solov2_r50_fpn_3x_coco_20220512_125856-fed092d4.pth'
