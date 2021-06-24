CREATE TABLE Admin(
admin_id NUMBER(10) NOT NULL,
admin_name VARCHAR2(30) NOT NULL,
admin_pwd VARCHAR2(20) NOT NULL,
CONSTRAINTS admin_id_PK PRIMARY KEY(admin_id)
);

CREATE TABLE [dbo].[Admin] (
    [admin_id]          INT              IDENTITY (1, 1) NOT NULL,
    [admin_name]        NVARCHAR (30)    NOT NULL,
    [admin_pwd]         NVARCHAR (20)    NOT NULL,
    PRIMARY KEY CLUSTERED ([admin_id] ASC)
);

INSERT INTO Admin VALUES (1, "Admin1", "Admin1");
INSERT INTO Admin VALUES (2, "Admin2", "Admin2");
-----------------------------------------------------------------------------------------------------------------

CREATE TABLE Lecturer(
lect_id NUMBER(10) NOT NULL,
lect_name VARCHAR2(50) NOT NULL,
lect_email VARCHAR2(20),
lect_pwd VARCHAR2(20) NOT NULL,
lecturer_modify_date DATE,
admin_id NUMBER(10) NOT NULL,
CONSTRAINTS lect_id_PK PRIMARY KEY(lect_id),
CONSTRAINTS admin_id_FK FOREIGN KEY(admin_id) REFERENCES Admin(admin_id)
);

CREATE TABLE [dbo].[Lecturer] (
    [lect_id]               INT             IDENTITY (1, 1) NOT NULL,
    [lect_name]             NVARCHAR (50)   NOT NULL,
    [lect_email]            NVARCHAR (20)   ,
    [lect_pwd]              NVARCHAR (20)   NOT NULL,
    [lecturer_modify_date]  TIMESTAMP       NOT NULL,
    [admin_id]              INT             NOT NULL,
    PRIMARY KEY CLUSTERED ([lect_id] ASC),
    CONSTRAINT [admin_id_lect_FK] FOREIGN KEY ([admin_id]) REFERENCES [dbo].[Admin] ([admin_id])
);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE Student(
student_id NUMBER(10) NOT NULL,
student_name VARCHAR2(50) NOT NULL,
student_email VARCHAR2(20),
student_pwd VARCHAR2(20) NOT NULL,
student_modify_date DATE,
admin_id NUMBER(10) NOT NULL,
CONSTRAINTS student_id_PK PRIMARY KEY(student_id),
CONSTRAINTS admin_id_FK FOREIGN KEY(admin_id) REFERENCES Admin(admin_id)
);

CREATE TABLE [dbo].[Student] (
    [student_id]            INT             IDENTITY (1, 1) NOT NULL,
    [student_name]          NVARCHAR (50)   NOT NULL,
    [student_email]         NVARCHAR (20)   ,
    [student_pwd]           NVARCHAR (20)   NOT NULL,
    [student_modify_date]   TIMESTAMP       NOT NULL,
    [admin_id]              INT             NOT NULL,
    PRIMARY KEY CLUSTERED ([student_id] ASC),
    CONSTRAINT [admin_id_student_FK] FOREIGN KEY ([admin_id]) REFERENCES [dbo].[Admin] ([admin_id])
);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE Subject(
subject_id NUMBER(10) NOT NULL,
subject_name VARCHAR2(50) NOT NULL,
subject_modify_date DATE,
admin_id NUMBER(10) NOT NULL,
CONSTRAINTS subject_id_PK PRIMARY KEY(subject_id),
CONSTRAINTS admin_id_FK FOREIGN KEY(admin_id) REFERENCES Admin(admin_id)
);

CREATE TABLE [dbo].[Subject] (
    [subject_id]            INT             IDENTITY (1, 1) NOT NULL,
    [subject_name]          NVARCHAR (50)   NOT NULL,
    [subject_modify_date]   TIMESTAMP       NOT NULL,
    [admin_id]              INT             NOT NULL,
    PRIMARY KEY CLUSTERED ([subject_id] ASC),
    CONSTRAINT [admin_id_subject_FK] FOREIGN KEY ([admin_id]) REFERENCES [dbo].[Admin] ([admin_id])
);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE Lecturer_Workload(
workload_id NUMBER(10) NOT NULL,
subject_id NUMBER(10) NOT NULL,
lect_id NUMBER(10) NOT NULL,
CONSTRAINTS workload_id_PK PRIMARY KEY(workload_id),
CONSTRAINTS subject_id_FK FOREIGN KEY(subject_id) REFERENCES Subject(subject_id),
CONSTRAINTS lect_id_FK FOREIGN KEY(lect_id) REFERENCES Lecturer(lect_id)
);

CREATE TABLE [dbo].[Lecturer_Workload] (
    [workload_id]           INT             IDENTITY (1, 1) NOT NULL,
    [subject_id]            INT             NOT NULL,
    [lect_id]               INT             NOT NULL,
    PRIMARY KEY CLUSTERED ([workload_id] ASC),
    CONSTRAINT [subject_id_workload_FK] FOREIGN KEY ([subject_id]) REFERENCES [dbo].[Subject] ([subject_id]),
    CONSTRAINT [lect_id_workload_FK] FOREIGN KEY ([lect_id]) REFERENCES [dbo].[Lecturer] ([lect_id])
);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE Subject_Registered(
subj_reg_id NUMBER(10) NOT NULL,
quizTF_mark NUMBER(3) NOT NULL,
quizObj_mark NUMBER(3) NOT NULL,
workload_id NUMBER(10) NOT NULL,
student_id NUMBER(10) NOT NULL,
CONSTRAINTS subj_reg_id_PK PRIMARY KEY(subj_reg_id)
CONSTRAINTS workload_id_FK FOREIGN KEY(workload_id) REFERENCES Lecturer_Workload(workload_id),
CONSTRAINTS student_id_FK FOREIGN KEY(student_id) REFERENCES Student(student_id)
);

CREATE TABLE [dbo].[Subject_Registered] (
    [subj_reg_id]           INT             IDENTITY (1, 1) NOT NULL,
    [quizTF_mark]           INT             NOT NULL,
    [quizObj_mark]          INT             NOT NULL,
    [workload_id]           INT             NOT NULL,
    [student_id]            INT             NOT NULL,
    PRIMARY KEY CLUSTERED ([subj_reg_id] ASC),
    CONSTRAINT [workload_id_subrej_FK] FOREIGN KEY ([workload_id]) REFERENCES [dbo].[Lecturer_Workload] ([workload_id]),
    CONSTRAINT [student_id_subrej_FK] FOREIGN KEY ([student_id]) REFERENCES [dbo].[Student] ([student_id])
);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE Quiz_TF(
quizTF_id NUMBER(10) NOT NULL,
quizTF_True NUMBER(1) NOT NULL,
quizTF_modify_date DATE,
quizTF_Questions VARCHAR2(60) NOT NULL,
workload_id NUMBER(10) NOT NULL,
CONSTRAINTS quizTF_id_PK PRIMARY KEY(quizTF_id),
CONSTRAINTS workload_id_FK FOREIGN KEY(workload_id) REFERENCES Lecturer_Workload(workload_id)
);

CREATE TABLE [dbo].[Quiz_TF] (
    [quizTF_id]             INT             IDENTITY (1, 1) NOT NULL,
    [quizTF_True]           INT             NOT NULL,
    [quizTF_Questions]      NVARCHAR(60)    NOT NULL,
    [quizTF_modify_date]    TIMESTAMP       NOT NULL,
    [workload_id]           INT             NOT NULL,
    PRIMARY KEY CLUSTERED ([quizTF_id] ASC),
    CONSTRAINT [workload_id_quizTF_FK] FOREIGN KEY ([workload_id]) REFERENCES [dbo].[Lecturer_Workload] ([workload_id]),
);

CREATE TABLE [dbo].[Quiz_TF] (
    [quizTF_id]             INT             IDENTITY (1, 1) NOT NULL,
    [quizTF_True]           INT             NOT NULL,
    [quizTF_Questions]      NVARCHAR(60)    NOT NULL,
    [quizTF_modify_date]    TIMESTAMP       NOT NULL,
    [workload_id]           INT             NOT NULL,
    PRIMARY KEY CLUSTERED ([quizTF_id] ASC),
    CONSTRAINT [workload_id_quizTF_FK] FOREIGN KEY ([workload_id]) REFERENCES [dbo].[Lecturer_Workload] ([workload_id]),
);

-----------------------------------------------------------------------------------------------------------------

CREATE TABLE Quiz_Obj(
quizObj_id NUMBER(10) NOT NULL,
quizObj_Questions VARCHAR2(60) NOT NULL,
quiz_answerA NUMBER(1) NOT NULL,
quiz_answerB NUMBER(1) NOT NULL,
quiz_answerC NUMBER(1) NOT NULL,
quiz_answerD NUMBER(1) NOT NULL,
quiz_correct_ans VARCHAR2(1) NOT NULL,
quizObj_modify_date DATE,
workload_id NUMBER(10) NOT NULL,
CONSTRAINTS quizobj_id_PK PRIMARY KEY(quizObj_id),
CONSTRAINTS workload_id_FK FOREIGN KEY(workload_id) REFERENCES Lecturer_Workload(workload_id)
);

CREATE TABLE [dbo].[Quiz_Obj] (
    [quizObj_id]            INT             IDENTITY (1, 1) NOT NULL,
    [quizObj_Questions]     NVARCHAR(200)   NOT NULL,
    [quiz_answerA]          INT             NOT NULL,
    [quiz_answerB]          INT             NOT NULL,
    [quiz_answerC]          INT             NOT NULL,
    [quiz_answerD]          INT             NOT NULL,
    [quiz_correct_ans]      NVARCHAR(1)     NOT NULL,
    [quizObj_modify_date]   TIMESTAMP       NOT NULL,
    [workload_id]           INT             NOT NULL,    
    PRIMARY KEY CLUSTERED ([quizObj_id] ASC),
    CONSTRAINT [workload_id_quizObj_FK] FOREIGN KEY ([workload_id]) REFERENCES [dbo].[Lecturer_Workload] ([workload_id]),
);

-----------------------------------------------------------------------------------------------------------------

Web App Requirements 

Pages :
    1. Login Page
        - Update PASSWORD
        Requirements
            - Error Message Wrong Username/Password 
            - Error if login without choosing
            - Prompt for Password Update when 1st Time Login

    2. Module for Admin
        - Register Admin
            - Add
            - Update
            - Delete 
        - Register Student
            - Add
            - Update
            - Delete
        - Register Lecturer
            - Add
            - Update
            - Delete
        - Register Subject
            - Add
            - Update
            - Delete
        - Register Workload Lecturer
            - Add
            - Update
            - Delete
        Requirements
            - Register Admin (Check for Deletion)
            - Register Admin (Check for Deletion/Include Modified Who & When/ Auto Assign Password & Email)
            - Register Student (Check for Deletion/Include Modified Who & When/ Auto Assign Password & Email)
            - Register Subject (Check for Deletion/Include Modified Who & When)
            - Assign Workload (No duplication of data)
            - Dynamic Dropdown 
                - Subject
                - Lecturer

    3. Module for Lecturer
        - View QuizTF and QuizObj Results
        - Create/Update/Delete QuizTF
        - Create/Update/Delete QuizObj
        - Create/Upload Tutorial/Assignment/Lab
        - View/Download Tutorial/Assignment/Lab 
        Requirements 
            - Subject List taught for each Lecturer
            - Allow create quiz TF & quiz Obj (Add/Update/Delete)
            - View Result quiz TF & quiz Obj (Add/Update/Delete) (Include Number of Pass or Fail)
            - Lecturer File Upload 
            - Lecturer File Download (No File Deletion)

    4. Module for Student
        - Register Subject 
        - View Registered Subject 
        - Take QuizTF 
        - Take QuizMultipleChoice
        - View/Download Tutorial/Assignment/Lab
        - View/Download Tutorial/Assignment/Lab
        Requirements
            - Show subject list. Cannot Register Twice
            - View Registered Subject and Quiz marks
            - Answer Quiz TF & Calculate marks
            - Answer Quiz Obj & Calculate marks  
            - Retake Quiz if Marks = 0
            - View, Download & Upload Assignment/Tutorial/Lab