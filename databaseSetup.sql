DROP TABLE questions;
DROP TABLE answers;
DROP TABLE questionsMissed;
DROP TABLE highscores;

CREATE TABLE questions(qid integer primary key, question char(75), difficulty integer);
CREATE TABLE answers(aid integer primary key, qid integer, answer char(50));
CREATE TABLE questionsMissed(qid integer, aid integer);
CREATE TABLE highscores(scores integer, difficulty integer);



INSERT INTO questions VALUES(1, "contains a", 1);
INSERT INTO answers VALUES(1, 1, "a");
INSERT INTO questions VALUES(2, "contains ing", 1);
INSERT INTO answers VALUES(2, 2, "ing");
INSERT INTO questions VALUES(3, "ends with s", 1);
INSERT INTO answers VALUES(3,3,"s$");
INSERT INTO questions VALUES(4, "starts with q", 1);
INSERT INTO answers VALUES(4,4,"^q");
INSERT INTO questions VALUES(5, "starts with t,u or v", 1);
INSERT INTO answers VALUES(5,5, "^[tuv]");
INSERT INTO questions VALUES(6, "any character (almost)", 1);
INSERT INTO answers VALUES(6,6,".");
INSERT INTO questions VALUES(7, "match gray or grey", 1);
INSERT INTO answers VALUES(7,7,"gr[ae]y");
INSERT INTO questions VALUES(8, "contains a number", 1);
INSERT INTO answers VALUES(8,8, "[0-9]");
INSERT INTO questions VALUES(9, "blank line", 1);
INSERT INTO answers VALUES(9,9,"^$");
INSERT INTO questions VALUES(10,"ends with a vowel", 1);
INSERT INTO answers VALUES(10,10,"[aeiou]$");
INSERT INTO questions VALUES(11, "starts with a consonant", 2);
INSERT INTO answers VALUES(11, 11, "^[a-z-[aeiou]]");
INSERT INTO questions VALUES(12, "contains .", 2);
INSERT INTO answers VALUES(12, 12, "\.");
INSERT INTO questions VALUES(13, "word break", 2);
INSERT INTO answers VALUES(13, 13, "\b");
INSERT INTO questions VALUES(14, "contains the word 'and'", 2);
INSERT INTO answers VALUES(14, 14, "[\b]and[\b]");
INSERT INTO questions VALUES(15, "contains only capital letters", 2);
INSERT INTO answers VALUES(15, 15, "^[A-Z]*$");
INSERT INTO questions VALUES(16, "first three characters are numbers", 2);
INSERT INTO answers VALUES(16, 16, "^[0-9]{3}");
INSERT INTO questions VALUES(17, "doesn't start with a", 2);
INSERT INTO answers VALUES(17, 17, "^[^a]");
INSERT INTO questions VALUES(18, "contains double letters", 2);
INSERT INTO answers VALUES(18, 18, "([a-zA-Z])\1");
INSERT INTO questions VALUES(19, "number between 1000 and 9999", 2);
INSERT INTO answers VALUES(19, 19, "\b[1-9][0-9]{3}\b");
INSERT INTO questions VALUES(20, "Check beginning of file", 1);
INSERT INTO answers VALUES(20,20, "^");
INSERT INTO questions VALUES(21, "Check end of file", 1);
INSERT INTO answers VALUES(21, 21, "$");
INSERT INTO questions VALUES(22, "Check if p is at beginning of file",1);
INSERT INTO answers VALUES(22,22,"^[p]");
INSERT INTO questions VALUES(23, "Check if word has a space",1);
INSERT INTO answers VALUES(23,23,"\s");
INSERT INTO questions VALUES(24, "Check if word has a tab",1);
INSERT INTO answers VALUES(24, 24, "\t");
INSERT INTO questions VALUES(25, "Match numbers",1);
INSERT INTO answers VALUES(25, 25, "[0-9]");
INSERT INTO questions VALUES(26,"Check if line does not end with a number",1);
INSERT INTO answers VALUES(26,26,"[^0-9]$");
INSERT INTO questions VALUES(27, "Match lowercase letter or number",1);
INSERT INTO answers VALUES(27,27,"[a-z0-9]");
INSERT INTO questions VALUES(28, "Match capital letter or number",1);
INSERT INTO answers VALUES(28,28,"[A-Z0-9]");
INSERT INTO questions VALUES(29, "Look for uppercase, then lower case letters", 3);
INSERT INTO answers VALUES(29,29,"^[A-Z]([a-z][A-Z]?)+$");
INSERT INTO questions VALUES(30, "Match a username that has letters and numbers, up to 16 characters", 3);
INSERT INTO answers VALUES(30,30,"^[a-z0-9]{0-16}$");
INSERT INTO questions VALUES(31, "Match a zip code", 3);
INSERT INTO answers VALUES(31,31,"\b\d{5}");




