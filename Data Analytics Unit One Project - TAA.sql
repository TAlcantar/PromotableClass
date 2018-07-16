/*Data Analytics - Unit 1 Project*/
  
/* I will be looking at a dataset containing information on Chicago Airbnb listings that I found here: http://insideairbnb.com/get-the-data.html*/


CREATE TABLE chicago_airbnb (
listing VARCHAR(300),
host_name VARCHAR(300),
neighbourhood VARCHAR(300),
room_type VARCHAR(300),
price INT,
minimum_nights INT,
number_of_reviews INT,
last_review DATE,
reviews_per_month DECIMAL(2,2),
calculated_host_listings_count INT,
availability_365 INT);

/* First Hypothisis: The Loop is a popular tourist desitination. Because of that, I hypothesis that there will be more listings in the loop then in other neighborhoods. */

/* LIST OF ALL DISTINCT NEIGHBORHOODS, NUMBER OF LISTINGS FOR EACH NEIGHBORHOOD */
SELECT COUNT(neighbourhood) AS number_of_instances, neighbourhood
FROM chicago_airbnb
GROUP BY neighbourhood
ORDER BY number_of_instances DESC;

/*Conclusion 1: With 306 listings, the Loop actually has the 7th largest number of listings. West Town was number one with 928 lists. Perhaps, this is because of it's proximity to the Loop. */

/* Second Hypothisis: Everyone likes to feel like they got a deal. I hypothisize that listings that include include the word 'free' in the title will have a higher average number of reviews (indicating more stays) then the average number of reviews for the entire dataset.*/

SELECT AVG(number_of_reviews)
FROM chicago_airbnb;

SELECT AVG(`number_of_reviews`)
FROM chicago_airbnb
WHERE listings LIKE "%free%";

/*Conclusion 2: The average number of reviews for all listings is 30. The average number of reviews for a listing with the word 'free' in the title is 43. I think these finds support my hypothesis that the 'free' could possible intice for people to book that listing.*/



