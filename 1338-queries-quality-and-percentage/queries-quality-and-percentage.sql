# Write your MySQL query statement below
select query_name,
Round(AVG(rating*1.0/position),2) as quality,
Round(sum(case when rating<3 Then 1 else 0 end)*100/count(*),2) as poor_query_percentage
from Queries
group by query_name