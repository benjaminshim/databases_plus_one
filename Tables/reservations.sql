-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 28, 2023 at 01:08 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `csv_db 6`
--

-- --------------------------------------------------------

--
-- Table structure for table `restaurant_reservations`
--

CREATE TABLE `reservations` (
  `ReservationID` int(11) NOT NULL AUTO_INCREMENT,
  `RestaurantID` int(11) NOT NULL,
  `UserID` int(11) NOT NULL,
  `ReservationDate` date NOT NULL,
  `ReservationTime` time NOT NULL,
  `PartySize` int(5) NOT NULL,
  PRIMARY KEY (`ReservationID`),
  FOREIGN KEY (`RestaurantID`) REFERENCES `one_star_michelin_restaurants`(`ID`),
  FOREIGN KEY (`UserID`) REFERENCES `users`(`UserID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `one_star_michelin_restaurants`
--

INSERT INTO `restaurant_reservations` (`RestaurantID`, `UserID`, `ReservationDate`, `ReservationTime`, `PartySize`) VALUES
(1, 1, '2023-10-30', '19:00:00', 2),
(2, 2, '2023-11-05', '20:00:00', 4),
(3, 3, '2023-11-12', '18:30:00', 3),
(4, 4, '2023-11-15', '19:30:00', 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
