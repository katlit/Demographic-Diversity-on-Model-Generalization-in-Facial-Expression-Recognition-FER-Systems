# Manual Annotation Process

## Overview
This folder contains resources, scripts, and outputs related to the manual annotation process for facial expression recognition (FER) datasets. The goal of this process is to ensure accurate and consistent demographic annotations for ethnicity, gender, and age. Below is a brief description of the contents in this folder.

---

## Folder and File Descriptions

### **Key Scripts and Documents**
- **`AnnotationGuide.pdf`**: A comprehensive guide outlining the methodology and instructions for performing manual annotations.
- **`AnnotationInterface`**: The tool/interface used by annotators for labeling the selected images.
- **`Annotation_Manual-Combine`**: Combines annotations from multiple annotators into a single dataset.
- **`Annotation_Manual-Evaluation`**: Evaluates inter-annotator agreement and calculates metrics like Fleiss' Kappa.

### **Individual Annotations**
- **`Annotation_Manual-Annotator1`**, **Annotator2**, **Annotator3**: Files containing annotations made by each individual annotator.
- **`annotations_1`**, **annotations_2**, **annotations_3**: Excel files corresponding to the annotations from the annotators.

### **Final Outputs**
- **`annotationsManual_ALL`**: A consolidated file containing all manual annotations across all annotators.
- **`FinalManualLabels`**: The finalized manual labels after reviewing and resolving discrepancies.

### **Evaluation and Results**
- **`Manual_Annotation_Evaluation`**: Scripts and resources for analyzing the quality and consistency of manual annotations.

---

## How to Use
1. **Annotation Process**:
   - Follow the steps described in `AnnotationGuide.pdf` to perform or review manual annotations.
   - Use `AnnotationInterface` to label the selected pictures in the `SelectedPictures` folder.
2. **Combine Annotations**:
   - Run `Annotation_Manual-Combine` to merge annotations from multiple annotators.
3. **Evaluate Consistency**:
   - Use `Annotation_Manual-Evaluation` to calculate inter-annotator agreement and assess annotation reliability.
4. **Review Final Labels**:
   - Check `FinalManualLabels` for our consolidated and reviewed annotation data.

---

## Notes
- **Inter-annotator Agreement**: Evaluations performed using Fleiss' Kappa to ensure annotation reliability for demographic categories.
- **Labeled Data**: Final labels and annotations are stored in `annotationsManual_ALL` and `FinalManualLabels`.

For questions or further details, refer to the `AnnotationGuide.pdf`.
