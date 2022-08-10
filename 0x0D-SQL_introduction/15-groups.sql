-- a script lists the number of records with
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
