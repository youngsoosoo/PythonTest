-- 코드를 입력하세요
SELECT a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_OUTS a inner join ANIMAL_INS b on a.ANIMAL_ID = b.ANIMAL_ID
where a.SEX_UPON_OUTCOME not like "intact%" and b.SEX_UPON_INTAKE like "intact%"
order by a.ANIMAL_ID