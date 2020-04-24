# Readme for the Workflow

## Aim

After this "practical", you should know:

1. The basic idea of "Centralized Workflow" (Chacon, S. and Straub, B. 2018).
2. How to handle conflicts when pushing your commits.

## Backgrounds

### The Emergence of Conflict

When you're about to push your commits to the server, conflicts emerge when your commit is not **fast-forward**. The git server will **Reject** your commit and you should **Merge** what is on the server to your workflow.

e. g. `git clone` on local1

```
Remote 1-->2
       |   |
Local1 1-->2
```

`git commit` on local1

```
Remote 1-->2
       |   |
Local1 1-->2-->4
# Your commit is fast-forward. You can push and no conflict will emerge.
```

However, if someone else pushed his/her commits before yours, there will be problems. e. g.

```
Remote 1-->2---->3
       |   |     |
Local1 1-->2-->4 |
                 |
Local2 1-->2---->3
```

Now, what you should do is to pull others' commit and merge them into your workflow.

### Merge

Sometimes, merge can be done by git automatically. However, this mechanism fails when you and Local2 both modified a specific line. Under that circumstance, you should reopen the file, merge the changes by an editor, add and commit.

## Procedure

1. Open the file `trial.py` and add some words to **the second line**. Stage and commit your changes.
2. Push your changes back to GitHub. If your changes are **NOT** rejected, back to step 1.
3. If your changes are rejected, pull the newest changes from GitHub and merge them properly.
4. *(Optional)* After finishing those steps, do it again by command line interface.

## Please Pay Attention

1. **DO NOT PERFORM FORCE PUSH.** That can destroy the entire repository!
2. USE `LF` instead of `CRLF` in line endings.

## The Code

These code should be typed into a GNU/Linux terminal. You do not need to append them to `trial.py`.

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