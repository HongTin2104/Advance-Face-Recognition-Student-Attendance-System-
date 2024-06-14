/*
   Tuesday, June 4, 20247:37:57 AM
   User: 
   Server: DESKTOP-NJ3K8EH\SQLEXPRESS
   Database: Face_Recognition 
   Application: 
*/

/* To prevent any potential data loss issues, you should review this script in detail before running it outside the context of the database designer.*/
BEGIN TRANSACTION
SET QUOTED_IDENTIFIER ON
SET ARITHABORT ON
SET NUMERIC_ROUNDABORT OFF
SET CONCAT_NULL_YIELDS_NULL ON
SET ANSI_NULLS ON
SET ANSI_PADDING ON
SET ANSI_WARNINGS ON
COMMIT
BEGIN TRANSACTION
GO
CREATE TABLE dbo.Students
	(
	Department nvarchar(45) NULL,
	Year nvarchar(45) NULL,
	Semester nvarchar(45) NULL,
	Student_ID int NOT NULL,
	Name nvarchar(45) NULL,
	Class nvarchar(45) NULL,
	Gender nvarchar(45) NULL,
	DoB nvarchar(45) NULL,
	Email nvarchar(45) NULL,
	Phone nvarchar(45) NULL,
	Address nvarchar(45) NULL,
	Teacher nvarchar(45) NULL,
	PhotoSample nvarchar(45) NULL,
	)  ON [PRIMARY]
GO
ALTER TABLE dbo.Students ADD CONSTRAINT
	PK_Students PRIMARY KEY CLUSTERED 
	(
	Student_ID
	) WITH( STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

GO
ALTER TABLE dbo.Students SET (LOCK_ESCALATION = TABLE)
GO
COMMIT
select Has_Perms_By_Name(N'dbo.Students', 'Object', 'ALTER') as ALT_Per, Has_Perms_By_Name(N'dbo.Students', 'Object', 'VIEW DEFINITION') as View_def_Per, Has_Perms_By_Name(N'dbo.Students', 'Object', 'CONTROL') as Contr_Per 
