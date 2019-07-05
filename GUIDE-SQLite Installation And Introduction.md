# SQLite

From the [SQLite homepage](https://www.sqlite.org/index.html), SQLite is a C-based library that implements a complete, although basic, SQL database engine (more information about SQL can be found [here](https://en.wikipedia.org/wiki/SQL)). While other SQL-based databases might require softwares to be installed, SQLite does not really (it requires files to be downloaded and extracted but not to be installed). It also has the advantages of being lightweight (the **lite** of SQ**Lite**), crossplatform and the database can be contained in a single file. However, SQLite does not natively incorporate security features (so no users and passwords). It is ideal for compact databases located in a single place on a device.

### Installing SQLite for your operating system

Go to the [SQLite download page](https://www.sqlite.org/download.html) and download the **shell** under the **precompiled binaries** for the relevant operating system (the **shell** should be marked as **tools**). Once downloaded, simply extract the files in the desired folder and sqlite will be ready to go. (On windows, you will also want the **dll** files.)

#### Adding SQLite to your PATH variable on windows

At this point, it should be possible for the user to directly execute the sqlite3.exe file through the graphical interface. However, since it is likely that sqlite will be ran through a **secure shell** on the cafeine2 server, it is a good idea to add sqlite3 to windows' system path variable. To do so, you will need to open your command prompt **as an administrator** and then type the following command before you hit enter :

```
> setx /m path "%path%;YOURPATH"
```

It should print a message about succeeding and the specific value being registered. This will allow your shell to execute sqlite3.exe from any working directory, regardless of where it is located on the computer.

#### On Cafeine2

Sqlite3 has already been added to the cafeine2 server, somewhere on its drive as well as on the system path. This means that if you want to practice directly on the server, you can simply log into it using a Secure Shell (**SSH**) and type `sqlite3` to begin. You can check the HOW-TO [here](https://github.com/DCC-Lab/Documentation/blob/master/HOWTO-MountPOMOnCafeine2.md) to learn to use the SSH and more.

### Installing SQLite for Python

Python already has tools integrated in its standard library for handling SQLite, in the form of the module `sqlite3`. However, other modules can be used such as `pysql` or `aspw`. These can be found these on [PyPi](https://pypi.org/). However, it is important to note that python is somewhat quirky when it comes to transactions and committing changes to the database. These quirks will be covered further below.

Also something to note, if you are using something like Anaconda to manage your python libraries, since python comes with sqlite3 in its standard library, you can use your Anaconda command prompt to activate sqlite by, again, simply typing `sqlite3` and pressing enter.

## Using SQLite in Shell

Now that you have a working **shell** for SQLite, it is possible to do your first few commands. You could run the sqlite3.exe you just downloaded but since you might have to run sqlite remotely, we will do so from the basic operating system shell. If you added the path to the sqlite3.exe folder to your system path as described above, you will be able to directly run sqlite by simply typing :

```
> sqlite3
```

Otherwise, you will have to first navigate to the directory where the exe file is located through your shell, then type the command above. You will get a message of confirmation containing information like your sqlite version and a connection to an in-memory database :

```
[...]
SQLite version #.#.# YYYY-DD-MM HH:MM:SS
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persitant database.
sqlite>
```

Once you are done doing whatever it was that you wanted to do in sqlite, type `.quit`/`.exit`/`.qui`/ and press enter to quit sqlite3. Also note that if you do a wrong command, say you type `quit` and press enter, nothing will happen and you might end up with something like this :

```
[...]
sqlite>quit
  ...>.quit
  ...>.exit
  ...>.kill
  ...>
```
This is because sqlite3 tries to *read* and *understand* your commands on several lines. If it can't find a pattern that it recognize from the start of your commands, it will keep reading until you tell it that it has reached the end of the command using `;`. At that point, it will most likely tell you that it cannot recognize your command :

```
[...]
sqlite>quit
  ...>.quit
  ...>.exit
  ...>.kill
  ...>;
Error: near "quit": syntax error
sqlite>
```

So remember that if you start seeing `...>`, you most likely forgot to put a `.` before your *dot command* or a `;` at the end of your *statement*.

## Connecting to or Creating a database

Although you might be led to believe that `.open FILENAME` can only open (or *connect to*) an existing database, it is not the case. It is also possible to create a database using `.open FILENAME`. If the `FILENAME` doesn't exist, sqlite will interpret the command as the user trying to create a new database and will act accordingly :

```
sqlite>.open test.db
sqlite>
```

SQLite will not give you any confirmation that you did create or connect to the database when you are successful. Note that you can also do `.open :memory:` to create an in-memory database. (It would seem that whenever you start sqlite3 through a command prompt as was done above, you will start in an in-memory database.) You can confirm in which database you are working by typing `.databases` or `.database`. If you do so, you should see :

```
sqlite>.open test.db
sqlite>.databases
main: YOUR/PATH/test.db
sqlite>.open :memory:
sqlite>.databases
main:
sqlite>
```

In the case of an in-memory database, `.main` will be left blank. An in-memory database will always be deleted once you disconnect from the database using `.quit`. However, these are useful when you want to create quick, temporary tables for an application and don't want to risk leaving files on your machine afterwards (in case of an error or a crash). Also, since it uses your RAM instead of your drive, it's much faster to read and write into an in-memory database than a persistant database. (See [here](https://en.wikipedia.org/wiki/In-memory_database) to know more.) No, to continue, you can start sqlite3 AND connect to or create a database directly from the command prompt using :

```
>sqlite3 test.db
SQLite version #.#.# YYYY-DD-MM HH:MM:SS
Enter ".help" for usage hints.
sqlite>
```

## Creating and Dropping a table

So far, all that you've done is use commands specific to SQLite3, called *dot commands* (`.`). While these commands are useful and can do various things, SQLite also uses a platform specific language called `SQL` (the **SQL** in **SQL**ite). This language has a different form and syntax than what you have seen so far. (Typing `.help` in sqlite will give you a list of all the dot commands available. You can also view them [here](https://sqlite.org/cli.html#special_commands_to_sqlite3_dot_commands_).) The first `SQL` command we will use, also called a *statement*, is the statement to [create a table](https://www.sqlite.org/lang_createtable.html) which is : `CREATE TABLE table_name(column_1 type_1, column_2 type_2);` While in sqlite3, you can try the following command :

```
sqlite>CREATE TABLE persons(first_name TEXT, last_name TEXT, age INTEGER);
sqlite>
```

In the above statement, `persons` is the table's name. `first_name`, `last_name`, and `age` are the columns. `TEXT`, `TEXT`, and `INTEGER` are the columns associated data type. The semicolon (`;`) is there to mark the end of the statement. If you forget it, sqlite will prompt you for a continuation of your statement until it finds a semicolon. It is also possible to see all tables in a database using the dot command `.table` which, in this case, would yield :

```
sqlite>.tables
persons
sqlite>
```

Only 5 data types are available in sqlite3, which are `NULL`, `TEXT`, `INTEGER`, `REAL`, and `BLOB`. Although this might seem restrictive, there are data affinities which are also recognized by sqlite3. These can be found [here](https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm) and provide more options as some sort of sub-types to your data types. Now that your first table is created, knowing how to delete a table which was made using the wrong name, columns and/or types might be useful. [Dropping](https://www.sqlite.org/lang_droptable.html) can be done in the same way, using the statement `DROP TABLE table_name;`, as follow :

```
sqlite>DROP TABLE persons;
sqlite>.table
sqlite>
```

Running `.table` immediately afterwards shows us that the table does not exist anymore. When creating a table, more options are available such as the use of [primary keys](https://www.sqlite.org/lang_createtable.html#primkeyconst) (and composite keys), [foreign keys](https://www.sqlite.org/foreignkeys.html), [autoincrementing](https://www.sqlite.org/autoinc.html) fields, not null fields, etc. However, all these are more advanced and more specific options not quite suitable for an introduction.

### Some Examples of tables

To insert data into a database, you must have a table first. In this example, we will start by creating two rather simple tables ; a table of positions at a company and a table of employees of said company.

```
sqlite>.open company.db
sqlite>.databases
main: YOUR/PATH/company.db
sqlite>CREATE TABLE IF NOT EXISTS positions(title TEXT PRIMARY KEY, salary INT NOT NULL);
sqlite>CREATE TABLE IF NOT EXISTS employees(id INT PRIMARY KEY, name TEXT, position TEXT, FOREIGN KEY (position) REFERENCES positions(title));
sqlite>.tables
employees positions
sqlite>
```

We can see three new things here : 
1. Although it doesn't really stop you from continuing working in sqlite when you are using it in a shell, the `IF NOT EXISTS` conditions is useful when you want to avoid trying to make two tables with the same name in the same database. If you were to try to do so, sqlite would throw an error and, say you were working in python, it might stop your script or throw errors.
2. The `PRIMARY KEY` constraint on some of the columns (columns are referenced as *keys* in `SQL`, similarily to python's dictionaries) means that those columns cannot be `NULL` (however, note that the `NOT NULL` implied by the `PRIMARY KEY` condition is not strictly enforced due to bugs in previous versions of sqlite) and must also always be different from other entries in the table (the `UNIQUE` constraint).
3. The `FOREIGN KEY` constraint means that this entry references to an entry in a *different table*. This is useful if you want to create relations between different tables.
4. The `NOT NULL` constraint means that whatever value is in that field can never be a `NULL` value.

## Inserting data into a table

If you've followed this guide, you know that databases are made of tables and those tables are made of keys (the columns) and rows (the entries). When you want to put data into the database, you will need to target a table and associate the keys with values. This means that you want to do an `INSERT` statement into the database. An `INSERT` statement usually has the following form :

```
INSERT INTO table (key_1, key_2, ...) VALUES (value_1, value_2, ...);
```

Following the example above, we have a database called **company.db** with a table called **positions**. This table has two keys, `title` and `salary`. And so an `INSERT` statement would something look like this :

```
[...]
sqlite>INSERT INTO positions (title, salary) VALUES ('President', 300000);
sqlite>
```

Now, if you did a table similar to the one in the example above and you want to test your constraints, you might want to try the two following inserts :

```
[...]
sqlite>INSERT INTO positions (title) VALUES ('Intern');
Error: NOT NULL constraint failed: positions.salary
sqlite>INSERT INTO positions (title, salary) VALUES ('President', 450000);
Error: UNIQUE constraint failed: positions.title
sqlite>
```

So we can see that our constraints, which are `PRIMARY KEY` on title and `NOT NULL` on salary are working as intended. You can also insert many new entries at once doing something like :

```
[...]
sqlite>INSERT INTO positions (title, salary) VALUES ('Intern', 10000), ('Engineer', 75000), ('Secretary', 30000);
sqlite>
```

## Reading data from a table (`SELECT`)

Databases aren't just meant to store data but to also provide that data at a later date. This means that you need to be able to read entries from a table. In `SQL`, this means that you want to do a `SELECT` statement on the table (or many tables). A `SELECT` statement, in its most basic shape, has the following syntax :

```
SELECT keys FROM table;
```

Still using the table created in the example above, we can quickly check if our table positions contains the right entries by doing a search on all keys using `*` :

```
[...]
sqlite>SELECT * FROM positions;
President|300000
Intern|10000
Engineer|75000
Secretary|30000
sqlite>
```

You can also specify the keys you want to get like so :

```
[...]
sqlite>SELECT title FROM positions;
President
Intern
Engineer
Secretary
sqlite>
```

A more advanced `SELECT` statement implies conditions. You can specify conditions using `WHERE` :

```
[...]
sqlite>SELECT * FROM positions WHERE title='Intern';
Intern|10000
sqlite>
```

The conditions following `WHERE` can get quite complex, which is where `SQL` has an advantage over other softward using tables like Excel, Google Sheets and Numbers. Using SQLite dot commands, you can also add some features to your queries and change the output, for example :

```
[...]
sqlite>.headers on
sqlite>.mode csv
sqlite>SELECT * FROM positions WHERE salary>30000;
title,salary
President,300000
Engineer,75000
sqlite>
```

Or even move your outputs from the command prompt to a file using `.output file.type` like so :

```
[...]
sqlite>.headers on
sqlite>.mode csv
sqlite>.output someEmployees.csv
sqlite>SELECT * FROM positions WHERE salary>30000;
sqlite>
```

## More complex example

### Query out of context

The following query was done on the Molecular Tools Platform database, which contained 4 tables. Two of those tables are used for these queries, `cziMetadata` and `cziChannels`. The query was meant to check if the image channels of `.czi` files had the marker `DAPI` or `mCher` and if so, to find the associated `path` in `cziMetadata` while avoiding duplicates which would have occured had we only searched in `cziChannels`. Then it returns the query as a `csv` file with the header and containing only the file paths..

```
sqlite>.headers on
sqlite>.mode csv
sqlite>.output example.csv
sqlite>SELECT path FROM cziMetadata WHERE path IN (SELECT file_id FROM cziChannels WHERE channel_name="DAPI" or channel_name="mCher");
sqlite>
```
