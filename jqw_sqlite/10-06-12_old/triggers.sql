-- ********************************************************
-- Global triggers for the logging portion of this database
-- ********************************************************


-- ********************************************************
-- Maintain the timestamps inside the MASTER_LOG table 
-- after changes are made to the table
-- ********************************************************
CREATE TRIGGER UPDATE_MASTER_LOG_TIMESTAMP AFTER UPDATE ON MASTER_LOG
BEGIN
	UPDATE TIMESTAMP_GMT SET TIMESTAMP_GMT = DATETIME('NOW') WHERE
		rowid = new.rowid;
END;


-- ********************************************************
-- Add timestamp to rows added to the MASTER_LOG table.
-- ********************************************************
CREATE TRIGGER INSERT_MASTER_LOG_TIMESTAMP AFTER INSERT ON MASTER_LOG
BEGIN
	UPDATE TIMESTAMP_GMT SET TIMESTAMP_GMT = DATETIME('NOW') WHERE
		rowid = new.rowid;
END;

