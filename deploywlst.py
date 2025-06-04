import sys

def deployComposite():
    user = "weblogic"
    password = "redhat@123"
    url = "http://localhost:7001"
    sarLocation = "while_loop.jar"
    compositeName = "while_loop"
    revision = "1.0"
    partition = "default"

    # Correct syntax: use variables directly, no `${}` or `$`
    connect(user, password, url)

    print('Deploying composite...')
    sca_deployComposite(sarLocation, partition, user, password, url, overwrite=True)
    print('Deployment complete.')

    disconnect()

if __name__ == '__main__':
    deployComposite()
