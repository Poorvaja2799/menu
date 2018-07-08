-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: 127.0.0.1    Database: project
-- ------------------------------------------------------
-- Server version	8.0.11

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
-- Table structure for table `tbl_role_privileges`
--

DROP TABLE IF EXISTS `tbl_role_privileges`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_role_privileges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_ID` int(11) NOT NULL,
  `role_ID` int(11) NOT NULL,
  `access` bit(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_role_privileges`
--

LOCK TABLES `tbl_role_privileges` WRITE;
/*!40000 ALTER TABLE `tbl_role_privileges` DISABLE KEYS */;
INSERT INTO `tbl_role_privileges` VALUES (1,1,1,''),(2,2,1,''),(3,3,1,''),(4,4,1,''),(5,5,1,''),(6,6,1,''),(7,7,1,''),(8,8,1,''),(9,9,1,''),(10,10,1,''),(11,1,2,''),(12,2,2,''),(13,3,2,''),(14,4,2,''),(15,5,2,''),(16,6,2,'\0'),(17,7,2,'\0'),(18,8,2,''),(19,9,2,'\0'),(20,10,2,'\0'),(23,1,3,''),(24,2,3,''),(25,3,3,''),(26,4,3,''),(27,5,3,''),(28,6,3,''),(29,7,3,''),(30,8,3,'\0'),(31,9,3,''),(32,10,3,'\0');
/*!40000 ALTER TABLE `tbl_role_privileges` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-08 23:15:16
