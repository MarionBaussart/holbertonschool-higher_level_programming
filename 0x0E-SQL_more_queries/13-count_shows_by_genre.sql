-- script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
--
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
SELECT tv_genres.name AS genre, COUNT(DISTINCT tv_shows_genres.genre_id) AS number_of_shows
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows_genres.genre_id IS NOT NULL
ORDER BY number_of_shows DESC;