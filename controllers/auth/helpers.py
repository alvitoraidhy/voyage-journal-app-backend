import os, base64, hashlib


# ref: https://stackoverflow.com/questions/51333374/shortest-possible-generated-unique-id
def generate_token():
    return base64.b64encode(os.urandom(32), b"az")[:8].decode()


def hash_password(password: str):
    return hashlib.md5(password.encode()).hexdigest()


class Session:
    data: dict = {}

    def create_session(self, payload: dict):
        while (token := generate_token()) in self.data.keys():
            pass

        self.data[token] = payload

        return token
    
    def read_session(self, token: str):
        return self.data.get(token)
    
    def update_session(self, token: str, payload: dict):
        if not token in self.data.keys():
            return False

        self.data[token] = payload

        return True

    def delete_session(self, token):
        if not token in self.data.keys():
            return False
        
        self.data.pop(token)

        return True
