movies = [
    {
        "title": "The Godfather",
        "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "type": "Crime",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 9,
    },
    {
        "title": "The Lord of the Rings: The Fellowship of the Ring",
        "description": "A meek Hobbit from the Shire and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.",
        "type": "Fantasy",
        "file_size": 2100000000,  # 2.1 GB
        "popularity": 8,
    },
    {
        "title": "The Avengers",
        "description": "Earth's mightiest heroes must come together and learn to fight as a team if they are going to stop the mischievous Loki and his alien army from enslaving humanity.",
        "type": "Action",
        "file_size": 1800000000,  # 1.8 GB
        "popularity": 7,
    },
    {
        "title": "Jurassic Park",
        "description": "During a preview tour, a theme park suffers a major power breakdown that allows its cloned dinosaur exhibits to run amok.",
        "type": "Adventure",
        "file_size": 2200000000,  # 2.2 GB
        "popularity": 6,
    },
    {
        "title": "E.T. the Extra-Terrestrial",
        "description": "A troubled child summons the courage to help a friendly alien escape Earth and return to his home world.",
        "type": "Science Fiction",
        "file_size": 2000000000,  # 2 GB
        "popularity": 8,
    },
    {
        "title": "Titanic",
        "description": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
        "type": "Romance",
        "file_size": 2350000000,  # 2.35 GB
        "popularity": 9,
    },
    {
        "title": "The Silence of the Lambs",
        "description": "A young FBI cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.",
        "type": "Crime",
        "file_size": 1900000000,  # 1.9 GB
        "popularity": 7,
    },
    {
        "title": "The Lion King",
        "description": "Lion cub and future king Simba searches for his identity. His eagerness to please others and penchant for testing his boundaries sometimes gets him into trouble.",
        "type": "Animation",
        "file_size": 2050000000,  # 2.05 GB
        "popularity": 8,
    },
    {
        "title": "The Revenant",
        "description": "A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear and left for dead by members of his own hunting team.",
        "type": "Adventure",
        "file_size": 2500000000,  # 2.5 GB
        "popularity": 9,
    },
    {
        "title": "Forrest Gump",
        "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
        "type": "Drama",
        "file_size": 1950000000,  # 1.95 GB
        "popularity": 7,
    },
    {
        "title": "The Dark Knight Rises",
        "description": "Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City from the brutal guerrilla terrorist Bane.",
        "type": "Action",
        "file_size": 2300000000,  # 2.3 GB
        "popularity": 8,
    },
    {
        "title": "Inglourious Basterds",
        "description": "In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same.",
        "type": "War",
        "file_size": 2150000000,  # 2.15 GB
        "popularity": 6,
    },
    {
        "title": "The Social Network",
        "description": "As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.",
        "type": "Drama",
        "file_size": 1850000000,  # 1.85 GB
        "popularity": 9,
    },
    {
        "title": "The Grand Budapest Hotel",
        "description": "A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel's glorious years under an exceptional concierge.",
        "type": "Comedy",
        "file_size": 2000000000,  # 2 GB
        "popularity": 7,
    },
    {
        "title": "The Departed",
        "description": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
        "type": "Crime",
        "file_size": 2100000000,  # 2.1 GB
        "popularity": 8,
    },
    {
        "title": "The Shawshank Redemption",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "type": "Drama",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 6,
    },
    {
        "title": "Schindler's List",
        "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
        "type": "Historical Drama",
        "file_size": 2250000000,  # 2.25 GB
        "popularity": 9,
    },
    {
        "title": "Gladiator",
        "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "type": "Action",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 7,
    },
    {
        "title": "The Matrix",
        "description": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "type": "Action",
        "file_size": 2250000000,  # 2.25 GB
        "popularity": 8,
    },
    {
        "title": "Avatar",
        "description": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "type": "Science Fiction",
        "file_size": 2550000000,  # 2.55 GB
        "popularity": 9,
    },
    {
        "title": "Gladiator",
        "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "type": "Action",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 7,
    },
    {
        "title": "The Godfather Part II",
        "description": "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.",
        "type": "Crime",
        "file_size": 2300000000,  # 2.3 GB
        "popularity": 8,
    },
    {
        "title": "Goodfellas",
        "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.",
        "type": "Crime",
        "file_size": 2200000000,  # 2.2 GB
        "popularity": 7,
    },
    {
        "title": "The Shawshank Redemption",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "type": "Drama",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 9,
    },
    {
        "title": "Pulp Fiction",
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "type": "Crime",
        "file_size": 2100000000,  # 2.1 GB
        "popularity": 8,
    },
    {
        "title": "Fight Club",
        "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
        "type": "Drama",
        "file_size": 2300000000,  # 2.3 GB
        "popularity": 8,
    },
    {
        "title": "Forrest Gump",
        "description": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
        "type": "Drama",
        "file_size": 2250000000,  # 2.25 GB
        "popularity": 9,
    },
    {
        "title": "The Dark Knight",
        "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",
        "type": "Action",
        "file_size": 2350000000,  # 2.35 GB
        "popularity": 9,
    },
    {
        "title": "Star Wars: Episode IV - A New Hope",
        "description": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station while also attempting to rescue Princess Leia from the mysterious Darth Vader.",
        "type": "Science Fiction",
        "file_size": 2450000000,  # 2.45 GB
        "popularity": 8,
    },
    {
        "title": "The Matrix Reloaded",
        "description": "Neo and his allies race against time before the machines discover the city of Zion and destroy it. While seeking the truth about the Matrix, Neo must save Trinity from a dark fate within his dreams.",
        "type": "Action",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 7,
    },
    {
        "title": "The Incredibles",
        "description": "A family of undercover superheroes, while trying to live the quiet suburban life, is forced into action to save the world.",
        "type": "Animation",
        "file_size": 1950000000,  # 1.95 GB
        "popularity": 7,
    },
    {
        "title": "The Dark Knight Rises",
        "description": "Eight years after the Joker's reign of anarchy, Batman, with the help of the enigmatic Catwoman, is forced from his exile to save Gotham City from the brutal guerrilla terrorist Bane.",
        "type": "Action",
        "file_size": 2300000000,  # 2.3 GB
        "popularity": 8,
    },
    {
        "title": "Inglourious Basterds",
        "description": "In Nazi-occupied France during World War II, a plan to assassinate Nazi leaders by a group of Jewish U.S. soldiers coincides with a theatre owner's vengeful plans for the same.",
        "type": "War",
        "file_size": 2150000000,  # 2.15 GB
        "popularity": 6,
    },
    {
        "title": "The Social Network",
        "description": "As Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, he is sued by the twins who claimed he stole their idea, and by the co-founder who was later squeezed out of the business.",
        "type": "Drama",
        "file_size": 1850000000,  # 1.85 GB
        "popularity": 9,
    },
    {
        "title": "The Grand Budapest Hotel",
        "description": "A writer encounters the owner of an aging high-class hotel, who tells him of his early years serving as a lobby boy in the hotel's glorious years under an exceptional concierge.",
        "type": "Comedy",
        "file_size": 2000000000,  # 2 GB
        "popularity": 7,
    },
    {
        "title": "The Departed",
        "description": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
        "type": "Crime",
        "file_size": 2100000000,  # 2.1 GB
        "popularity": 8,
    },
    {
        "title": "The Shawshank Redemption",
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
        "type": "Drama",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 6,
    },
    {
        "title": "Schindler's List",
        "description": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.",
        "type": "Historical Drama",
        "file_size": 2250000000,  # 2.25 GB
        "popularity": 9,
    },
    {
        "title": "Gladiator",
        "description": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "type": "Action",
        "file_size": 2400000000,  # 2.4 GB
        "popularity": 7,
    },
    {
        "title": "Avatar",
        "description": "A paraplegic Marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "type": "Science Fiction",
        "file_size": 2550000000,  # 2.55 GB
        "popularity": 9,
    },
    {
        "title": "The Godfather Part II",
        "description": "The early life and career of Vito Corleone in 1920s New York City is portrayed, while his son, Michael, expands and tightens his grip on the family crime syndicate.",
        "type": "Crime",
        "file_size": 2300000000,  # 2.3 GB
        "popularity": 8,
    },
    {
        "title": "Goodfellas",
        "description": "The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.",
        "type": "Crime",
        "file_size": 2200000000,  # 2.2 GB
        "popularity": 7,
    },
    {
        "title": "Pulp Fiction",
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "type": "Crime",
        "file_size": 2100000000,  # 2.1 GB
        "popularity": 8,
    },
    {
        "title": "Fight Club",
        "description": "An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.",
        "type": "Drama",
        "file_size": 2300000000,  # 2.3 GB
        "popularity": 8,
    },
]

servers = [
    {
        "endpoint": "server1.example.com",
        "is_active": True,
        "remaining_storage": 2000000000000,
    },  # 2 TB in bytes
    {
        "endpoint": "server2.example.com",
        "is_active": True,
        "remaining_storage": 4000000000000,
    },  # 4 TB in bytes
    {
        "endpoint": "server3.example.com",
        "is_active": False,
        "remaining_storage": 3000000000000,
    },  # 3 TB in bytes
    {
        "endpoint": "server4.example.com",
        "is_active": True,
        "remaining_storage": 5000000000000,
    },  # 5 TB in bytes
    {
        "endpoint": "server5.example.com",
        "is_active": False,
        "remaining_storage": 6000000000000,
    },  # 6 TB in bytes
    {
        "endpoint": "server6.example.com",
        "is_active": True,
        "remaining_storage": 7000000000000,
    },  # 7 TB in bytes
    {
        "endpoint": "server7.example.com",
        "is_active": True,
        "remaining_storage": 8000000000000,
    },  # 8 TB in bytes
    {
        "endpoint": "server8.example.com",
        "is_active": False,
        "remaining_storage": 9000000000000,
    },  # 9 TB in bytes
    {
        "endpoint": "server9.example.com",
        "is_active": True,
        "remaining_storage": 10000000000000,
    },  # 10 TB in bytes
    {
        "endpoint": "server10.example.com",
        "is_active": True,
        "remaining_storage": 11000000000000,
    },  # 11 TB in bytes
    {
        "endpoint": "server11.example.com",
        "is_active": True,
        "remaining_storage": 12000000000000,
    },  # 12 TB in bytes
    {
        "endpoint": "server12.example.com",
        "is_active": False,
        "remaining_storage": 13000000000000,
    },  # 13 TB in bytes
    {
        "endpoint": "server13.example.com",
        "is_active": True,
        "remaining_storage": 14000000000000,
    },  # 14 TB in bytes
    {
        "endpoint": "server14.example.com",
        "is_active": True,
        "remaining_storage": 15000000000000,
    },  # 15 TB in bytes
    {
        "endpoint": "server15.example.com",
        "is_active": False,
        "remaining_storage": 16000000000000,
    },  # 16 TB in bytes
    {
        "endpoint": "server16.example.com",
        "is_active": True,
        "remaining_storage": 17000000000000,
    },  # 17 TB in bytes
    {
        "endpoint": "server17.example.com",
        "is_active": True,
        "remaining_storage": 18000000000000,
    },  # 18 TB in bytes
    {
        "endpoint": "server18.example.com",
        "is_active": False,
        "remaining_storage": 19000000000000,
    },  # 19 TB in bytes
    {
        "endpoint": "server19.example.com",
        "is_active": True,
        "remaining_storage": 20000000000000,
    },  # 20 TB in bytes
    {
        "endpoint": "server20.example.com",
        "is_active": True,
        "remaining_storage": 21000000000000,
    },  # 21 TB in bytes
    {
        "endpoint": "server21.example.com",
        "is_active": True,
        "remaining_storage": 22000000000000,
    },  # 22 TB in bytes
    {
        "endpoint": "server22.example.com",
        "is_active": True,
        "remaining_storage": 23000000000000,
    },  # 23 TB in bytes
    {
        "endpoint": "server23.example.com",
        "is_active": False,
        "remaining_storage": 24000000000000,
    },  # 24 TB in bytes
    {
        "endpoint": "server24.example.com",
        "is_active": True,
        "remaining_storage": 25000000000000,
    },  # 25 TB in bytes
    {
        "endpoint": "server25.example.com",
        "is_active": False,
        "remaining_storage": 26000000000000,
    },  # 26 TB in bytes
    {
        "endpoint": "server26.example.com",
        "is_active": True,
        "remaining_storage": 27000000000000,
    },  # 27 TB in bytes
    {
        "endpoint": "server27.example.com",
        "is_active": True,
        "remaining_storage": 28000000000000,
    },  # 28 TB in bytes
    {
        "endpoint": "server28.example.com",
        "is_active": False,
        "remaining_storage": 29000000000000,
    },  # 29 TB in bytes
    {
        "endpoint": "server29.example.com",
        "is_active": True,
        "remaining_storage": 30000000000000,
    },  # 30 TB in bytes
    {
        "endpoint": "server30.example.com",
        "is_active": True,
        "remaining_storage": 31000000000000,
    },  # 31 TB in bytes
]
