# Kent Commute Compass — Manual Testing Checklist

Use this checklist after changes to the data pipeline, dashboard, or deployment, and before each release. It documents the v0.1.0 baseline and can be adapted as location coverage expands.

## How to use

1. Start from the repository root with the project dependencies installed.
2. If testing a data refresh, ensure the required raw Land Registry CSV files are available locally, then run `python main.py`. This regenerates `data/historical_prices.csv` and `data/comparison_data.csv`.
3. Launch the dashboard with `streamlit run app.py`.
4. Work through the checks below. Mark each checkbox only after observing the expected result. Record failures and the steps needed to reproduce them.
5. For deployment checks, open the published Streamlit application separately.

> **Important:** `app.py` reads the processed CSV files; launching Streamlit alone does not regenerate them. The train data expansion for v0.2.0 does not, by itself, add new towns to the v0.1.0 property queries.

## v0.1.0 manual checks

### Local launch and baseline data

- [ ] **Local launch:** `streamlit run app.py` opens the dashboard without an error or traceback. The title **Kent Commute Compass** and **2025 Location Comparison** heading appear.
- [ ] **Default comparison table:** With the default £1,000,000 budget and 100-minute commute limits, the table displays the expected v0.1.0 locations: **Sevenoaks, Tonbridge, Tunbridge Wells, Paddock Wood, and Staplehurst**. Check that the displayed columns include location, median price, properties sold, year, train journey, and morning trains; compare a few values against `data/comparison_data.csv`.

### Filters

- [ ] **Maximum property budget:** Reduce the budget slider in £50,000 increments. Locations above the selected median-price threshold disappear; eligible locations remain. Restore the default afterward.
- [ ] **Maximum train journey:** Reduce the commute slider in 5-minute increments. Locations above the selected median journey threshold disappear; eligible locations remain. Restore the default afterward.
- [ ] **Combined filters:** Set both sliders below their defaults. Every displayed location satisfies **both** limits. Restoring both defaults restores the expected comparison table.
- [ ] **No-results warning:** Select limits that exclude every location (for example, a £0 maximum budget). The message **“No locations match your current budget and commute requirements. Try increasing one or both limits.”** appears instead of the comparison table. Restore the defaults and confirm the table returns.

### Historical chart

- [ ] **Historical median prices:** The chart headed **Median Semi-Detached House Prices (2023-2025)** displays **2023, 2024, and 2025** for all five baseline locations. Compare selected plotted values with `data/historical_prices.csv`. Change the sliders and confirm the historical chart still shows all five locations.

### Deployment and documentation

- [ ] **Deployed application:** Open the published Streamlit app after the relevant changes have been pushed and deployed. Confirm it loads without errors, displays the expected table and chart, and responds to both sliders and the no-results case.
- [ ] **Reusable checklist:** Confirm this `TESTING.md` file is committed to the repository so the same checks can be repeated after future updates.

## Test run record

Copy this section for each test session, or record results in the relevant GitHub Issue or pull request.

- **Date:**
- **Version / commit:**
- **Environment:** Local / deployed / both
- **Result:** Pass / Fail / Partial
- **Failed or skipped checks:**
- **Notes and follow-up Issue links:**

## Scope and limitations

- These are **manual checks**, not automated tests. They confirm observed application behaviour but do not prove every source record is correct.
- The v0.1.0 baseline contains five property locations. Update expected location counts when a later release deliberately expands coverage.
- Property medians represent sales recorded in each year, not appreciation of the same individual properties.
- The historical chart is intentionally **not filtered** by the comparison-table sliders.
- A successful local launch is not a substitute for checking the deployed application.
