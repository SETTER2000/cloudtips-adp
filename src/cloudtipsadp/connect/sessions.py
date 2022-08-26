from src.cloudtipsadp.connect.clients import Connect

Session = Connect

if __name__ == '__main__':
    token = Session().get_token()
    print(token)

    token = Session().refresh_token()
    print(token)
