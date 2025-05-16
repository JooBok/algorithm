-- 코드를 입력하세요
SELECT ANIMAL_ID, NAME, IF(SUBSTRING_INDEX(SEX_UPON_INTAKE, " ", 1) IN ("Neutered", "Spayed"), "O", "X") AS "중성화"
FROM ANIMAL_INS