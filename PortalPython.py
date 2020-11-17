# https://portal.ptit.edu.vn/?s=hi

from requests import get

response = get('https://portal.ptit.edu.vn/?s=hi').text

print(response)