create database college;
use college;

create table student(
rollno Int Primary key,
name varchar(50),
marks int,
grade char(1),
city varchar(50)
);

insert into student values
(101, 'Anil', 78, 'C', 'Pune'),
(102, 'Aman', 93, 'A', 'Goa'),
(103, 'Bhumi', 85, 'B', 'Goa'),
(104, 'Chetan', 96, 'A', 'Delhi'),
(105, 'Rohit', 12, 'F', 'Delhi'),
(106, 'Raman', 82, 'B', 'Delhi'),
(107, 'Sid', 72, 'B', 'Pune');

select * from student;

select name from student where city = "Delhi";
select count(*) from student where city = "Delhi";
select * from student order by marks asc;
select * from student where name like "A%";
select * from student where marks between 70 and 80;
SELECT name, marks 
FROM student
WHERE marks = (SELECT MAX(marks) FROM student);

SELECT name, marks
FROM student
ORDER BY marks DESC
LIMIT 3;

select avg(marks) from student;
select  name, rollno,grade,city from student where city = "delhi" or grade = "C";
select avg (marks)  from student where city = "Delhi";

SELECT DISTINCT city,marks,name 
FROM student
WHERE marks > 80;

update student set name = "Shakti" where rollno = 101;
select * from student;

update  student set city = null where name = 'Shakti';
select * from student ;
UPDATE student 
SET city = NULL 
WHERE name = 'Shakti';

SELECT * FROM student;
UPDATE student 
SET city = NULL 
WHERE rollno = 101;
SELECT * FROM student;

alter table student add column age int ;
insert into student (rollno,age) values 
(101,18);
select * from student;
UPDATE student
SET age = 19
WHERE rollno = 105;

select * from student;
CREATE TABLE marks (
    rollno INT,
    marks INT
);

INSERT INTO marks VALUES
(101, 78),
(102, 93),
(103, 85),
(106, 82);
SELECT student.name, marks.marks
FROM student
INNER JOIN marks
ON student.rollno = marks.rollno;
alter table marks add column id int ;

ALTER TABLE marks
ADD CONSTRAINT fk_marks_student
FOREIGN KEY (id)
REFERENCES student(rollno);
 
DESC marks;
ALTER TABLE marks
ADD CONSTRAINT fk_marks_student
FOREIGN KEY (rollno)
REFERENCES student(rollno);
SELECT * FROM marks;