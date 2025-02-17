### To Run:

1. Run the **5 ExtendedScrape Jupyter notebooks** in the "data_collection" folder in ascending order, followed by the merge notebook. These notebooks will search for papers on Google Scholar based on combinations of FER dataset names (`fer_datasets_LONG`) and relevant topics (`topics`) This process creates the file `Scrapes_ALL.csv` in the `1_scraping` folder.
2. Run the notebooks in the **"full_text_extraction"** folder in ascending order. This step will produce 3 files in the `results` folder containing the full texts extracted from each source.
3. Run the **"AllFullTextsTOCSV"** notebook to merge the 3 files produced in the previous step into a single file, `FullText_ALL.csv`, which will be saved in the `/1_scraping/` folder.

---

### Folder Structure

- **`dataset_collection`**:
  - Contains 5 notebooks for data collection and corresponding saved CSV files.
  - Includes the notebook `Scrape_Merge.ipynb`, where scraped data is merged and saved to `1_scraping/Scrapes_ALL.csv`.

- **`full_text_extraction`**:
  - Contains notebooks used to extract full text from links provided in the `Scrape_Merge.csv` file.

- **`results`**:
  - Stores the results from the `full_text_extraction` process.

- **`ALLFullTextsTOCSV.ipynb` Notebook**:
  - Merges all the data collected from the previous steps into the file `FullText_ALL.csv`.

---

### Dataset Columns Description

The final dataset contains the following columns:

- **`ID`**: A unique identifier for each entry in the dataset.
- **`Title`**: The title of the academic paper.
- **`Authors`**: The names of the authors of the paper.
- **`Year`**: The publication year of the paper.
- **`Cited By`**: The number of citations the paper has received.
- **`Detected_Dataset`**: The name(s) of the FER datasets detected in the paper.
- **`Detected_Topic`**: The topic(s) identified as relevant in the paper.
- **`Abstract`**: The abstract or summary of the paper.
- **`Journal`**: The journal or publication in which the paper appeared.
- **`URL`**: The link to the paper's source.
- **`Full_Text`**: The extracted full text of the paper.

