# IBM Applied Data Science Capstone — SpaceX Falcon 9 Landing Prediction

**Student repository:** https://github.com/Sanskruti104/IBM-SpaceX-Data-Science-Capstone

This is a reproducible project scaffold for the IBM Applied Data Science Capstone. It creates notebooks for API collection, web scraping, data wrangling, EDA, SQL, Folium mapping, and classification.

## Important
- These notebooks are newly organized starter code, not proof that the project has already been executed.
- Run each notebook in order and inspect outputs/errors.
- The public SpaceX API and Wikipedia page can change. For the IBM graded assignment, the official course-provided dataset snapshots may be preferable because your results must match your course labs.
- Do not submit placeholder or unexecuted results as if they were verified. Include actual chart images, SQL result tables, dashboard screenshots, model metrics, and confusion matrix in the final presentation.
- The map marks launchpads. Proximity claims require a separate trusted geographic dataset and calculated distances.

## Notebook order
1. `notebooks/01_data_collection_api.ipynb`
2. `notebooks/02_web_scraping.ipynb`
3. `notebooks/03_data_wrangling.ipynb`
4. `notebooks/04_eda_visualization.ipynb`
5. `notebooks/05_eda_sql.ipynb`
6. `notebooks/06_folium_map.ipynb`
7. `notebooks/07_predictive_analysis.ipynb`

## Setup
Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

Run notebooks from the `notebooks/` directory, in order. Each notebook writes files relative to the project root.

## Data sources
- SpaceX API: https://api.spacexdata.com/v4/launches/query
- Wikipedia launch history: https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches
- IBM course: Applied Data Science Capstone course labs and provided datasets.

## Expected deliverables
- Executed notebooks with saved outputs
- `data/processed/` datasets and SQLite database
- `outputs/figures/` charts and map HTML
- `outputs/model_results/` SQL/model tables
- Final presentation PDF and completed report PDF
