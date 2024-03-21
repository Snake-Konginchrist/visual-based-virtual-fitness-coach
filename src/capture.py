import cv2


def capture_video():
    """
    使用摄像头捕获视频流，并实时返回每一帧图像。
    """
    cap = cv2.VideoCapture(0)  # 0代表计算机默认摄像头
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # 这里可以添加其他处理帧的代码
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按'q'退出
            break
    cap.release()
    cv2.destroyAllWindows()
