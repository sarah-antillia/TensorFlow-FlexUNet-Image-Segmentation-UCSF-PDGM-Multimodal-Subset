# Copyright 2026 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# 2026/09/16
# MultimodalImageMaskDatasetGenerator.py

import os
import cv2
import glob
import nibabel as nib
import shutil
import traceback
import numpy as np
import traceback

class MultimodalImageMaskDatasetGenerator:

  def __init__(self, subset_ratio=0.3,  resize=256):

    self.subset_ratio = subset_ratio

    # Modalities: NIfTI file extentions  
    self.NII_FILES = ["_FLAIR.nii", "_t1.nii", "_t1c.nii", "_t2.nii"]   

    # Mask:         NIfTI file extentions
    self.SEG_FILE  = "_tumor_segmentation.nii"

    self.RESIZE = (resize, resize)
    self.NORMALIZE = True
    self.ROTATION = cv2.ROTATE_90_COUNTERCLOCKWISE

    # Class-color-mapping dict.
    # Class 3 is missing
    """
    1:  NCR/NET 
    2:  ED
    4:  ET
    """
    self.MASK_BGR_COLORS = {1:(0,0,255), 2:(0,255,0), 4:(255,0,0)}


  def colorize_mask(self, mask):
     h, w = mask.shape[:2]
     colorized = np.zeros((h, w, 3), dtype=np.uint8)
     # RGB        NCR/NET:red, ED: green, ET:blue,  
     mask_color_keys = self.MASK_BGR_COLORS.keys()
     print(mask_color_keys)
     for key in mask_color_keys: 
       bgr_color = self.MASK_BGR_COLORS[key]
       print(key,bgr_color)
       index = int(key)
       colorized[np.equal(mask, index)] = bgr_color
     return colorized

  def normalize(self, data):
    min = data.min()
    max = data.max()
    if max - min != 0:
      normalized = ((data - min) / (max - min) * 255).astype(np.uint8)
    else:
      normalized = np.zeros_like(data, dtype=np.uint8)
    return normalized
   
  def get_mask_slice(self, i, data):
    # Get i-th mask slice from the data.
    mask = data[:, :, i]  
    if self.ROTATION:
      mask = cv2.rotate(mask, self.ROTATION)
    if self.RESIZE:
      mask = cv2.resize(mask, self.RESIZE)

    # Is this mask emtpy (all black) or not?
    valid_mask = False
    if mask.any() > 0:   
      mask = self.colorize_mask(mask)
      valid_mask = True
    return valid_mask, mask, 
  
  def get_image_slice(self, i, data):
    # Get i-th image slice from the data.
    image = data[:,:,i]
    if self.NORMALIZE:
      image = self.normalize(image)
    if self.ROTATION:
      image = cv2.rotate(image, self.ROTATION)
    if self.RESIZE:
      image = cv2.resize(image, self.RESIZE)
    return image
  
  def generate(self, data_dir, output_images_dir, output_masks_dir):
      subdirs = os.listdir(data_dir)
      case_index = 1000
      num_subdirs = len(subdirs)
      subset = int(num_subdirs * self.subset_ratio)

      for i in range(subset):
        subdir = subdirs[i]
        case_index += 1
        fullsubdir = os.path.join(data_dir, subdir)

        # Getting image nii filepaths
        image_nii_filepaths = []

        for nii_file in self.NII_FILES:
          nii_subdir  = subdir.replace("_nifti", nii_file)
          nii_fullpath = os.path.join(fullsubdir, nii_subdir)
          nii_filepath = glob.glob(nii_fullpath + "/*.nii")[0]

          image_nii_filepaths.append(nii_filepath)

        # Getting a segmentation nii filepath 
        seg_subdir  = subdir.replace("_nifti", self.SEG_FILE)
        seg_fullpath = os.path.join(fullsubdir, seg_subdir)
        #print("seg_fullpath", seg_fullpath)
        seg_nii_filepath  = glob.glob(seg_fullpath + "/*" + self.SEG_FILE)[0]
        print(seg_nii_filepath)

        for image_nii_filepath in  image_nii_filepaths:
          if not os.path.exists(image_nii_filepath):
            raise Exception("Not found " + image_nii_filepath )
          
        self.generate_one(case_index, image_nii_filepaths, seg_nii_filepath,
                                  output_images_dir, output_masks_dir)        

  def generate_one(self, case_index, image_nii_filepaths, seg_nii_filepath,
                     output_images_dir, output_masks_dir):
       
       mask_data = nib.load(seg_nii_filepath).get_fdata()
       print(mask_data.shape)

       num_mask_slices = mask_data.shape[2]
       
       all_images_data = []
       for i in range(len(image_nii_filepaths)):
         # Get an image data (numpy array).
         image_data = nib.load(image_nii_filepaths[i]).get_fdata()
         num_image_slices = image_data.shape[2]

         # Compare the number of image_slices and mask_slices. 
         if num_mask_slices != num_image_slices:
           raise Exception("Unmatched num_mask_slices and num_image_slices")
       
         print("Num slices", i, num_image_slices)
         all_images_data.append(image_data)

       for slice_index in range(num_mask_slices):
          valid, mask = self.get_mask_slice(slice_index, mask_data)
          #If a non-empty mask found, then generate a corresponding npy image file.
          if valid == True:
            all_image_slices = []
            for image_data in all_images_data:
              image_slice = self.get_image_slice(slice_index, image_data)
              all_image_slices.append(image_slice)

            filename = str(case_index) + "_" + str(slice_index) + ".png"
            mask_filepath = os.path.join(output_masks_dir, filename)
            cv2.imwrite(mask_filepath, mask)
            print("Mask shape", mask.shape)
            print("Saved", mask_filepath)

            multimodal_slice = np.stack(all_image_slices, axis=-1)
            print("Multimodal slice shape", multimodal_slice.shape)

            npy_filename = str(case_index) + "_" + str(slice_index) + ".npy"
            npy_filepath = os.path.join(output_images_dir, npy_filename)

            np.save(npy_filepath, multimodal_slice)
            print("Saved", npy_filepath)
       
          else:
            print("Skipped for an empty mask case.")


if __name__ == "__main__":
  try:
    data_dir = "./ucsf/"
  
    output_dir = "./UCSF-PDGM-Multimodal-Subset"
    if os.path.exists(output_dir):
      shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    output_images_dir = os.path.join(output_dir, "images")
    output_masks_dir  = os.path.join(output_dir, "masks")
    os.makedirs(output_images_dir)
    os.makedirs(output_masks_dir)

    subset   = 0.5
    resize   = 256
    generator = MultimodalImageMaskDatasetGenerator(subset_ratio = subset, 
                                                    resize = resize)
    generator.generate(data_dir, output_images_dir, output_masks_dir)

  except:
    traceback.print_exc()


                