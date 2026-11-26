select
    player_id,
    min(event_date) as first_login
from Activity
group by player_id;


-- 오답 
-- select
--     player_id,
--     event_date as first_login
-- from Activity
-- group by player_id
-- having event_date = min(event_date)