create table if not exists users (
	id int not null auto_increment primary key,
    email varchar(255) not null unique,
    name varchar(255),
    country enum('US', 'CO', 'TN') 	default 'US' not null
);