-- INSERT INTO users (first_name, last_name)
-- VALUES ("Amy", "Giver"), ("Maria", "Arriviello"), ("Eli", "Byers"), ("Marky", "Mark"), ("Big", "Bird"), ("Kermit", "The Frog");

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES (1, 2), (1,4), (1,6), (2,1), (2,3), (2,5), (3,2), (3,5), (4,3), (5,1);

-- SELECT user_id, friend_id from friendships;

-- INSERT INTO friendships (user_id, friend_id)
-- VALUES (6, 2), (6, 3);

-- SELECT users.first_name as first_name, users.last_name as last_name, users2.first_name as friend_first, users2.last_name as friend_last FROM users
-- JOIN friendships ON users.id = friendships.user_id
-- LEFT JOIN users as users2 ON users2.id = friendships.friend_id;

SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_with FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id=1;


