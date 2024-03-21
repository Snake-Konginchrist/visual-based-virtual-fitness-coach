import cv2


def detect_human(frame):
    """
    从给定的图像帧中检测人体，并返回检测到的人体边界框。
    """
    # 示例中使用OpenCV的预训练Haar级联分类器进行人脸检测
    # 实际应用中可替换为更高级的人体检测模型
    haar_file_path = "data/models/haarcascade_fullbody.xml"
    body_cascade = cv2.CascadeClassifier(haar_file_path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame
