import cv2

from src.action_recognition import recognize_action
from src.detection import detect_human
from src.feedback import provide_feedback
from src.pose_estimation_v2 import estimate_pose


def main():
    # 初始化摄像头
    cap = cv2.VideoCapture(0)

    while True:
        # 捕获视频帧
        ret, frame = cap.read()
        if not ret:
            break

        # 检测人体
        frame_with_detection = detect_human(frame)

        # 姿态估计
        pose_estimated_frame = estimate_pose(frame_with_detection)

        # 动作识别
        action = recognize_action(pose_estimated_frame)

        # 提供反馈
        feedback = provide_feedback(action)
        print(feedback)

        # 显示结果
        cv2.imshow('Fitness Coach', pose_estimated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源并关闭窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
