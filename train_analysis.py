import duckdb

result = duckdb.sql("""
    SELECT station, MEDIAN(journey_minutes) AS median_train_time, COUNT(*) AS morning_trains
    FROM read_csv('data/train_times.csv')
    GROUP BY station
    ORDER BY median_train_time ASC;
""")

print(result)