import matplotlib.pyplot as plt
import sys

import settings as settings
import track_generator as tg
import callback as cb

settings.init()


def generate_from_list():
    # Generate track
    center_line, right_line, left_line, settings.YELLOW_CONES, \
        settings.BLUE_CONES, settings.ORANGE_CONES = tg.create_track(
            settings.TRACK_POINTS)
    settings.TRACK_GENERATED = True

    # Plot centerline and border lines
    settings.CENTER_LINE_PLOT = plt.plot(
        center_line[:, 0], center_line[:, 1], '-k')[0]
    plt.plot(right_line[:, 0], right_line[:, 1], '--y', alpha=.5)
    plt.plot(left_line[:, 0], left_line[:, 1], '--b', alpha=.5)

    # Plot the cones
    plt.plot(settings.BLUE_CONES[:, 0], settings.BLUE_CONES[:, 1], '*b')
    plt.plot(settings.YELLOW_CONES[:, 0], settings.YELLOW_CONES[:, 1], '*y')
    plt.plot(settings.ORANGE_CONES[:, 0], settings.ORANGE_CONES[:, 1],
             linestyle='None', marker='*', color='tab:orange')

    # Create title
    plt.title('Generated track from given list. Press \'h\' to toggle centerline')


def generate_from_click():
    # Connect additional event listeners
    settings.MOUSE = settings.FIG.canvas.mpl_connect(
        'button_press_event', cb.on_click)
    settings.T_KEY = settings.FIG.canvas.mpl_connect(
        'key_press_event', cb.on_t_press)
    settings.X_KEY = settings.FIG.canvas.mpl_connect(
        'key_press_event', cb.on_x_press)

    # Create title
    plt.title(
        'Click to add points, press \'x\' to remove point, press \'t\' to generate track')


if __name__ == '__main__':
    # Check which mode we are running
    try:
        mode = sys.argv[1]
    except IndexError:
        print("Please enter if 'click' or 'list' mode")
        exit()
    try:
        assert mode == 'click' or mode == 'list'
    except AssertionError:
        print('Please enter valid argument \'click\' or \'list\'')
        exit()

    # Set up plot
    plt.xlim([-100, 100])
    plt.ylim([-100, 100])

    # Keys that are always active
    settings.D_KEY = settings.FIG.canvas.mpl_connect(
        'key_press_event', cb.on_d_press)
    settings.H_KEY = settings.FIG.canvas.mpl_connect(
        'key_press_event', cb.on_h_press)

    # Choose mode
    if mode == 'list':
        generate_from_list()
    else:
        generate_from_click()

    # Display window
    plt.show()
