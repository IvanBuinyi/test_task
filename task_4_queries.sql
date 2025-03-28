
--Query #1
select dept_name
from employees
join departments
on department_id = dept_id
group by  dept_name
having AVG(salary) > 50000
;
--Query #2
select full_name
from (
select full_name, salary,
    AVG(salary) OVER (PARTITION BY department_id) AS AVG_DEP_SALARY,
    COUNT(distinct project_id) OVER (PARTITION BY emp_id) AS CNT_PROJECTS
from employees e
join employee_projects ep
on e.emp_id = ep.emp_id
join projects p
ep.project_id = p.project_id
) t
where 1=1
and salary > AVG_DEP_SALARY
and CNT_PROJECTS > 1
;
--Query #3
select full_name
from (
select full_name, project_name,
    DENSE_RANK() OVER (PARTITION BY e.department_id ORDER BY  coalesce(salary, 0)  desc) as rnk
from employees e
join employee_projects ep
on e.emp_id = ep.emp_id
join projects p
ep.project_id = p.project_id
) t
where rnk = 1
;