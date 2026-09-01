USE coffee_analytics_db;

-- 1. Analisis Jam Sibuk Operasional (Peak-Hour Demand)
SELECT 
    hour AS transaction_hour,
    COUNT(transaction_id) AS total_orders,
    ROUND(SUM(money), 2) AS total_revenue,
    ROUND(AVG(money), 2) AS avg_ticket_size,
    ROUND(COUNT(transaction_id) * 100.0 / (SELECT COUNT(*) FROM coffee_transactions), 2) AS pct_of_total_orders
FROM coffee_transactions
GROUP BY hour
ORDER BY total_orders DESC;

-- 2. Pareto Menu Analysis (Cumulative Revenue Share)
WITH MenuSales AS (
    SELECT 
        coffee_name,
        COUNT(transaction_id) AS total_sold,
        ROUND(SUM(money), 2) AS menu_revenue
    FROM coffee_transactions
    GROUP BY coffee_name
),
RankedMenu AS (
    SELECT 
        coffee_name,
        total_sold,
        menu_revenue,
        SUM(menu_revenue) OVER (ORDER BY menu_revenue DESC) AS running_total_revenue,
        SUM(menu_revenue) OVER () AS overall_revenue
    FROM MenuSales
)
SELECT 
    coffee_name,
    total_sold,
    menu_revenue,
    ROUND((menu_revenue / overall_revenue) * 100, 2) AS pct_revenue_share,
    ROUND((running_total_revenue / overall_revenue) * 100, 2) AS cumulative_revenue_share
FROM RankedMenu
ORDER BY menu_revenue DESC;

-- 3. Customer RFM Segmentation
WITH CustomerAgg AS (
    SELECT 
        customer_id,
        DATEDIFF((SELECT MAX(datetime) FROM coffee_transactions), MAX(datetime)) AS recency_days,
        COUNT(transaction_id) AS frequency,
        ROUND(SUM(money), 2) AS monetary
    FROM coffee_transactions
    WHERE customer_id != 'CASH_GUEST_USER'
    GROUP BY customer_id
),
RFM_Scores AS (
    SELECT 
        customer_id,
        recency_days,
        frequency,
        monetary,
        NTILE(4) OVER (ORDER BY recency_days ASC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency ASC) AS f_score,
        NTILE(4) OVER (ORDER BY monetary ASC) AS m_score
    FROM CustomerAgg
)
SELECT 
    customer_id,
    recency_days,
    frequency,
    monetary,
    CONCAT(r_score, f_score, m_score) AS rfm_cell,
    CASE 
        WHEN r_score >= 3 AND f_score >= 3 AND m_score >= 3 THEN 'Champions / Loyal Regulars'
        WHEN r_score >= 3 AND f_score <= 2 THEN 'Recent / Potential Loyalists'
        WHEN r_score <= 2 AND f_score >= 3 THEN 'At Risk / Need Re-activation'
        ELSE 'Hibernating / One-Off Buyers'
    END AS customer_segment
FROM RFM_Scores
ORDER BY monetary DESC;
