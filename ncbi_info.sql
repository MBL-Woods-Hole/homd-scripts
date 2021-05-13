-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: 192.168.1.40    Database: annotation
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ncbi_info`
--

DROP TABLE IF EXISTS `ncbi_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ncbi_info` (
  `ncbi_info_id` int NOT NULL AUTO_INCREMENT,
  `seq_id` varchar(20) NOT NULL,
  `assembly_name` varchar(20) NOT NULL DEFAULT '',
  `organism_name` varchar(50) NOT NULL DEFAULT '',
  `infraspecific_name` varchar(20) NOT NULL DEFAULT '',
  `taxid` varchar(20) NOT NULL DEFAULT '',
  `biosample` varchar(20) NOT NULL DEFAULT '',
  `bioproject` varchar(20) NOT NULL DEFAULT '',
  `submitter` varchar(50) NOT NULL DEFAULT '',
  `date` varchar(20) NOT NULL DEFAULT '',
  `assembly_type` varchar(20) NOT NULL DEFAULT '',
  `release_type` varchar(20) NOT NULL DEFAULT '',
  `assembly_level` varchar(20) NOT NULL DEFAULT '',
  `genome_representation` varchar(20) NOT NULL DEFAULT '',
  `wgs_project` varchar(20) NOT NULL DEFAULT '',
  `assembly_method` varchar(50) NOT NULL DEFAULT '',
  `genome_coverage` varchar(10) NOT NULL DEFAULT '',
  `sequencing_technology` varchar(10) NOT NULL DEFAULT '',
  `relation_to_type_material` varchar(50) NOT NULL DEFAULT '',
  `refseq_category` varchar(50) NOT NULL DEFAULT '',
  `genbank_assembly_accession` varchar(20) NOT NULL DEFAULT '',
  `refseq_assembly_accession` varchar(20) NOT NULL DEFAULT '',
  `refseq_assembly_and_genbank_assemblies_identical` varchar(10) NOT NULL DEFAULT '',
  PRIMARY KEY (`ncbi_info_id`),
  UNIQUE KEY `seq_id` (`seq_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ncbi_info`
--

LOCK TABLES `ncbi_info` WRITE;
/*!40000 ALTER TABLE `ncbi_info` DISABLE KEYS */;
INSERT INTO `ncbi_info` VALUES (4,'SEQF2411','Afip_broo_ATCC_49717','Afipia broomeae ATCC 49717 (a-proteobacteria)','strain=ATCC 49717','883078','SAMN02596753','PRJNA52155','Broad Institute','2013-2-6','n/a','major','Scaffold','full','AGWX01','ALLPATHS v. R39721','110x','Illumina','assembly from type material','Representative Genome','GCA_000314675.2','GCF_000314675.2','yes'),(5,'SEQF3148','ASM671700v1','Bosea vestrisii (a-proteobacteria)','strain=3192','151416','SAMN12025610','PRJNA547149','DOE Joint Genome Institute','2019-07-08','na','major','Contig','full','VFQA01','SPAdes v. 3.13.0','no','254.0x','Illumina','Representative Genome','GCA_006717005.1','GCF_006717005.1','yes');
/*!40000 ALTER TABLE `ncbi_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13 15:36:42
