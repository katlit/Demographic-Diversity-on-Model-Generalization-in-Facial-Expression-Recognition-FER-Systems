# Investigating the Impact of Demographic Diversity on Model Generalization in Facial Expression Recognition (FER) Systems

This repository includes all the code and resources necessary for investigating how demographic diversity impacts model generalization in FER systems. It contains scripts for data collection, analysis, and annotation, as well as access to relevant FER datasets.

The `Project_Report.pdf` file provides a detailed overview of the project. For a comprehensive understanding of the project, its findings, and their implications, please read the report before proceeding with the next steps.

The report covers the following key aspects:

- Introduction to the problem of demographic bias in facial expression recognition (FER) systems
- Data collection and analysis of frequently cited FER datasets and their reported performance metrics
- Evaluation of demographic representation in selected FER datasets through automated and manual annotation processes
- Discussion of the relationship between dataset diversity and model performance, as well as the implications of the findings for FER research and applications
- Limitations and potential future work, including the need for refined data cleaning, increased manual annotations, and addressing biases in automated annotation systems
- Conclusions highlighting the critical role of demographic diversity in shaping the fairness and reliability of FER systems

## Getting Started

To run the code, please follow the instructions below:

### 1. Data Collection
- If you want to collect the data on your own, follow the `README.md` file in the `1_scraping` folder.
- Alternatively, you can use our pre-collected data available in `1_scraping/FullText_ALL.csv`.

### 2. Analyzing Collected Data
- The analysis of the collected data can be found in the `2_FER_paper_analysis` folder. Run the `FER_Paper_Analysis.ipynb` notebook to analyze the data and get visualisations.
- Accuracy metrics can be added to the collected data using the following csv files: 
  - **CK+, JAFFE, FER2013 Dataset Accuracy**: `combined_datasets_accuracy.csv` -- Extracted from Shan Li and Weihong Deng’s paper, *“Deep Facial Expression Recognition: A Survey”*, published in *IEEE Transactions on Affective Computing, Volume 13, Issue 3 (July 2022), Pages 1195–1215*. DOI: [10.1109/TAFFC.2020.2981446](https://dx.doi.org/10.1109/TAFFC.2020.2981446).
  - **AffectNet+ Accuracy**: `affectnet_accuracy.csv` -- Extracted from *Ali Pourramezan Fard et al., "AffectNet+: A Database for Enhancing Facial Expression Recognition with Soft-Labels" (2024)*. Available on arXiv: [2410.22506](https://arxiv.org/abs/2410.22506).

### 3. Image Datasets
- The `3_image_datasets` folder contains raw FER image datasets.
- The `affectnet` subfolder includes our manual annotation selections, located in the `SelectionManualAnnotation` folder.

### 4. Annotation Process
- The `4_annotation` folder contains all code and resources related to the annotation process.
- If you're interested in exploring or replicating the annotation process (both **manual** and **automated**), please refer to the `README.md` file inside the `4_annotation` folder.

## Datasets Generated in This Project

### Dataset 1: `1_scraping/FullText_ALL.csv`
This dataset contains metadata and full text extracted from academic papers. Below are the column descriptions:

#### Column Names:
- **ID**: Unique identifier for each paper.
- **Title**: Title of the academic paper.
- **Authors**: Names of the paper's authors.
- **Year**: Year of publication.
- **Cited By**: Number of citations.
- **Detected_Dataset**: FER datasets mentioned in the paper.
- **Detected_Topic**: Topics relevant to the paper.
- **Abstract**: Abstract of the paper.
- **Journal**: Journal in which the paper was published.
- **URL**: Link to the paper's source.
- **Full_Text**: Extracted full text of the paper.

---

### Dataset 2: `4_annotation/3_annotation_results/2_Annotation_AutomatedResults.csv`
This secondary dataset contains the results of automated annotations, focusing on demographic attributes. Below are the details:


#### Column names:
- **datasetName**
- **folderName**
- **imageName**
- **Age**
- **Gender**
- **Ethnicity**



