## Операции в SQL


**Конкатенация**

_SQL SERVER_:

```sql
select concat(ename, ' WORKS AS A' , job) as msg
    from emp
where deptno=10
```

_Postgresql_:

```sql
select ename || ' WORKS AS A'|| job as msg
    from emp
where deptno=10
```

**Условная логика**

```sql
select ename, sal
    case when sal <= 2000 then 'UNDERPAID'
         when sal >= 4000 then 'OVERPAID'
         else 'OK'
    end as status
from emp
```

**Замена значений NULL значениями не-NULL**

```sql
select coalesce(comm, 0) from emp
```

```sql
select case 
    when comm is not null then comm
    else 0
    end
from emp
```

```sql
select concat(ename, ' WORKS AS A' , job) as msg
    from emp
where deptno=10
```

**Поиск по шаблону**

```sql
select name, job
    from emp
where deptno in (10, 20)
```

[//]: # (В именах которфх есть буква 'I" или заканчивается на 'ER')

```sql
select name, job from emp
where deptno in (10, 20) and (ename like '%I%' or job like '%ER')
```

