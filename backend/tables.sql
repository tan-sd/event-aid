CREATE schema event_aid;

use event_aid;


CREATE TABLE `Planner` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`username`)
);

CREATE TABLE `Senior` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
   PRIMARY KEY (`username`)
);

CREATE TABLE `Guardian` (
  `guardian_username` varchar(255) NOT NULL ,
  `guardian_password` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  PRIMARY KEY (`guardian_username` , `username`),
  FOREIGN KEY (`username`) REFERENCES `Senior`(`username`)
);

CREATE TABLE `Event`(
	`event_id` INT(10) AUTO_INCREMENT,
    `datetime` datetime,
    `location` varchar(255) NOT NULL,
    `title` varchar(255) NOT NULL,
    `description` varchar(255) NOT NULL,
    `planner_username` varchar(255) NOT NULL,
    PRIMARY KEY (`event_id`),
	FOREIGN KEY (`planner_username`) REFERENCES `Planner`(`username`)
);

CREATE TABLE `User_event`(
	`event_id` INT(10) NOT NULL,
	`senior_username`varchar(255) NOT NULL,
    `is_sign_up` boolean ,
    `is_confirmed` boolean,
    PRIMARY KEY (`event_id`, `senior_username`),
	FOREIGN KEY (`event_id`) REFERENCES `Event`(`event_id`),
    FOREIGN KEY (`senior_username`) REFERENCES `Senior`(`username`)
);













