Make certain you are in the appropriate virtualenv
To activate a virtualenv
` source ~/.virtualenvs/<project>/bin/activate `

To Deactivate
`deactivate`



To install a new package
`pip install <package> && pip freeze > requirements.txt`


To install all packages
`pip install -r requirements.txt` or simply `make restore`

To lint
`make build`

To Run
`make run`




