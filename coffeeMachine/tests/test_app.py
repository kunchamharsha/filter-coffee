import copy
from coffeeMachine.model_data.apps import App
from coffeeMachine.model_data.users import User
from rest_framework.test import APITestCase
from rest_framework import status

class AppTest(APITestCase):    
    
    
    @classmethod
    def setUpTestData(cls):
        
        cls.user = User.objects.create(name="rajat",profile_picture="https://batman.fandom.com/wiki/The_Joker_%28Nolanverse%29")

        cls._data = {
        "name": "payment system-6",
        "display_picture": "https://www.comestri.com/wp-content/uploads/2020/11/Order-Process-Graphic.png",
        "user":cls.user,
        "description":"app for payment integration-updation"
        }

        cls.app = App.objects.create(**cls._data)
        cls.app_manual = App.objects.create(name="payment sys-7",display_picture="image.png",user=cls.user,description="payment integration")

    
    def test_app_creation(self):
        _data = copy.deepcopy(self._data)
        _data['user'] = self.user.id
        
        _response = self.client.post('/coffeemachine/app/',data=_data,format="json")
        print(_response.data)
        self.assertEqual(_response.status_code,status.HTTP_201_CREATED)


    def test_app_get(self):
        user = User.objects.create(name="rajat",profile_picture="https://batman.fandom.com/wiki/The_Joker_%28Nolanverse%29")
        
        _data = {
        "name": "payment system-6",
        "display_picture": "https://www.comestri.com/wp-content/uploads/2020/11/Order-Process-Graphic.png",
        "user":user,
        "description":"app for payment integration-updation"
        }
        app = App.objects.create(**_data)

        _response = self.client.get('/coffeemachine/app/%s/'%app.id,data=_data,format="json")

        self.assertEqual(_response.status_code,status.HTTP_200_OK)
    
    
    def test_app_delete(self):
        user = User.objects.create(name="rajat",profile_picture="https://batman.fandom.com/wiki/The_Joker_%28Nolanverse%29")
        
        _data = {
        "name": "payment system-6",
        "display_picture": "https://www.comestri.com/wp-content/uploads/2020/11/Order-Process-Graphic.png",
        "user":user,
        "description":"app for payment integration-updation"
        }
        app = App.objects.create(**_data)

        _response = self.client.delete('/coffeemachine/app/%s/'%app.id,format="json")
        self.assertEqual(_response.status_code,status.HTTP_204_NO_CONTENT)
    

    def test_app_update(self):
        user = User.objects.create(name="rajat",profile_picture="https://batman.fandom.com/wiki/The_Joker_%28Nolanverse%29")
        
        _data = {
        "name": "payment system-6",
        "display_picture": "https://www.comestri.com/wp-content/uploads/2020/11/Order-Process-Graphic.png",
        "user":user.id,
        "description":"app for payment integration-updation"
        }
        
        app = App.objects.create(name="payment sys-7",display_picture="image.png",user=user,description="payment integration")
        
        _response = self.client.put('/coffeemachine/app/%s/'%app.id,data=_data,format="json")
        
        self.assertEqual(_response.status_code,200)
        self.assertEqual(_response.data.get('name'), _data.get('name'))
        self.assertEqual(_response.data.get('display_picture'), _data.get('display_picture'))
