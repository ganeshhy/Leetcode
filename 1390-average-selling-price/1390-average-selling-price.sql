select p.product_id, ROUND(IFNULL(sum(un.units*p.price)/sum(un.units),0),2) as average_price
from Prices p
LEFT join UnitsSold un
on p.product_id=un.product_id
AND un.purchase_date between p.start_date and p.end_date
group by p.product_id
