import os


class GitAI:
    def install_git_with_brew():
        """Install Git with Homebrew on Mac OS"""
        os.system("brew install git")

    def selfupdate_macports():
        """Install Git with MacPorts on Mac OS"""
        os.system("sudo port selfupdate")

    def install_git_linux():
        """Install Git on Linux"""
        os.system("sudo apt-get install git")

    def show_git_version():
        """Shows the current version of Git"""
        os.system("git --version")

    def init_git_repo():
        """Initializes a new Git repository in the current directory"""
        os.system("git init")

    def init_git_repo_in_directory(directory):
        """Initializes a new Git repository in the specified directory
        directory: The directory where the repository will be initialized
        """
        os.system(f"git init {directory}")

    def clone_repository(repository_url):
        """Clones a repository from a remote server to your local machine
        repository_url: The URL of the remote repository
        """
        os.system(f"git clone {repository_url}")

    def clone_specific_branch(branch_name, repository_url):
        """Clones a specific branch from a repository
        branch_name: The name of the branch to clone
        repository_url: The URL of the remote repository
        """
        os.system(f"git clone --branch {branch_name} {repository_url}")

    def add_file_to_staging(file):
        """Adds a specific file to the staging area
        file: The file to add to the staging area
        """
        os.system(f"git add {file}")

    def add_all_files_to_staging():
        """Adds all modified and new files to the staging area"""
        os.system("git add .")

    def show_git_status():
        """Shows the current state of the repository"""
        os.system("git status")

    def show_ignored_files_status():
        """Displays ignored files in addition to the regular status output"""
        os.system("git status --ignored")

    def show_git_diff():
        """Shows the changes between the working directory and the staging area (index)"""
        os.system("git diff")

    def show_commit_diff(commit1, commit2):
        """Displays the differences between two commits
        commit1: The first commit
        commit2: The second commit
        """
        os.system(f"git diff {commit1} {commit2}")

    def show_staged_diff():
        """Displays the changes between the staging area and the last commit"""
        os.system("git diff --staged")

    def show_head_diff():
        """Displays the difference between the current directory and the last commit"""
        os.system("git diff HEAD")

    def commit_changes():
        """Creates a new commit with the changes in the staging area and opens the default text editor for adding a commit message"""
        os.system("git commit")

    def commit_with_message(message):
        """Creates a new commit with the changes in the staging area and specifies the commit message inline
        message: The commit message
        """
        os.system(f'git commit -m "{message}"')

    def commit_all_changes():
        """Commits all modified and deleted files in the repository without explicitly using git add to stage the changes"""
        os.system("git commit -a")

    def add_git_note():
        """Creates a new note and associates it with an object (commit, tag, etc.)"""
        os.system("git notes add")

    def restore_file(file):
        """Restores the file in the working directory to its state in the last commit
        file: The file to restore
        """
        os.system(f"git restore {file}")

    def reset_to_commit(commit):
        """Moves the branch pointer to a specified commit, resetting the staging area and the working directory to match the specified commit
        commit: The commit to reset to
        """
        os.system(f"git reset {commit}")

    def soft_reset_to_commit(commit):
        """Moves the branch pointer to a specified commit, preserving the changes in the staging area and the working directory
        commit: The commit to reset to
        """
        os.system(f"git reset --soft {commit}")

    def hard_reset_to_commit(commit):
        """Moves the branch pointer to a specified commit, discarding all changes in the staging area and the working directory
        commit: The commit to reset to
        """
        os.system(f"git reset --hard {commit}")

    def remove_file(file):
        """Removes a file from both the working directory and the repository, staging the deletion
        file: The file to remove
        """
        os.system(f"git rm {file}")

    def move_or_rename_file(source, destination):
        """Moves or renames a file or directory in the repository
        source: The current location of the file or directory
        destination: The new location of the file or directory
        """
        os.system(f"git mv {source} {destination}")

    def commit_new_feature(message):
        """Creates a new commit with a specific message indicating a new feature
        message: The commit message
        """
        os.system(f'git commit -m "feat: {message}"')

    def commit_bug_fix(message):
        """Creates a new commit with a specific message indicating a bug fix
        message: The commit message
        """
        os.system(f'git commit -m "fix: {message}"')

    def commit_chore(message):
        """Creates a new commit with a specific message indicating routine tasks or maintenance
        message: The commit message
        """
        os.system(f'git commit -m "chore: {message}"')

    def commit_refactor(message):
        """Creates a new commit with a specific message indicating code refactoring
        message: The commit message
        """
        os.system(f'git commit -m "refactor: {message}"')

    def commit_docs_change(message):
        """Creates a new commit with a specific message indicating documentation changes
        message: The commit message
        """
        os.system(f'git commit -m "docs: {message}"')

    def commit_style_change(message):
        """Creates a new commit with a specific message indicating styling and formatting changes
        message: The commit message
        """
        os.system(f'git commit -m "style: {message}"')

    def commit_test_change(message):
        """Creates a new commit with a specific message indicating test-related changes
        message: The commit message
        """
        os.system(f'git commit -m "test: {message}"')

    def commit_performance_change(message):
        """Creates a new commit with a specific message indicating performance-related changes
        message: The commit message
        """
        os.system(f'git commit -m "perf: {message}"')

    def commit_ci_change(message):
        """Creates a new commit with a specific message indicating CI system-related changes
        message: The commit message
        """
        os.system(f'git commit -m "ci: {message}"')

    def commit_build_change(message):
        """Creates a new commit with a specific message indicating build process-related changes
        message: The commit message
        """
        os.system(f'git commit -m "build: {message}"')

    def commit_revert(message):
        """Creates a new commit with a specific message indicating a revert of a previous commit
        message: The commit message
        """
        os.system(f'git commit -m "revert: {message}"')

    def list_branches():
        """Lists all branches in the repository"""
        os.system("git branch")

    def create_branch(branch_name):
        """Creates a new branch with the specified name
        branch_name: The name of the new branch
        """
        os.system(f"git branch {branch_name}")

    def delete_branch(branch_name):
        """Deletes the specified branch
        branch_name: The name of the branch to delete
        """
        os.system(f"git branch -d {branch_name}")

    def list_all_branches():
        """Lists all local and remote branches"""
        os.system("git branch -a")

    def list_remote_branches():
        """Lists all remote branches"""
        os.system("git branch -r")

    def switch_branch(branch_name):
        """Switches to the specified branch
        branch_name: The name of the branch to switch to
        """
        os.system(f"git checkout {branch_name}")

    def create_and_switch_branch(branch_name):
        """Creates a new branch and switches to it
        branch_name: The name of the new branch
        """
        os.system(f"git checkout -b {branch_name}")

    def discard_changes(file):
        """Discards changes made to the specified file and reverts it to the version in the last commit
        file: The file to discard changes from
        """
        os.system(f"git checkout -- {file}")

    def merge_branch(branch_name):
        """Merges the specified branch into the current branch
        branch_name: The name of the branch to merge
        """
        os.system(f"git merge {branch_name}")

    def show_commit_history():
        """Displays the commit history of the current branch"""
        os.system("git log")

    def show_branch_commit_history(branch_name):
        """Displays the commit history of the specified branch
        branch_name: The name of the branch
        """
        os.system(f"git log {branch_name}")

    def show_file_commit_history(file):
        """Displays the commit history of a file, including its renames
        file: The file to show the commit history of
        """
        os.system(f"git log --follow {file}")

    def show_all_commit_history():
        """Displays the commit history of all branches"""
        os.system("git log --all")

    def stash_changes():
        """Stashes the changes in the working directory"""
        os.system("git stash")

    def list_stashes():
        """Lists all stashes in the repository"""
        os.system("git stash list")

    def apply_and_remove_stash():
        """Applies and removes the most recent stash"""
        os.system("git stash pop")

    def drop_stash():
        """Removes the most recent stash"""
        os.system("git stash drop")

    def list_tags():
        """Lists all tags in the repository"""
        os.system("git tag")

    def create_tag(tag_name):
        """Creates a lightweight tag at the current commit
        tag_name: The name of the tag
        """
        os.system(f"git tag {tag_name}")

    def create_tag_at_commit(tag_name, commit):
        """Creates a lightweight tag at the specified commit
        tag_name: The name of the tag
        commit: The commit to tag
        """
        os.system(f"git tag {tag_name} {commit}")

    def create_annotated_tag(tag_name, message):
        """Creates an annotated tag at the current commit with a custom message
        tag_name: The name of the tag
        message: The custom message
        """
        os.system(f'git tag -a {tag_name} -m "{message}"')

    def fetch_changes():
        """Retrieves changes from a remote repository"""
        os.system("git fetch")

    def fetch_changes_from_remote(remote):
        """Retrieves changes from the specified remote repository
        remote: The name of the remote repository
        """
        os.system(f"git fetch {remote}")

    def prune_fetch():
        """Removes any remote-tracking branches that no longer exist on the remote repository"""
        os.system("git fetch --prune")

    def pull_changes():
        """Fetches changes from the remote repository and merges them into the current branch"""
        os.system("git pull")

    def pull_changes_from_remote(remote):
        """Fetches changes from the specified remote repository and merges them into the current branch
        remote: The name of the remote repository
        """
        os.system(f"git pull {remote}")

    def rebase_pull():
        """Fetches changes from the remote repository and rebases the current branch onto the updated branch"""
        os.system("git pull --rebase")

    def push_changes():
        """Pushes local commits to the remote repository"""
        os.system("git push")

    def push_changes_to_remote(remote):
        """Pushes local commits to the specified remote repository
        remote: The name of the remote repository
        """
        os.system(f"git push {remote}")

    def push_changes_to_branch(remote, branch):
        """Pushes local commits to the specified branch of the remote repository
        remote: The name of the remote repository
        branch: The name of the branch
        """
        os.system(f"git push {remote} {branch}")

    def push_all_branches():
        """Pushes all branches to the remote repository"""
        os.system("git push --all")

    def list_remotes():
        """Lists all remote repositories"""
        os.system("git remote")

    def add_remote(name, url):
        """Adds a new remote repository with the specified name and URL
        name: The name of the remote repository
        url: The URL of the remote repository
        """
        os.system(f"git remote add {name} {url}")

    def show_commit_details():
        """Shows the details of a specific commit"""
        os.system("git show")

    def show_specific_commit_details(commit):
        """Shows the details of the specified commit
        commit: The commit to show details of
        """
        os.system(f"git show {commit}")

    def revert_commit(commit):
        """Creates a new commit that undoes the changes introduced by the specified commit
        commit: The commit to revert
        """
        os.system(f"git revert {commit}")

    def revert_no_commit(commit):
        """Undoes the changes introduced by the specified commit, but does not create a new commit
        commit: The commit to revert
        """
        os.system(f"git revert --no-commit {commit}")

    def rebase_branch(branch):
        """Reapplies commits on the current branch onto the tip of the specified branch
        branch: The branch to rebase onto
        """
        os.system(f"git rebase {branch}")
