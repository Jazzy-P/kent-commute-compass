# Kent Commute Compass

**Explore semi-detached house prices and morning rail commutes across five Kent locations.**

Kent Commute Compass is an interactive Python dashboard for comparing the cost of buying a semi-detached home with the time spent commuting to London Bridge. It combines HM Land Registry transaction data with a manually compiled sample of direct morning train services.

**Status:** Live public MVP
**Current Version:** `v0.1.0`
**Live App:** https://kent-commute-compass.streamlit.app/

## What it does

- Compares **Sevenoaks, Tonbridge, Tunbridge Wells, Paddock Wood and Staplehurst** using 2025 median semi-detached sale prices, recorded sales counts, median train journey times and sampled morning train counts.
- Filters locations by **maximum property budget** and **maximum train journey time**, including a helpful message when no locations match.
- Shows an interactive chart of **annual median semi-detached sale prices from 2023 to 2025** for all five locations. This wider-market view stays visible regardless of the filters.

The comparison helps explore trade-offs between affordability and commuting time; it does not predict the price of an individual home.

## Why I built it

Choosing where to live often involves balancing property affordability with commuting time. This project brings those considerations together in one place while providing hands-on experience with Python, SQL, data analysis and interactive applications.

## Technology

| Tool | Role |
| --- | --- |
| Python | Application logic |
| SQL | Filtering, joining and aggregating property and train data |
| DuckDB | Querying and aggregating CSV data |
| Pandas | Reshaping data for display and charts |
| Streamlit | Interactive dashboard |

## Run locally

### 1. Get the code

Clone this repository or download it as a ZIP, then open a terminal in the project folder.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Download property data

The raw property CSV files are **not stored in this repository**. Download the **yearly Price Paid Data CSV files** for **2023, 2024 and 2025** from the official [HM Land Registry Price Paid Data downloads](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads).

Extract the CSVs if necessary, and place them in the `data/` directory using these exact names:

```text
data/
├── pp-2023.csv
├── pp-2024.csv
├── pp-2025.csv
└── train_times.csv
```

The repository includes `data/train_times.csv`. Keep the original Price Paid Data CSV structure; the DuckDB query expects the raw files without a header row. Run the application from the project root so relative file paths resolve correctly.

### 5. Start the dashboard

```bash
python -m streamlit run app.py
```

Open the local URL shown in the terminal (typically `http://localhost:8501`).

## Updating the data

Kent Commute Compass uses preprocessed CSV files to keep the deployed Streamlit application lightweight and responsive.

The raw HM Land Registry Price Paid Data is processed locally using Python, DuckDB and SQL. The resulting datasets are saved as smaller CSV files that the Streamlit application reads directly.

### Source files

The data processing workflow uses:

- `data/pp-2023.csv`, `data/pp-2024.csv`, `data/pp-2025.csv` — raw HM Land Registry property sales data.
- `data/train_times.csv` — manually collected train timetable data.

The large raw Land Registry files are stored locally and are not committed to GitHub.

### Refresh procedure

1. Update the relevant raw property data or `train_times.csv`, ensuring the existing file structure and expected columns are preserved.
2. Open a terminal in the project directory and activate the Python virtual environment.
3. Run the processing script:

   `python main.py`

4. The script regenerates and overwrites:
   - `data/comparison_data.csv`
   - `data/historical_prices.csv`
5. Check which files have changed:

   `git status`

6. Launch the application locally:

   `streamlit run app.py`

7. Verify that the comparison table, property price and journey time sliders, and historical price chart work correctly.
8. Review the changed files before committing and pushing the updated processed datasets to GitHub.

### Deployment

The deployed Streamlit application reads `comparison_data.csv` and `historical_prices.csv` directly. It does not run the raw data processing pipeline when users open the dashboard.

Once updated processed CSV files are committed and pushed to the connected GitHub repository, Streamlit Community Cloud can redeploy the application with the refreshed data.

### Important notes

- Running `python main.py` overwrites the existing processed CSV files rather than creating additional copies.
- The raw Land Registry datasets must be available locally to regenerate the processed files.
- Refreshing the processed datasets does not automatically change the source data.
- Changes to the train timetable sample or geographic methodology should also be reflected in the project's documentation.

## Data and methodology

### Property sales

**Source:** [HM Land Registry Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads), 2023–2025.

- Retains transactions marked as **semi-detached**.
- Identifies property locations using the HM Land Registry locality field (`column10`), falling back to the town/city field (`column11`) when locality is missing. The selected place names are matched directly; no geographic boundaries, distance calculations or station catchment areas are used.
- Calculates the **median recorded sale price** and **number of matching transactions** by location and year.
- Uses **2025** results in the comparison table and **2023–2025** results in the historical chart.

### Train journeys

**Source:** Google Maps, manually transcribed into `data/train_times.csv`.

**Timetable sample dates:**
- Original five locations (v0.1.0): Thursday, 12 November 2026.
- Additional stations collected for v0.2.0: Thursday, 19 November 2026.

- Includes sampled direct services scheduled to arrive at London Bridge between 08:00 and 09:00 on the relevant sample date.
- Calculates median scheduled journey duration for each station.
- Counts the sampled services in that arrival window.

Journey details were collected manually from Google Maps for the dates stated above. These are single-day samples of scheduled journeys, not live journey information or measures of service reliability. The sample dates differ between the original locations and the additional stations collected for v0.2.0.

## How to interpret the results

- **Median sale prices are not asking prices or individual property valuations.** They describe the transactions in the dataset.
- **Changes in annual medians are not like-for-like house price growth.** Different properties may have sold in each year.
- **Location matching is approximate.** Place-name fields do not define exact town or station catchment boundaries.
- **Journey times are scheduled, sampled and direct.** Delays, cancellations, changes in timetables, travel to the station and onward journeys are not included.
- **Coverage is deliberately limited.** The dashboard currently compares five Kent locations and one London destination.

Use the dashboard for initial exploration, and verify current property listings and train services before making a financial or relocation decision.

## Repository structure

```
kent-commute-compass/
├── app.py
├── main.py
├── train_analysis.py
├── requirements.txt
├── .gitignore
├── README.md
├── TESTING.md
└── data/
    ├── train_times.csv
    ├── comparison_data.csv
    └── historical_prices.csv
```

The three downloaded `pp-YYYY.csv` files also belong in `data/` locally, but are excluded from Git.

## Project status and roadmap

The core dashboard is working. The project is live and currently on the `v0.1.0` release.

Potential next steps:

- [ ] Complete release testing and verify the published setup instructions on a fresh machine.
- [ ] Add a dashboard screenshot to the repository.
- [ ] Expand to more Kent locations and London destinations.
- [ ] Improve geographic matching and timetable coverage.
- [ ] Refine visualisations and data explanations.

These are possible enhancements, not promised release dates.

## Data attribution

Property transaction information is sourced from **HM Land Registry Price Paid Data** and contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

Train journey information was manually compiled from Google Maps using timetable samples from Thursday, 12 November 2026 (original locations) and Thursday, 19 November 2026 (additional stations collected for v0.2.0). It is provided as a limited comparison sample, not as live travel advice; check current schedules with an official journey planner before travelling.
