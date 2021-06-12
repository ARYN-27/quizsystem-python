DROP TABLE IF EXISTS Admin;
DROP TABLE IF EXISTS Lecturer;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Subject;
DROP TABLE IF EXISTS Lecturer_Workload;
DROP TABLE IF EXISTS Subject_Registered;
DROP TABLE IF EXISTS Quiz_TF;
DROP TABLE IF EXISTS Quiz_Obj;

CREATE TABLE Admin(
    admin_id INTEGER PRIMARY KEY NOT NULL,
    admin_name TEXT(30) NOT NULL,
    admin_pwd TEXT(20) NOT NULL
);

CREATE TABLE Lecturer(
    lect_id INTEGER PRIMARY KEY NOT NULL,
    lect_name TEXT(50) NOT NULL,
    lect_email TEXT(20),
    lect_pwd TEXT(20) NOT NULL,
    lecturer_modify_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    admin_id INTEGER NOT NULL,
    FOREIGN KEY(admin_id) REFERENCES Admin(admin_id)
);
CREATE TABLE Student(
    student_id INTEGER PRIMARY KEY NOT NULL,
    student_name TEXT(50) NOT NULL,
    student_email TEXT(20),
    student_pwd TEXT(20) NOT NULL,
    student_modify_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    admin_id INTEGER NOT NULL,
    FOREIGN KEY(admin_id) REFERENCES Admin(admin_id)
);
CREATE TABLE Subject(
    subject_id INTEGER PRIMARY KEY NOT NULL,
    subject_name TEXT(50) NOT NULL,
    subject_modify_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    admin_id INTEGER NOT NULL,
    FOREIGN KEY(admin_id) REFERENCES Admin(admin_id)
);
CREATE TABLE Lecturer_Workload(
    workload_id INTEGER PRIMARY KEY NOT NULL,
    subject_id INTEGER NOT NULL,
    lect_id INTEGER NOT NULL,
    FOREIGN KEY(subject_id) REFERENCES Subject(subject_id),
    FOREIGN KEY(lect_id) REFERENCES Lecturer(lect_id)
);
CREATE TABLE Subject_Registered(
    subj_reg_id INTEGER PRIMARY KEY NOT NULL,
    quizTF_mark INTEGER NOT NULL,
    quizObj_mark INTEGER NOT NULL,
    workload_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    FOREIGN KEY(workload_id) REFERENCES Lecturer_Workload(workload_id),
    FOREIGN KEY(student_id) REFERENCES Student(student_id)
);
CREATE TABLE Quiz_TF(
    quizTF_id INTEGER PRIMARY KEY NOT NULL,
    quizTF_True INTEGER NOT NULL,
    quizTF_modify_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    quizTF_Questions TEXT(60) NOT NULL,
    workload_id INTEGER NOT NULL,
    FOREIGN KEY(workload_id) REFERENCES Lecturer_Workload(workload_id)
);
CREATE TABLE Quiz_Obj(
    quizObj_id INTEGER PRIMARY KEY NOT NULL,
    quizObj_Questions TEXT(60) NOT NULL,
    quiz_answerA INTEGER,
    quiz_answerB INTEGER,
    quiz_answerC INTEGER,
    quiz_answerD INTEGER,
    quiz_correct_ans TEXT(1) NOT NULL,
    quizObj_modify_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    workload_id INTEGER NOT NULL,
    FOREIGN KEY(workload_id) REFERENCES Lecturer_Workload(workload_id)
);