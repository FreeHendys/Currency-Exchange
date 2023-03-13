# Conceptual Exercise

## Answer the following questions below

- **What are important differences between Python and JavaScript?**
  Javascript is used for front end development and integration of client side programs while Python is used in the bad end to communicate with the server and database

- **Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you can try to get a missing key (like "c") _without_ your programming crashing.**
  Two ways you can get a missing key from a dictionary like `{"a": 1, "b": 2}` without crashing your program is the _in_ operator and get(). The _in_ operator will check the dictionary for the key and will return a boolean value depending if it is there or not. get() will return the value of the associated key and if the key is not pressent it will return a defualt value or _None_

- **What is a unit test?**
  A unit test tests one “unit” of functionality usually one function or method

- **What is an integration test?**
  A integration test tests that components work together properly and seemlessly

- **What is the role of web application framework, like Flask?**
  The role of a web application framework like Flask is to process requests and issue responses via HTTP from a webpage to a server

- **You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel' or using a URL query param (like'foods?type=pretzel'). How might you choose which one is a better fit for an application?**
  foods?type is probably more for search based routing while /foods/pretzel is predefined

- **How do you collect data from a URL placeholder parameter using Flask?**
  request.args

- **How do you collect data from the query string using Flask?**
  request.url

- **How do you collect data from the body of the request using Flask?**
  request.args.get

- **What is a cookie and what kinds of things are they commonly used for?**
  Cookie are small bits of data that are connect to a user that will be accessed whenever you visit a website.

- **What is the session object in Flask?**
  A session stores information on a user's system that is carried over during the use of a browser. It tracks updating variables and is not affected by refreshes

- **What does Flask's `jsonify()` do?**
  Jsonify will return flask data that need to be turned into JSON format
