
CREATE TABLE Cards (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    sale FLOAT,
    cashback FLOAT,
    interest_on_loan FLOAT,
    bank VARCHAR(255),
    rating SMALLINT
);

CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    money INTEGER,
    cashback_importance SMALLINT
);

CREATE TABLE user_cards (
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    card_id INT REFERENCES cards(card_id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, card_id)  -- Composite primary key
);


CREATE TABLE Transactions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    card_id INT,
    category_id INT,
    FOREIGN KEY (user_id) REFRENCES users(user_id),
    FOREIGN KEY (card_id) REFERENCES cards(card_id),
    FOREIGN KEY (category_id) REFERENCES cards(card_id)
);

CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);
