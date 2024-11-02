#### ENV and Install modules

`python -m venv rasp`
`pip install -r requirements.txt`

#### Host on local network so raspberrypi can send lil messages :)

`flask --app index run --host=0.0.0.0 --debug`
