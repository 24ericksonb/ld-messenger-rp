from flask import Flask, request
import pygame
import threading
import time

app = Flask(__name__)
received_message = "Welcome!"  # Default message

@app.route('/send_message', methods=['POST'])
def send_message():
    global received_message
    received_message = request.json.get('message', '')
    return {'status': 'success', 'message': 'Message received'}

def run_flask_app():
    app.run(host='0.0.0.0', port=5000, threaded=True)

def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 320))
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        text_surface = font.render(received_message, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10))
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    # Run the Flask server in a separate thread
    threading.Thread(target=run_flask_app, daemon=True).start()
    # Run the Pygame display in the main thread
    main()
