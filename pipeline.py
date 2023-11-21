from github import Github
import logging
import os

# Constant variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

#set up logger
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Authenticate with github and get the latest diff
def get_latest_commit_diff():
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo("NiyiOdumosu/kafkamanager")
        latest_commit = repo.get_commits()[0]
        diff = latest_commit.files[0]
        print(diff)
        return diff
    except Exception as e:
        logger.error(f"Error getting latest commit diff: {e}")
        raise


if __name__ == "__main__":
    diff = get_latest_commit_diff()
