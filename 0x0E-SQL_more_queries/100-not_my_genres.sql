-- @DB1: hbtn_0d_tvshows
-- @SHOW1: Dexter

-- Uses the @DB1 DATABSE to list all genres not linked to the show @SHOW1
SELECT DISTINCT tv_genres.name FROM
tv_genres
WHERE tv_genres.name NOT IN (SELECT tv_genres.name FROM
tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.name ASC;
