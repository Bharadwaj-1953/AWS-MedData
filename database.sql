/*
SQLyog Enterprise - MySQL GUI v6.56
MySQL - 11.3.0-MariaDB : Database - multisource
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`multisource` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `multisource`;

/*Table structure for table `addoctors` */

DROP TABLE IF EXISTS `addoctors`;

CREATE TABLE `addoctors` (
  `int` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `age` int(100) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`int`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `addoctors` */

insert  into `addoctors`(`int`,`name`,`age`,`role`) values (1,'preeti',25,'doctor');

/*Table structure for table `addrequesttodoctor` */

DROP TABLE IF EXISTS `addrequesttodoctor`;

CREATE TABLE `addrequesttodoctor` (
  `sno` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `disease` varchar(100) DEFAULT NULL,
  `patientid` varchar(100) DEFAULT NULL,
  `doctorsname` varchar(100) DEFAULT NULL,
  `doctorid` varchar(50) DEFAULT NULL,
  `appointmentdate` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `doctorname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `addrequesttodoctor` */

insert  into `addrequesttodoctor`(`sno`,`name`,`age`,`disease`,`patientid`,`doctorsname`,`doctorid`,`appointmentdate`,`status`,`doctorname`) values (1,'nakku','28','fever','1','preeti','1','2023-11-18','accepted','preeti');

/*Table structure for table `adpatients` */

DROP TABLE IF EXISTS `adpatients`;

CREATE TABLE `adpatients` (
  `sno` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `age` int(100) DEFAULT NULL,
  `disease` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `adpatients` */

insert  into `adpatients`(`sno`,`name`,`age`,`disease`) values (1,'nakku',28,'fever');

/*Table structure for table `doctor` */

DROP TABLE IF EXISTS `doctor`;

CREATE TABLE `doctor` (
  `sno` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `cpwd` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `role` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `doctor` */

insert  into `doctor`(`sno`,`name`,`email`,`age`,`pwd`,`cpwd`,`gender`,`mobile`,`role`) values (1,'preeti','preeti@gmail.com','25','1234','1234','Female','06589745632','doctor');

/*Table structure for table `filesupload` */

DROP TABLE IF EXISTS `filesupload`;

CREATE TABLE `filesupload` (
  `sno` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `age` varchar(200) DEFAULT NULL,
  `disease` varchar(200) DEFAULT NULL,
  `doctorsname` varchar(200) DEFAULT NULL,
  `fname` varchar(200) DEFAULT NULL,
  `files` longblob DEFAULT NULL,
  `requeststofiles` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `filesupload` */

insert  into `filesupload`(`sno`,`name`,`age`,`disease`,`doctorsname`,`fname`,`files`,`requeststofiles`) values (1,'nakku','28','fever','preeti','file','îz≤KiΩiˇEåQÄ0G\'◊`çò!/ÂºbG-=”Ÿ—“É19Ö.˝\"U’©5$	≥Ü@”Ócm‹i','pending');

/*Table structure for table `patient` */

DROP TABLE IF EXISTS `patient`;

CREATE TABLE `patient` (
  `sno` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `age` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `cpwd` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `mobile` varchar(100) DEFAULT NULL,
  `disease` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `patient` */

insert  into `patient`(`sno`,`name`,`email`,`age`,`pwd`,`cpwd`,`gender`,`mobile`,`disease`) values (1,'nakku','nakku@gmail.com','28','1234','1234','Female','09685745892','fever');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
