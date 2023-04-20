import requests


class Client:
  addr = "http://admin:admin@127.0.0.1"

  def __init__(self, addr: str):
    self.addr = addr

  def events(self, camid: int, timeat: int):
    r = requests.get(f'{self.addr}/api/events?camera_id={camid}&time_at={timeat}')
    return r.json()

  def event_image(self, path:str):
    r = requests.get(f'{self.addr}/{path}')
    return r.content