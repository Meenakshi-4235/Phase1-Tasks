# Phase1-Tasks
IN Phase1 there are 4 tasks
TASK-1A:
i)Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Cricket","Ludo"].
ii) Convert emoji into text in Python - Converting emoticons or emojis into text in Python can be done using thedemoji module. It is used to accurately remove and replace emojis in text strings
TASK1B:
i)Design a ‘book’ class with title, author, publisher, price and author’s royalty as instance variables. Provide getter and setter properties for all variables. Also define a method royalty() to calculate royalty amount author can expect to
receive the following royalties:10% of the retail price on the first 500 copies; 12.5%for the next 1,000 copies sold, then 15% for all further copies sold. Then design a new ‘ebook’ class inherited from ‘book’ class. Add ebook format (EPUB,
PDF,MOBI etc) as additional instance variable in inherited class. Override royalty() method to deduct GST @12% on ebooks.
ii) Implement simple FLAMES game using Python.
According to first task,

Task-1:Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Cricket","Ludo"].
  1.Define Lists:

    We start by defining three lists: one for subjects, one for verbs, and one for objects.
    subjects contains the possible subjects of the sentences.
    verbs contains the possible verbs.
    objects contains the possible objects.
  2.Nested Loops:

    We use nested loops to iterate over each combination of subject, verb, and object.
    The outer loop iterates over each subject.
    The middle loop iterates over each verb.
    The inner loop iterates over each object.
  3.Constructing Sentences:

    For each combination of subject, verb, and object, we construct a sentence by concatenating them with spaces in between.
    The sentence is then stored in a list.
  4.Printing Sentences:

    After all possible sentences are generated, we print each sentence.

    
Task-2:Convert emoji into text in Python - Converting emoticons or emojis into text in Python can be done using thedemoji module. It is used to accurately remove and replace emojis in text strings
  1.Import demoji:

      The program starts by importing the demoji module, which provides the necessary functions to work with emojis.
  2.Download Emoji Codes:

      demoji.download_codes() is called to download the latest emoji definitions. This step is crucial for ensuring that the module has the most up-to-date emoji data.
  3.Function Definition:

      convert_emojis_to_text(text) is defined to take a string text as input.
      Inside the function, demoji.replace(text, "") is used to replace each emoji in the input text with its description. The second argument "" is the default string to replace each emoji with its description.
  4.Sample Text:

      A sample string text_with_emojis is defined that includes emojis to demonstrate the conversion process.
  5.Convert and Print:

      The sample text is passed to convert_emojis_to_text, and the result is stored in text_without_emojis.
      The original text and the converted text are printed to show the difference.


Task-3:Design a ‘book’ class with title, author, publisher, price and author’s royalty as instance variables. Provide getter and setter properties for all variables. Also define a method royalty() to calculate royalty amount author can expect to
receive the following royalties:10% of the retail price on the first 500 copies; 12.5%for the next 1,000 copies sold, then 15% for all further copies sold. Then design a new ‘ebook’ class inherited from ‘book’ class. Add ebook format (EPUB,
PDF,MOBI etc) as additional instance variable in inherited class. Override royalty() method to deduct GST @12% on ebooks.
  1.Book Class:

    Instance Variables: title, author, publisher, price, and royalty.
    Getters and Setters: Provided for each instance variable.
    royalty() Method: Calculates the royalty based on the number of copies sold.
  2.EBook Class:

    Inherits from the Book class.
    Additional Instance Variable: format (e.g., EPUB, PDF, MOBI).
    Override royalty() Method: Adjusts the calculated royalty to deduct 12% GST.
Task4:Implement simple FLAMES game using Python.
  1.Code Usage
  
      remove_common_chars(): This function removes the common characters between the two names.
      count_remaining_chars(): This function counts the remaining characters after removing common characters.
      flames_game(): This function implements the FLAMES game logic.
      flames_meaning(): This function returns the meaning of each letter in FLAMES.
2.How to Use:

    Run the script.
    Input the two names when prompted.
    The script will output the relationship between the two names according to the FLAMES game.
This script simplifies the process of playing the FLAMES game and demonstrates the basic string manipulation and loop control techniques in Python.
