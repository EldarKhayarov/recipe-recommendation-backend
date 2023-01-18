from locust import HttpUser, task, between


files = [
    (
        "image",
        (
            "apple_banana.jpeg",
            bytes(open("tests/loadtest/apple_banana.jpeg", "rb").read()),
            "image/jpeg",
        ),
    ),
]


class BackLocust(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_items(self):
        files = [
            (
                "image",
                (
                    "apple_banana.jpeg",
                    bytes(open("tests/loadtest/apple_banana.jpeg", "rb").read()),
                    "image/jpeg",
                ),
            ),
        ]
        response = self.client.post(f"/api/recipes/detect", files=files, name="/detect")
        print(response.status_code)
