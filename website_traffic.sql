-- Active: 1772520994257@@127.0.0.1@3306@website_analysis
SELECT COUNT(*) AS total_sessions FROM traffic_data;

#Bounce Rate
SELECT 
    ROUND(AVG(Bounce) * 100, 2) AS bounce_rate_percent
FROM traffic_data;

#Conversion Rate
SELECT 
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate_percent
FROM traffic_data;

-- ================================
-- . KPI DASHBOARD QUERY
-- ================================
SELECT 
    COUNT(*) AS total_sessions,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate_percent,
    ROUND(AVG(Bounce) * 100, 2) AS bounce_rate_percent,
    ROUND(AVG(Time_Spent_Seconds), 2) AS avg_time_spent
FROM traffic_data;

-- ================================
-- . TRAFFIC SOURCE ANALYSIS
-- ================================
SELECT 
    Traffic_Source,
    COUNT(*) AS total_users,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate,
    ROUND(AVG(Bounce) * 100, 2) AS bounce_rate
FROM traffic_data
GROUP BY Traffic_Source
ORDER BY conversion_rate DESC;

-- ================================
-- . DEVICE TYPE ANALYSIS
-- ================================
SELECT 
    Device_Type,
    COUNT(*) AS users,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate
FROM traffic_data
GROUP BY Device_Type
ORDER BY conversion_rate DESC;

-- ================================
-- . COUNTRY ANALYSIS
-- ================================
SELECT 
    Country,
    COUNT(*) AS users,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate
FROM traffic_data
GROUP BY Country
ORDER BY conversion_rate DESC;

-- ================================
-- . PAGE VISITS
-- ================================
SELECT 
    Page_Visited,
    COUNT(*) AS visits
FROM traffic_data
GROUP BY Page_Visited
ORDER BY visits DESC;

-- ================================
-- . USER ENGAGEMENT SEGMENTATION
-- ================================
SELECT 
    CASE 
        WHEN Time_Spent_Seconds < 60 THEN 'Low Engagement'
        WHEN Time_Spent_Seconds BETWEEN 60 AND 300 THEN 'Medium Engagement'
        ELSE 'High Engagement'
    END AS engagement_level,
    
    COUNT(*) AS users,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate

FROM traffic_data
GROUP BY engagement_level
ORDER BY conversion_rate DESC;

-- ================================
-- . BOUNCE VS CONVERSION
-- ================================
SELECT 
    Bounce,
    COUNT(*) AS users,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate
FROM traffic_data
GROUP BY Bounce;

-- ================================
-- . BEST PERFORMING COMBINATIONS
-- ================================
SELECT 
    Traffic_Source,
    Device_Type,
    Country,
    ROUND(AVG(Conversion) * 100, 2) AS conversion_rate
FROM traffic_data
GROUP BY Traffic_Source, Device_Type, Country
ORDER BY conversion_rate DESC
LIMIT 10;

-- ================================
-- . WINDOW FUNCTION (ADVANCED)
-- ================================
SELECT 
    Traffic_Source,
    COUNT(*) AS users,
    RANK() OVER (ORDER BY COUNT(*) DESC) AS ranking
FROM traffic_data
GROUP BY Traffic_Source;

-- ================================
-- . HIGH VALUE USERS
-- ================================
SELECT *
FROM traffic_data
WHERE Time_Spent_Seconds > 300
AND Conversion = 1;

-- =========================================
-- END OF PROJECT
-- =========================================