-- @DB1: hbtn_0d_tvshows
-- @GENRE1: Comedy

-- Lists all shows without the genre @GENRE1 in the DATABASE @DB1
SELECT DISTINCT tv_shows.title FROM
tv_shows
WHERE 'Comedy' NOT IN (SELECT DISTINCT tv_genres.name FROM
tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows AS subquery_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE subquery_shows.title = tv_shows.title)
ORDER BY tv_shows.title ASC;
