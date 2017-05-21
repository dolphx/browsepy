from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def exposure_africa(self):
        self.client.get("/browse/Exposure/5x5/Africa")

    @task
    def flood_hazard_maps(self):
        self.client.get("/browse/Hazard/Flood_hazard_maps")

    #@task
    #def flood_scenarios(self):
    #    self.client.get("http://gar.mnm-team.org/browse/Hazard/Flood%20scenarios")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000

