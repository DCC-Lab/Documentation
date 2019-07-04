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

### Installing SQLite for Python

Python already has tools integrated in its standard library for handling SQLite, in the form of the module `sqlite3`. However, other modules can be used such as `pysql` or `aspw`. These can be found these on [PyPi](https://pypi.org/). However, it is important to note that python is somewhat quirky when it comes to transactions and committing changes to the database. These quirks will be covered further below.

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
main:YOUR/PATH/test.db
sqlite>.open :memory:
main:
sqlite>
```

In the case of an in-memory database, `.main` will be left blank. Finally, you can start sqlite3 AND connect to or create a database directly from the command prompt using :

```
>sqlite3 test.sqlite
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

## Inserting data into a table

TO DO

## Selecting data from a table

TO DO

## More complex example

Using what we have seen so far, and a bit more, we can do querries such as the following one to find very specific things and immediately export the results into a csv file.

```
sqlite>.headers on
sqlite>.mode csv
sqlite>.output example.csv
sqlite>SELECT name FROM cziMetadata WHERE path IN (SELECT file_id FROM cziChannels WHERE channel_name="DAPI" or channel_name="mCher");
sqlite>
```
