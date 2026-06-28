--1. Top 5 funds by NAV
select * from fact_nav
order by nav desc
limit 5;

--2.Total transactions
select count(*) as total_transactions
from fact_transactions;

--3. Average NAV
select avg(nav) as average_nav
from fact_nav;

--4. Maximum NAV
select max(nav) as maximum_nav
from fact_nav;

--5. Minimum NAV
select min(nav) as minimum_nav
from fact_nav;

--6. Total NAV records
select count(*) as total_nav_records
from fact_nav;

--7. NAV by AMFI Code
select amfi_code,avg(nav) as average_nav
from fact_nav group by amfi_code;

--8. Highest NAV
select amfi_code,max(nav) as highest_nav
from fact_nav group by amfi_code;

--9. Lowest NAV
select amfi_code,min(nav) as lowest_nav
from fact_nav group by amfi_code;

--10. Total NAV by AMFI Code
select amfi_code,sum(nav) as total_nav
from fact_nav group by amfi_code;