"""Модуль для запуска простого HTTP-сервера."""

import http.server
import socketserver

PORT = 8000


class TestMe():
    """Пример класса с тестовыми методами."""

    def take_five(self):
        """Возвращает число 5."""
        return 5

    def port(self):
        """Возвращает порт сервера."""
        return PORT


if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
        