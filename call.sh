curl -X POST  \
	--header 'Content-Type: application/json' \
	--data '{"ID": [20], "Sex": [2],"Smoking": [2], "Age": [100]}' \
	localhost:8000/mymodel
