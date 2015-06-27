CREATE DATABASE LightHouse;

CREATE TABLE Questions(
    q_id INT PRIMARY KEY AUTO_INCREMENT, 
    q_question varchar(512) NOT NULL, 
    q_ref_id varchar(50) NOT NULL, 
    q_user_id varchar(50) NOT NULL, 
    q_votes INT, 
    q_state INT);

INSERT INTO Questions(q_question, q_ref_id, q_user_id, q_votes, q_state) VALUES ("How do you solve question number 5?", "2342", "234234234", 1, 0);
INSERT INTO Questions(q_question, q_ref_id, q_user_id, q_votes, q_state) VALUES ("How do you solve question number 7?", "2343", "234234234", 1, 0);
INSERT INTO Questions(q_question, q_ref_id, q_user_id, q_votes, q_state) VALUES ("How do you solve question number 8?", "2342", "234234234", 1, 0);


CREATE TABLE Answers(
    a_id INT PRIMARY KEY AUTO_INCREMENT, 
    a_answer varchar(512) NOT NULL, 
    q_id INT, 
    a_user_id varchar(50) NOT NULL, 
    a_votes INT, a_state INT, 
    FOREIGN KEY (q_id) REFERENCES Questions(q_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE);
 
INSERT INTO Answers(a_answer, q_id, a_user_id, a_votes, a_state) VALUES ("Look at the video below for the hint", 0, "234234234", 0, 0);
INSERT INTO Answers(a_answer, q_id, a_user_id, a_votes, a_state) VALUES ("Look at the doc below for the hint", 1, "234234234", 0, 0);
INSERT INTO Answers(a_answer, q_id, a_user_id, a_votes, a_state) VALUES ("Look at the doc below for the hint", 2, "234234234", 0, 0);
