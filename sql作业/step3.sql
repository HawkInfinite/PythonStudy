-- 3-1.把peoples表中school不是GDUFS的人全部找出来？（包括school为NULL的人）写出MySQL语句。
select * from peoples where school != 'GDUFS' or school is NULL;
-- 3-2.查找计算机系每次考试学生的平均成绩(最终显示学生姓名, 考试名称, 平均分)。
select name,avg(grade) 
from student as T1 
inner join department 
on T1.dept_name = department.dept_name 
inner join exam 
on T1.ID = exam.student_ID
where T1.dept_name = 'computer' 
group by name;
-- 3-3.查找女学霸（考试平均分达到80分或80分以上的女生的姓名, 分数）。
select name,avg(grade)
from student as T1 
inner join department on T1.dept_name = department.dept_name 
inner join exam on T1.ID = exam.student_ID 
where T1.sex = 'f' group by name having avg(grade) >= 80;
select name,grade from student where exam.grade >= 80 and sex = 'f';
-- 3-4.找出人数最少的院系以及其年度预算。
select distinct department.dept_name,budget,count(*)
from department 
inner join student 
on department.dept_name = student.dept_name 
group by student.dept_name 
order by count(*) 
limit 0,1;
-- 3-5.计算机系改名了，改成计算机科学系（comp. sci.），写出mysql语句。
update department set dept_name = 'comp. sci.' where dept_name = 'computer';
-- 3-6.修改每个系的年度预算，给该系的每个学生发2000元奖金。（修改每个系的年度预算为 原预算+该系人数*2000）。
select distinct department.dept_name,count(*),budget 
as t1 
from department 
inner join student 
on department.dept_name = student.dept_name 
group by student.dept_name;
-- update t1 set budget = budget + 2000 * count(*);
-- 3-7.向department表中插入一条数据, dept_name属性的值为avg_budget, building为空, 年度预算为所有院系的年度预算平均值.
insert into department (dept_name, building, budget) values("avg_budget", NULL, 21400.00);
-- 3-8. 删除计算机系中考试成绩平均分低于70的学生.
delete from student where exists
(	select distinct student_ID 
	from exam 
	group by name 
	having avg(grade) < 70);
select distinct name from student inner join exam on student.ID = exam.student_ID group by name having avg(grade) < 70;
-- 3-9.找出所有正在谈恋爱,但是学习成绩不佳(考试平均分低于75)的学生,强制将其情感状态改为单身.
-- select distinct name,avg(grade) 
-- from student 
-- 	inner join exam 
-- 	on student.ID = exam.student_ID 
-- 	where emotion_state = 'loving' 
-- 	group by name 
-- 	having avg(grade) < 75 ;
-- update student set emotion_state = 'single' where exists (select name from exam group by name having avg(grade) < 75);
update student set emotion_state = 'single' where name = '公孙子晨' or name = '尹枫起';
-- 3-10(选做). 对每个学生, 往exam表格中插入名为Avg_Exam的考试, 考试分数为之前学生参加过考试的平均分.
