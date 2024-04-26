from locust import HttpUser, task, between
import random
 
class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
            
    @task
    def convert_temperature(self):
        fahrenheit = random.uniform(0, 100)
        json = {"fahrenheit": fahrenheit}
        headers = {"Content-Type": "application/json"}
        self.client.post("/convert", json=json, headers=headers)
        
    @task
    def convert_temperature_ai(self):
        fahrenheit = random.uniform(0, 100)
        json = {"fahrenheit": fahrenheit}
        headers = {"Content-Type": "application/json"}
        self.client.post("/convert_ai", json=json, headers=headers)