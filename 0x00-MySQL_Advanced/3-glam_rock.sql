-- List all bands with 'Glam rock' as their main style ranked by
-- their longevity
-- 2022 is used as the current year instead of YEAR(CURDATE())
SELECT band_name,
       CASE
           WHEN split IS NULL THEN 2022 - formed
           ELSE split - formed
       END AS lifespan
  FROM metal_bands
 WHERE style LIKE '%Glam rock%'
 ORDER BY lifespan DESC;
