CREATE DATABASE IF NOT EXISTS judjen;
USE judjen;

CREATE TABLE IF NOT EXISTS users(
	user_id VARCHAR(4) PRIMARY KEY,
    email VARCHAR(64) NOT NULL,
    bio VARCHAR(80),
    recovery_token VARCHAR(16),
    password VARCHAR(64) NOT NULL,
    anonymous_name VARCHAR(24) NOT NULL,
    created_on DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS user_notifications(
    notification_id INT PRIMARY KEY AUTO_INCREMENT,
	user_id VARCHAR(4) NOT NULL,
	target_id VARCHAR(4) NOT NULL,
    notification_type INT NOT NULL,
    created_on DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (target_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS stories(
	story_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(64) NOT NULL,
    content TEXT NOT NULL,
    created_on DATE NOT NULL,
  	user_id VARCHAR(4) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE tags(
	tag_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL
);

CREATE TABLE IF NOT EXISTS storytags(
	tag_id INT NOT NULL,
    story_id INT NOT NULL,
    PRIMARY KEY (story_id, tag_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id),
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS friends(
	user_id VARCHAR(4) NOT NULL,
    friend_id VARCHAR(4) NOT NULL,
    created_on DATE NOT NULL,
    PRIMARY KEY (user_id, friend_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (friend_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS friendrequests(
	user_id VARCHAR(4) NOT NULL,
    target_id VARCHAR(4) NOT NULL,
    created_on DATE NOT NULL,
    PRIMARY KEY (user_id, target_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (target_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS reposts (
    user_id VARCHAR(4) NOT NULL,
    story_id INT NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY (user_id, story_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
);

CREATE TABLE IF NOT EXISTS favorites (
    user_id VARCHAR(4) NOT NULL,
    story_id INT NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY(user_id, story_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (story_id) REFERENCES stories(story_id)
)
