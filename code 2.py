print("\nYour Astrological sign is :",sign)

  user=input("\nDo you want to read your horoscope?\nEnter Y to read your scope and N to exit\n")

  if user=='Y':
    print("Here is your horoscope!!!!")

    if sign=="Sagittarius":
      print("\nYou hate people telling you what to do. However, rarely do you do anything, \n"
          "other than complain. You take your own path even if the Google/Apple Maps is \n"
          "showing you that you are heading towards a landfill.\n")
    elif sign=='Capricorn':
      print("\nYou are too calculative for the people around you. The reason you get ahead is\n"
          "not because you are smarter, but because you are a perfect con. The karma is \n"
          "around and it is watching you.\n")
    elif sign == "Aquarius":
      print("\nFocus on one thing in your life for once! Stop being a flake and actually do one\n"
          "thing you promised people. Your communication skills this week are worse than\n"
          "Babu Bhaiyaa. Speak up!\n")
    elif sign == "Pisces":
      print("\nYou need to come back to earth. datedreaming and maxing your credit card won’t make \n"
          "you happy. Neither would alcohol dependence to drown your sorrows. You are popular \n"
          "among your friends because you have a free stash.\n")
    elif sign == "Aries":
      print("\nYour impulsive nature gets you into a lot of trouble. It has also created a hole in \n"
          "your pocket. Do yourself a favor and get on that bus that goes nowhere.Since you are\n"
          "very ambitious and loud, there will surely be a way out.\n")
    elif sign == "Taurus":
      print("\nYou are often called stubborn. There is a reason for it. You want to win an argument \n"
          "even if it’s with a child. You will also be chased by the street dog on the way home \n"
          "this week. Keep your eyes open.\n")
    elif sign == "Gemini":
      print("\nThe voices in your head are getting louder and your neighbors are starting to notice.\n"
          "Your positive karmic cycle is all wrong kinds of screwed up. You will spot your crush \n"
          "or the love of your life. With someone ELSE.\n")
    elif sign == "Cancer":
      print("\nYou need to stop crying about why that waiter gave you cold food. You crustaceans are \n"
          "moody enough to make stale cheese. You claim yourself to be a wanderer and a dreamer, \n"
          "however, you never leave your stinky shell to do anything risky or new.\n")
    elif sign == "Leo":
      print("\nYou will miss all your deadlines this week. While you are running to be on time for that\n"
          "one meeting, your shoes will fall apart. Also, a child beggar on the street will harass \n"
          "you till you lose your faith in humanity.\n")
    elif sign == "Virgo":
      print("\nYou need to stop waiting for your mom to clean your laundry. You stink, literally. Your \n"
          "watchman thinks of garbage collector whenever you are around. Take a shower, and do planet\n"
          "earth a favor.\n")
    elif sign == "Libra":
      print("\nTalking your way out of problems does not mean the problems are resolved. When you are done\n"
          "deciding what to eat for lunch, you need to get back to life. Your constant confusion\n"
          "is showing, clearly!\n")
    elif sign == "Scorpio":
      print("\nThere is one thing that you love more than your reflection. Your photograph. Strangers think\n"
          "you are mysterious, but they don’t realize that you are a creep, waiting to be found out. \n"
          "You think you are smooth and can be the life of the party, but you aren’t getting invited to the right ones.\n")

  elif user=="N":
    print('Thank You for your time!!')
    break

  else:
    print("Invalid Input, Please enter the correct input.")
