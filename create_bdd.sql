-- --------------------------------------------------------
-- Hôte :                        127.0.0.1
-- Version du serveur:           10.5.8-MariaDB - mariadb.org binary distribution
-- SE du serveur:                Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Listage de la structure de la base pour supervision
CREATE DATABASE IF NOT EXISTS `supervision` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `supervision`;

-- Listage de la structure de la table supervision. cpu_usage
CREATE TABLE IF NOT EXISTS `cpu_usage` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `cpu_percent` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=465 DEFAULT CHARSET=latin1;

-- Listage de la structure de la table supervision. disk_usage_c
CREATE TABLE IF NOT EXISTS `disk_usage_c` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `total` bigint(20) DEFAULT NULL,
  `used` bigint(20) DEFAULT NULL,
  `free` bigint(20) DEFAULT NULL,
  `percent` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=428 DEFAULT CHARSET=latin1;

-- Listage de la structure de la table supervision. disk_usage_d
CREATE TABLE IF NOT EXISTS `disk_usage_d` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `total` bigint(20) DEFAULT NULL,
  `used` bigint(20) DEFAULT NULL,
  `free` bigint(20) DEFAULT NULL,
  `percent` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=423 DEFAULT CHARSET=latin1;

-- Listage de la structure de la table supervision. memory
CREATE TABLE IF NOT EXISTS `memory` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `total` bigint(20) DEFAULT NULL,
  `available` bigint(20) DEFAULT NULL,
  `percent` bigint(20) DEFAULT NULL,
  `used` bigint(20) DEFAULT NULL,
  `free` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=430 DEFAULT CHARSET=latin1;

-- Listage de la structure de la table supervision. net_io_counter
CREATE TABLE IF NOT EXISTS `net_io_counter` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `name` varchar(255) NOT NULL,
  `bytes_sent` bigint(20) DEFAULT NULL,
  `bytes_recv` bigint(20) DEFAULT NULL,
  `packets_sent` bigint(20) DEFAULT NULL,
  `packets_recv` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3952 DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
