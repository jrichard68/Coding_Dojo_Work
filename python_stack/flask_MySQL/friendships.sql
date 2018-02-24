
SELECT users.first_name, users.last_name, friends.first_name AS friend_first_name, friends.last_name AS friend_last_name
FROM users 
LEFT JOIN friendships ON  users.id = friendships.user_id
LEFT JOIN users AS friends ON friends.id = friendships.friend_id;

