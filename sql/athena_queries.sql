CREATE EXTERNAL TABLE IF NOT EXISTS trips (
    trip_id INT,
    trip_date DATE,
    distance_km DOUBLE,
    fare_amount DOUBLE,
    payment_type STRING
)
STORED AS PARQUET
LOCATION 's3://simple-data-lake-b68fd3cb/silver/trips/';

SELECT COUNT(*) AS total_trips
FROM trips;

SELECT SUM(fare_amount) AS total_revenue
FROM trips;

SELECT
    trip_date,
    SUM(fare_amount) AS revenue
FROM trips
GROUP BY trip_date
ORDER BY trip_date;

SELECT
    payment_type,
    COUNT(*) AS total
FROM trips
GROUP BY payment_type
ORDER BY payment_type;
