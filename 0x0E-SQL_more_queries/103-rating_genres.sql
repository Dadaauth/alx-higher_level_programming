-- @DB1: hbtn_0d_tvshows_rate

-- Lists all genres in the DATABASE @DB1 by their rating
SELECT tv_genres.name, SUM(rate.rate) AS rating FROM
tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_show_ratings AS rate
ON tv_shows.id = rate.show_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
