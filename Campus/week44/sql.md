
## 0. What is SQL? 

SQL = **Structured Query Language**
Used to **communicate with databases**: read, insert, update, and delete data.

Common databases: MySQL, PostgreSQL, SQL Server, SQLite.

---

## 1. Basic Table Example 

Example table: `students`

| id | name  | age | grade |
| -- | ----- | --- | ----- |
| 1  | Alice | 17  | 91    |
| 2  | Bob   | 18  | 85    |
| 3  | Chloe | 17  | 88    |

---

## 2. SELECT – Reading Data 

```sql
SELECT * FROM students;
```

Select specific columns:

```sql
SELECT name, grade FROM students;
```

Filtering:

```sql
SELECT * FROM students
WHERE grade > 90;
```

Sorting:

```sql
SELECT * FROM students
ORDER BY grade DESC;
```

Limiting results:

```sql
SELECT * FROM students
LIMIT 5;
```

---

## 3. INSERT – Adding Data

```sql
INSERT INTO students (name, age, grade)
VALUES ('David', 18, 92);
```

---

## 4. UPDATE – Changing Data

```sql
UPDATE students
SET grade = 95
WHERE name = 'Bob';
```

 **Always!!** use `WHERE` — otherwise, every row is updated.

---

## 5. DELETE – Removing Data

```sql
DELETE FROM students
WHERE id = 2;
```

Again: **never** forget `WHERE`.

---

## 6. Filtering  

### AND / OR

```sql
SELECT * FROM students
WHERE grade > 80 AND age = 17;
```

### LIKE (partial match)

```sql
SELECT * FROM students
WHERE name LIKE 'A%';  -- starts with A
```

### IN

```sql
SELECT * FROM students
WHERE age IN (17, 18);
```

---

## 7. Aggregation 

Built-in functions: `AVG`, `MIN`, `MAX`, `COUNT`, `SUM`

```sql
SELECT AVG(grade) FROM students;
SELECT MAX(grade) FROM students;
SELECT COUNT(*) FROM students;
```

Grouped aggregation:

```sql
SELECT age, AVG(grade)
FROM students
GROUP BY age;
```

---

## 8. JOINs (The Heart of SQL)

### Example tables

**students**

| id | name  |
| -- | ----- |
| 1  | Alice |
| 2  | Bob   |

**courses**

| student_id | course  |
| ---------- | ------- |
| 1          | Math    |
| 1          | Science |
| 2          | English |

### INNER JOIN

Returns matching rows only:

```sql
SELECT students.name, courses.course
FROM students
INNER JOIN courses
    ON students.id = courses.student_id;
```

### LEFT JOIN

Returns *all* students, even without a course:

```sql
SELECT students.name, courses.course
FROM students
LEFT JOIN courses
    ON students.id = courses.student_id;
```

---

## 9. Indexes 

Indexes = speed up lookups (like a book index)

```sql
CREATE INDEX idx_students_name ON students(name);
```

> Use indexes on columns used in WHERE / JOIN
> But don't index everything (slower inserts/updates)

---

## 10. Normalization

**Goal**: reduce duplicated data.

Bad example (duplicate student info):

| name  | course  | grade |
| ----- | ------- | ----- |
| Alice | Math    | 90    |
| Alice | Science | 92    |

Better: separate into `students` + `grades` table → JOIN them.

---

## Quick Recap

| Task        | SQL Command |
| ----------- | ----------- |
| Read data   | `SELECT`    |
| Add data    | `INSERT`    |
| Change data | `UPDATE`    |
| Remove data | `DELETE`    |
| Filter rows | `WHERE`     |
| Combine     | `JOIN`      |
| Summaries   | `GROUP BY`  |

---