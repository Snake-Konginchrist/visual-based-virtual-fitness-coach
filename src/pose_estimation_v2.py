import cv2
import mediapipe as mp

# mp_pose = mp.solutions.pose
# pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5, model_complexity=2)
#
# cap = cv2.VideoCapture(0)
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     # 转换图像颜色空间
#     image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     image.flags.writeable = False
#
#     # 姿态检测
#     results = pose.process(image)
#
#     # 在原图上绘制姿态注释
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     mp.solutions.drawing_utils.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#
#     cv2.imshow('MediaPipe Pose', image)
#     if cv2.waitKey(5) & 0xFF == 27:  # 按ESC键退出
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# 初始化MediaPipe Pose组件。
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False,
                    model_complexity=1,
                    smooth_landmarks=True,
                    enable_segmentation=False,
                    smooth_segmentation=True,
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5)


def estimate_pose(frame):
    """
    使用MediaPipe进行姿态估计。

    参数:
    - frame: 输入的图像帧

    返回:
    - frame: 经过姿态估计绘制了姿态关键点的图像帧
    """

    # 转换颜色空间从BGR到RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 设置图像为不可写，以提高性能
    frame_rgb.flags.writeable = False

    # 进行姿态估计
    results = pose.process(frame_rgb)

    # 设置图像为可写，以便在其上绘制关键点
    frame_rgb.flags.writeable = True

    # 转换颜色空间回BGR，以便与OpenCV兼容
    frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

    # 绘制姿态关键点
    mp_drawing = mp.solutions.drawing_utils

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame,
                                  results.pose_landmarks,
                                  mp_pose.POSE_CONNECTIONS)

    return frame
