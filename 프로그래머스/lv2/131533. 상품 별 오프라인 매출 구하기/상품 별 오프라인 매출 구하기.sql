-- 코드를 입력하세요
SELECT PRODUCT_CODE, sum(SALES_AMOUNT*PRICE) as SALES
from PRODUCT p, OFFLINE_SALE o
where p.PRODUCT_ID = o.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc, PRODUCT_CODE