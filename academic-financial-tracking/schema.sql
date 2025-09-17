CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT,
    year INT
);

CREATE TABLE Scholarships (
    scholarship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    amount REAL
);

CREATE TABLE Loans (
    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INT,
    amount REAL,
    status TEXT,
    FOREIGN KEY(student_id) REFERENCES Students(student_id)
);

-- Indexes for optimization
CREATE INDEX idx_student_name ON Students(name);
CREATE INDEX idx_loan_status ON Loans(status);
