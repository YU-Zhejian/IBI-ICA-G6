# Python Specifications

The following specifications are made to make our code more readable:

## Comments

1. Use `# TODO: blablabla` when pending to do something.

2. The way of indenting pseudocode should be the same as those uncommented codes.

## Indentations

1. Use **FOUR WHITE SPACE** or **ONE TAB CHARACTER** as indentation.

## Others

1. There're **NO** need of adding `#!/usr/bin/env python` at the head of a file. The reason why I add this line is because this enables me to execute the script directly under a GNU/Linux terminal without specifying `python` as my interpreter.
2. **DO ADD A NEWLINE CHARACTER AT THE END OF A FILE.** That is, to make the last line of your script **blank**. The reason of doing this is to make your colleagues read the code more easily under a GNU/Linux Terminal by `cat`.
3. **USE `CRLF` INSTEAD OF `LF` AS LINE ENDINGS.** There is a little script to change the line endings and the reason of doing this is to allow your colleagues to execute it under GNU/Linux without ambiguous mistakes. E. g., `Syntax Error: blablabla\r`.

