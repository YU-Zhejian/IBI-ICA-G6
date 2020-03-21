# Readme for the Workflow

## Aim

After this "practical", you should know:

1. The basic idea of "Centralized Workflow" (Chacon, S. and Straub, B. 2018).
2. How to handle conflicts when pushing your commits.

## Procedure

1. Open the file `trial.py` and add some words to the second line. Stage and commit your changes.
2. Push your changes back to GitHub. If your changes are **NOT** rejected, back to step 1.
3. If your changes are rejected, pull the newest changes from GitHub and merge them properly.
4. *(Optional)* After finishing those steps, do it again by command line interface.

## Please Pay Attention

1. **DO NOT PERFORM FORCE PUSH.** That can destroy the entire repository!
2. USE `LF` instead of `CRLF` in line endings.

## The Code

````bash
git pull
notepad workflow/trial.py
git add .
git commit -m "YOUR COMMIT MESSAGE"
git push
````

If there are conflicts:

````bash
git pull
# Here you should see an error message.
notepad workflow/trial.py
git add .
git commit -m "YOUR COMMIT MESSAGE"
git push
````

You can use `git status` to check if there are conflicts to be solved.

## Reference

Chacon, S. and Straub, B. (2018) *Pro Git 2.1.87*, APress. doi: 10.1007/978-1-4842-0076-6. Available from `/docs/progit.pdf`.