-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- Host: w.rdc.sae.sina.com.cn:3307
-- Generation Time: Nov 25, 2015 at 01:35 AM
-- Server version: 5.5.23
-- PHP Version: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `app_agathehello`
--

-- --------------------------------------------------------

--
-- Table structure for table `menu0`
--

CREATE TABLE IF NOT EXISTS `menu0` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `openid` varchar(255) NOT NULL,
  `menu` varchar(3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `menu0`
--

INSERT INTO `menu0` (`id`, `openid`, `menu`) VALUES
(6, 'oFj6OwoJ2ZnjQlI6PjKN_V_emXYU', 'rea');
