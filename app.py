import streamlit as st
from main import get_comparison_data, get_historical_prices

def format_journey_time(journey_minutes):
    minutes = int(journey_minutes)
    seconds = int((journey_minutes % 1) * 60)
    return f"{minutes}m {seconds}s"

st.title("Kent Commute Compass")
st.write("Compare median semi-detached property sale prices and morning train journey times across five Kent locations, using direct trains arriving at London Bridge between 08:00-09:00.")
st.subheader("2025 Location Comparison")
st.write ("Drag the sliders to find locations that suit your budget and commute preferences.")

max_budget = st.slider(
    "Maximum Property Budget (£)",
    min_value = 0,
    max_value = 1000000,
    value = 1000000,
    step = 50000,
    format = "£%,d"
)

max_commute = st.slider(
    "Maximum Train Journey (Mins)",
    min_value = 0,
    max_value = 100,
    value = 100,
    step = 5,
    format = "%d min"
)

comparison_data = get_comparison_data()
historical_prices = get_historical_prices()

chart_data = historical_prices.pivot(
    index = "sale_year",
    columns = "location",
    values = "median_price"
)

chart_data.index = chart_data.index.astype(str)

comparison_data = comparison_data.rename(columns={
    "location": "Location",
    "median_price": "Median Price (£)",
    "total_sales": "Properties Sold",
    "sale_year": "Year",
    "median_train_time": "Train Journey (Mins)",
    "morning_trains": "Morning Trains"
})
filtered_data = comparison_data[
    comparison_data["Median Price (£)"] <= max_budget
]

filtered_data = filtered_data[
    filtered_data["Train Journey (Mins)"] <= max_commute
]

display_data = filtered_data.copy()
display_data["Train Journey (Mins)"] = display_data["Train Journey (Mins)"].apply(format_journey_time)

if filtered_data.empty:
    st.warning ("No locations match your current budget and commute requirements. Try increasing one or both limits.")
else:
    st.dataframe(
        display_data,
        hide_index = True,
        column_config={
            "Median Price (£)": st.column_config.NumberColumn(
                "Median Price (£)", format="£%,d"
            )
        }      
    )

st.subheader ("Median Semi-Detached House Prices (2023-2025)")
st.write ("Compare median sale prices of semi-detached houses across five Kent locations, based on properties sold in each year.")

st.line_chart(
    chart_data,
    y_label = "Median Sale Price (£)")

st.write ("Historical prices show all five lovations regardless of the filters above.")