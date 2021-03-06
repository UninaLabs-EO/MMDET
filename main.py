# Config my baseline with 
import os
import torch
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import warnings

from utils import *

warnings.filterwarnings("ignore")
plt.style.use(['science','nature','no-latex'])
torch.cuda.empty_cache()
os.system('clear')
cwd = os.getcwd()

models = ['retina18','retina50','retina101','mask50','mask101','cascade_mask50','cascade_mask101',
          'detr','centripetalnet','vfnet','efficientdet','sparce_rcnn50',
          'hrnet40_cascade','ssd_vgg16','fovea50']

# bands = ['B2','B3','B4','B8']
bands = ['B2']

if __name__ == '__main__':
     # Select Model and specify if to train and test
     train_bool = True
     test_bool = True
     # Hyper-Parameters:
     max_epochs = 50
     # band = 'B2'
     for selection in ['fovea50','sparce_rcnn50','efficientdet','hrnet40_cascade']:
          for band in bands:
               lr = 0.001
               lr_schedule = 'CosineAnnealing' # "CosineAnnealing" or "step"
               load_from = None
               img_size=768 # Specify in the dataset, here won't be collected!
               data_root = band_selector(band)

               workdir = f'checkpoints/{band}/{selection}/{selection}_'+getCurrentTime()+f'_{img_size}_{max_epochs}e_{band}_lr_{lr}_{lr_schedule}'
               extra_args = {'max_epochs':max_epochs, 'lr':lr, 'load_from':load_from, 'lr_cfg':lr_schedule,
                              'data_root':data_root} # extra_args = None # None to use default values.


               if train_bool:
                    train(selection=selection, workdir=workdir, extra_args=extra_args)
               if test_bool:
                    test(selection=selection, workdir=workdir)
               
               plotRes(workdir, title=selection+f'_{band}_')
               keepGoodWeight(workdir)


 
