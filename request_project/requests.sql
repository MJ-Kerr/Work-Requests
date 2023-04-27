-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema requests
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `requests` ;

-- -----------------------------------------------------
-- Schema requests
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `requests` DEFAULT CHARACTER SET utf8 ;
USE `requests` ;

-- -----------------------------------------------------
-- Table `requests`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `requests`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(250) NOT NULL,
  `email` VARCHAR(250) NOT NULL,
  `username` VARCHAR(250) NOT NULL,
  `password` VARCHAR(250) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `requests`.`admin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `requests`.`admin` (
  `admin_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(200) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  `users_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`admin_id`),
  INDEX `fk_admin_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_admin_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `requests`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `requests`.`requests`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `requests`.`requests` (
  `request_id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(100) NOT NULL DEFAULT 'CHECK (type IN(  \'Full Stack\', \'Front End\', \'Back End\' ))',
  `description` TEXT NOT NULL,
  `language` VARCHAR(200) NOT NULL DEFAULT 'CHECK (language IN ( \'Python\', \'SQL\', \'JAVA\', \'JavaScript\', \'MERN'\, \'C#\'))',
  `wireframe` VARCHAR(450) NOT NULL,
  `users_id` INT NOT NULL,
  `admin_admin_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() on UPDATE NOW(),
  PRIMARY KEY (`request_id`),
  INDEX `fk_requests_users_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_requests_admin1_idx` (`admin_admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_requests_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `requests`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_requests_admin1`
    FOREIGN KEY (`admin_admin_id`)
    REFERENCES `requests`.`admin` (`admin_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
