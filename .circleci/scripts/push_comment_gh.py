"""Script to read developer.md and issues.md and post them as comments to github"""
import sys
import logging
from github import Github


def main(
    github_user_token: str,
    github_repo_owner: str,
    github_repo_name: str,
    pull_request_num: str,
    path: str,
) -> None:
    """
    This function will take in environment variables (usually from CI environment) and
    post a comment where the content is linting output (issues.md and developer.md).
    The script takes in args when you call it.

    Args:
        github_user_token (str): https://github.com/settings/tokens for the CI Github
            user, a token must be passed to use github's api.
        github_repo_owner (str): name of owner/account/org owning the repo of
            interest (current repo).
        github_repo_name (str): the current repos name. In otherwords whatever repo this
            script is living in, that repo.
        pull_request_number (int): the number of the pull request. Can be found in the
            url.
        path (str): path to issues.md and developer.md e.g. /User/home/project

    Returns:
        Nothing
    """
    # create payload str that will be the comment
    file_handler = open(path+'/developer.md')
    content_dev = file_handler.read()
    file_handler = open(path+'/issues.md')
    content_iss = file_handler.read()
    content_full = 'developer.md:\n'+content_dev+'\nissues.md:\n'+content_iss
    g = Github(github_user_token)
    repo = g.get_user(github_repo_owner).get_repo(github_repo_name)
    pr = repo.get_pull(pull_request_num)
    pr.create_issue_comment(content_full)


if __name__ == "__main__":
    if len(sys.argv) < 6:
        logging.error(
            "Proper use: python push_comment_gh.py <GITHUB_USER_TOKEN> <GITHUB_REP_OWNER> <GITHUB_REPO_NAME> <PR_NUM> <PATH>"
            "For example: python push_comment_gh.py abcd3fg4 renewdotcom renew-looker-template 4 /Users/user/renew-looker-template"
        )
        # returns a non successful code
        return 1
    else:
        github_user_token = str(sys.argv[1])
        github_repo_owner = str(sys.argv[2])
        github_repo_name = str(sys.argv[3])
        pull_request_num = int(sys.argv[4])
        path = str(sys.argv[5])
        main(github_user_token, github_repo_owner, github_repo_name, pull_request_num, path)
