import duckdb

def get_comparison_data():
    result = duckdb.sql("""
        WITH property_locations AS (SELECT COALESCE (column10, column11) AS location, column01 AS sold_price, YEAR(CAST(column02 AS DATE)) AS sale_year
        FROM read_csv('data/pp-202*.csv', header = false)
        WHERE column04 = 'S'
        ),
        train_stats AS (SELECT station, MEDIAN(journey_minutes) AS median_train_time, COUNT(*) AS morning_trains
            FROM read_csv('data/train_times.csv')
            GROUP BY station
        )
        SELECT location, MEDIAN(sold_price) AS median_price, COUNT(*) AS total_sales, sale_year, train_stats.median_train_time, train_stats.morning_trains
        FROM property_locations
        JOIN train_stats
        ON property_locations.location = train_stats.station
        WHERE location IN ('SEVENOAKS', 'TONBRIDGE', 'TUNBRIDGE WELLS', 'PADDOCK WOOD', 'STAPLEHURST') AND sale_year = 2025
        GROUP BY location, sale_year, train_stats.median_train_time, train_stats.morning_trains
        ORDER BY sale_year DESC, median_price ASC
        LIMIT 20;
    """)
    return result.df()

def get_historical_prices():
    result = duckdb.sql("""
        WITH property_locations AS (SELECT COALESCE (column10, column11) AS location, column01 AS sold_price, YEAR(CAST(column02 AS DATE)) AS sale_year
        FROM read_csv('data/pp-202*.csv', header = false)
        WHERE column04 = 'S'
        ),
        SELECT location, MEDIAN(sold_price) AS median_price, COUNT(*) AS total_sales, sale_year
        FROM property_locations
        WHERE location IN ('SEVENOAKS', 'TONBRIDGE', 'TUNBRIDGE WELLS', 'PADDOCK WOOD', 'STAPLEHURST')
        GROUP BY location, sale_year
        ORDER BY sale_year DESC, median_price ASC
    """)
    return result.df()

if __name__ == "__main__":
        print(get_historical_prices())