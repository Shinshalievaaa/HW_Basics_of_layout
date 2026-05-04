import http.server
import socketserver
import os

PORT = 8080

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Если запрос к корню или к несуществующему файлу, обслуживаем contacts.html
        if self.path == '/' or not os.path.exists(self.translate_path(self.path)):
            self.path = 'src/contacts.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


Handler = CustomHandler

# Запускаем сервер
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    print(f"Доступ к вашему приложению: http://localhost:{PORT}")
    print("Для остановки сервера прервите выполнение этой ячейки.")
    httpd.serve_forever()