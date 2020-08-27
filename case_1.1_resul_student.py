
# coding: utf-8

# # Pre-Case Setup: Python, Jupyter Notebook, Git

# ## Goals
# 
# By the end of this case you should have properly set up and familiarized yourself with Python, Jupyter, Anaconda, and GitHub. 
# 
# You should further have a working knowledge of various fundamental building blocks of Python (listed at the end of the case). This means being able to write simple code to perform analytical tasks such as creating metrics for making a business decision.

# ## Python and Jupyter
# 
# Python is a general purpose programming language that allows for both simple and complex data analysis. Python is incredibly versatile, allowing analysts, consultants, engineers, and managers to obtain and analyze information for insightful decision-making.
# 
# The [Jupyter Notebook](https://jupyter.org/index.html) is an open-source web application that allows for Python code development. Jupyter further allows for inline plotting and provides useful mechanisms for viewing data that make it an excellent resource for a variety of projects and disciplines.
# 
# The following section will outline how to install and begin working with Python and Juypter.

# ## Setting up the Python Environment
# 
# Instruction guides for Windows and MacOS are included below. Follow the one that corresponds with your operating system.
# 
# ### Windows Install
# 
# 1. Open your browser and go to https://www.anaconda.com/distribution/
# 
# 2. Click on "Windows" and then "Download" for Python 3.7 64-bit installer
# 
# 3. Run the downloaded file found in the downloads section from Step 2
# 
# 4. Click through the install prompts
# 
# 5. Go to menu (or Windows Explorer), find the Anaconda3 folder, and double-click to run
# 
# ### MacOS Install
# 
# 1. Open your browser and go to https://www.anaconda.com/distribution/
# 
# 2. Click on "MacOS" and then "Download" for Python 3.7 64-bit installer
# 
# 3. Run the downloaded file found in the downloads section from Step 2
# 
# 4. Click through the install prompts
# 
# 5. Use a Spotlight Search and type "Navigator", select and run the Anaconda Navigator program. Note that MacOS also comes with Python pre-installed, but you should _not_ use this version, which is used by the system. Anaconda will run a second installation of Python and you should ensure that you only use this second installation for all tasks.

# ## File Management with Python and Jupyter
# 
# It is common practice to have a main folder where all projects will be located (e.g. "jupyter_research"). The following are guidelines you can use for Python projects to help keep your code organized and accessible:
# 
# 1. Create subfolders for each Jupyter-related project
# 3. Group related .ipynb (the file format for Jupyter Notebook) files together in the same folder
# 2. Create a "Data" folder within individual project folders if using a large number of related data files
# 
# You should now be set up and ready to begin coding in Python!

# ## Setting up Git, GitHub, and cloning a repository

# Git is a free and open-source distributed version-control system. It is very useful for both simple software projects and large multi-functional projects that span thousands of files.  The main website for Git documentation is https://git-scm.com/. We will go over a brief introduction to Git here to get up and running with the software, in addition to understanding how its version control system operates. We'll create a new repository and also cover how to clone a repository from GitHub. GitHub is an online platform that hosts repositories for users to interact with on their own projects and collaborative projects.
# 
# Here is a [Git tutorial](https://www.youtube.com/watch?v=HVsySz-h9r4) you can watch in your spare time to advance your understanding of this distributed file-sharing system.
# 
# There are also numerous specialized [GUIs for Git](https://git-scm.com/downloads/guis/). These are effectively different editors for Git and you can choose one that you like. We recommend you search for a simple introductory tutorial on the editor of your choice as well.
# 
# The following steps outline how to get started with Git, sign up for a GitHub account, create a repository, and clone a repository to your computer:

# 1. Open your browser and go to https://git-scm.com/downloads and download Git for your operating system
# 
# 2. Create a new repository by browsing to the folder on your computer that you'd like to work under. From this folder, run the command: git init
# 
# 3. Open your browser and go to https://github.com/ and sign up for a Github account
# 
# 4. On GitHub, navigate to the main page of the repository you are interested in using. Note that when you create a repository on GitHub, it is a remote repository. We will clone a repository to create a local copy on your computer and we can then sync between the two locations when needed. Hence, we will have a local copy of the repository and a remote copy of the repository.
# 
# 5. Under the repository name on Github, click clone or download
# 
# 6. In the Clone with HTTPS section, copy the clone URL link
# 
# 7. Open your command line and navigate to the current working directory to the location where you want the cloned directory to be made. Type and run the command: git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY (paste the link that you copied before).
# 
# You should have now created your local clone of the repository. Let's cover some of the utilities available with Git.

# ## Understanding the Git workflow
# 
# Git is a distributed version-control system. This means that it allows you to track _changes_ to a set of files. You might be used to seeing files with names like "Essay(2)(2)\_FINAL(2)\_edits2March(3).docx" as you try to keep different versions of a file in sync while it is being changed by multiple people. Git solves this problem by tracking changes as specific **commits**, allowing you to go back in time to previous versions, and merge versions of files worked on by different people.
# 
# Git is an advanced and highly complex tool with a steep learning curve, so don't worry if not everything makes sense from the start. You'll only need to learn a few concepts to start using Git. Specifically, you'll need to know how to:
# 
# * Indicate which files you want to track using git
# * Commit changes to these files at specific points in time
# * Push these changes to a remote host
# 
# Note the difference between "git" (the software you run locally that has been in use for years) and "GitHub" (the most popular host for git repositories). You'll use the software `git` on your local machine, and then push your code to GitHub for sharing, collaboration, and as a backup of your files.
# 
# The most important git commands you'll need to use in the beginning are `git add` (which indicates which files you want git to track), `git commit` (which indicates when you want to create a "checkpoint" of your tracked files) and `git push` (which indicates when you want to push data from your local machine to GitHub).
# 
# Let's go through a simple example of committing a change to some text file ```hello.txt```:
# 
# 1. Create a text file `hello.txt` on your local computer in the folder you will be using Git from.
# 
# 2. Edit the file to add one line to the text file; e.g. you add "Hello World" as the first line. Save the file.
# 
# 3. Track this file using git. To do this, use the command: ```git add hello.txt```. (If you have multiple files and you'd like to add all the files with changes in the folder to be tracked by git you can use the command: ```git add *```)
# 
# 4. To commit the changes on all tracked files, use the command: ```git commit -m "Commit message"``` where "Commit message" should be a short but descriptive reminder of the changes you've made since the last time you ran a commit (for the first one, you can use something like "initial commit" as a message, but using as descriptive a message as possible will help debug any problems further down the line).
# 
# 5. You've created a checkpoint of your files now (something you could revert back to later if needed), but it still only exists on your local machine. To push the changes to your remote repository, use the command: ```git push origin master```
# 
# Some other useful commands that you can use to check the status and history of your repository include:
# 
# * ```git status```, which shows you whether files are untracked, or tracked but have changes and need to be committed.
# * ```git log```, which shows you a list of commit messages that have been applied.

# This covers the basics of Git. While it takes considerable practice to master, we've covered the cloning, adding, committing, and pushing features that are the backbone of the Git version control software.
# 
# We're ready to begin the case.

# # Identifying Expansion Opportunities for Luxury Commercial Airline Flights

# ## Case Introduction
# 
# **Business Context.** You are an employee for GrowthAir, a growing commercial airline company. In the past few years, GrowthAir has expanded luxury flight services to locations across the globe. Following your team's excellent performance in identifying new business opportunities last year, you have been tasked with identifying the top countries to further expand GrowthAir's luxury flight service.
# 
# **Business Problem.** Your manager has asked you to answer the following question: <b>"In which countries should GrowthAir expand its luxury flight service?"</b>
# 
# **Analytical Context.** The relevant data is a series of success estimates (i.e. probabilities of success) that your internal marketing research teams have come up with. Using your ability to conduct data analysis in Python, you will embark on summarizing the available success estimates to produce a concise recommendation to your boss.
# 
# **Execution**. In this case, you will look at simple metrics on the data such as mean, median, min/max, and ultimately make your suggestion based on these elementary statistics. The analysis portion should be relatively simple and every student should be able to do this with pen and paper. However, what is special about this case is that you will perform these tasks in a Python environment to familiarize yourself with new techniques and tools. 

# ## Fundamentals of Python
# 
# [Python](https://docs.python.org/3/) is an [interpreted, high-level general-programming language](https://www.webopedia.com/TERM/O/object_oriented_programming_OOP.html) that was first released in 1991. Python allows users to easily manipulate data and store values in what are known as <b>objects</b>. Everything in Python is an object and has a <b>type</b>. 
# 
# For example, if a user aims to store the integer 5 in an object named ```my_int```, this can be accomplished by writing the Python statement, ```my_int = 5```. If you're used to syntax from mathematics, this can seem confusing. In this case `my_int` is a variable, much like you might find in algebra, but the `=` sign is for _assignment_ not _equality_ (the latter is denoted with `==`). So in this case `my_int = 5` should be taken to mean something more like `Let my_int be equal to 5` rather than `my_int is equal to 5`.
# 
# Here, `my_int` is an example of a _variable_ because it can change value (we could later assign a different value to it) and it is of type Integer, known in Python simply as `int`. Unlike some other programming languages, Python guesses the type of the variable from the value that we assign, so we do not need to specify the type of the variable explicitly.
# 
# Python variables have a variety of data types. If you are used to using Microsoft Excel, this is similar to how Excel distinguishes between data types such as Text, Number, Currency, Date, or Scientific. Here are some common data types that you will come across in Python:
# 
# 1. Integers, type ```int```: ```my_int = 1```
# 2. Float type ```float```: ```my_float = 25.5```
# 3. Strings, type ```str```: ```my_string = 'Hello'```
# 
# Note that the names `my_int`, `my_float` and `my_string` are arbitrary here. While it is useful to name your variables so that the names contain some information about what they are used for, this code would be functionally identical to if we had used `x`, `xrtqp2` and `my_very_long_variable_name`, respectively.
# 
# Here we see (1) <b>integers</b> and (2) <b>floats</b> store numeric data.  The difference between the two is that floats store decimal variables (fractions), whereas the integer type can only store integer variables (whole numbers). Finally, (3) is the <b>string</b> type. Strings are used to store textual data in Python (a string of one or more characters). Later in this case we will use string variables to store country names. They are often used to store identifiers such as person names, city names, and more.
# 
# There are other data types available in Python; however, these are the three fundamental types that you will see across almost every Python program. Always keep in mind that **every** object in Python has a type and some of these "types" can be custom-defined by the user, which is one of the benefits of Python.
# 
# The simplest use of Python is as a calculator. We have seen how to assign values to variables, but we can also carry out computations on these variables. A Python program contains one or more lines of code, which are executed in a top-down fashion (with some exceptions that we'll come across later). The following Python program demonstrates this functionality:
# 
# ```
# x = 5
# y = 7
# z = x + y -1 
# print(z)
# ```
# 
# The `print` function simply outputs data to your screen (it has nothing to do with a computer printer, and won't waste your ink or paper!). In the code above, we start at the top and work down. This means we assign the value `5` to the variable `x`, then the value `7` to the variable `y` and finally the sum of the values `x` and `y` minus `1` to the variable `z`. Make sure that you can create this Python program and that you get the output `11` before you continue.
# 
# There is a lot more to Python than the above. In this case, we will introduce you to more basic Python concepts. If you prefer, you can first go through the more extensive [official Python tutorial](https://docs.python.org/3/tutorial/introduction.html) and/or the [W3School Python tutorial](https://www.w3schools.com/python/) and practice more fundamental concepts before proceeding with this case. It is highly recommended that you go through either or both of these tutorials either before or after going through this notebook to solidify and augment your understanding of Python.

# ### Exercise 0:
#  
# #### 0.1
# 
# * Use Python to calculate the answer to 1675 - 886 and print it out
# 
# * Assign your name to a Python variable and print it out
# 
# * Calculate the result of 65.4 + 7 - 6 + 2 and print it out

# kevin=1675-886
# print(kevin)
# print(65.4+7-6+2)

# -------

# #### 0.2
# 
# We mentioned before that variables can change value. Let's take a look at how this works, and also introduce a few more Python operations:

# In[5]:


x = 4
print(x)
y = 2
x = y + x
print(x)


# Again, if you're used to syntax from mathematics "x = y + x" might look very wrong at first glance. However, it simply means "throw out the existing value of x, and assign a new value which is calculated as the sum of y and x". Here, we can see that the value of x changes, demonstrating why we call them "variables".
#     
# We can also use more operators than just `+` and `-`. We use `*` for multiplication, `/` for division, and `**` for power. The standard order of operations rules from mathematics also applies and parentheses `()` can be used to override these:

# In[12]:


x = 2
y = 3
print (x + y ** x)
print((x+y)**x)


# Now try it yourself. Assign the values 3, 4, 5 to three different variables called `a`, `b`, and `c`, and calculate the values of 
# 
# * `c` squared
# * `a` squared + `b` squared

# a=3
# b=4
# c=5
# print(c**2)
# print(a**2+b**2)

# a=3
# b=4
# c=5
# print(c**2)
# print(a**2+b**2)

# Now that we've covered the fundamentals of Python, let's take a look at GrowthAir's proprietary company data on country success estimates.

# ## Exploring company data on success estimates
# 
# Your company has some proprietary data that they need you to analyze. This data consists of estimates of the probability of success for global expansion projects by country, created by several leading analysis agencies.
# 
# The ```success_estimates``` variable below is a Python dictionary. Before, we showed how variables could contain simple data types like a single integer, or a string. As an extension of that, variables can also refer to **data structures**. These are more complicated data types that comprise many single pieces of data, organized in a specific way.
# 
# As before, we use `=`, the **assignment operator**, to assign a value to the variable. 
# 
# Python's dictionary type stores a mapping of key-value pairs that allow users to quickly access information for a particular key. By specifying a key, the user can return the value corresponding to the given key. Python's syntax for [dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) uses curly braces {}:
# 
# ```python
# user_dictionary = {'Key1': Value1, 'Key2': Value2, 'Key3': Value3}
# ```
# 
# The ```success_estimates``` dictionary has keys which are strings, and values which are of type <b>list</b>. A [list](https://www.w3schools.com/python/python_lists.asp) is an incredibly useful data structure in Python that can store any number of Python objects, and are denoted by the use of square brackets ```[]```. 
# 
# In ```success_estimates``` below, the list contains float types. Lists are versatile and can be expanded by adding new elements to the end of the list (the right-most side is considered the end of the list). Moreover, list elements (i.e. the objects in the list) can be accessed easily using integer indices. Interestingly, lists can also store other lists (called a lists of lists).  This makes them a powerful tool for holding complex data sets.
# 
# Let's take a look at the ```success_estimates``` data. Each estimate (each item in each list) here is a number (float) between 0 and 1 inclusive, which represents the probability that expanding to that country will be successful. For example, we have 4 estimates of success for expanding into Australia, These are 0.6 (fairly likely that we will succeed), 0.33 (fairly unlikely that we will succeed), 0.11 (very unlikely that we will succeed) and 0.14 (also very unlikely that we succeed). Overall, Australia does not seem like a good choice.

# In[13]:


# Lines that start with the `#` symbol are comments, and are ignored by Python completely
# They only exist to make your code more readable for humans
# It's good practice to have one or more comments above non-obvious parts of code 
# to explain what they do

# Data on probability of expansion success by country estimates
success_estimates = {
    'Australia': [0.6, 0.33, 0.11, 0.14],
    'France': [0.66, 0.78, 0.98, 0.2],
    'Italy': [0.6],
    'Brazil': [0.22, 0.22, 0.43],
    'USA': [0.2, 0.5, 0.3],
    'England': [0.45],
    'Canada': [0.25, 0.3],
    'Argentina': [0.22],
    'Greece': [0.45, 0.66, 0.75, 0.99, 0.15, 0.66],
    'Morocco': [0.29],
    'Tunisia': [0.68, 0.56],
    'Egypt': [0.99],
    'Jamaica': [0.61, 0.65, 0.71],
    'Switzerland': [0.73, 0.86, 0.84, 0.51, 0.99],
    'Germany': [0.45, 0.49, 0.36]
}


# Above, we have defined out dataset, mapping specific countries to lists of values (estimates). The simplest thing we can do with this data is to output it, again using the `print()` function as follows:

# In[14]:


#no quotations marks needed when printing an existing variable
print(success_estimates)


# We would like to recommend that the business put effort into the country with the highest success estimate. But what does this mean when there are multiple success estimates for some countries, and only one for others? We can use metrics such as averages to resolve this. We will explore this next.

# ## Interacting with dictionaries and lists
# 
# Taking a careful look at the ```success_estimates``` dictionary, you notice some countries only have one success estimate, while others have many. For example, England has only one estimate contained in its list [0.45], while Jamaica has three estimates contained in its list [0.61, 0.65, 0.71]. Let's zoom in on Jamaica and take a look at some summary statistics of the estimates.
# 
# In Python, the dictionary type has built-in methods (functions, which we will discuss later) to access the dictionary keys and values. These methods are called by typing ```.keys()``` or ```.values()``` after the dictionary object. We will change the return type of calling ```.keys()``` and ```.values()``` to a list by using the ```list()``` method.

# In[15]:


# Look at the keys...
success_estimates.keys()


# Note above that the first thing you see is `dict_keys`, indicating the **type** of the data. Let's convert it to a list which is a simpler and more common data type. We can do this by passing the data into `list(...)`

# In[16]:


# now let's look at the keys in list form. This is more legible and usable for us later on.
list(success_estimates.keys())


# Note above that the data is similar but no longer starts with `dict_keys`:

# In[17]:


# We can also see the corresponding values (estimates) for each key as follows
list(success_estimates.values())


# We will make use of the access to keys and values of a dictionary later in the case when comparing across numerous countries' estimates. For now, just remember that you can access a dictionary's full list of keys or values simply by calling built-in methods.
# 
# We'd also like to check if a country name is one the keys in the dictionary. Python allows us to check if a key is in a dictionary through the use of the ```in``` keyword. The statement ```key in dictionary``` will return a <b>boolean type</b> of ```True``` if the key is one of the keys in the dictionary and ```False``` otherwise. Let's take a look at how this works.

# In[18]:


print('Checking if Morocco key is present:')
print('Morocco' in success_estimates) # print the VALUE of "Morocco in success_estimates"

print('Checking if Japan key is present:')
japan_boolean = 'Japan' in success_estimates
print(japan_boolean)


# We'd now like to access the value corresponding to a specific key in the ```success_estimates``` dictionary. Simply type the value name in square brackets adjacent to the dictionary name. For example, ```success_estimates['Jamaica']``` will return Jamaica's list of estimates:

# In[19]:


success_estimates['Jamaica'] 


# If you would like to store the result in a variable to be used later, use the assignment operator ```'='```:

# In[20]:


jamaica_list = success_estimates['Jamaica'] 


# You can then view the contents of the list via the ```print()``` method:

# In[21]:


print(jamaica_list)


# To access specific items in a dictionary, we used the **key name**. For example, we used `success_estimates['Jamaica']` to access the data about Jamaica. By contrast, to access specific elements in a list, we use an **index**, stating whether we want to access the first element, the second element, etc. Python uses **zero-based indexing**, which can be confusing at the start. This means that the first item in the list has index `0`, the second item has index `1`, and so on.
# 
# We can access each of the first three items in the `jamaica_list` variable as follows:

# In[22]:


# Each successive print statement will print on a new line
print(jamaica_list[0]) # prints the first element of the list
print(jamaica_list[1]) # prints the second element of the list
print(jamaica_list[2]) # prints the third element of the list


# [Slicing and indexing lists](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/) (among other objects such as arrays, dataframes) is a crucial and essential part of basic Python. You will see this often in your data science career. Instead of accessing a single item in the list, we can access sublists of the list as follows.

# In[23]:


# taking the last 2 elements of jamaica_list
print(jamaica_list[-2:])  # (go from the second last element until the end)
print(jamaica_list[1:])  # (go from the secon d element until the end)


# In[24]:


# multi-layered slicing
print(success_estimates['Jamaica'][0]) # getting the first jamaican estimate from the dictionary


# Above, we do both in a single line of code. In most cases, Python operates from left to right, so it will first get the "Jamaica" item from the dictionary, and then get the first (zeroth) item from that list.

# Python also offers a simple way to determine the length of a list: the ```len()``` method. We expect the length of ```jamaica_list``` to be 3 since it has three elements:

# In[29]:


len(jamaica_list) # returns the length of the list


# ### Exercise 1:
# 
# Print the length of the success estimate lists for France, Greece, and Morocco.

# **Answer.**

# In[203]:


France_list = success_estimates['France'] 
Grecee_list = success_estimates['Greece'] 
Marocco_list = success_estimates['Morocco'] 
print(len(France_list))
print(len(Grecee_list))
print(len(Marocco_list))


# ### Exercise 2:
# 
# Which of the following would be useful to store project success estimates if they were available at a regional level instead of a country level?
# 
# (a) List
# 
# (b) Dictionary
# 
# (c) Float
# 
# (d) String
# 
# **Answer.** 

# (b) Dictionary

# Now that we're familiar with using lists and know that lists are ordered data structures while dictionaries are unordered data structures, let's begin to compare success estimates across countries.

# ## Calculating a country-specific average success estimate

# Continuing our analysis on Jamaica, the list contains three numbers, [0.61, 0.65, 0.71]. Recall these numbers are of type ```float``` in Python, which stores numeric decimal values. One logical way to summarize these estimates so that they can be compared across countries is to use the arithmetic average. Let's use basic arithmetic operators to calculate the average success estimate for Jamaica, storing the result in a new variable ```avg_jamaica```.

# In[45]:


avg_jamaica = (0.61 + 0.65 + 0.71) / 3
print(avg_jamaica)


# We see the average probability of success estimate for Jamaica is approximately 0.657.  However, we produced this estimate by hand-coding the values. If we were to do this for every country, it would take quite a long time. So we'd like to use a more automated way of producing the average.

# To produce an average we can utilize a <b>function</b>. Functions operate on data and variables in Python to perform a desired action. Functions may have both <b>inputs</b> and <b>outputs</b>, just like familiar mathematical operators like addition, subtraction, multiplication, and division (which each have two inputs and one output). While functions in Python may still be for a mathematical purpose, such as squaring an integer, Python allows for more abstract function behaviour, such as printing to the screen. In this case, the ```print()``` function will print its input to the screen.

# Let's use Python's built-in mathematical functions ```sum()```, ```min()```, and ```max()``` to calculate Jamaica's average success estimate, minimum success estimate, and maximum success estimate, respectively:

# In[31]:


country_name = 'Jamaica'
jamaica_list = success_estimates[country_name] # list of the estimates for Jamaica
print(jamaica_list)


# In[32]:


avg_jamaica = sum(jamaica_list) / len(jamaica_list)
min_jamaica = min(jamaica_list)
max_jamaica = max(jamaica_list)
print("Country:",country_name,", Average:",avg_jamaica)
print("Country:",country_name,", Min:",min_jamaica)
print("Country:",country_name,", Max:",max_jamaica)


# Above, note how we pass the entire `jamaica_list` as input to the `min()` function. The output is then immediately assigned to a new variable which we have called `min_jamaica`. Also, note how we can pass more than one argument to the `print()` function, separating them with commas. This allows us to combine dynamic (variable) data with fixed descriptive strings to get readable outputs. We'll come across better ways to combine variable data into strings later on.

# As expected, we get the same average result of approximately 0.657. Note that we could also have rounded the results to two decimal places using the [round()](https://www.w3schools.com/python/ref_func_round.asp) method. This can improve readability.

# In[42]:


avg_jamaica = round(sum(jamaica_list) / len(jamaica_list),2)
min_jamaica = round(min(jamaica_list),2)
max_jamaica = round(max(jamaica_list),2)
print("Country:",country_name,", Average:",avg_jamaica)
print("Country:",country_name,", Min:",min_jamaica)
print("Country:",country_name,", Max:",max_jamaica)


# Functions in Python are a very powerful tool to increase productivity and perform more complex tasks.

# ### Exercise 3:
# 
# Write a script to calculate the average success for every country. Output (using ```print()```) each country's average success estimate to the screen. The print statements should output each country on a new line, for example:
# ```
# Country: France , Average: 0.655
# Country: Brazil , Average: 0.29
# ```

# **Answer.**

# In[206]:


for country, value in success_estimates.items():
    med= sum(value) / len (value)
    print('Country: {} , Average: {} '.format(country,med))


# ## Systematically determine the average success estimate for all of the countries

# The end goal of this analysis is a recommendation for where global expansion opportunities should be considered. To reach a conclusion, it'd be ideal to have the average success probability for each country.
# 
# To achieve this, we will use a control flow element in Python -  the [for loop](https://www.w3schools.com/python/python_for_loops.asp).  The ```for``` loop allows one to execute the same statements over and over again (i.e. looping). This saves a significant amount of time coding repetitive tasks and aids in code readability.  The general structure of a `for` loop is:
# 
# ```python
# for iterator_variable in some_sequence:
#     statements(s)
# ```
# 
# The `for` loop iterates over ```some_sequence``` and performs ```statements(s)``` at each iteration. That is, at each iteration the ```iterator_variable```  is updated to the next value in ```some_sequence```. As a concrete example, consider the loop:
# 
# ```python
# for i in [1,2,3,4]:
#     print(i*i)
# ```
# 
# Here, the `for` loop will print to the screen four times; that is it will print ```1``` on the first iteration of the loop, ```4``` on the second iteration, ```9``` on the third, and ```16``` on the fourth. Hence, the `for` loop statement will iterate over all the elements of the list ```[1,2,3,4]```, and at each iteration it updates the iterator variable ```i``` to the next value in the list ```[1,2,3,4]```. In `for` loops, it is an extremely good habit to choose an iterator variable that provides context rather than a random letter. In this case, we will use both to get you accustomed to both since you will mostly likely see both throughout the course of your data science career, but we encourage you to not use a generic name like `i` whenever possible for ease of communication.
# 
# Let's use a `for` loop on our country data by getting a list of all the keys in ```success_estimates```:

# In[102]:


# Get all the keys from the success_estimates dictionary
country_name_list = list(success_estimates.keys())
print(country_name_list)


# Here we loop through all the elements in ```country_name_list```, extract the corresponding value from ```success_estimates``` (which will be of type list), and subsequently take the mean of the list. Detailed printing will guide you through the `for` loop execution:

# In[29]:


# Loop through all countries and calculate their mean success estimate
for i in country_name_list:
    print('--Begin one iteration of loop--')
    print('Element of country_name_list, placeholder i = ' + i)
    print('Access value from dict success_estimates[i]: ', success_estimates[i])
    print('Average of list from success_estimates[i]: ', sum(success_estimates[i]) / len(success_estimates[i]))
    print('--Go to next iteration of loop--')
    print()


# Let's take a closer look at the above ```for``` loop. The ```country_name_list``` has 15 countries which the ```for``` loop is iterating over. The ```for``` loop uses a placeholder variable, denoted ```i``` in this case, to store the element of ```country_name_list``` that each loop iteration corresponds to. Namely, for the first iteration of the ```for``` loop, ```i = 'Brazil'```. For the second iteration, ```i = 'Canada'```. And so on until the loop reaches the final element of ```country_name_list```, which it then completes and exits the looping process.
# 
# Why is this looping process useful? Well, we've performed the same calculation statements 15 times while only writing the code once! Notice that for each iteration, the corresponding value from ```success_estimates``` is accessed, and the mean of the returned list is calculated. The ```for``` loop process also enhances code readability.

# ### Exercise 4:
# 
# Write a `for` loop to instead calculate the minimum and maximum of each country's list of success estimates, printing each out consecutively as in the `for` loop example above.

# **Answer.**

# In[207]:


for i in country_name_list:
    print('--Begin one iteration of loop--')
    print('Element of country_name_list, placeholder i = ' + i)
    print('Access value from dict success_estimates[i]: ', success_estimates[i])
    print('Min of list from success_estimates[i]: ', min(success_estimates[i]))
    print('Max of list from success_estimates[i]: ', max(success_estimates[i]))
    print('--Go to next iteration of loop--')
    print()
   


# ### Exercise 5:
# 
# Using the `for` loop, write code to determine the country with the largest range of success estimates (that is, the largest difference between the smallest and largest estimate for a country).

# **Answer.**

# In[208]:


Vect = [[i,round(max(success_estimates[i]),2)-round(min(success_estimates[i]),2)] for i in success_estimates] 
Vect_ordenados = sorted(Vect, key=lambda x : x[1], reverse=True)
Vect_ordenados


# ## Using list comprehensions to determine the number of estimates

# Moving forward, we are interested in knowing the number of success estimates available for each country. Python offers a concise way to achieve this goal through the use of <b>list comprehensions</b>. Every list comprehension can also be rewritten as a `for` loop. The list comprehension syntax is simply more concise.
# 
# [List comprehensions](https://www.programiz.com/python-programming/list-comprehension) allow one to concisely build a list. Let's take a look at how this works:

# In[101]:


key_name_list = [i for i in success_estimates] # loop over each item i in success_estimates and put i in the list
key_name_list


# Here we see that we've looped over each key of the dictionary `success_estimates` (hence each country), and extracted the country name, all in one line of code. We can also access the values of each key in `success_estimates`:

# In[194]:


value_name_list = [success_estimates[country] for country in success_estimates] # loop over each item in success_estimates and put success_estimates[i] in the list
value_name_list    


# In the list comprehension above, each value of the ```iterator_variable``` is a country name and the value is returned when ```success_estimates[country]``` is called. We see the list comprehension is an effective and concise way to write a `for` loop that creates a list.
# 
# We can use this to quickly determine how many success estimates are available for each country:

# In[202]:


#Number of estimates available for each country
[[i, len(success_estimates[i])] for i in success_estimates] 


# ### Exercise 6:

# Using list comprehensions, write a script to create a <b>list of lists</b> called ```sum_squares_list```, where each element of the list is a two-item list [country name, value]. The value item in the list should be the sum of squares of that country's success estimates. For example, one element of ```sum_squares_list``` should be for Jamaica, where the two-item list is [Jamaica, 1.2987] (since 1.2987 = 0.61^2 + 0.65^2 + 0.71^2).

# **Answer.**

# In[212]:


sum_squares_list=[[i, sum(k*k for k in values)] for i , values in success_estimates.items()]
print(sum_squares_list)


# ### Exercise 7:
# 
# We'd like to determine the spread around the mean success estimate for each country. Using list comprehensions, write a script that subtracts the mean success estimate for a given country from each success estimate for that country. Store the results in a list named ```removed_mean_list```. Round values to two decimal places. Your output should produce the following list of lists:
# 
# ```
# [['Australia', [0.3, 0.03, -0.19, -0.16]],
#  ['France', [0.01, 0.12, 0.32, -0.46]],
#  ['Italy', [0.0]],
#  ['Brazil', [-0.07, -0.07, 0.14]],
#  ['USA', [-0.13, 0.17, -0.03]],
#  ['England', [0.0]],
#  ['Canada', [-0.03, 0.02]],
#  ['Argentina', [0.0]],
#  ['Greece', [-0.16, 0.05, 0.14, 0.38, -0.46, 0.05]],
#  ['Morocco', [0.0]],
#  ['Tunisia', [0.06, -0.06]],
#  ['Egypt', [0.0]],
#  ['Jamaica', [-0.05, -0.01, 0.05]],
#  ['Switzerland', [-0.06, 0.07, 0.05, -0.28, 0.2]],
#  ['Germany', [0.02, 0.06, -0.07]]]
# ```

# **Answer.**

# In[221]:


removed_mean_list=[[i, list((k-sum(values)/len(values)) for k in values)] for i , values in success_estimates.items()]
print(removed_mean_list)


# As list comprehension gets more complicated, it becomes more and more important to use proper naming conventions for variables. Good naming conventions dramatically improve the readability of your code.

# ## Reflecting on the country-specific mean success estimate

# Based on the above analysis, we see the mean country success estimates vary widely, from the lowest, Canada = 0.275, to the highest, Egypt = 0.99. However, notice that Egypt's mean is calculated from 1 success estimate. Are we confident in trusting a single estimate as a proxy for the average success estimate?
# 
# Given that the global expansion project will utilize valuable company resources, we decide it is best to restrict our analysis to countries that have two or more success estimates. To accomplish this task, we will use a control structure in Python known as the <b>[if...elif...else statement](https://www.w3schools.com/python/python_conditions.asp)</b>. The general structure follows:
# 
# ```python
# if test_expression_1:
#     block1_statement(s)
# elif test_expression_2:
#     block2_statement2(s)
# else:
#     block3_statement(s)
# ```
# 
# Here, ```test_expression_1``` and ```test_expression_2``` must evaluate to ```True``` or ```False```, a Python <b>boolean</b> type. The boolean type is associated with variables that are either ```True``` or ```False```.
# 
# If ```test_expression_1``` is True, ```block1_statement(s)``` will execute and the other block statements will not. If ```test_expression_1``` is False yet ```test_expression_2``` is True, then ```block2_statement2(s)``` will execute and the others will not. Finally, if ```test_expression_1``` and ```test_expression_2``` are both False, then the else section's ```block3_statement(s)``` will execute. This conditional structure of an if statement allows one to control the flow of Python code.
#     
# The `elif` and `else` blocks are optional. You can also have a plain `if` block that simply executes some lines of code or skips them, depending on the evaluation of the conditional. As an example, let's look at only two countries from our dataset: Italy and Jamaica:

# In[222]:


italy = success_estimates['Italy']
jamaica = success_estimates['Jamaica']

print(len(italy) > 1)
print(len(jamaica) > 1)


# Above, we used the greater than operator `>` to compare two numbers and produce a boolean (the simplest Python data type - always either True or False). In the first case, we got False because the length of the `italy` list is **not** larger than 1. Put differently, it is not True that 1 > 1, so we get False. By contrast, Jamaica has 3 items, so the evaluation simplifies to `3 > 1` which is True, so on the second line above we see the output `True`.
# 
# We can combine these expressions with `if` statements to control the flow of our code. An example is shown below:

# In[223]:


if len(italy) > 1:
    print("Italy has more than 1 estimate")

if len(jamaica) > 1:
    print("Jamaica has more than 1 estimate")


# Above, we can see that the second line of code got skipped. It was never executed and we see no output for the statement that is "gated off" there.
#     
# The above shows two separate `if` blocks. Note that there is a difference between having two separate `if` blocks and an `if else` block, as shown below:

# In[224]:


# **Incorrect logic warning**
if len(italy) > 0:
    print("Italy has more than 0 estimates")
elif len(jamaica) > 0:
    print("Jamaica has more than 0 estimates")
else:
    print("this will only execute if neither of the above lines do")


# The example above shows how careful you have to be when coding. We use `0` instead of `1` as the minimum length of the list that we are interested in. Because the first statement evaluates to `True` (Italy *does* have more than zero estimates), Python skips the rest of the code without looking at it. Even though the next condition for Jamaica is _also_ true, because it is in an `elif` block it will never execute if any expression further above in the same block evaluated to True.
#    
# You'll see more advanced use of conditional logic using `if` later. For now, let's combine `if` statements with `for` loops to filter out all of the countries that only have one success estimate.

# ## Selecting only multi-observation countries for global expansion potential

# We will use the if statement above to remove countries with less than one success estimate. For convenience of viewing the result, we will store the mean estimates for each country in a new dictionary ```country_means```:

# In[225]:


# Get a list of all the country names
country_name_list = list(success_estimates.keys())

# Create an empty dictionary to hold country mean estimates
country_means = {}

# Loop through all countries and calculate their mean success estimate
for i in country_name_list:
    list_country_estimates = success_estimates[i] # list of estimates for a country

    # if more than one country estimate, then record the mean estimate, otherwise go to next loop iteration
    if len(success_estimates[i]) > 1:
        print("adding the mean for",i)
        country_mean_value = sum(list_country_estimates) / len(list_country_estimates)
        country_means[i] =  country_mean_value # insert country mean value into dict using country name as key
    else:
        print("....skipping", i)


# Note that countries which do not have more than one estimate are skipped. Not only are the `print` lines ignored, but every line in the `if` block are also ignored, so the means for the countries with only one estimate are not added to `country_means`.

# Let's format our results, [modifying the string output](https://www.geeksforgeeks.org/python-format-function/) to the screen to use 2 decimals when printing the float type. This is accomplished using the string type's ```.format()``` functionality. The ```{0:s}``` and ```{1:.2f}``` in the string indicate to the ```.format()``` method to format the first variable it receives as input as a string and replace the ```{0:s}``` placeholder, and to format the second variable it receives as input as a 2-decimal float and replace the ```{1:.2f}``` placeholder.
# 
# With this formatting, the ```country_key``` variable will be displayed as a string in place of ```{0:s}```, while the ```country_means[country_key]``` variable will be displayed as a 2-decimal float in place of ```{1:.2f}```.  This advanced string formatting approach is useful to improve the clarity of the results:

# In[41]:


# Nicely format the result for printing to the screen
for country_key in country_means: 
    print("Country: {0:s}, Avg Success Estimate: {1:.2f}".format(country_key, country_means[country_key]))


# Observing the resulting country means, we notice the country with the largest mean success estimate is Switzerland at 0.79, while the lowest mean success estimate is Canada at 0.28.

# ### Exercise 8:
# 
# After reviewing company policy on statistical procedures, you notice the company recommends that all estimates (averages, minimums, maximums) must have at least three values contributing to the summary statistic. Write a `for` loop and use the ```if``` statement structure to select and print the average success estimates for the countries satisfying this policy. If the country does not satisfy the policy, print the country name and ``"*Does not meet company policy*"``. Each country should appear on a new line.

# **Answer.**

# In[286]:


[[i, round(sum(k for k in values),2),max(t for t in values), min(m for m in values)]
         if len(values)>2 else (print("*Does not meet company policy:{}".format(i))) 
         for i , values in success_estimates.items()]


# ### Exercise 9:
# 
# In addition to the above policy, the company wants to flag countries where the range of estimates is too big, as this is usually due to the estimates being taken at very different times, or outright containing errors. They want to pay special attention to cases where the range (the difference between the largest and smallest estimates) is larger than 0.6. Calculate the range for each country and indicate if it should be flagged.

# **Answer.**

# In[264]:


policy= [print(['should be flagged', i]) 
     if   (max(success_estimates[i])-min(success_estimates[i])) >0.6 else (print("[ Not should be flagged:{}".format(i))) 
     for i in success_estimates] 


# ### Exercise 10:
# 
# What is another approach to resolve the one-sample problem for some countries? Think in terms of the factors that drive confidence in data-driven business decisions.
# 
# (a) Group countries together to larger regions to ensure each region has at least one estimate
# 
# (b) Only remove a country if its estimates are very large or very small compared to other estimates
# 
# (c) Use a different summary statistic for the analysis other than the average value
# 
# (d) Revisit why some countries only have one estimate and see if more data can be sourced for these countries
# 
# **Answer.**

# (d)

# ## Putting it all together

# We've used for loops and control structures to calculate partial summary statistics for each of the countries. Let's put it all together to obtain a recommendation on which country we should choose to expand the luxury flight services.

# ### Exercise 11:
# 
# Write code to print each country name and summary statistics. Each line should show one country and the corresponding summary statistics: Min Estimate (float), Average Estimate (float), Max Estimate (float), Number of Estimates (int), Meets Company Policy of at least 3 estimates (bool). For example, the line for France would appear as:
# ```
# Country: France , Min: 0.2 , Average: 0.655 , Max: 0.98 , NumEst: 4 , MeetsPolicy: True
# ```

# **Answer.**

# In[290]:


A=[print([("Country: {0:s}").format(i), ("Average: {}").format(round(sum(k for k in values)/len(values),2)),("Max: {}").format(max(t for t in values)), ("Min: {}").format(min(m for m in values)),("MeetsPolicy:{}").format(True if len(values)>2 else False)]) 
   for i , values in success_estimates.items()]


# ###  Exercise 12:
# 
# We can see that Switzerland has the highest average by looking at all of the values, but let's take this one step further and get Python to calculate that for us. 
# 
# Loop through the data again but keep track of the best country **that meets policy** and output data about only this country.

# **Answer.**

# In[311]:


b=[[round(sum(k for k in values)/len(values),2),i]
        for i,values in success_estimates.items() if len(values)>2] 
print(max(b))        


# ###  Exercise 13:
# 
# We found the best country on average, but we are also interested in the safest or most conservative choice. This is defined by looking only at the **minimum** (that is, the most pessimistic) estimate for each country and taking the highest of those (still only considering ones **that meet policy**). Write code to determine and output data about this country.

# **Answer.**

# In[312]:


b=[[min(values),i]
        for i,values in success_estimates.items() if len(values)>2] 
print(max(b))


# Note that above we used the Python `and` keyword to combine two booleans into one. The result is True only if **both** of the components are True. It has the same effect as the nested `if` statement in Exercise 12. You can read more about logical operators at the [W3Schools tutorial](https://www.w3schools.com/python/python_operators.asp).

# Before we conclude, let's push all of our work up to GitHub for safe keeping. 
# 
# * Make sure any code and notebook files you have open are saved
# * Open your command prompt or terminal application and navigate to your git repository (which should also contain your work)
# * run `git status` to check the status of files. Delete any files that you do not want to push to GitHub.
# * run `git add *` to add all the files
# * run `git commit -m "finished Python preparation case"`
# * run `git push origin master`
# 
# You should see output on your terminal confirming that the files were pushed, and if you log into github.com and navigate to your repository, you should see the files with the latest changes through the web interface.

# Now that we have summary statistics for a variety of country estimates, let's construct our actionable business recommendation.

# ## Conclusions
# 
# From the analysis, Switzerland is the country with the largest chance of success for global expansion with an estimated success rate of 0.79. The summary statistic for Switzerland was calculated with an adequate number of estimates according to company policy. Thus, it is recommended that management explore opportunities in Switzerland for luxury flight services. Jamaica is also recommended as a conservative choice. Although it did not come out top overall, none of the estimates gave it a very low probability.
# 
# In addition, another country that should be closely monitored for luxury flight services is France, which held a 0.66 average success estimate. If there are additional resources in the future for further luxury service expansion, France may be an apt choice, but more investigation should be done to see why one estimate gave France only a 0.2 success estimate.

# ## Takeaways
# 
# In this case, we've learned the foundations of Python. Through identifying global expansion opportunities for an airline company we've covered fundamental data types, control structures, and a useful Python workflow to analyze a given set of data. You also learned about various summary statistics and how much confidence you can have in drawing conclusions from them.
# 
# To recap, these are some of the building blocks of Python we just covered and we recommend you become very familiar with them before moving ahead:
# - variables
# - data types
# - `print` (how to format within `print` function)
# - lists
# - dictionaries
# - slicing/iterating
# - `for` loop
# - `if...elif...else` statements
# - list comprehension
# 
# You can use these Python tools as both a foundation and a framework to build more complex projects and solve critical business problems. Python continues to be an outstanding tool to perform data-driven analysis and deliver key business insights.
