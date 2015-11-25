-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- Host: w.rdc.sae.sina.com.cn:3307
-- Generation Time: Nov 25, 2015 at 01:36 AM
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
-- Table structure for table `diary0`
--

CREATE TABLE IF NOT EXISTS `diary0` (
  `ts` datetime NOT NULL,
  `diary` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `diary0`
--

INSERT INTO `diary0` (`ts`, `diary`) VALUES
('2015-11-14 23:40:56', 'Test. Line Number 0.'),
('2015-11-16 21:47:41', 'Test for record inserting.'),
('2015-11-16 21:48:16', 'the 3rd line.'),
('2015-11-16 21:49:37', 'More tests.'),
('2015-11-16 21:49:57', 'Wow this looks nice.'),
('2015-11-18 09:09:16', 'test'),
('2015-11-18 10:44:37', 'good job'),
('2015-11-18 11:00:16', 'hi'),
('2015-11-18 11:25:40', 'hello from Whale'),
('2015-11-18 11:25:48', 'hello from Whale'),
('2015-11-18 11:35:02', '中文可以吗'),
('2015-11-18 11:35:22', 'no chinese'),
('2015-11-19 14:32:02', '中文输入修复了吗？'),
('2015-11-20 16:29:37', 'sb'),
('2015-11-20 17:57:14', '楼下sb'),
('2015-11-22 01:11:21', 'test'),
('2015-11-25 01:22:50', 'Yoyoyo '),
('2015-11-25 01:24:52', '饿了');
