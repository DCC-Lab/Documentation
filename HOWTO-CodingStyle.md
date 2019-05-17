# Coding style and practices in DCC Lab

We all code in MATLAB, C, Python, Objective-C, Swift, C ++, assembler. The act of programming is the basis of many of the tasks we do, so it must be done well.

## The rules

1. The code should read as a text.
  Variable names and function names are important. A boolean variable can be called `isDone`. A table representing an image can be called `image`. A function can have an action verb in its name.

2. We take a "camel-case" style, that is, the first letter is lowercase, and then each word is capitalized, as in `createRayPlot()`. We never use underscores (_) which are reserved for internal, hidden, private, low-level variables.

3. Just because the code works does not mean the code is good.
   The validity tests, the style, the simplicity, the ease of maintaining the code are all essential characteristics of a well done task.

4. There are no worse comments than comments that are out of date or redundant. If the code reads as text, comments are not necessary.

5. If-else are written and indented like this because this style is compact:

   ```
   if (condition) {
      // some code
   } else {
      // more code
   }
   ```

6. A function should do only one thing.

7. The best function has no argument. The second best function has only one argument. The third best function has only two arguments. There is no fourth best function.

8. **Code without tests is incomplete code**. MATLAB has `UnitTest`. Python has `unitTest`. Swift and Objective-C have `XCTest`, C ++ has several libraries of Unit Testing. All languages ​​now have test libraries (even LabView for goodness sake).
  Writing tests makes it possible to better understand and better factorize your own code, in addition to making it more reliable. It allows you to embark on big changes without being afraid of breaking something. Write tests.

9. The use of a versioning system GitHub is essential.
  The versioning allows to modify the code with assurance and allows to give it to a collaborator as it was at the time of a publication. The dcclab group has a [page](https://github.com/DCC-Lab) on the server.

10. No one should work in `master`.  Make a branch with a name that is indicative of what you are trying to accomplish (e.g., `optimizationImageSegmentation`).

11. A branch should have a lifetime of approximately 1 week, never more than 2 weeks.

12. Commit the code as a group of changes by subproject and commit all the files together that were modified. Commit often.

    