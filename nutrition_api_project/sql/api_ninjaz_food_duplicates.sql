/*

Query Name: api_ninjaz_food_duplicates.sql

Author: Rishov Chatterjee and Brady Hong

Description: This query will find the count of foods that contain duplicates in the destination table.

Approach:

1. Create a common table expression (CTE) which has each food's name along with how many times it appears in the dataset.
2. Apply a HAVING clause to ensure the count is greater than 1 to be known as a duplicate.
3. Query the CTE to get the count of the rows to get the number of foods that have a duplicate.

*/

with foods_with_duplicates as (
    -- Food name is the _name column
    -- Rename the count to frequency
    SELECT _name, count(*) as frequency
    FROM food_results
    -- 1 refers to the _name column and 2 refers to the count()
    GROUP BY 1
    -- Duplicates will be known as having a count that is greater than 1
    HAVING count(*) > 1
    ORDER BY 2 DESC
)

-- Query the CTE by selecting the count of all the records
-- Rename the count to number_duplicates
select count(*) as number_duplicates
from foods_with_duplicates;
