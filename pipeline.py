from github import Github
import logging
import os

# Constant variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Authenticate with github and get the latest diff
def get_latest_commit_diff():
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo("NiyiOdumosu/kafkamanager")
        latest_commit = repo.get_commits()[0]
        t = repo.head.commit.tree
        diff = repo.git.diff(t)
        # check the commit files and search for specific files (topic.json etc) then get the diff of those specific files and return that diff
        # diff = repo.compare(latest_commit.files[0].sha, latest_commit.files[1].sha)
        # diff = latest_commit.files[0].sha
        print(diff)
        return diff
    except Exception as e:
        logger.error(f"Error getting latest commit diff: {e}")
        raise


if __name__ == "__main__":
    diff = get_latest_commit_diff()
