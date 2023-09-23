-- @DB1: hbtn_0d_tvshows

-- lists all genres from @DB1 and displays the number of shows linked to it
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.show_id) AS number_of_shows FROM
tv_show_genres
RIGHT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY (tv_genres.name)
ORDER BY number_of_shows DESC;
