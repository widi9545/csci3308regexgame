-- MySQL dump 10.13  Distrib 5.7.12, for Linux (x86_64)
--
-- Host: localhost    Database: regexMemoryGame
-- ------------------------------------------------------
-- Server version	5.7.12-0ubuntu1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `answers`
--

DROP TABLE IF EXISTS `answers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answers` (
  `aid` int(11) NOT NULL,
  `qid` int(11) DEFAULT NULL,
  `answer` char(50) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answers`
--

LOCK TABLES `answers` WRITE;
/*!40000 ALTER TABLE `answers` DISABLE KEYS */;
INSERT INTO `answers` VALUES (1,1,'a'),(2,2,'ing'),(3,3,'s$'),(4,4,'^q'),(5,5,'^[tuv]'),(6,6,'.'),(7,7,'gr[ae]y'),(8,8,'[0-9]'),(9,9,'^$'),(10,10,'[aeiou]$'),(11,11,'^[a-z-[aeiou]]'),(12,12,'.'),(13,13,''),(14,14,'[]and[]'),(15,15,'^[A-Z]*$'),(16,16,'^[0-9]{3}'),(17,17,'^[^a]'),(18,18,'([a-zA-Z])1'),(19,19,'[1-9][0-9]{3}');
/*!40000 ALTER TABLE `answers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `highscores`
--

DROP TABLE IF EXISTS `highscores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `highscores` (
  `scores` int(11) DEFAULT NULL,
  `difficulty` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `highscores`
--

LOCK TABLES `highscores` WRITE;
/*!40000 ALTER TABLE `highscores` DISABLE KEYS */;
INSERT INTO `highscores` VALUES (100,1),(200,2),(300,1);
/*!40000 ALTER TABLE `highscores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questions` (
  `qid` int(11) NOT NULL,
  `question` char(50) DEFAULT NULL,
  `difficulty` int(11) DEFAULT NULL,
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'contains a',1),(2,'contains ing',1),(3,'ends with s',1),(4,'starts with q',1),(5,'starts with t,u or v',1),(6,'any character (almost)',1),(7,'match gray or grey',1),(8,'contains a number',1),(9,'blank line',1),(10,'ends with a vowel',1),(11,'starts with a consonant',2),(12,'contains .',2),(13,'word break',2),(14,'contains the word \'and\'',2),(15,'contains only capital letters',2),(16,'first three characters are numbers',2),(17,'doesn\'t start with a',2),(18,'contains double letters',2),(19,'number between 1000 and 9999',2);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionsMissed`
--

DROP TABLE IF EXISTS `questionsMissed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `questionsMissed` (
  `qid` int(11) DEFAULT NULL,
  `aid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionsMissed`
--

LOCK TABLES `questionsMissed` WRITE;
/*!40000 ALTER TABLE `questionsMissed` DISABLE KEYS */;
INSERT INTO `questionsMissed` VALUES (1,1),(2,2);
/*!40000 ALTER TABLE `questionsMissed` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-16 15:47:10
