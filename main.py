import time

from config import GITHUB_TOKEN, GITHUB_API_BASE_URL
import requests


class GithubService:
    def __init__(self):
        self.headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }

    def get_invitations(self):
        try:
            url = f"{GITHUB_API_BASE_URL}/user/repository_invitations"
            response = requests.get(url, headers=self.headers)

            return response.json()
        except Exception as e:
            print(e)
            return []

    def accept_invitation(self, invitation_id):
        try:
            url = f"{GITHUB_API_BASE_URL}/user/repository_invitations/{invitation_id}"
            requests.patch(url, headers=self.headers)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    service = GithubService()
    while True:
        time.sleep(10)
        try:
            invitations = service.get_invitations()
            if not invitations:
                continue

            for invitation in invitations:
                service.accept_invitation(invitation["id"])
                print(f"Accept invitation {invitation['id']}")

            print("Accept all invitations")
        except Exception as e:
            print(e)
