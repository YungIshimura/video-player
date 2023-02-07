from livereload import Server


server = Server()
server.watch('style.css')
server.serve(root='.')