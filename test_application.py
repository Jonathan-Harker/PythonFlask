import application

def test_multiResults():
	assert application.multiResults("https://reqres.in/api/users?page=1", []) != ""


