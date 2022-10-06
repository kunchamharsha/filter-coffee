from coffeeMachine.model_data.rules import Rules
from coffeeMachine.model_data.ruleset import Ruleset
from coffeeMachine.model_data.apps import App
from coffeeMachine.model_data.users import User
from rest_framework.test import APITestCase
from rest_framework import status

class RuleTest(APITestCase):    
    
    
    def setUp(self):
        pass
    
    def test_rule_create(self):
        
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

        _rule_data =  {
                "name": "Trialpack",
                "description": "Discount feature for Trial pack-3",
                "expression": "device_create_time==0 and locale=='IN' and platform=='android'",
                "fields": {
                    "fields": [
                        "device_create_time",
                        "locale",
                        "platform"
                    ]
                },
                "weightage": 8,
                "payload": {
                    "plan_id": 26
                },
                "ruleset": ruleset.id,
            }
        _response = self.client.post('/coffeemachine/rules/',data=_rule_data,format="json")
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)

    def test_rule_get(self):
        
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

        _rule_data =  {
                "name": "Trialpack",
                "description": "Discount feature for Trial pack-3",
                "expression": "device_create_time==0 and locale=='IN' and platform=='android'",
                "fields": {
                    "fields": [
                        "device_create_time",
                        "locale",
                        "platform"
                    ]
                },
                "weightage": 8,
                "payload": {
                    "plan_id": 26
                },
                "ruleset": ruleset,
            }
        rule = Rules.objects.create(**_rule_data)

        _response = self.client.get('/coffeemachine/rules/%s/'%rule.id,data=_rule_data,format="json")
      
        self.assertEqual(_response.status_code,status.HTTP_200_OK)

    def test_rule_delete(self):
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

        _rule_data =  {
                "name": "Trialpack",
                "description": "Discount feature for Trial pack-3",
                "expression": "device_create_time==0 and locale=='IN' and platform=='android'",
                "fields": {
                    "fields": [
                        "device_create_time",
                        "locale",
                        "platform"
                    ]
                },
                "weightage": 8,
                "payload": {
                    "plan_id": 26
                },
                "ruleset": ruleset,
            }
        
        rule = Rules.objects.create(**_rule_data)

        _response = self.client.delete('/coffeemachine/rules/%s/'%rule.id,format="json")
        self.assertEqual(_response.status_code,status.HTTP_204_NO_CONTENT)


    def test_rule_update(self):
        _data = {
            "name": "Ram harsha-2",
            "profile_picture": "https://batman.fandom.com/wiki/The_Joker_%28Nolanverse%29"
            }
        user = User.objects.create(name="ram",profile_picture="dummy pic")
        _response = self.client.put('/coffeemachine/user/%s/'%user.id,data=_data,format="json")
        self.assertEqual(_response.status_code,200)
        self.assertEqual(_response.data.get('name'), _data.get('name'))
        self.assertEqual(_response.data.get('profile_picture'), _data.get('profile_picture'))

