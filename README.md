<h2>TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-Multimodal-Subset (2026/09/17)</h2>
Sarah T. Arai<br>
Software Laboratory antillia.com <br><br>
This is the first experiment in Image Segmentation for <b>UCSF-PDGM (UCSF Preoperative Diffuse Glioma MR) Filtered 
Multimodal Subset </b>
 based on
our <a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model">TensorFlowFlexUNet Model</a>
 (<b>TensorFlow Flexible UNet Image Segmentation Model for Multiclass</b>) and a 256x256-pixel <b>NPY images containing the four modalities
  (FLAIR, T1, T1c, and T2)</b> and 
 <b>PNG masks </b>
 <a href="https://drive.google.com/file/d/182BeqlJKKVEWws0AZLqGIeu5ksTU7BGg/view?usp=sharing">
UCSF-PDGM-Multimodal-ImageMask-Subset.zip</a> with colorized masks 
(<a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>),
  which was derived by us from the Kaggle website 
<br><br>
<a href="https://www.kaggle.com/datasets/rukiyeaydn/ucsf-pdgm-filtered">
<b>UCSF-PDGM Filtered</b>
</a> 
<br>Glioblastoma MRI Dataset for Brain Tumor Segmentation
<br>by Rukiye Aydın.
<br><br>
For comparison of segmentation performance between a single-modal and this multimodal FlexUNet model, 
please see also the following experiments:
<ul>
<li>
 <a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-FLAIR-Subset">
TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-FLAIR-Subset
</a>
</li>
<li>
 <a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-Multimodal-Combined-Subset">
TensorFlow-FlexUNet-Image-Segmentation-UCSF-Multimodal-Combined-Subset
</a>
</li>
</ul>
<br>
<hr>
<b>Actual Image Segmentation for UCSF-PDGM-Multimodal Images of 256x256 pixels</b><br>
As shown below, the inferred masks resemble the ground-truth masks. <br>
<br>
<a href="#1"><b>class_color_mapping_table</b></a><br>
<br>
<table>
<tr>
<th  width="320" height="auto">T2 slice in NPY</th>
<th  width="320" height="auto">Mask (ground_truth)</th>
<th  width="320" height="auto">Prediction: inferred_mask</th>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1008_90.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1008_90.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1008_90.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1104_121.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1104_121.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1104_121.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1104_126.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1104_126.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1104_126.png" width="320" height="auto"></td>
</tr>
</table>
<hr>
<br>
<h3>1. Dataset Citation</h3>
The dataset used here was derived from the following Kaggle website:<br><br>
<a href="https://www.kaggle.com/datasets/rukiyeaydn/ucsf-pdgm-filtered">
<b>UCSF-PDGM Filtered</b>
</a> 
<br>Glioblastoma MRI Dataset for Brain Tumor Segmentation
<br>by Rukiye Aydın.
<br><br>
The following explanation was taken from the website above.
<br><br>
<b>Abstract</b><br>
This dataset is a curated subset of the <b>UCSF Preoperative Diffuse Glioma MRI (UCSF-PDGM)</b> v5 
dataset, originally published by Calabrese et al. (2022) and hosted on 
The Cancer Imaging Archive (TCIA). The original dataset contains 501 patients with 
histopathologically confirmed WHO grade II–IV diffuse gliomas, 
imaged preoperatively on a standardized 3 Tesla MRI protocol at the University of 
California San Francisco.
<br>
<br>
From the original dataset, only the following five files per patient were retained for use 
in multimodal survival prediction research:
<ul>
<li>T1-weighted image (T1)</li>
<li>T1 post-contrast image (T1c)</li>
<li>T2-weighted image (T2)</li>
<li>T2/FLAIR image (FLAIR)</li>
<li>Multicompartment tumor segmentation mask (tumor_segmentation)</li>
</ul>
<br>
All other modalities (DWI, SWI, ASL, DTI, HARDI) were excluded to reduce storage size from 142 GB to approximately 6.3 GB, 
while retaining all information necessary for deep learning-based feature extraction 
and survival modeling.
<br><br>
<b>Original Citation:</b><br>
Calabrese, E., Villanueva-Meyer, J., Rudie, J., Rauschecker, A., Baid, U., Bakas, S., Cha, S.,<br>
 Mongan, J., Hess, C. (2022). <br>
The University of California San Francisco Preoperative Diffuse Glioma MRI (UCSF-PDGM) (Version 5) [dataset].<br>
 The Cancer Imaging Archive. <a href="https://doi.org/10.7937/tcia.bdgf-8v37">
 https://doi.org/10.7937/tcia.bdgf-8v37</a>
 <br><br>
<b>License</b><br>
<a href="<a href="https://creativecommons.org/licenses/by-sa/4.0/">
CC BY-SA 4.0</a>.
<br>
<br>
<h3>
2. UCSF-PDGM-Multimodal-ImageMask-Subset
</h3>
<h3>2.1 Download ImageMask Dataset</h3>
 If you would like to train this UCSF-PDGM-Multimodal Segmentation model,
 please download the dataset from Google Drive  
 <a href="https://drive.google.com/file/d/182BeqlJKKVEWws0AZLqGIeu5ksTU7BGg/view?usp=sharing">
UCSF-PDGM-Multimodal-ImageMask-Subset.zip</a> ( <a href="<a href="https://creativecommons.org/licenses/by-sa/4.0/">
CC BY-SA 4.0</a>). 
Expand the downloaded ImageMaskDataset and put it under the <b>./dataset</b> folder
<br>
<pre>
./dataset
└─UCSF-PDGM-Multimodal-Subset
    ├─test
    │   ├─images
    │   └─masks
    ├─train
    │   ├─images
    │   └─masks
    └─valid
         ├─images
         └─masks
</pre>
<br>
<b>UCSF-PDGM-Multimodal Statistics</b><br>
<img src ="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/UCSF-PDGM-Multimodal-Subset_Statistics.png" width="512" height="auto"><br>
<br>
As shown above, the number of images in the training and validation datasets is large enough to use for the
 training set of our segmentation model.
<br>
<br>
<h3>2.2 Derivation of UCSF-PDGM-Multimodal </h3>
The original dataset's folder structure is as follows.
It contains four modalities (FLAIR, T1, T1c, and T2) of NIfTI files and one corresponding type of NIfTI segmentation files,
but we used a subset (half of the original) in this experiment.
<pre>
./UCSF-PDGM-Filtered  
    ├─UCSF-PDGM-0004_nifti
    │   ├─UCSF-PDGM-0004_FLAIR.nii
    │   ├─UCSF-PDGM-0004_T1.nii
    │   ├─UCSF-PDGM-0004_T1c.nii
    │   ├─UCSF-PDGM-0004_T2.nii
    │   └─UCSF-PDGM-0004_tumor_segmentation.nii
...
    └─UCSF-PDGM-0541_nifti
         ├─UCSF-PDGM-0541_FLAIR.nii
         ├─UCSF-PDGM-0541_T1.nii
         ├─UCSF-PDGM-0541_T1c.nii
         ├─UCSF-PDGM-0004_T2.nii
         └─UCSF-PDGM-0541_tumor_segmentation.nii
</pre>
We generated a 256x256-pixel <b>NPY images containing the four modalities</b> and <b>PNG masks</b> dataset using the Python script
<a href="./generator/MultimodalImageMaskDatasetGenerator.py">
MultimodalImageMaskDatasetGenerator.py</a>. 
However, for simplicity, we excluded all black empty masks and the corresponding images because they are irrelevant for 
training our segmentation model.<br>
We also used the following class_color_mapping table to generate the colorized masks.
<br><br>
<a id="1"><b>class_color_mapping_table</b></a>
<br><br>
<table border=1 style='border-collapse:collapse;' cellpadding='5'>
<tr><th>Indexed Color</th><th>Color</th><th>RGB</th><th>Class</th></tr>
<tr><td>1</td><td with='80' height='auto'><img src='./color_class_mapping/1.png' widith='40' height='25'></td><td>(255, 0, 0)</td>
<td>Non-enhancing Tumor Core / Necrosis: NET/NCR</td></tr>
<tr><td>2</td><td with='80' height='auto'><img src='./color_class_mapping/2.png' widith='40' height='25'></td><td>(0, 255, 0)</td>
<td>Peritumoral Edema: ED</td></tr>
<tr><td>3</td><td with='80' height='auto'><img src='./color_class_mapping/3.png' widith='40' height='25'></td><td>(0, 0, 255)</td>
<td>GD-Enhancing Tumor: ET</td></tr>
</table>
<br>

<h3>2.3 Train Sample Images and Masks</h3>
<b>Train_sample_T2_slices in NPY </b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/train_t2_images_sample.png" width="1024" height="auto">
<br>
<b>Train_sample_masks</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/train_masks_sample.png" width="1024" height="auto">
<br>
<h3>
3. Train TensorFlowFlexUNet Model
</h3>
 We trained the UCSF-PDGM-Multimodal TensorFlowFlexUNet model using the following
<a href="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/train_eval_infer.config"> <b>train_eval_infer.config</b></a> file. <br>
Please move to ./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal and run the following bat file.<br>
<pre>
>1.train.bat
</pre>
This simply runs the following command.<br>
<pre>
>python ../../../src/TensorFlowFlexUNetTrainer.py ./train_eval_infer.config
</pre>
<hr>
<b>Model parameters</b><br>
Defined a small <b>base_filters=16 </b> and large <b>base_kernels=(11,11)</b> for the first Conv Layer of Encoder Block of 
<a href="./src/TensorFlowFlexUNet.py">TensorFlowFlexUNet.py</a> 
and a large <b>num_layers=8</b> (including a bridge between Encoder and Decoder Blocks).
<pre>
[model]
; You may specify your own UNet class derived from our TensorFlowFlexModel
model         = "TensorFlowFlexUNet"
generator     =  False
image_width    = 256
image_height   = 256
; Specify the number of modalities (FLAIR, T1,T1c,T2)
image_channels = 4

num_classes    = 4
base_filters   = 16
base_kernels   = (11,11)
num_layers     = 8
dropout_rate   = 0.05
dilation       = (1,1)
</pre>
<b>Learning rate</b><br>
Defined a small learning rate.  
<pre>
[model]
learning_rate  = 0.00007
</pre>
<b>Loss and metrics functions</b><br>
Specified "categorical_crossentropy" and <a href="./src/dice_coef_multiclass.py">"dice_coef_multiclass"</a>.<br>
<pre>
[model]
loss           = "categorical_crossentropy"
metrics        = ["dice_coef_multiclass"]
</pre>
<b>Dataset class</b><br>
Specifed <a href="./src/ImageCategorizedMaskDataset.py">ImageCategorizedMaskDataset</a> class.<br>
<pre>
[dataset]
class_name    = "ImageCategorizedMaskDataset"
</pre>
<br>
<b>Learning rate reducer callback</b><br>
Enabled the learning_rate_reducer callback and a small reducer_patience.
<pre> 
[train]
learning_rate_reducer = True
reducer_factor     = 0.4
reducer_patience   = 4
</pre>
<b>Early stopping callback</b><br>
Enabled early stopping callback with the patience parameter.
<pre>
[train]
patience      = 10
</pre>
<b>Image</b><br>
Please specify "NPY" for <b>file_format</b> in case of an NPY image dataset.
<pre>
[image]
color_order = "RGB"
file_format = "NPY"
</pre>
<br>
<b>RGB Color map</b><br>
Specified RGB color map dict for UCSF-PDGM-Multimodal 1+4 classes.<br>
<pre>
[mask]
mask_datatyoe    = "categorized"
mask_file_format = ".png"
; UCSF-PDGM-Multimodal RGB color map dict for 1+3 classes.
;        Background: black, NET/NCR: red, ED: green, ET: blue 
rgb_map = {(0,0,0):0,(255,0,0):1, (0,255,0):2,(0,0,255):3,}
</pre>

<b>Epoch change inference callback</b><br>
Enabled <a href="./src/EpochChangeInferencer.py">epoch_change_infer callback</a></b>.<br>
<pre>
[train]
epoch_change_infer       = True
epoch_change_infer_dir   =  "./epoch_change_infer"
num_infer_images         = 6
</pre>

By using this callback, on every epoch_change, the inference procedure can be called
 for 6 images in the <b>mini_test</b> folder. This will help you confirm how the predicted mask changes 
 at each epoch during your training process.<br> 
<br> 
As shown below, early in the model training, the predicted masks from our UNet segmentation model showed 
discouraging results.
 However, as training progressed through the epochs, the predictions gradually improved. 
 <br> 
<br>
<b>Epoch_change_inference output at starting (epoch 1,2,3)</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/epoch_change_infer_at_start.png" width="1024" height="auto"><br>
<br>
<b>Epoch_change_inference output at middlepoint (epoch 26,27,28)</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/epoch_change_infer_at_middle.png" width="1024" height="auto"><br>
<br>
<b>Epoch_change_inference output at ending (epoch 53,54,55)</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/epoch_change_infer_at_end.png" width="1024" height="auto"><br>
<br>
In this experiment, the training process was terminated at epoch 55.<br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/train_console_output_at_epoch55.png" width="1024" height="auto"><br>
<br>
<a href="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/eval/train_metrics.csv">train_metrics.csv</a><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/eval/train_metrics.png" width="520" height="auto"><br>
<br>
<a href="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/eval/train_losses.csv">train_losses.csv</a><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/eval/train_losses.png" width="520" height="auto"><br>
<br>
<h3>
4. Evaluation
</h3>
Please move to <b>./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal</b> folder,
and run the following bat file to evaluate the TensorFlowUNet model for UCSF-PDGM-Multimodal.<br>
<pre>
>./2.evaluate.bat
</pre>
This simply runs the following command.
<pre>
>python ../../../src/TensorFlowFlexUNetEvaluator.py ./train_eval_infer.config
</pre>

Evaluation console output:<br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/evaluate_console_output_at_epoch55.png" width="1024" height="auto">
<br><br>Image-Segmentation-UCSF-PDGM-Multimodal

<a href="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/evaluation.csv">evaluation.csv</a><br>
The loss (categorical_crossentropy) to this UCSF-PDGM-Multimodal-Subset/test was low, and dice_coef_multiclass  
high, as shown below.
<br>
<pre>
categorical_crossentropy,0.0072
dice_coef_multiclass,0.9964
</pre>
These scores are a little bit better than those of the  
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-Multimodal-Combined-Subset">
Multimodal Combined case.</a>
<br>
<pre>
categorical_crossentropy,0.0096
dice_coef_multiclass,0.9952
</pre>
<br>
<h3>
5. Inference
</h3>
Please move to <b>./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal</b> folder
and run the following bat file to infer segmentation regions for images using the trained TensorFlowUNet model for
 UCSF-PDGM-Multimodal.<br>
<pre>
>./3.infer.bat
</pre>
This simply runs the following command.
<pre>
>python ../../../src/TensorFlowFlexUNetInferencer.py ./train_eval_infer.config
</pre>
<hr>
<b>mini_test_t2_slices</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/mini_test_t2_slices.png" width="1024" height="auto"><br>
<b>mini_test_mask(ground_truth)</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/mini_test_masks.png" width="1024" height="auto"><br>

<hr>
<b>Inferred test masks</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/asset/mini_test_output.png" width="1024" height="auto"><br>
<br>
<hr>
<b>Enlarged images and masks for UCSF-PDGM-Multimodal  Images of 256x256 pixels</b><br>
As shown below, the inferred masks look similar to the ground truth masks.<br>
<br>
<a href="#1"><b>class-color-mapping-talbe</b></a><br>
<br>
<table>
<tr>
<th>T2 slice in NPY</th>
<th>Mask (ground_truth)</th>
<th>Inferred-mask</th>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1003_93.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1003_93.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1003_93.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1021_84.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1021_84.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1021_84.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1039_108.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1039_108.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1039_108.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1104_121.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1104_121.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1104_121.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1116_119.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1116_119.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1116_119.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_t2_slices/1164_108.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test/masks/1164_108.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_output/1164_108.png" width="320" height="auto"></td>
</tr>
</table>
<hr>
<br>
<!--
<h3>
6. 3D Volume Segmentation
</h3>
Please move to <b>./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal</b> folder
and run the following bat file to infer image segmentation for 2D slices of 3D volume NIfTI files
 using the trained TensorFlowFlexUNet model for UCSF-PDGM-Multimodal.<br>
<pre>
>./5.infer3d.bat
</pre>
This simply runs the following command.
<pre>
>python ../../../src/TensorFlowFlexUNet3DInferencer.py ./train_eval_infer.config
</pre>
<b>infer3d section </b> in <a href="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/train_eval_infer.config">
train_eval_infer.config
<a></b>
<pre>
[infer3d] 
; Specify an images_dir which contains NIfTI or NPY files
images_dir    = "./mini_test_3d/images/"
output_dir    = "./mini_test_3d_output/"
slice_shape_order = "hwd"
slice_normalize = True
slice_resize   = (256,256)
; Specify a cv2.rotation mode as a string.
slice_rotation = "cv2.ROTATE_90_COUNTERCLOCKWISE" 

mask_overlay  = True
</pre>
<hr>
<b>Acutual Image Segmentation for 2D Slices of a UCSF-PDGM-Multimodal NIfTI</b><br>
Some Slices, Inferred Masks and Mask overlays for a 3D volume <b>UCSF-PDGM-0004_T2.nii</b> file in 
<b>ucsf</b> folder.<br>
<br>
<a href="#1"><b>class-color-mapping-talbe</b></a><br>
<br>
<table>
<tr>
<th width="320" height="auto">Combined Image</th>
<th width="320" height="auto">Inferred-mask</th>
<th width="320" height="auto">Mask overlay</th>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/slices/10060.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/masks/10060.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/overlays/10060.png" width="320" height="auto"></td>
</tr>

<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/slices/10070.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/masks/10070.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/overlays/10070.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/slices/10080.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/masks/10080.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/overlays/10080.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/slices/10090.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/masks/10090.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/overlays/10090.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/slices/10110.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/masks/10110.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/overlays/10110.png" width="320" height="auto"></td>
</tr>
<tr>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/slices/10120.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/masks/10120.png" width="320" height="auto"></td>
<td><img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/mini_test_3d_output/UCSF-PDGM-0004_T2.nii/overlays/10120.png" width="320" height="auto"></td>
</tr>
</table>
<hr>
<br>
<h3>
7. MaskOverlay Video of 3D Volume Segmentation
</h3>
Please move to the <b>./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal</b> folder and run the following bat file 
to generate <b>overlays.mp4</b> or <b>overlay.gif</b> for MaskOverlays of 3D Volume Segmentation. <br>
<pre>
>./6.video3d.bat
</pre>
This simply runs the following command.
<pre>
>python ../../../src/MaskOverlayVideoGenerator.py ./train_eval_infer.config
</pre>
<br>
<b>infer3d section </b> in <a href="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/train_eval_infer.config">
train_eval_infer.config
<a></b>
<pre>
[infer3d] 
mask_overlay  = True
; Specify ".mp4" or ".gif".
;video_fileformat  = ".mp4"
video_fileformat  = ".gif"
</pre>
<br>
<b>overlays.gif</b><br>
<img src="./projects/TensorFlowFlexUNet/UCSF-PDGM-Multimodal-Subset/video_3d/overlays.gif">
<br>
-->
<br>
<h3>
References
</h3>
<b>1. TensorFlow-FlexUNet-Image-Segmentation-Multiclass-BraTS2023-Subset</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Multiclass-BraTS2023-Subset">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Multiclass-BraTS2023-Subset
</a>
<br><br>
<b>2. TensorFlow-FlexUNet-Image-Segmentation-BraTS-Africa-Glioma-T2W</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-BraTS-Africa-Glioma-T2W">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-BraTS-Africa-Glioma-T2W
</a>
<br><br>
<b>3. TensorFlow-FlexUNet-Image-Segmentation-Multiclass-BraTS2020</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Multiclass-BraTS2020">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Multiclass-BraTS2020
</a>
<br><br>
<b>4. TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-FLAIR-Subset</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-FLAIR-Subset">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-FLAIR-Subset</a>
<br><br>
<b>5 TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-Combined-Subset</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-Multimodal-Combined-Subset">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-UCSF-PDGM-Multimodal-Combined-Subset</a>
<br><br>
<b>6 TensorFlow-FlexUNet-Image-Segmentation-Model</b><br>
Toshiyuki Arai<br>
<a href="https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model">
https://github.com/sarah-antillia/TensorFlow-FlexUNet-Image-Segmentation-Model
</a>
<br><br>
