-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2020 at 12:44 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sih`
--

-- --------------------------------------------------------

--
-- Table structure for table `app_status`
--

CREATE TABLE `app_status` (
  `appid` int(100) NOT NULL,
  `jid` int(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `compid` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `applied_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `test_score` varchar(100) NOT NULL DEFAULT 'Not Attempted',
  `iet` int(10) NOT NULL DEFAULT '0',
  `test_link` varchar(100) DEFAULT NULL,
  `iei` int(10) NOT NULL DEFAULT '0',
  `interview_link` varchar(100) DEFAULT NULL,
  `idate` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `award`
--

CREATE TABLE `award` (
  `srno` int(11) NOT NULL,
  `compid` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `from_org` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `award`
--

INSERT INTO `award` (`srno`, `compid`, `title`, `from_org`, `year`) VALUES
(1, 'john', 'Best Media', 'Zee business', '2020'),
(5, 'Capgemini', 'Best project management', 'CNBC Awards', '1998-2020'),
(6, 'tcs', 'Best Media', 'Zee business', '2020'),
(7, 'tcs', 'Best Infrastructure', 'Infrastructure', '2019');

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `pname` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `phone` int(10) NOT NULL,
  `blogg` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `company_register`
--

CREATE TABLE `company_register` (
  `compid` varchar(100) NOT NULL,
  `compname` varchar(100) NOT NULL,
  `doe` date NOT NULL,
  `compaddress` varchar(100) NOT NULL,
  `compemail` varchar(100) NOT NULL,
  `compurl` varchar(150) NOT NULL,
  `compphone` varchar(100) NOT NULL,
  `compdescription` varchar(1000) NOT NULL,
  `comppassword` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `company_register`
--

INSERT INTO `company_register` (`compid`, `compname`, `doe`, `compaddress`, `compemail`, `compurl`, `compphone`, `compdescription`, `comppassword`) VALUES
('Capgemini', 'CAPGEMINI', '2020-08-13', 'Mumbai', 'maheshmahajan.20998@gmail.com', 'https://www.google.com', '9619880253', 'this is demo hello', '$6$rounds=656000$CeS6Pn0PcnTxoWaF$cSjUhDsWp9TUD1FCLwy86d0Z6TTIK0kZqzgm8YGr9IQuFh2JiUgSHDjokZyB2kLegAbB2zoJlCVOXKbNQ0y.y.'),
('tcs', 'TCS', '2020-08-01', 'Mumbai', 'maheshmahajan.20998@gmail.com', 'https://twitter.com/', '8828382566', 'TCS company here', '$6$rounds=656000$QfLn2iFqO2ku7Z6d$SOMKInEtLMDiEaTF2fIo5F1FJzOnpgZTMc7JlSyzVwsFXZIC.oVMOUKwDESyMBZe.f0HmUsDQ2LkOGeLUAihV0');

-- --------------------------------------------------------

--
-- Table structure for table `compfow`
--

CREATE TABLE `compfow` (
  `srno` int(11) NOT NULL,
  `compid` varchar(100) NOT NULL,
  `fow` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `compfow`
--

INSERT INTO `compfow` (`srno`, `compid`, `fow`) VALUES
(13, 'tcs', ' Business'),
(14, 'tcs', 'Marketing'),
(15, 'tcs', 'Transport and logistics');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` int(10) NOT NULL,
  `msg_subject` varchar(100) NOT NULL,
  `message` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `edu`
--

CREATE TABLE `edu` (
  `srno` int(11) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `degree` varchar(100) NOT NULL,
  `institute` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `edu`
--

INSERT INTO `edu` (`srno`, `uname`, `title`, `degree`, `institute`, `year`) VALUES
(11, 'john', 'UG', 'BE', 'PCE', '2020'),
(12, 'john', 'U', 'BE', 'PIpppT', '2020'),
(13, 'john', 'UGc', 'BE in it', 'PCo', '2020');

-- --------------------------------------------------------

--
-- Table structure for table `fow`
--

CREATE TABLE `fow` (
  `srno` int(11) NOT NULL,
  `field` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fow`
--

INSERT INTO `fow` (`srno`, `field`) VALUES
(-1, 'Accountancy'),
(2, 'banking and finance'),
(3, ' Business'),
(4, 'consulting and management\r\n'),
(6, 'Charity and voluntary work'),
(7, 'Creative arts and design'),
(8, 'Energy and utilities'),
(9, 'Engineering and manufacturing'),
(10, 'Environment and agriculture'),
(11, 'Healthcare'),
(12, 'Hospitality and events management'),
(13, 'Information technology'),
(14, 'Law'),
(15, 'Law enforcement and security'),
(16, 'Leisure'),
(17, 'sport and tourism'),
(18, 'Marketing'),
(19, 'advertising and PR'),
(20, 'Media and internet'),
(21, 'Property and construction'),
(22, 'Public services and administration'),
(23, 'Recruitment and HR'),
(24, 'Retail'),
(25, 'Sales\r\n'),
(26, 'Science and pharmaceuticals'),
(27, 'Social care'),
(28, 'Teacher training and education'),
(29, 'Transport and logistics');

-- --------------------------------------------------------

--
-- Table structure for table `geoloc`
--

CREATE TABLE `geoloc` (
  `srno` int(11) NOT NULL,
  `compid` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `geoloc`
--

INSERT INTO `geoloc` (`srno`, `compid`, `city`, `country`) VALUES
(1, 'capgemini', 'New York', 'United States'),
(2, 'capgemini', 'Mumbai', 'India'),
(3, 'tcs', 'Navi Mumbai', 'India'),
(4, 'tcs', 'Pune', 'India'),
(5, 'tcs', 'banglore', 'india');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `jid` int(11) NOT NULL,
  `jtitle` varchar(50) DEFAULT NULL,
  `jdescription` varchar(512) DEFAULT NULL,
  `jagelimit` int(11) DEFAULT NULL,
  `compid` varchar(100) DEFAULT NULL,
  `jsalary` float DEFAULT NULL,
  `jvacancies` int(11) DEFAULT NULL,
  `jlocation` varchar(50) DEFAULT NULL,
  `jpostd` datetime DEFAULT CURRENT_TIMESTAMP,
  `jlastd` datetime DEFAULT NULL,
  `jtype` varchar(32) DEFAULT NULL,
  `jexperience` float DEFAULT NULL,
  `s1` varchar(64) DEFAULT NULL,
  `s2` varchar(64) DEFAULT NULL,
  `s3` varchar(64) DEFAULT NULL,
  `s4` varchar(64) DEFAULT NULL,
  `s5` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`jid`, `jtitle`, `jdescription`, `jagelimit`, `compid`, `jsalary`, `jvacancies`, `jlocation`, `jpostd`, `jlastd`, `jtype`, `jexperience`, `s1`, `s2`, `s3`, `s4`, `s5`) VALUES
(100010, 'Python dev', 'Just develop cool apps', 50, 'tcs', 35000, 3, 'Mumbai', '2020-08-03 14:55:13', '2020-08-15 00:00:00', 'Part Time', 6, 'Python', 'Critical Thinking', 'Java', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `keypeep`
--

CREATE TABLE `keypeep` (
  `srno` int(11) NOT NULL,
  `compid` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `keypeep`
--

INSERT INTO `keypeep` (`srno`, `compid`, `name`, `designation`) VALUES
(1, 'capgemini', 'Ajju Paleri', 'CEO'),
(4, 'capgemini', 'Sundar Pichai', 'COO'),
(5, 'Capgemini', 'Ramakant', 'pandu'),
(6, 'Capgemini', 'hi', 'hi'),
(7, 'tcs', 'Sundar Pichai', 'CEO'),
(8, 'tcs', 'Mahesh Mahajan', 'COO');

-- --------------------------------------------------------

--
-- Table structure for table `link`
--

CREATE TABLE `link` (
  `srno` int(11) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `link` varchar(100) NOT NULL,
  `value` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `link`
--

INSERT INTO `link` (`srno`, `uname`, `link`, `value`) VALUES
(1, 'john', 'Preetam ba', 'www.Linkedin.com');

-- --------------------------------------------------------

--
-- Table structure for table `notification-candidate`
--

CREATE TABLE `notification-candidate` (
  `nid` int(11) NOT NULL,
  `description` varchar(500) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `viewed` int(5) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `appid` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `notification-candidate`
--

INSERT INTO `notification-candidate` (`nid`, `description`, `timestamp`, `viewed`, `uname`, `appid`) VALUES
(1, 'this is test notification', '2020-07-31 18:56:41', 1, 'john', '123213'),
(2, 'this is test notification 2', '2020-07-31 18:56:41', 1, 'john', '12311'),
(3, 'Your Application for Python dev post have been successfully submitted', '2020-08-03 03:45:55', 1, 'john', '15'),
(4, 'TCS has responded to your Application for Python dev', '2020-08-03 03:46:54', 1, 'john', '15'),
(5, 'TCS has responded to your Application for Python dev', '2020-08-03 04:03:12', 1, 'john', '15'),
(6, 'Your Application for Python dev post have been successfully submitted', '2020-08-03 04:06:25', 1, 'john', '16'),
(7, 'TCS has responded to your Application for Python dev', '2020-08-03 04:07:18', 1, 'john', '16'),
(8, 'Test for Python dev have sucessfully completed, sent for review to concerned department', '2020-08-03 04:08:06', 1, 'john', '16'),
(9, 'Congratualations you have cleared the test for Python dev post, an interview have been scheduled', '2020-08-03 04:10:59', 1, 'john', '16'),
(10, 'TCS have rejected to your Application for Python dev', '2020-08-03 04:11:55', 1, 'john', '16'),
(11, 'Congratualations you have been selected for Python dev post.', '2020-08-03 04:12:32', 1, 'john', '16'),
(12, 'Your Application for Python dev post have been successfully submitted', '2020-08-03 06:10:23', 1, 'john', '17'),
(13, 'Your Application for Python dev post have been successfully submitted', '2020-08-03 06:11:27', 1, 'john', '18'),
(14, 'TCS has responded to your Application for Python dev', '2020-08-03 06:12:03', 1, 'john', '18'),
(15, 'Test for Python dev have sucessfully completed, sent for review to concerned department', '2020-08-03 06:12:54', 1, 'john', '18'),
(16, 'Congratualations you have cleared the test for Python dev post, an interview have been scheduled', '2020-08-03 06:14:53', 1, 'john', '18'),
(17, 'TCS have rejected to your Application for Python dev', '2020-08-03 06:15:44', 1, 'john', '18'),
(18, 'Your Application for Python dev post have been successfully submitted', '2020-08-03 06:46:20', 1, 'john', '19'),
(19, 'TCS has responded to your Application for Python dev', '2020-08-03 06:46:45', 1, 'john', '19'),
(20, 'Test for Python dev have sucessfully completed, sent for review to concerned department', '2020-08-03 06:47:39', 1, 'john', '19'),
(21, 'Congratualations you have cleared the test for Python dev post, an interview have been scheduled', '2020-08-03 06:48:14', 1, 'john', '19'),
(22, 'Congratualations you have been selected for Python dev post.', '2020-08-03 06:48:51', 1, 'john', '19'),
(23, 'Your Application for Python dev post have been successfully submitted', '2020-08-03 09:26:50', 1, 'john', '20'),
(24, 'TCS has responded to your Application for Python dev', '2020-08-03 09:28:58', 1, 'john', '20'),
(25, 'Test for Python dev have sucessfully completed, sent for review to concerned department', '2020-08-03 09:29:41', 1, 'john', '20'),
(26, 'Congratualations you have cleared the test for Python dev post, an interview have been scheduled', '2020-08-03 09:30:29', 1, 'john', '20'),
(27, 'Congratualations you have been selected for Python dev post.', '2020-08-03 09:32:30', 1, 'john', '20'),
(28, 'Your Application for DB Admin post have been successfully submitted', '2020-08-03 10:12:06', 1, 'john', '21'),
(29, 'TCS has responded to your Application for DB Admin', '2020-08-03 10:12:37', 1, 'john', '21'),
(30, 'Test for DB Admin have sucessfully completed, sent for review to concerned department', '2020-08-03 10:13:12', 1, 'john', '21'),
(31, 'Congratualations you have cleared the test for DB Admin post, an interview have been scheduled', '2020-08-03 10:13:40', 1, 'john', '21'),
(32, 'Congratualations you have been selected for DB Admin post.', '2020-08-03 10:14:18', 1, 'john', '21');

-- --------------------------------------------------------

--
-- Table structure for table `offer`
--

CREATE TABLE `offer` (
  `oid` int(11) NOT NULL,
  `uname` varchar(50) NOT NULL,
  `compid` varchar(50) NOT NULL,
  `jid` int(11) NOT NULL,
  `offer_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `post_job`
--

CREATE TABLE `post_job` (
  `job_id` int(10) NOT NULL,
  `job_title` varchar(20) NOT NULL,
  `company` varchar(20) NOT NULL,
  `job_desc` varchar(500) NOT NULL,
  `location` varchar(20) NOT NULL,
  `job_type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `post_job`
--

INSERT INTO `post_job` (`job_id`, `job_title`, `company`, `job_desc`, `location`, `job_type`) VALUES
(1, 'analyst', 'tcs', 'analyst', 'mumbai', 'permanant'),
(5, 'analyst1', 'LTI', 'kata le', 'work from home', 'temporary'),
(6, 'analyst1', 'LTI', 'kata le', 'work from home', 'temporary'),
(7, 'analyst1', 'LTI', 'kata le', 'work from home', 'temporary'),
(8, 'hello', 'hello', 'dd', 'Mumbai', 'on'),
(9, 'hello', 'hello', 'dd', 'Mumbai', 'on'),
(10, 'hello', 'hello', 'dd', 'Mumbai', 'on'),
(11, '', '', '', '', 'Full Time'),
(12, '', '', '', '', 'Internship'),
(13, '', '', '', '', 'Full Time'),
(14, '', '', '', '', 'Freelance'),
(15, '', '', '', '', 'Temporary');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `uname` varchar(50) NOT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `mname` varchar(20) NOT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `phone` int(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `dob` date NOT NULL,
  `address` varchar(50) DEFAULT NULL,
  `sex` char(5) DEFAULT NULL,
  `city` varchar(10) DEFAULT NULL,
  `state` varchar(10) DEFAULT NULL,
  `password` varchar(150) DEFAULT NULL,
  `descr` varchar(150) NOT NULL,
  `afw` int(11) NOT NULL DEFAULT '0',
  `profile_pic` varchar(128) NOT NULL DEFAULT 'static/img/dashboard/1.jpg'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`uname`, `fname`, `mname`, `lname`, `phone`, `email`, `dob`, `address`, `sex`, `city`, `state`, `password`, `descr`, `afw`, `profile_pic`) VALUES
('john', 'John', '', 'Doe', 0, 'mahajanmgit16e@student.mes.ac.in', '2020-07-17', 'f', 'femal', 'Barmiak', 'Sikkim', '$6$rounds=656000$6o3Q5MWN2gHtrSiD$fbGV9gfJ0CxkpXuSSM1xfIhC5aFZMy69gscS8c4K/xkoNjfSJGuGwFVEkAwLZusuoPPHSbqDfGQqgYq28DECs/', 'd', 1, 'static/img/dashboard/2016PE0226.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `skills`
--

CREATE TABLE `skills` (
  `srno` int(11) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `skname` varchar(100) NOT NULL,
  `percent` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `skills`
--

INSERT INTO `skills` (`srno`, `uname`, `skname`, `percent`) VALUES
(1, 'john', 'c++', '70'),
(2, 'john', 'Java', '90'),
(3, 'john', 'Python', '70'),
(4, 'john', 'Critical Thinking', '55');

-- --------------------------------------------------------

--
-- Table structure for table `work`
--

CREATE TABLE `work` (
  `srno` int(11) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `jobtitle` varchar(100) NOT NULL,
  `org` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `year` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `work`
--

INSERT INTO `work` (`srno`, `uname`, `jobtitle`, `org`, `duration`, `year`) VALUES
(2, 'john', 'Intern', 'Infosys', '2 monthes', '2020');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app_status`
--
ALTER TABLE `app_status`
  ADD PRIMARY KEY (`appid`);

--
-- Indexes for table `award`
--
ALTER TABLE `award`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `company_register`
--
ALTER TABLE `company_register`
  ADD PRIMARY KEY (`compid`);

--
-- Indexes for table `compfow`
--
ALTER TABLE `compfow`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `edu`
--
ALTER TABLE `edu`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `fow`
--
ALTER TABLE `fow`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `geoloc`
--
ALTER TABLE `geoloc`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`jid`);

--
-- Indexes for table `keypeep`
--
ALTER TABLE `keypeep`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `link`
--
ALTER TABLE `link`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `notification-candidate`
--
ALTER TABLE `notification-candidate`
  ADD PRIMARY KEY (`nid`);

--
-- Indexes for table `offer`
--
ALTER TABLE `offer`
  ADD PRIMARY KEY (`oid`);

--
-- Indexes for table `post_job`
--
ALTER TABLE `post_job`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`uname`);

--
-- Indexes for table `skills`
--
ALTER TABLE `skills`
  ADD PRIMARY KEY (`srno`);

--
-- Indexes for table `work`
--
ALTER TABLE `work`
  ADD PRIMARY KEY (`srno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app_status`
--
ALTER TABLE `app_status`
  MODIFY `appid` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `award`
--
ALTER TABLE `award`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `compfow`
--
ALTER TABLE `compfow`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `edu`
--
ALTER TABLE `edu`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `fow`
--
ALTER TABLE `fow`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `geoloc`
--
ALTER TABLE `geoloc`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `jid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100012;

--
-- AUTO_INCREMENT for table `keypeep`
--
ALTER TABLE `keypeep`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `link`
--
ALTER TABLE `link`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `notification-candidate`
--
ALTER TABLE `notification-candidate`
  MODIFY `nid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `offer`
--
ALTER TABLE `offer`
  MODIFY `oid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `post_job`
--
ALTER TABLE `post_job`
  MODIFY `job_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `skills`
--
ALTER TABLE `skills`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `work`
--
ALTER TABLE `work`
  MODIFY `srno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
