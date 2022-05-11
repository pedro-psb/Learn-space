1 - Cheatsheet
2 - Samples

# Cheatsheet

### Create repo

git init <repo>
git config --global/local user.name "name"
git config --global/local user.name "email"

git remote
    Show the all the remote repositories (can be on local machine)
git remote -v
    Show the remote repositories to push and pull from.
git remote add <destination> <link>
    Usually: 'origin github.com...'
git remote rename <nome> <nome-2>

git push <remote-name> <local-branch-to-push>
    Remote-name is usually 'origin'. push -u sets the given remote the default.
git pull <remote-name> <remote-branch-to-push>

git log --oneline
git add .
git commit -m "message"

### GitHub

git remote add origin master

# Samples
git init
git config --global user.name "Pedro Pessoa"
git config --global user.email "pedropsb95@gmail.com"
git remote add origin