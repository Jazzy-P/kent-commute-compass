import duckdb

def test_location():
    result = duckdb.sql("""
        SELECT column10 AS location, column11 AS locality
        FROM read_csv('data/pp-2025.csv', header = false)
        WHERE column04 = 'S' AND (location = 'DOVER' OR locality = 'DOVER');
    """)
    return result.df()

print(test_location())