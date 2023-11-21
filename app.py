import streamlit as st

st.sidebar.title("Zomato Case Study")

st.markdown("##### 1) Count Number of Rows")
st.code("""
select count(*) from orders;
select count(*) from users;
select count(*) from order_details;
""")

st.markdown("##### 2) Return n random records")
st.code("""
select * from users order by rand() limit 5;
""")

st.markdown("##### 3) Find Null values")
st.code("""
select * from orders where restaurant_rating is null;
""")

st.markdown("##### 4) Find number of orders placed by each customer")
st.code("""
SELECT 
    t1.user_id, COUNT(*) AS num_orders
FROM
    orders t1
        JOIN
    users t2 ON t1.user_id = t2.user_id
GROUP BY t1.user_id;
""")

st.markdown("##### 5) find restaurant with most number of menu items")
st.code("""
SELECT 
    r_name,count(*)
FROM
    restaurants t1
        JOIN
    menu t2 ON t1.r_id = t2.r_id
GROUP BY t1.r_id;
""")

st.markdown("##### 6) Find number of votes and avg rating for all the restaurants")
st.code("""
SELECT 
    t2.r_name, COUNT(*), round(AVG(restaurant_rating),2)
FROM
    orders t1
        JOIN
    restaurants t2 ON t1.r_id = t2.r_id where restaurant_rating is not null
GROUP BY t1.r_id;
""")

st.markdown("##### 7) Find the food that is being sold at most number of restaurants")
st.code("""
SELECT 
    f_name, COUNT(*) AS most_sold
FROM
    menu t1
        JOIN
    food t2 ON t1.f_id = t2.f_id
GROUP BY t1.f_id
ORDER BY most_sold DESC
LIMIT 1;
""")

st.markdown("##### 8) Find restaurant with max revenue in a given month -> (May)")
st.code("""
SELECT 
    r_name, SUM(amount) AS revenue
FROM
    orders t1
        JOIN
    restaurants t2 ON t1.r_id = t2.r_id
WHERE
    MONTHNAME(DATE(date)) = 'May'
GROUP BY t1.r_id
ORDER BY revenue DESC
LIMIT 1;
""")

st.markdown("##### 9) Find retaurants with sales greater than x")
st.code("""
SELECT 
    r_name, SUM(amount) AS revenue
FROM
    orders t1
        JOIN
    restaurants t2 ON t1.r_id = t2.r_id
GROUP BY t1.r_id
HAVING SUM(amount) > 1500;
""")

st.markdown("##### 10) Find customers who have never ordered")
st.code("""
select count(*) from orders;
select count(*) from users;
select count(*) from order_details;
""")

st.markdown("##### 11) Show order details of a particular customer in a given date range")
st.code("""
SELECT 
    t2.order_id, f_name, date
FROM
    orders t1
        JOIN
    order_details t2 ON t1.order_id = t2.order_id
        JOIN
    food t3 ON t2.f_id = t3.f_id
WHERE
    user_id = 1
        AND date BETWEEN '2022-05-15' AND '2022-06-15';
""")

st.markdown("##### 12) Customer favourite Food")
st.code("""
SELECT 
    t3.name, t4.f_name, COUNT(DISTINCT t4.f_name) AS count_of
FROM
    orders t1
        JOIN
    order_details t2 ON t1.order_id = t2.order_id
        JOIN
    users t3 ON t1.user_id = t3.user_id
        JOIN
    food t4 ON t2.f_id = t4.f_id
GROUP BY t1.user_id
ORDER BY count_of DESC;
""")

st.markdown("##### 13) Find most costly restaurants (avg price per dish)")
st.code("""
SELECT 
    r_name, COUNT(*), SUM(price) / COUNT(*) AS average
FROM
    menu t1
        JOIN
    restaurants t2 ON t1.r_id = t2.r_id
GROUP BY t1.r_id
ORDER BY average DESC;
""")

st.markdown("##### 14) Find delivery partner compensation using the formula (no of deliveries * 100 + 1000*avg_rating)")
st.code("""
SELECT 
    t1.partner_id,
    t2.partner_name,
    COUNT(*) * 100 + AVG(delivery_rating) * 1000 AS salary
FROM
    orders t1
        JOIN
    delivery_partner t2 ON t1.partner_id = t2.partner_id
GROUP BY partner_id
ORDER BY salary DESC;
""")

st.markdown("##### 15) Find all the vegetarian restaurants")
st.code("""
SELECT 
    r_name
FROM
    menu t1
        JOIN
    food t2 ON t1.f_id = t2.f_id
        JOIN
    restaurants t3 ON t1.r_id = t3.r_id
WHERE
    type = 'veg'
GROUP BY t1.r_id;
""")

st.markdown("##### 16) Month by Month revenue for a particular restaurant -> (KFC)")
st.code("""
SELECT 
    MONTHNAME(date) AS months, SUM(amount) AS revenue
FROM
    orders t1
        JOIN
    restaurants t2 ON t1.r_id = t2.r_id
WHERE
    r_name = 'kfc'
GROUP BY MONTHNAME(DATE(date));
""")

st.markdown("##### 17) Find customers who have never ordered")
st.code("""
SELECT user_id,name 
FROM users 
EXCEPT (SELECT t1.user_id,name 
       FROM orders t1 
       JOIN users t2 ON t1.user_id = t2.user_id);
""")
