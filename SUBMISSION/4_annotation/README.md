# Annotation Scripts

## Overview
This folder contains all the scripts, resources, and outputs related to our annotation process. The annotation process is divided into three main components, each with a dedicated folder:

### 1. `1_manual`
This folder contains resources and scripts used for the **manual annotation process**.

### 2. `2_automated`
This folder contains scripts and tools used for the **automated annotation process**.  
Read the `README.md` file inside the folder, or use our results from the `2_automated/results` folder.  
You can choose which dataset you are interested in: AffectNet - Test, CK+, FER2013, or JAFFE.

### 3. `3_annotation_results`
This folder contains the consolidated results of the manual and automated annotations, along with tools for further analysis. It includes:
- **Merged datasets**: Contains both manual and automated annotations for each image.  
  - `AutomatedAnnotations_ALL.csv`: Generated in `1_Automated_Merge.ipynb`.
- **Analysis notebook**:  
  - `2_Annotation_AutomatedResults.ipynb` includes:
    - Results of demographic analysis highlighting disparities or imbalances across datasets.
    - Scripts for visualizing demographic distributions and analyzing annotation accuracy.

---

## How to Use
1. Navigate to the folder corresponding to the annotation process you're interested in (`1_manual` or `2_automated`).
2. Run the provided scripts or view the output file in the `3_annotation_results` folder.
3. Use the visualization and analysis scripts to explore the demographic characteristics of your annotated datasets.

---

## Additional Features
- **Inter-annotator Agreement**:
  - Calculated using Fleiss' Kappa for demographic categories like gender and ethnicity.
  - Provides metrics on consistency between manual annotations.
  
- **Demographic Analysis**:
  - Includes distribution analysis for ethnicity, age, and gender across annotated datasets.
  - Results are presented in both tabular and visual formats for clarity.

- **Validation of Automated Annotations**:
  - Automated annotations are compared to manual annotations to assess their reliability and identify potential biases in pre-trained models.


