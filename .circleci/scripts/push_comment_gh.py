"""Script to read developer.md and issues.md and post them as comments to github"""
import sys
import os
import logging
import github


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
    g = github.Github(github_user_token)
    repo = g.get_user(github_repo_owner).get_repo(github_repo_name)
    # if there is no PR open then log the content
    if pull_request_num == "" or pull_request_num is None:
        logging.info(content_dev)
        logging.info(content_iss)
    else:
        pr = repo.get_pull(pull_request_num)
        pr.create_issue_comment(content_dev)
        try:
            pr.create_issue_comment(content_iss)
        except github.GithubException as e:
            logging.error(e)
            if e.data['errors'][0]['message'].startswith('Body is too long'):
                logging.error("Comment is too long for posting as a comment to Github. Logging comment here.")
                link = os.environ['CIRCLE_BUILD_URL']
                pr.create_issue_comment("Linting errors detected, but output is too long to be posted in Github comment. See CircleCI job for full output: " + link + " \nNote you can download the output from circle and rename the file from .txt -> .md.")
                logging.error(content_iss)
            else:
                logging.error("unexpected error")

if __name__ == "__main__":
    if len(sys.argv) < 6:
        logging.error(
            "Proper use: python push_comment_gh.py <GITHUB_USER_TOKEN> <GITHUB_REP_OWNER> <GITHUB_REPO_NAME> <PR_NUM> <PATH>"
            "For example: python push_comment_gh.py abcd3fg4 renewdotcom renew-looker-template 4 /Users/user/renew-looker-template"
        )
        # returns a non successful code
        exit(1)
    else:
        github_user_token = str(sys.argv[1])
        github_repo_owner = str(sys.argv[2])
        github_repo_name = str(sys.argv[3])
        pull_request_num = int(sys.argv[4])
        path = str(sys.argv[5])
        main(github_user_token, github_repo_owner, github_repo_name, pull_request_num, path)
