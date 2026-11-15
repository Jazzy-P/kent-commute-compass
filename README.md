# Kent Commute Compass

**Explore semi-detached house prices and morning rail commutes across five Kent locations.**

Kent Commute Compass is an interactive Python dashboard for comparing the cost of buying a semi-detached home with the time spent commuting to London Bridge. It combines HM Land Registry transaction data with a manually compiled sample of direct morning train services.

**Status:** Pre-release development · **Target version:** `v0.1.0`

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

## Data and methodology

### Property sales

**Source:** [HM Land Registry Price Paid Data](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads), 2023–2025.

- Retains transactions marked as **semi-detached**.
- Matches the five locations using place-name fields in the Price Paid Data records, rather than precise geographical boundaries.
- Calculates the **median recorded sale price** and **number of matching transactions** by location and year.
- Uses **2025** results in the comparison table and **2023–2025** results in the historical chart.

### Train journeys

**Source:** Google Maps, manually transcribed into `data/train_times.csv`. **Sample date:** Thursday, 12 November 2026.

- Includes sampled direct services **scheduled to arrive at London Bridge between 08:00 and 09:00 on Thursday, 12 November 2026**.
- Calculates median scheduled journey duration for each station.
- Counts the sampled services in that arrival window.

Journey details were collected manually from Google Maps for the stated date. This is a **single-day sample of scheduled journeys**, not a Google Maps dataset, live journey information, or a measure of service reliability.

## How to interpret the results

- **Median sale prices are not asking prices or individual property valuations.** They describe the transactions in the dataset.
- **Changes in annual medians are not like-for-like house price growth.** Different properties may have sold in each year.
- **Location matching is approximate.** Place-name fields do not define exact town or station catchment boundaries.
- **Journey times are scheduled, sampled and direct.** Delays, cancellations, changes in timetables, travel to the station and onward journeys are not included.
- **Coverage is deliberately limited.** The dashboard currently compares five Kent locations and one London destination.

Use the dashboard for initial exploration, and verify current property listings and train services before making a financial or relocation decision.

## Repository structure

```text
kent-commute-compass/
├── app.py                  # Streamlit dashboard
├── main.py                 # DuckDB queries and data functions
├── train_analysis.py       # Train-data SQL experimentation
├── requirements.txt        # Python dependencies
├── .gitignore              # Files excluded from Git
├── README.md               # Project documentation
└── data/
    └── train_times.csv     # Manually compiled timetable sample
```

The three downloaded `pp-YYYY.csv` files also belong in `data/` locally, but are excluded from Git.

## Project status and roadmap

The core dashboard is working. The project is in **pre-release testing and documentation** ahead of its first `v0.1.0` release.

Potential next steps:

- [ ] Complete release testing and verify the published setup instructions on a fresh machine.
- [ ] Add a dashboard screenshot to the repository.
- [ ] Expand to more Kent locations and London destinations.
- [ ] Improve geographic matching and timetable coverage.
- [ ] Refine visualisations and data explanations.

These are possible enhancements, not promised release dates.

## Data attribution

Property transaction information is sourced from **HM Land Registry Price Paid Data** and contains public sector information licensed under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).

Train journey information was manually compiled from Google Maps for Thursday, 12 November 2026. It is provided as a limited comparison sample, not as live travel advice; check current schedules with an official journey planner before travelling.
