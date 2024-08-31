-- Use the event_aid schema
USE event_aid;

-- Insert data into the Planner table
INSERT INTO `Planner` (`username`, `password`) VALUES
('planner1', 'password123'),
('planner2', 'securepass456');

-- Insert data into the Senior table
INSERT INTO `Senior` (`username`, `password`) VALUES
('senior1', 'seniorpass1'),
('senior2', 'seniorpass2'),
('senior3', 'seniorpass3');

-- Insert data into the Guardian table
INSERT INTO `Guardian` (`guardian_username`, `guardian_password`, `username`) VALUES
('guardian1', 'guardianpass1', 'senior1'),
('guardian2', 'guardianpass2', 'senior2'),
('guardian3', 'guardianpass3', 'senior3');

-- Insert data into the Event table
INSERT INTO `Event` (`datetime`, `location`, `title`, `description`, `planner_username`) VALUES
('2024-09-15 10:00:00', 'Community Center', 'Health Check-up', 'A health check-up for seniors.', 'planner1'),
('2024-09-20 14:00:00', 'Park', 'Yoga Session', 'A yoga session to promote wellness.', 'planner2'),
('2024-09-25 09:00:00', 'Library', 'Book Reading', 'Reading session with a local author.', 'planner1');

-- Insert data into the User_event table
INSERT INTO `User_event` (`event_id`, `senior_username`, `is_sign_up`, `is_confirmed`) VALUES
(1, 'senior1', TRUE, TRUE),
(1, 'senior2', TRUE, FALSE),
(2, 'senior3', TRUE, TRUE),
(3, 'senior1', TRUE, FALSE),
(3, 'senior2', TRUE, TRUE);