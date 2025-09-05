from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

g = Github(ACCESS_TOKEN)
print(f"Authenticated as: {g.get_user().login}")

repositories = g.search_repositories(query="topic:machine-learning language:python")
repo = repositories[0]

print(f"Found repository: {repo.full_name}")
commits = repo.get_commits()

latest_commit = commits[0]
print(f"Latest commit SHA: {latest_commit.sha}")
print(f"Commit author: {latest_commit.commit.author.name}")
print(f"Commit date: {latest_commit.commit.author.date}")
print(f"Commit message: {latest_commit.commit.message}")

commit = repo.get_commit(sha=latest_commit.sha)

for file in commit.files:
    print(f"\n--- File Changed: {file.filename} ---")
    print(f"Status: {file.status}")  # 'added', 'modified', 'removed'
    print(f"Additions: {file.additions}")
    print(f"Deletions: {file.deletions}")

    # the 'patch' attribute contains the diff information.
    print("\n--- Diff ---")
    print(file.patch)
