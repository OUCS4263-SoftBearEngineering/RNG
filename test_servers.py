import requests
import unittest
import yaml
from datetime import datetime

class TestResponseTime(unittest.TestCase):
    """
    Outputs response time for single request for each server
    """
    def test_response_time(self):
        with open("test.yaml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

            for group in data.values():
                for region in group.values():
                    for server_data in region.values():
                        print(server_data.get('server'))
                        num = requests.get(server_data.get('server'))
                        server_data['time'] = str(num.elapsed)
                        server_data['random_number'] = num

        with open("test.yaml", "w") as f:
            yaml.dump(data, f, default_flow_style=False)
                        

if __name__ == '__main__':
    unittest.main()
