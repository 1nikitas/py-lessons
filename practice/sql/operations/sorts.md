**Сортировка порядкового элемента**

```sql
select ename, job, sal
from emp
where deptno = 10
order by 3 desc
```

**Сортировка по нескольких атрибутам**


```sql
select ename, job, sal
from emp
where deptno = 10
order by ename, job desc
```

**Сортировка по подстрокам**

```sql
select ename, job
from emp
order bt substr(job, length(job) - 1)
```

**Обработка NULL**

[//]: # (Все значения не-NULL столбца COMM  сортируются по возрастанию все значения null размещаются в начале списка)
```sql
select ename, sal, comm
    from (
        select enamem, sal, comm
            case when comm is null then 0 else 1 end
    as is_null
    from emp
    ) x
order by is_null desc, comm
```

[//]: # (Все значения не-NULL столбца COMM  сортируются по возрастанию все значения null размещаются в конце списка)
```sql
select ename, sal, comm
    from emp
order by comm nulls last
```

[//]: # (Все значения не-NULL столбца COMM  сортируются по убыванию все значения null размещаются в начале списка)
```sql
select ename, sal, comm
    from emp
order by comm desc nulls first
```

**Сортировка по ключу зависящему от данных**

```sql
select ename, sal, job, comm
from emp
order by case when job = 'SALESMAN' the comm else sal end
```

OR

```sql
select ename, sal, job, comm,
 case when job = 'SALESMAN' the comm else sal end as ordered
 from emp
order by 5
```

