import hashlib

def hide_password(password):
    hash_object = hashlib.sha512(password.encode())
    return hash_object.hexdigest()
    
all_pw = ['123@567A', 
          '12!4567B', 
          '12$C4567', 
          '1234D#67',
          'B1#34567',
          'B@234567']
        
ALL_USERS = [[("Rositsa Zlateva", hide_password(all_pw[0])),
              ("Slavayana Monkova", hide_password(all_pw[1])),
              ("Radoslav Georgiev", hide_password(all_pw[2])),
              ("Krasimira Badova", hide_password(all_pw[3])),
              ("Kiril Hristov", hide_password(all_pw[4])),
              ("Vladimir Delchev", hide_password(all_pw[5]))],
              [("Filythy Frank", hide_password(all_pw[0])),
              ("Pink Guy", hide_password(all_pw[1])),
              ("Saffary Man", hide_password(all_pw[2])),
              ("Negi Gen 3000", hide_password(all_pw[3])),
              ("Chin Chin", hide_password(all_pw[4])),
              ("Ima LEMON", hide_password(all_pw[5]))],
              [("Stan Marsh", hide_password(all_pw[0])),
              ("Keney McKormik", hide_password(all_pw[1])),
              ("Eric Cartman", hide_password(all_pw[2])),
              ("Kyle Broflovski", hide_password(all_pw[3])),
              ("Butters Stotch", hide_password(all_pw[4])),
              ("Scott Malcolmson", hide_password(all_pw[5]))] ]
              
              
ALL_MOVIES = [[("The Hunger Games: Catching Fire", 7.9),
               ("Wreck-It Ralph", 7.8),
               ("Her", 8.3)],
              [("PIMP my wheelchair", 10.0),
               ("Evil Narrator", 8.8),
               ("FILTHY FRANK VS CHIN CHIN", 9.3)],
              [("Generic MOVIE1", 4.5),
               ("Generic MOVIE 2", 5.8),
               ("Generic MOVIE 3", 5.3)]]            
                 
ALL_PROJECTIONS = [[(1, "3D", "2014-04-01", "19:10"),
                    (1, "2D", "2014-04-01", "19:00"),
                    (1, "4DX", "2014-04-02", "21:00"),
                    (3, "2D", "2014-04-02", "20:20"),
                    (2, "3D", "2014-04-02", "22:00"),
                    (2, "2D", "2014-04-02", "19:30")],
                   [(1, "3D", "2014-04-01", "19:10"),
                    (1, "2D", "2014-04-01", "19:00"),
                    (1, "4DX", "2014-04-02", "21:00"),
                    (3, "2D", "2014-04-02", "20:20"),
                    (2, "3D", "2014-04-02", "22:00"),
                    (2, "2D", "2014-04-02", "19:30")],
                   [(1, "3D", "2014-04-01", "19:10"),
                    (1, "2D", "2014-04-01", "19:00"),
                    (1, "4DX", "2014-04-02", "21:00"),
                    (3, "2D", "2014-04-02", "20:20"),
                    (2, "3D", "2014-04-02", "22:00"),
                    (2, "2D", "2014-04-02", "19:30")]]                 
              
ALL_RESERVATIONS = [[(3, 1, 2, 1),
                     (3, 1, 3, 5),
                     (3, 1, 7, 8),
                     (2, 3, 1, 1),
                     (2, 3, 1, 2),
                     (5, 5, 2, 3),
                     (6, 5, 2, 4)],
                    [(3, 1, 2, 1),
                     (3, 1, 8, 5),
                     (3, 1, 6, 8),
                     (2, 3, 7, 5),
                     (2, 3, 7, 2),
                     (5, 5, 5, 3),
                     (6, 5, 4, 1)]]            
              
              
              
              
              
              
              
              
              
              
