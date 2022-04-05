-- MySQL dump 10.13  Distrib 5.1.33, for Win32 (ia32)
--
-- Host: localhost    Database: hms
-- ------------------------------------------------------
-- Server version	5.1.33-community

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
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bill` (
  `bno` int(11) NOT NULL AUTO_INCREMENT,
  `pid` int(11) DEFAULT NULL,
  `ndays` int(11) DEFAULT NULL,
  `charges` int(11) DEFAULT NULL,
  `tamt` int(11) DEFAULT NULL,
  `bdate` date DEFAULT NULL,
  `btime` time DEFAULT NULL,
  PRIMARY KEY (`bno`),
  KEY `pid` (`pid`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`pid`) REFERENCES `patient` (`p_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,1,3,1000,3000,'2022-03-05','02:03:28'),(2,2,3,1000,3000,'2022-03-05','02:03:26');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `doctor` (
  `did` varchar(10) NOT NULL,
  `dname` varchar(30) DEFAULT NULL,
  `speciality` varchar(30) DEFAULT NULL,
  `day_available` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES ('D01','Dr. Mahesh Shah','Cardiologist','MON-WED-FRI'),('D02','Dr. Rajesh Sharma','Neurogist','TUES-FRI-SAT'),('D03','Dr. Anubhav Sing','Dentist','WED-SAT-SUN'),('D04','Dr. Harsh Gujral','Gynaecologist','MON-TUE-SAT'),('D05','Dr. Aakash Gupta','Paediatrician','MON-FRI-SUN');
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `User` varchar(10) DEFAULT NULL,
  `password` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('harshb','hbhattad123'),('kunj','kc123'),('daksh','dj123'),('pranesh','pk123');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `patient` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `P_Name` varchar(30) DEFAULT NULL,
  `P_Age` int(11) DEFAULT NULL,
  `P_Gender` varchar(15) DEFAULT NULL,
  `p_contact_no` bigint(20) DEFAULT NULL,
  `P_Disease` varchar(50) DEFAULT NULL,
  `P_Status` varchar(20) DEFAULT NULL,
  `Consultant_Doc` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  KEY `Consultant_Doc` (`Consultant_Doc`),
  CONSTRAINT `patient_ibfk_1` FOREIGN KEY (`Consultant_Doc`) REFERENCES `doctor` (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'Ansh',15,'Male',9876543210,'Tooth Decay','no','D03'),(2,'Angel',19,'Female',8765432190,'Coronary artery','yes','D01'),(3,'Patrick',19,'Male',8767876546,'Epilepsy','no','D02'),(4,'Robert',34,'Male',8889995556,'Dysmenorrhea','no','D04'),(5,'Aryana',28,'Female',6668885899,'pneumonia','no','D05');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-08 19:56:57
