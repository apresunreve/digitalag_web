CREATE TABLE user{
uniqueID int,
name varchar(255),
thridP varchar(255),
}

CREATE TABLE map{
    UNIQUE uniqueID int,
    UNIQUE tag varchar(255),
    PRIMARY KEY(uniqueID, tag),
    FOREIGN KEY (uniqueID) REFERENCES(user)
}