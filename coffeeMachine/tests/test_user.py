from coffeeMachine.model_data.users import User
from rest_framework.test import APITestCase
from rest_framework import status

class UserTest(APITestCase):    
    
    @classmethod
    def setUpTestData(cls):
        
        cls._data = {
            "name": "Dummy name-2",
            "profile_picture": "https://batman.fandom.com/wiki/The_Joker_%28Nolanverse%29"
            }
        cls.user = User.objects.create(name="dummy name",profile_picture="dummy pic")
        
    
    def test_user_create(self):

        _response = self.client.post('/coffeemachine/user/',data=self._data,format="json")
      
        self.assertEqual(_response.status_code,201)

    def test_user_get(self):
      
        _response = self.client.get('/coffeemachine/user/%s/'%self.user.id,format="json")
      
        self.assertEqual(_response.status_code,200)
    
    def test_user_update(self):
       
        _response = self.client.put('/coffeemachine/user/%s/'%self.user.id,data=self._data,format="json")
        self.assertEqual(_response.status_code,200)
        self.assertEqual(_response.data.get('name'), self._data.get('name'))
        self.assertEqual(_response.data.get('profile_picture'), self._data.get('profile_picture'))


    def test_user_delete(self):

        _response = self.client.delete('/coffeemachine/user/%s/'%self.user.id,format="json")
        self.assertEqual(_response.status_code,status.HTTP_204_NO_CONTENT)
 