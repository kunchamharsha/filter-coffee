from coffeeMachine.model_data.ruleset import Ruleset
from coffeeMachine.model_data.apps import App
from coffeeMachine.model_data.users import User
from rest_framework.test import APITestCase
from rest_framework import status

class RulesetTest(APITestCase):    
    
    
    def setUp(self):
        pass
    
    def test_ruleset_get(self):
        user = User.objects.create(name="ram",profile_picture="image.png")
        _app_data = {
        "name": "payment system-6",
        "display_picture": "https://www.comestri.com/wp-content/uploads/2020/11/Order-Process-Graphic.png",
        "user":user,
        "description":"app for payment integration-updation"
        }
        app = App.objects.create(**_app_data)
        _data = {
            "name": "Payment System",
            "description": "working on payment system",
            "user_id": user.id,
            "service_id": app.id,
       }
        ruleset = Ruleset.objects.create(**_data)
        _response = self.client.get('/coffeemachine/ruleset/%s/'%ruleset.id,data=_data,format="json")
       
        self.assertEqual(_response.status_code,status.HTTP_200_OK)

    def test_ruleset_create(self):
        user = User.objects.create(name="ram",profile_picture="image.png").pk
        _app_data = {
        "name": "payment system-6",
        "display_picture": "https://www.comestri.com/wp-content/uploads/2020/11/Order-Process-Graphic.png",
        "user_id":user,
        "description":"app for payment integration-updation"
        }
        app = App.objects.create(**_app_data).pk
        _data = {
            "name": "Payment System",
            "description": "working on payment system",
            "user": user,
            "service": app,
       }
        _response = self.client.post('/coffeemachine/ruleset/',data=_data,format="json")
     
        self.assertEqual(_response.status_code,201)


    def test_ruleset_delete(self):
        user = User.objects.create(name="ram",profile_picture="image.png")
        _app_data = {
        "name": "payment system-6",
        "display_picture": "https://www.comestri.com/wp-content/uploads/2020/11/Order-Process-Graphic.png",
        "user":user,
        "description":"app for payment integration-updation"
        }
        app = App.objects.create(**_app_data)
        
        _data = {
            "name": "Payment System",
            "description": "working on payment system",
            "user_id": user.id,
            "service_id": app.id,
       }
        ruleset = Ruleset.objects.create(**_data)
        _response = self.client.delete('/coffeemachine/ruleset/%s/'%ruleset.id,data=_data,format="json")


    def test_ruleset_update(self):
        _data = {
            "name": "dummy name-2",
            "profile_picture": "https://batman.fandom.com/wiki/The_Joker_%28Nolanverse%29"
            }
        user = User.objects.create(name="ram",profile_picture="dummy pic")
        _response = self.client.put('/coffeemachine/user/%s/'%user.id,data=_data,format="json")
        self.assertEqual(_response.status_code,200)
        self.assertEqual(_response.data.get('name'), _data.get('name'))
        self.assertEqual(_response.data.get('profile_picture'), _data.get('profile_picture'))