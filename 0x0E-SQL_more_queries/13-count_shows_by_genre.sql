-- Lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_genres.name AS genre, 
COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id 
WHERE tv_show_genres.show_id IS NOT NULL
GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
