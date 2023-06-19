import yaml

data = {
    "apiVersion": "batch/v1beta1",
    "kind": "CronJob",
    "metadata": {
        "name": "monitoring-cronjob"
    },
    "spec": {
        "schedule": "*/5 * * * *",
        "jobTemplate": {
            "spec": {
                "template": {
                    "spec": {
                        "containers": [
                            {
                                "name": "monitoring-cronjob-container",
                                "imagePullPolicy": "IfNotPresent",
                                "image": "monitoring-cronjob",
                                "command": ["/bin/sh"],
                                "args": [
                                    "-c",
                                    "/usr/local/cloudops/sbin/check_ple_delay.sh ia-gcp >>/tmp/ple_delay.log 2>&1"
                                ]
                            }
                        ],
                        "restartPolicy": "OnFailure"
                    }
                }
            }
        },
        "status": {}
    }
}

yaml_data = yaml.dump(data)

with open("cronjob.yaml", "w") as file:
    file.write(yaml_data)
