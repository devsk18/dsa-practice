#!/usr/bin/env python3
"""
Leetcode Solution Automation Script - Interactive

Usage: python scripts/add_solution.py <lc_no> "Problem Name"
Example: python scripts/add_solution.py 13 "Roman to Integer"

This script launches an interactive menu after taking arguments.
"""

import sys
import os
import subprocess


def slugify(name: str) -> str:
    """Convert problem name to slug format (capitalize each word, hyphenated)."""
    return "-".join(word.capitalize() for word in name.split())


def get_repo_root() -> str:
    """Get the repository root directory (parent of scripts folder)."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(script_dir)


def get_filepath(lc_no: str, problem_name: str) -> str:
    """Get the filepath for the solution file."""
    repo_root = get_repo_root()
    slug = slugify(problem_name)
    filename = f"{lc_no}-{slug}.py"
    return os.path.join(repo_root, "leetcode", filename)


def create_solution_file(lc_no: str, problem_name: str) -> str:
    """Create a clean solution file (no template, empty file)."""
    filepath = get_filepath(lc_no, problem_name)

    if os.path.exists(filepath):
        print(f"\nFile already exists: {filepath}")
        return filepath

    # Create empty file
    with open(filepath, "w") as f:
        pass

    print(f"\nCreated clean file: {filepath}")
    return filepath


def add_and_commit(lc_no: str, problem_name: str) -> None:
    """Add the file and commit with approval prompt."""
    filepath = get_filepath(lc_no, problem_name)
    
    if not os.path.exists(filepath):
        print(f"\nError: File does not exist: {filepath}")
        print("Please create the file first (option 1).")
        return

    commit_msg = f"LC-{lc_no}: solved ({problem_name})"
    
    print(f"\nProposed commit message: \"{commit_msg}\"")
    print(f"File to add: {filepath}")
    
    approval = input("\nApprove commit? (y/n): ").strip().lower()
    
    if approval == 'y':
        try:
            subprocess.run(["git", "add", filepath], check=True)
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            print(f"\nCommitted successfully!")
        except subprocess.CalledProcessError as e:
            print(f"\nGit command failed: {e}")
    else:
        print("\nCommit aborted.")


def git_push() -> None:
    """Run git push command."""
    try:
        print("\nRunning git push...")
        result = subprocess.run(["git", "push"], check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        print("Push completed.")
    except subprocess.CalledProcessError as e:
        print(f"Git push failed: {e}")


def show_menu(lc_no: str, problem_name: str) -> None:
    """Display interactive menu and handle user choices."""
    filepath = get_filepath(lc_no, problem_name)
    
    while True:
        print("\n" + "=" * 40)
        print(f"Problem: #{lc_no} - {problem_name}")
        print(f"Target file: {filepath}")
        print("=" * 40)
        print("\nOptions:")
        print("1. Create solution file (clean/empty)")
        print("2. Add and commit changes")
        print("3. Push to remote")
        print("4. Exit")
        
        choice = input("\nSelect option (1-4): ").strip()
        
        if choice == '1':
            create_solution_file(lc_no, problem_name)
        elif choice == '2':
            add_and_commit(lc_no, problem_name)
        elif choice == '3':
            git_push()
        elif choice == '4':
            print("\nExiting...")
            break
        else:
            print("\nInvalid option. Please select 1-4.")


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/add_solution.py <lc_no> \"Problem Name\"")
        print('Example: python scripts/add_solution.py 13 "Roman to Integer"')
        sys.exit(1)

    lc_no = sys.argv[1]
    problem_name = sys.argv[2]

    # Ensure we're in the repo root for git commands
    repo_root = get_repo_root()
    os.chdir(repo_root)

    # Verify leetcode directory exists
    if not os.path.isdir("leetcode"):
        print("Error: 'leetcode' directory not found in repo root")
        sys.exit(1)

    # Start interactive menu
    show_menu(lc_no, problem_name)


if __name__ == "__main__":
    main()
