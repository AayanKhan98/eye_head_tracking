import sys

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import mediapipe as mp
import pygame
import time

cap = cv2.VideoCapture(0)
cap.set(3, 540)
cap.set(4, 580)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
HEIGHT = 540
WIDTH = 580
PAD_X = 100
PAD_Y = 100
THRESHOLD = 60


def load_images(pygame, gamescreen, image_path, answer):
    answer_img = ""
    all_images = []
    for i, img in enumerate(image_path):
        temp_img = pygame.image.load("images/" + img).convert_alpha()
        if i == answer:
            answer_img = temp_img
        if i == 0:
            all_images.append(temp_img)
            gamescreen.blit(temp_img, (0, 0 + PAD_Y))
        elif i == 1:
            all_images.append(temp_img)
            gamescreen.blit(temp_img, (340, 0 + PAD_Y))
        elif i == 2:
            all_images.append(temp_img)
            gamescreen.blit(temp_img, (0, 350))
        else:
            all_images.append(temp_img)
            gamescreen.blit(temp_img, (340, 350))
    return all_images, answer_img
    # moonImg = pygame.image.load("images/moon.png").convert_alpha()


def get_image_center(images, index):
    points = images[index].get_rect()
    center_x = int((points[2] - points[0]) / 2)
    center_y = int((points[3] - points[1]) / 2)

    return center_x, center_y


def get_answer_img():
    pass


def quiz1(pygame, screen, current_time):
    run = True
    text_surface = my_font.render('Where is SUN located ? ', False, (255, 255, 0))
    score_surface = my_font.render("Score : " + str(score), False, (255, 255, 0))
    answer_img = ""
    images = ["sun.png", "moon.png", "neptune.png", "venus.png"]

    is_timer_set = 0
    while run:
        clock.tick(30)
        screen.fill('black')
        screen.blit(text_surface, (0, 20))
        screen.blit(score_surface, (0, 550))
        all_imgs, sunImg = load_images(pygame, screen, images, 2)
        success, img = cap.read()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit(1)

        img = cv2.flip(img, 1)
        rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks

        new_x = -100
        new_y = -100

        if landmark_points:
            landmarks = landmark_points[0].landmark
            # print(landmarks.shape)
            for landmark in landmarks[469:477]:
                x = int(landmark.x * WIDTH)
                y = int(landmark.y * HEIGHT)
                # print(x, y)

                if (x < center_x - THRESHOLD) and (y < center_y - THRESHOLD):
                    # new_x, new_y = get_image_center(all_imgs, 0)
                    new_x = 100
                    new_y = 200

                elif (x > center_x + THRESHOLD) and (y < center_y - THRESHOLD):
                    new_x = 440
                    new_y = 200


                elif (x < center_x - THRESHOLD) and (y > center_y + THRESHOLD):

                    new_x = 100
                    new_y = 440
                elif (x > center_x + 60) and (y > center_y + 60):
                    new_x = 440
                    new_y = 440

                pygame.draw.circle(screen, 'blue', (x, y), 3)
                pygame.draw.circle(screen, 'red', (new_x, new_y), 20)

                if is_timer_set:
                    if not sunImg.get_rect().collidepoint((x, y - 100)):
                        is_timer_set = 0
                #print(sunImg.get_rect())
                if sunImg.get_rect().collidepoint((x, y - 100)):
                    if is_timer_set == 0:
                        t_start = pygame.time.get_ticks()
                        is_timer_set = 1

                    timer_end = pygame.time.get_ticks()
                    time_diff = timer_end - t_start

                    if time_diff > 2000:
                        run = False
                        is_timer_set = 0
                        # return 10

        pygame.display.flip()

    return 10
    # pygame.quit()


def quiz2(pygame, screen, current_time):
    run = True
    text_surface = my_font.render('Where is ROSE located ? ', False, (255, 255, 0))
    score_surface = my_font.render("Score : " + str(score), False, (255, 255, 0))
    answer_img = ""
    images = ["tulip.png", "rose.png", "tulip2.png", "lotus.png"]

    is_timer_set = 0
    while run:
        clock.tick(30)
        screen.fill('black')
        screen.blit(text_surface, (0, 20))
        screen.blit(score_surface, (0, 550))
        all_imgs, sunImg = load_images(pygame, screen, images, 1)
        success, img = cap.read()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit(1)

        img = cv2.flip(img, 1)
        rgb_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks

        new_x = -100
        new_y = -100

        if landmark_points:
            landmarks = landmark_points[0].landmark
            # print(landmarks.shape)
            for landmark in landmarks[469:478]:
                x = int(landmark.x * WIDTH)
                y = int(landmark.y * HEIGHT)
                # print(x, y)

                if (x < center_x - THRESHOLD) and (y < center_y - THRESHOLD):
                    new_x = 100
                    new_y = 200

                elif (x > center_x + THRESHOLD) and (y < center_y - THRESHOLD):
                    new_x = 440
                    new_y = 200

                elif (x < center_x - THRESHOLD) and (y > center_y + THRESHOLD):
                    new_x = 100
                    new_y = 440
                elif (x > center_x + 60) and (y > center_y + 60):
                    new_x = 440
                    new_y = 440

                pygame.draw.circle(screen, 'blue', (x, y), 3)
                pygame.draw.circle(screen, 'red', (new_x, new_y), 20)

                if is_timer_set:
                    if not sunImg.get_rect().collidepoint((x - 380, y - 100)):
                        is_timer_set = 0
                # print(sunImg.get_rect())
                if sunImg.get_rect().collidepoint((x - 380, y - 100)):
                    if is_timer_set == 0:
                        t_start = pygame.time.get_ticks()
                        is_timer_set = 1

                    timer_end = pygame.time.get_ticks()
                    time_diff = timer_end - t_start

                    if time_diff > 2000:
                        run = False
                        is_timer_set = 0
                        # return 10

        pygame.display.flip()

    return 10
    # pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Arial', 30)
    clock = pygame.time.Clock()
    current_time = 0
    screen = pygame.display.set_mode([540, 580])
    center_x = 270
    center_y = 290
    score = 0

    score += quiz1(pygame, screen, current_time)
    score += quiz2(pygame, screen, current_time)
    print(score)
    my_font = pygame.font.SysFont('Arial', 50)
    text_win = my_font.render('Congratulations!  ', False, (0, 255, 0))
    score_win = my_font.render("Your Score : " + str(score), False, (255, 255, 0))
    screen.fill('black')
    screen.blit(text_win, (0, 20))
    screen.blit(score_win, (0, 240))
    pygame.display.flip()
    pygame.event.pump()
    pygame.time.delay(5 * 1000)
    pygame.quit()

    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
