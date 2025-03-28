#
with
file as (select id, name, date_of_birth, salary, department_id
            from <file> --means data exported from the file
         ),
result as (--depending on what really mean column 'name' in the file, is it employee or department name, because there is not mentioned that file separate name columns for employee and departments
            SELECT emp_id, full_name, dob, salary, department_id
            --SELECT emp_id, dept_name, dob, salary, department_id
            FROM employees e
            left join departments d
            on department_id=dept_id
            )
select * from (
(select * from result
except
select * from file)
union all
(select * from file
except
select * from result)
) t
order by 1
;