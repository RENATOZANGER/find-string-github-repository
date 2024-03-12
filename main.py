from github import GitHubAPI
import warnings

warnings.filterwarnings("ignore")


def main():
    token = "Token_github"
    owner = "owner_repository"
    repo = "name_repository"
    texto = "text_to_find_in_repository"
    
    github = GitHubAPI(token)
    github.search_code(owner, repo, texto)


if __name__ == "__main__":
    main()
