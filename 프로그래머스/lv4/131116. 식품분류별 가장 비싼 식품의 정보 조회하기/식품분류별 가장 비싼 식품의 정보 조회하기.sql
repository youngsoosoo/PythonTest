-- 코드를 입력하세요 
SELECT CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from FOOD_PRODUCT
where (CATEGORY, PRICE) in (
    select CATEGORY, MAX(PRICE) as MAX_PRICE
    from FOOD_PRODUCT
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY
    )
order by 2 desc
    