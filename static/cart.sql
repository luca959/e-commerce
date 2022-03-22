DROP TABLE IF EXISTS cart;
CREATE TABLE cart(
    title TEXT,
    email TEXT,
    quantity INT DEFAULT 1
);

DROP TABLE IF EXISTS item;
CREATE TABLE item(
    title TEXT,
    info TEXT,
    img TEXT
);

DROP TABLE IF EXISTS user;
CREATE TABLE user(
    email TEXT NOT NULL,
    pwd TEXT NOT NULL,
    PRIMARY KEY (email)
  
);


INSERT INTO item(title,info,img) VALUES(
    'Stone Island',
    'Stone Island è un marchio italiano di abbigliamento fondato nel 1982 da Massimo Osti.',
    '../static/stone.png'

);
INSERT INTO item(title,info,img) VALUES(
    'C.P. Company',
    'C.P. Company è un marchio di abbigliamento italiano fondato nel 1971 dal designer Massimo Osti.',
    '../static/cp.jpg'
    
);
INSERT INTO item(title,info,img) VALUES(
    'Palm Angels',
    'Palm Angels is a luxury fashion label founded in 2015 by Italian art director and photographer, Francesco Ragazzi.',
    '../static/m.jpg'
);

INSERT INTO item(title,info,img) VALUES(
    'Moncler',
    'Moncler è stata fondata nel 1952 a Monestier-de-Clermont, località sciistica vicino a Grenoble, Francia da René Ramillon,'    ,
    '../static/p.jpeg'
);
