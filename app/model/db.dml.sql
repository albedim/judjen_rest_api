USE judjen;

INSERT INTO users VALUES ('3cv4', 'a@gmail.com', NULL, NULL, '0cc175b9c0f1b6a831c399e269772661', 'Shrouded Kayla 151', '2024-01-14');
INSERT INTO users VALUES ('35v4', 'b@gmail.com', "My Life is terrible, cringe stuff makes it better", NULL, '0cc175b9c0f1b6a831c399e269772661', 'Cipher Kayla 101', '2024-01-04');
INSERT INTO users VALUES ('3434', 'c@gmail.com', NULL, NULL, '0cc175b9c0f1b6a831c399e269772661', 'Masked Kyle 101', '2024-02-06');
INSERT INTO users VALUES ('3bv4', 'd@gmail.com', "Hey there, dunno what to write", NULL, '0cc175b9c0f1b6a831c399e269772661', 'Stealth Owen 108', '2023-12-14');
INSERT INTO users VALUES ('326v', 'e@gmail.com', NULL, NULL, '0cc175b9c0f1b6a831c399e269772661', 'Ghost Gavin 143', '2024-01-21');
INSERT INTO users VALUES ('3c45', 'f@gmail.com', NULL, NULL, '0cc175b9c0f1b6a831c399e269772661', 'Phantom Jackson 146', '2024-01-06');


INSERT INTO stories (title, content, created_on, user_id)
VALUES ('The Epic Quest for the Lost Sock', 'Once upon a time, in the mystical land of Laundrytopia, I embarked on an epic journey to find the lost sock that vanished mysteriously in the dryer. I battled lint monsters and faced the dreaded Fabric Softener Falls. Alas, the sock was never found, but my laundry basket was forever changed.', '2024-01-15', '3cv4');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('Attack of the Alien Pizza', 'Last night, I ordered a pizza from an intergalactic pizzeria. Little did I know, the pepperoni had tiny UFOs on them! Suddenly, my room turned into an extraterrestrial dance party. The pizza declared itself the leader, and we all danced our way to the moon.', '2024-01-05', '35v4');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('The Great Toothpaste Disaster', 'Attempting to squeeze out the last bit of toothpaste turned into a catastrophe. The toothpaste tube exploded, and the bathroom was covered in minty freshness. I now declare my bathroom the official Toothpaste Slip \'n Slide Park.', '2024-02-07', '3434');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('Invasion of the Pillow Fort', 'Late at night, my pillow fort declared war on the blanket kingdom. Fluffy pillow soldiers stormed the cozy blanket castles. The battle raged until morning, when we all realized we were late for school and needed to clean up the mess.', '2024-01-15', '3bv4');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('The Mystery of the Vanishing Homework', 'My homework vanished into thin air after I accidentally spilled a potion labeled \'Homework Houdini Elixir.\' Now, my dog speaks fluent Latin, and my teacher thinks I\'m a wizard prodigy. Abracadabra, homework gone!', '2024-01-01', '326v');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('Dance-Off with the Refrigerator Monster', 'While grabbing a midnight snack, the refrigerator transformed into a disco-dancing monster. We had a dance-off, and I emerged victorious with a stomach full of leftover pizza. The monster now serves as my personal chef.', '2024-01-22', '3c45');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('The Great Sneezing Epidemic', 'I accidentally unleashed a sneezing epidemic during a boring class. Everyone started sneezing uncontrollably, and the teacher joined in. The principal declared a sneeze holiday, and we all got a day off to recover.', '2024-01-14', '3c45');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('The Magical Hairbrush Incident', 'One morning, my hairbrush turned into a magical wand. Every time I brushed my hair, glitter and confetti flew out, turning my room into a sparkling wonderland. Now, I\'m the reigning monarch of Glitterland.', '2024-01-14', '3bv4');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('The Quest for the Missing Left Sock', 'My left sock mysteriously disappeared, so I embarked on a quest to find it. I traveled through the treacherous Land of Mismatched Socks and battled the infamous Laundry Goblin. Alas, the sock was never found, but I returned with a new appreciation for sock unity.', '2024-01-14', '3434');
INSERT INTO stories (title, content, created_on, user_id)
VALUES ('The Banana Phone Conspiracy', 'Convinced that my banana was secretly a phone, I spent hours talking to it about my day. Little did I know, the banana was part of a grand conspiracy to take over the fruit bowl. Now, my apple refuses to talk to me.', '2024-01-14', '3bv4');


INSERT INTO tags (tag_id, name) VALUES (1, 'Adventure');
INSERT INTO tags (tag_id, name) VALUES (2, 'Family');
INSERT INTO tags (tag_id, name) VALUES (3, 'Fantasy');
INSERT INTO tags (tag_id, name) VALUES (4, 'Funny');
INSERT INTO tags (tag_id, name) VALUES (5, 'Mystery');
INSERT INTO tags (tag_id, name) VALUES (6, 'Crime');
INSERT INTO tags (tag_id, name) VALUES (7, 'Black Humor');
INSERT INTO tags (tag_id, name) VALUES (8, 'Sex');
INSERT INTO tags (tag_id, name) VALUES (9, 'Weird');
INSERT INTO tags (tag_id, name) VALUES (10, 'Absurd');


INSERT INTO storytags (story_id, tag_id) VALUES (1, 1), (1, 3), (1, 9);
INSERT INTO storytags (story_id, tag_id) VALUES (2, 1), (2, 4), (2, 7);
INSERT INTO storytags (story_id, tag_id) VALUES (3, 3), (3, 6), (3, 10);
INSERT INTO storytags (story_id, tag_id) VALUES (4, 4), (4, 9);
INSERT INTO storytags (story_id, tag_id) VALUES (5, 5), (5, 10);
INSERT INTO storytags (story_id, tag_id) VALUES (6, 4), (6, 9), (6, 10);
INSERT INTO storytags (story_id, tag_id) VALUES (7, 4), (7, 7), (7, 9);
INSERT INTO storytags (story_id, tag_id) VALUES (8, 6), (8, 7), (8, 9);
INSERT INTO storytags (story_id, tag_id) VALUES (9, 1), (9, 3);
INSERT INTO storytags (story_id, tag_id) VALUES (10, 4), (10, 6);