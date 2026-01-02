-- Last updated: 1/2/2026, 12:17:33 PM
SELECT tweet_id
FROM Tweets
WHERE LENGTH(REPLACE(content, ' ', '')) > 15;
