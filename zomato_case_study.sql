use zomato;

SELECT * FROM orders;

-- 2) Count Number of Rows
select count(*) from orders;
select count(*) from users;
select count(*) from order_details;

-- 3) Return n random records
select * from users order by rand() limit 5;

-- 4) Find Null values
select * from orders where restaurant_rating is null;

-- To replace null values with 0
update orders set restaurant_rating = 0 where restaurant_rating is null;

-- 5) Find number of orders placed by each customer
select t1.user_id,count(*) as num_orders from orders t1 join users t2 on t1.user_id = t2.user_id group by t1.user_id;

-- 6) find restaurant with most number of menu items
SELECT 
    r_name,count(*)
FROM
    restaurants t1
        JOIN
    menu t2 ON t1.r_id = t2.r_id
GROUP BY t1.r_id;

-- 7) Find number of votes and avg rating for all the restaurants
SELECT 
    t2.r_name, COUNT(*), round(AVG(restaurant_rating),2)
FROM
    orders t1
        JOIN
    restaurants t2 ON t1.r_id = t2.r_id where restaurant_rating is not null
GROUP BY t1.r_id;

-- 8) Find the food that is being sold at most number of restaurants
select f_name,count(*) as most_sold from menu t1
join food t2 on t1.f_id = t2.f_id
group by t1.f_id
order by most_sold desc limit 1;

-- 9) Find restaurant with max revenue in a given month -> (May)
select  r_name,sum(amount) as revenue from orders t1 
join restaurants t2 on t1.r_id = t2.r_id 
where monthname(date(date)) = 'May'
group by t1.r_id order by revenue desc limit 1;

-- Month by Month revenue for a particular restaurant -> (KFC)
select monthname(date) as months, sum(amount) as revenue from orders t1 
join restaurants t2 on t1.r_id = t2.r_id
where r_name = 'kfc'
group by monthname(date(date));

-- 10) Find retaurants with sales greater than x
select r_name,sum(amount) as revenue from orders t1 
join restaurants t2 on t1.r_id = t2.r_id 
group by t1.r_id having sum(amount) > 1500;

-- 11) Find customers who have never ordered
select user_id,name from users 
except select t1.user_id,name 
from orders t1 join users t2 on t1.user_id = t2.user_id;

-- 12) Show order details of a particular customer in a given date range
select t2.order_id,f_name,date from orders t1 
join order_details t2 on t1.order_id = t2.order_id
join food t3 on t2.f_id = t3.f_id
where user_id = 1 and date between '2022-05-15' and '2022-06-15';

-- 13) Customer favourite Food
select t3.name,t4.f_name,count(distinct t4.f_name) as count_of from orders t1 join order_details t2 on t1.order_id = t2.order_id
join users t3 on t1.user_id = t3.user_id
join food t4 on t2.f_id = t4.f_id group by t1.user_id order by count_of desc;

-- 14) Find most costly restaurants (avg price per dish)
select r_name,count(*),sum(price)/count(*) as average from menu t1
join restaurants t2 on t1.r_id = t2.r_id group by t1.r_id
order by average desc;

-- 15) Find delivery partner compensation using the formula (no of deliveries * 100 + 1000*avg_rating)
select t1.partner_id,t2.partner_name, count(*) * 100 + avg(delivery_rating) * 1000 as salary from orders t1
join delivery_partner t2 on t1.partner_id = t2.partner_id
group by partner_id order by salary desc;

-- 17) Find correlation between delivery_time and rating
select corr(delivery_time,delivery_rating + restaurant_rating) from orders;

-- 18) Find all the vegetarian restaurants
select r_name from menu t1 join food t2 on t1.f_id = t2.f_id
join restaurants t3 on t1.r_id = t3.r_id where type = 'veg' group by t1.r_id;
