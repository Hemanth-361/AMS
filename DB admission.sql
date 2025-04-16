CREATE DATABASE  IF NOT EXISTS `admission` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `admission`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: admission
-- ------------------------------------------------------
-- Server version	8.0.37

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admission`
--

DROP TABLE IF EXISTS `admission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admission` (
  `Name` varchar(50) DEFAULT NULL,
  `Category` varchar(45) DEFAULT NULL,
  `caste` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `Reg` varchar(45) NOT NULL,
  `Language` varchar(45) DEFAULT NULL,
  `Combination` varchar(45) DEFAULT NULL,
  `DOA` varchar(45) DEFAULT NULL,
  `Fee` varchar(45) DEFAULT NULL,
  `Fine_Amount_if_Any` varchar(45) DEFAULT NULL,
  `Remarks` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Reg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admission`
--

LOCK TABLES `admission` WRITE;
/*!40000 ALTER TABLE `admission` DISABLE KEYS */;
INSERT INTO `admission` VALUES ('itachi','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0030','K/E','BCA','27/04/2005','2007','NA','online'),('itachI 3','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0032','K/E','BCA','27/04/2005','2007','NA','online'),('HIEMANTH','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0033','K/E','BCA','27/04/2005','2007','NA','online'),('HIEMANTH  GH','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0034','K/E','BCA','27/04/2005','2007','NA','online'),('MAYUR','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0035','K/E','BCA','27/04/2005','2007','NA','online'),('MAYUR','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0036','K/E','BCA','27/04/2005','2007','NA','online'),('MAYUR','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0038','K/E','BCA','27/04/2005','2007','NA','online'),('MAYUR','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0039','K/E','BCA','27/04/2005','2007','NA','online'),('MAYUR','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0041','K/E','BCA','27/04/2005','2007','NA','online'),('MAYUR','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0042','K/E','BCA','27/04/2005','2007','NA','online'),('MAYUR','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0043','K/E','BCA','27/04/2005','2007','NA','online'),('KIRAN','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0044','K/E','BCA','27/04/2005','2007','NA','online'),('ZAID','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0045','K/E','BCA','27/04/2005','2007','NA','online'),('SHABAZ','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0046','K/E','BCA','27/04/2005','2007','NA','online'),('PRIYANKA','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0047','K/E','BCA','27/04/2005','2007','NA','online'),('KAVITHA','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0048','K/E','BCA','27/04/2005','2007','NA','online'),('KAVITHA','Category II(A)','EDIGA','2nd','2nd_sem','U06GO21S0049','K/E','BCA','27/04/2005','2007','NA','online');
/*!40000 ALTER TABLE `admission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-08-18 22:41:34
