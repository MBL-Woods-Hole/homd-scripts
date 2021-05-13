-- MySQL dump 10.13  Distrib 5.6.17, for osx10.7 (x86_64)
--
-- Host: localhost    Database: annotation
-- ------------------------------------------------------
-- Server version	5.6.17

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
-- Table structure for table `gc_count`
--

DROP TABLE IF EXISTS `gc_count`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gc_count` (
  `gc_count_id` int(6) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `contig` int(6) NOT NULL DEFAULT '0',
  `start` int(11) NOT NULL DEFAULT '0',
  `stop` int(11) NOT NULL DEFAULT '0',
  `gc_percentage` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`gc_count_id`),
  UNIQUE KEY `genome` (`genome`,`annotation`,`contig`,`start`,`stop`,`gc_percentage`),
  KEY `contig` (`contig`),
  KEY `start` (`start`),
  KEY `stop` (`stop`)
) ENGINE=InnoDB AUTO_INCREMENT=53419 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `genome`
--

DROP TABLE IF EXISTS `genome`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `genome` (
  `genome_seq_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `molecule_id` int(11) NOT NULL DEFAULT '0',
  `mol_order` int(11) NOT NULL DEFAULT '0',
  `seq` text NOT NULL,
  PRIMARY KEY (`genome_seq_id`),
  UNIQUE KEY `genome` (`genome`,`annotation`,`molecule_id`,`mol_order`)
) ENGINE=InnoDB AUTO_INCREMENT=40014 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `gff`
--

DROP TABLE IF EXISTS `gff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gff` (
  `gff_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `seqid` varchar(30) NOT NULL DEFAULT '',
  `source` varchar(20) NOT NULL DEFAULT '',
  `type` varchar(20) NOT NULL DEFAULT '',
  `start` int(11) NOT NULL,
  `end` int(11) NOT NULL,
  `score` float NOT NULL,
  `strand` varchar(2) NOT NULL,
  `phase` tinyint(4) NOT NULL,
  `attributes` text NOT NULL,
  PRIMARY KEY (`gff_id`),
  UNIQUE KEY `genome` (`genome`,`annotation`,`seqid`,`source`,`type`,`start`,`end`)
) ENGINE=InnoDB AUTO_INCREMENT=19191 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `molecule`
--

DROP TABLE IF EXISTS `molecule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `molecule` (
  `molecule_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `accession` varchar(50) NOT NULL DEFAULT '',
  `name` varchar(100) NOT NULL DEFAULT '',
  `bps` int(11) NOT NULL DEFAULT '0',
  `GC` float NOT NULL,
  `date` varchar(15) NOT NULL DEFAULT '0000-00-00',
  PRIMARY KEY (`molecule_id`),
  UNIQUE KEY `genome` (`genome`,`annotation`,`accession`,`name`,`bps`,`GC`,`date`)
) ENGINE=InnoDB AUTO_INCREMENT=4869 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ncbi_info`
--

DROP TABLE IF EXISTS `ncbi_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ncbi_info` (
  `ncbi_info_id` int(11) NOT NULL AUTO_INCREMENT,
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
  `sequencing_technology` varchar(50) NOT NULL DEFAULT '',
  `relation_to_type_material` varchar(50) NOT NULL DEFAULT '',
  `refseq_category` varchar(50) NOT NULL DEFAULT '',
  `genbank_assembly_accession` varchar(20) NOT NULL DEFAULT '',
  `refseq_assembly_accession` varchar(20) NOT NULL DEFAULT '',
  `refseq_assembly_and_genbank_assemblies_identical` varchar(10) NOT NULL DEFAULT '',
  PRIMARY KEY (`ncbi_info_id`),
  UNIQUE KEY `seq_id` (`seq_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `orf_sequence`
--

DROP TABLE IF EXISTS `orf_sequence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orf_sequence` (
  `orf_seq_id` int(11) NOT NULL AUTO_INCREMENT,
  `genome` varchar(10) NOT NULL,
  `annotation` varchar(10) NOT NULL,
  `mol_id` int(11) NOT NULL DEFAULT '0',
  `length` int(11) NOT NULL DEFAULT '0',
  `gene` varchar(20) DEFAULT '0',
  `synonym` varchar(20) DEFAULT NULL,
  `PID` varchar(20) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL,
  `COD` varchar(20) DEFAULT NULL,
  `product` tinytext,
  `start` int(11) NOT NULL DEFAULT '0',
  `stop` int(11) NOT NULL DEFAULT '0',
  `seq_na` text,
  `seq_aa` text,
  PRIMARY KEY (`orf_seq_id`),
  UNIQUE KEY `genome` (`genome`,`annotation`,`mol_id`,`length`,`gene`,`synonym`,`PID`,`code`,`COD`),
  KEY `PID` (`PID`),
  KEY `start` (`start`),
  KEY `stop` (`stop`)
) ENGINE=InnoDB AUTO_INCREMENT=7995 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prokka_info`
--

DROP TABLE IF EXISTS `prokka_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prokka_info` (
  `prokka_info_id` int(11) NOT NULL AUTO_INCREMENT,
  `seq_id` varchar(20) NOT NULL,
  `organism` text NOT NULL,
  `contigs` int(11) NOT NULL,
  `bases` int(11) NOT NULL,
  `CDS` int(11) DEFAULT NULL,
  `rRNA` int(11) DEFAULT NULL,
  `repeat_region` int(11) DEFAULT NULL,
  `tmRNA` int(11) DEFAULT NULL,
  `tRNA` int(11) DEFAULT NULL,
  `misc_RNA` int(11) DEFAULT NULL,
  PRIMARY KEY (`prokka_info_id`),
  UNIQUE KEY `seq_id` (`seq_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2121 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13 12:47:39
