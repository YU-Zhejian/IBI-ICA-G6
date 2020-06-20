# FBI Warnings:

For those who wants to clone my repository and get a higher grade:

1. You are a liar, and;

2. Your action will be reported to the Examination Board.

# Readme @ IBI ICA Group6

Good morning! Welcome to Group 6! Before starting our project, it is important to state our rules:

1. 代码千万行，注释第一行；注释不规范，同事两行泪。(This line appears in every public project of me.)
2. This public projects prefers **MERGEING** than **REBASING**. If you follow that guideline, you’ll be fine. If you don’t, people will hate you, and you’ll be scorned by friends and family. And **NEVER PREFORM FORCE PUSH**. If you accidentally committed and pushed something wrong, fix it ASAP and commit & push it again.
3. Pull before you push, or you will be **rejected** by Git (the ***software***, not me).
4. Beware of merge conflicts, they bite you!
5. **DO NOT ADD ARCHIVES (e. g. Zip).** Use **Markdown** instead of Word or RTF when documenting changes. This allows Git to show what was modified by `git diff` instead of telling us this is a binary.
6. **THINK TWICE BEFORE YOU COMMIT OR PUSH.**
7. If there are temporary files created by the editor, please add them to `.gitignore` to make Git ignore them.
8. Use **LF** instead of **CRLF** as the line endings. Use UTF-8 instead of ANSI as default encoding. Those who use GNU/Linux will appreciate you. And **DO ADD A NEWLINE CHARACTER AT THE END OF A FILE.** That is, to left the last line of your script **blank**. The reason of doing this is to make your colleagues read the code more easily under a GNU/Linux Terminal by `cat`.

## The Workflow

Our workflow is simple. Just pull-edit-add-commit-push to the master branch.

### Branching

You're encouraged to branch offline, but please **DO NOT PUSH YOUR BRANCH ONLINE**, unless necessary (e. g. Huge disagreement within our team).

Why? Because if you pushed all your branches,

1. The size of our repository will be huge, which will greatly slow Git down.

2. Who will be responsible for merging them to master? It would be weird for me to merge all those branches and deal with those dick-checking conflicts.

So, why do I recommend our centralized model? Please read the following message:

> 我认为直接在master上开发能够分摊merge的压力（谁push不了谁来merge），历史清晰（一条线）且责任明确（出问题了看谁push的就行了）。

### Fork

I do not recommend you to fork our repository--If you're inside this group, please think of a way to merge your commit without creating a pull request (which will be ignored--I am not available to see your request). If you're not, we'll definitely accuse you of performing academic misconduct.

## File In This Folder (FITF) for /

`.gitignore` This file contains a list of patterns. Those files with their filename matching the pattern will be ignored by Git.

`BeforeAdd.sh` This is a bash script which turns `CRLF` into `LF`.

`FITF.md` This file.

`Readme.md` This indicates what is in this folder.

`Formative.md` Our formative ICA's answer.

`docs/` Folder containing documents which may be useful.

## Python Specifications

The following specifications are made to make our code more readable:

1. All `python` file should be ended with extension name `py` and under `python 3`.
2. Use `# TODO: blablabla` when pending to do something.
3. The way of indenting pseudocode should be the same as those uncommented codes.
4. Use **FOUR WHITE SPACE** or **ONE TAB CHARACTER** as indentation.
5. There're **NO** need of adding `#!/usr/bin/env python` at the head of a file. The reason why I add this line is because this enables me to execute the script directly under a GNU/Linux terminal without specifying `python` as my interpreter.

## Recommended Software

Use `Typora` to read & edit Markdown files.

## FAQ

1. Why don't we use `git-flow` on https://nvie.com/posts/a-successful-git-branching-model/ ? It seems to be a mature model of collaborating.

   *Life is short and we should not waste our time like this.*

2. Do you think our current workflow will make this project unstable?

   *No point to be stable--We'll check before handing it on.*
