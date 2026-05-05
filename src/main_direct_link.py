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

    def do_POST(self):
        """ Метод для обработки POST-запросов """
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        print(f'Получены данные: {body.decode('utf-8')}')
        self.send_response(303)
        self.send_header('Location', self.path)
        self.end_headers()


Handler = CustomHandler

# Запускаем сервер
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    print(f"Доступ к вашему приложению: http://localhost:{PORT}")
    print("Для остановки сервера прервите выполнение этой ячейки.")
    httpd.serve_forever()