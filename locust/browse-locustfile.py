from locust import task, run_single_user
from locust import FastHttpUser

class Browse(FastHttpUser):
    host = "http://localhost:5000"
    default_headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    }

    @task
    def view_browse(self):
        with self.client.get(
            "/browse",
            headers=self.default_headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status code: {response.status_code}")


if __name__ == "__main__":
    run_single_user(browse)
