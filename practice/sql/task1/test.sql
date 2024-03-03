SELECT p.model, p.type
    FROM pc
    join Product p on PC.model=p.model
    where maker = 'B'
union all
    SELECT p.model, p.type
    FROM printer pr
    join Product p on pr.model=p.model
    where maker = 'B'
union all
    SELECT p.model, p.type
    FROM laptop lp
    join Product p on lp.model=p.model
    where maker = 'B'
