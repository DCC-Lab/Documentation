# How to mount POM (or any other drive) on Cafeine2 (or any other Mac OS server)

Working in command lines can sometimes be a real pleasure. But for beginners, it can be a real pain.
I hope that this present document will help future students or researchers of the DCCLab to understand the not-so-magic behind command lines and server mounting. **Note** : This little tutorial is about POM and Cafeine2 but it can be generalized.

## PART 1: Accessing Cafeine2
To access Cafeine2, you need an account (see Daniel for details). When your account is created, you can access Cafeine by command lines.
To do so, open a terminal/command prompt (like `cmd` on Windows).
The main command to access the server is `ssh accountName@cafeine2.crulrg.ulaval.ca`
(where, obviously, you replace `accountName` by your account name). Use the `ssh` command when you want to access remote servers. Then, the terminal will ask for your password (if needed, like on Cafeine2). Don't panic if you type your password and nothing appears on screen, your password will still register when pressing `Enter`. Now, you are supposed to be on Cafeine2, in your personnal directory. For example, you should see something like `cafeine2:~ dcclab$` on your terminal screen (where `dcclab` is replaced by you username). Every command you write will be after your username (example: `cafeine2:~ dcclab$ python` to run python)

## PART 2: Preparing the field for POM
Part 1 was the easiest part. Now, you will need to use more complex commands. First of all, you will surely need or want to create a new
directory for mounting POM. This can be quite easily achieved by writing `mkdir directoryName`. This will create a new directory in the directory you are currently in. To confirm that the new directory is indeed created, type the `ls` command. This allows you to see everything in your current directory. Your newly created directory should be present in the list. Example:
```
(base) cafeine2:~ dcclab$ mkdir test
(base) cafeine2:~ dcclab$ ls
Applications
Desktop
Documents
Downloads
GitHub
Library
Movies
Music
Pictures
Public
StudentsWorkToStore
fibercomb_plate_v1.PDF
tempTestExtractingDataFromCZIFiles_GabrielGenest_Summer2019
test
```
As you can see, the `test` directory is present! Now let's mount POM!

## PART 3: Mounting POM
Let's say you want to mount POM in your new directory. First, you need to use the command `mount_smbfs`. This is a quite complex command because it requires and can take a lot of arguments. But for the purpose of mounting POM, it can be used without too much complications.
The basic syntax of `mount_smbfs` is 

`mount_smbfs //username@ipAddress/wantedDirectory/wantedDirectoryLayer2/... targetMountingDirectory`

where `username` is the username required to access the drive, `idAddress` is the ip address and `targetMountingDirectory` is the directory that will be used to access POM from your personnal space. After pressing `Enter`, you will be asked to type your password (if required). This can be skipped by using a similar but slightly different syntax :

`mount_smbfs //username:password@ipAddress/wantedDirectory/wantedDirectoryLayer2/... targetMountingDirectory`

You can also specify the directory you wish to mount by adding `/wantedDirectory/wantedDirectoryLayer2/...`. In our current example with POM, this part looks like:
```
(base) cafeine2:~ dcclab$ mount_smbfs //username@172.16.1.220/COLLABORATION/POM ./test
Password for 172.16.1.220: <enter the password>
```
Note that the username and password for POM are not your Cafeine2 username and password (see Daniel for more info). As you can see, POM's ip address is `172.16.1.220` and we want to mount the `COLLABORATION/POM` directory in `test` (the directory created in part 2). The `./` in front of `test` only means that `test` is in the current directory.

To confirm that POM is mounted in the directory you specified, you need to go into that directory. To do so, the command `cd` (for change directory) is what you want. It is a simple command because you only need to specify the directory you want to go into. The syntax is `cd directoryName`. It is possible to complexify the command by specifying deeper directories like

`cd directoryName/deeperDirectory/evenDeeperDirectory...`

Now, let's look at the syntax in action with our POM example:
```
(base) cafeine2:~ dcclab$ cd test
(base) cafeine2:test dcclab$ ls
Anne                            MEP                             Thumbs.db                       untitled folder 2
Julie                           New-03-Image Export-140         injection AAV
KINGSTON                        Test viabilite?? mCherry+EGFP   microscopie e??lectronique
```
We can see that `test` *contains* the directories within `COLLABORATION/POM`. We can now access one of these folders and see that everything is there. We can access anything in POM from this mount point. To return to you root directory, you can use the same command but with a different argument: `cd ..` (the two dots argument meaning "return to the previous directory in the hierarchy").
```
(base) cafeine2:test dcclab$ cd injection\ AAV/
(base) cafeine2:test dcclab$ ls
S58_AAV595.numbers      Virus                   re??sultats bruts
(base) cafeine2:injection AAV dcclab$ cd ..
(base) cafeine2:test dcclab$ ls
Anne                            New-03-Image Export-140         microscopie e??lectronique
Julie                           Test viabilite?? mCherry+EGFP   untitled folder 2
KINGSTON                        Thumbs.db
MEP                             injection AAV
```

Now, you are ready to work on Cafeine with an access to POM. You only need to figure out what is the right path to access your mounting point from any other directory. This can still be a pain, but it is still better than having to navigate deeply through Cafeine2 to find POM!

## PART 4: Unmount the beast
Now that you are done with POM and you want to unmount it from the mount point, there is one command to remember:

`diskutil unmount ./mountPoint` if you are in the directory of your mount point or 

`diskutil unmount ./mountPointParent/... /mountPoint`

Then, a message should appear on the screen explaining that the unmount was successful (or not). Then, when you return to your old mount point, the directory should be empty:
```
(base) cafeine2:~ dcclab$ diskutil unmount ./test
Unmount successful for ./test
(base) cafeine2:~ dcclab$ cd test
(base) cafeine2:test dcclab$ ls
(base) cafeine2:test dcclab$
```
Now that you safely unmounted POM, you can delete the mounting point directory with `rmdir dirName`. This command removes an empty directory (to remove existing files, use `rm fileName`):
```
(base) cafeine2:~ dcclab$ rmdir test
(base) cafeine2:~ dcclab$ ls
Applications
Desktop
Documents
Downloads
GitHub
Library
Movies
Music
Pictures
Public
StudentsWorkToStore
fibercomb_plate_v1.PDF
tempTestExtractingDataFromCZIFiles_GabrielGenest_Summer2019
```
`test` is now deleted and you can go on with your day.
