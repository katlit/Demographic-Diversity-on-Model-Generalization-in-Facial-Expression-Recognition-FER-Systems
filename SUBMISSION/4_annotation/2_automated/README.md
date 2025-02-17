# Annotation Scripts

## Overview
This folder contains Jupyter Notebook files designed for automated annotation of facial emotion datasets using the **DeepFace** framework. These scripts facilitate the analysis and labeling of images across various datasets, including AffectNet, CK+, FER2013, and JAFFE. By leveraging the pre-trained models provided by DeepFace, these notebooks automate the process of annotating image datasets with attributes such as **age**, **gender**, **race**, and **emotion**.

Please set the `DEMO` variable to `True` in the notebook files to enable the demonstration mode. 

## Folder Structure


2_automated/ 

-- Contains Jupyter Notebook files for automatic annotation of facial emotion datasets using the DeepFace framework.

01_-_Annotation_AutomaticLabeling_AFFECTNet.ipynb       # Automatic annotation for AffectNet 

02_-_Annotation_AutomaticLabeling_CK.ipynb              # Automatic annotation for CK+ dataset 

03_-_Annotation_AutomaticLabeling_FER.ipynb             # Automatic annotation for FER2013 dataset 

04_-_Annotation_AutomaticLabeling_JAFFE.ipynb           # Automatic annotation for JAFFE dataset 

3_annotation_results/

-- Contains the results of the automatic annotation in the form of CSV files.

