# Write your MySQL query statement below
select p.firstName, P.lastName, a.city,a.state
from Person p
Left Join Address a on p.personId=a.personId