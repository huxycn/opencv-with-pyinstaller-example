import os
import cv2
import time
from tqdm import tqdm


def write_subtitles_into_video(video_path, second_list, subtitle_list, left, top):
    cap = cv2.VideoCapture(video_path)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fps = int(cap.get(cv2.CAP_PROP_FPS))

    total_seconds = total_frames / fps

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print("""
    *************** Video Info ***************
                   width = {}
                  height = {}
            total frames = {}
                     fps = {}
           total seconds = {}
    ******************************************
    """.format(width, height, total_frames, fps, total_seconds))

    video_writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # seconds_list = [3, 10, 20, 30, 40, 50, 60, 63]
    # put_text = ['Start', '10', '20', '30', '40', '50', '60', '67']

    idx = 0
    for frame_cnt in tqdm(range(total_frames)):
        ret, frame = cap.read()

        if idx < len(second_list):
            if second_list[idx] * fps <= frame_cnt <= (second_list[idx] + 1) * fps:
                cv2.putText(frame, subtitle_list[idx], (int(left * width), int(top * height)), cv2.FONT_HERSHEY_PLAIN, 6, (255, 255, 255), 10)
                # cv2.imshow('imshow', frame)
                # cv2.waitKey()
                # cv2.destroyAllWindows()
            if frame_cnt == (second_list[idx] + 1) * fps:
                idx += 1
        video_writer.write(frame)

    cap.release()


def main():
    with open('subtitles.txt', 'r') as f:
        lines = f.readlines()
    video_path = lines[0].strip()
    left = float(lines[-2].strip().split(',')[1])
    top = float(lines[-1].strip().split(',')[1])
    second_list = []
    subtitle_list = []
    for line in lines[2:-3]:
        line = line.strip()
        second = int(line.split(',')[0])
        subtitle = line.split(',')[1]
        second_list.append(second)
        subtitle_list.append(subtitle)

    # print('1.Please enter your video path')
    # video_path = input('==> video path = ')
    # print()
    #
    # print('2.Please enter at [WHICH second] add [WHAT subtitle] ("second=-1" indicates stop entering)')
    # second_list = []
    # subtitle_list = []
    # while True:
    #     print('\t(Tip: "second=-1" indicates stop entering)')
    #     second = int(input('\t==> second = '))
    #     if second == -1:
    #         break
    #     subtitle = input('\t==> subtitle = ')
    #     second_list.append(second)
    #     subtitle_list.append(subtitle)
    #     print('\t[OK]\n\t{}'.format('-'*20))
    # print()
    #
    # print('3.Seconds and Subtitles to add')
    # print((len(second_list)+1) * 10 * '=')
    # second_list_str = 'second    ' + ''.join(['{:<10}'.format(second) for second in second_list])
    # print(second_list_str)
    # subtitle_list_str = 'subtitle  ' + ''.join(['{:<10}'.format(subtitle) for subtitle in subtitle_list])
    # print(subtitle_list_str)
    # print((len(second_list)+1) * 10 * '=')
    # print()
    #
    # confirm = input('4.Do you want to write the above subtitles into the video?(y/N)\n==> ')
    # if confirm == 'y':
    #     write_subtitles_into_video(video_path, second_list, subtitle_list)
    #     # for i in tqdm(range(10)):
    #     #     time.sleep(0.2)
    #     print('Complete.')
    # else:
    #     print('Exit.')
    write_subtitles_into_video(video_path, second_list, subtitle_list, left, top)
    current_dir = os.getcwd()
    output_path = os.path.join(current_dir, 'output.mp4')
    print('[OK] Video saved as {}'.format(output_path))
    key = input('Type "Enter" to exit ...')
    time.sleep(1)


if __name__ == '__main__':
    main()
