# dataset settings
dataset_type = 'CocoDataset'
data_root = 'data/coco/'
img_size = [(300, 300),(1000, 1000)]


img_norm_cfg = dict(
    mean=[128, 128, 128], std=[70, 70, 70], to_rgb=True)

# img_norm_cfg = dict(
#     mean=128, std=70)

classes = ('wake',)

train_pipeline = [
    dict(type='LoadImageFromFile', color_type='color'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=img_size, keep_ratio=False),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    # dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile', color_type='color'),
    dict(type='Resize', img_scale=img_size, keep_ratio=False),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect',
            meta_keys=('filename', 'ori_shape', 'img_shape','scale_factor'),
            keys=['img']),
    dict(type='WrapFieldsToLists')
    ]

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'annotations/instances_train2017.json',
        img_prefix=data_root + 'train2017/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'annotations/instances_val2017.json',
        img_prefix=data_root + 'val2017/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'annotations/instances_val2017.json',
        img_prefix=data_root + 'val2017/',
        pipeline=test_pipeline))


evaluation = dict(interval=100, metric='bbox')
