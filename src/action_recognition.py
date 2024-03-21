def recognize_action(results):
    """
    根据输入的姿态信息识别当前动作类别。

    参数:
    - results: MediaPipe Pose处理结果

    返回:
    - 识别出的动作类别
    """
    # if not results.pose_landmarks:
    #     return "无法识别"  # 当未检测到姿态时
    #
    # # 获取左手腕和鼻子的关键点
    # left_wrist = results.pose_landmarks.landmark[mp.solutions.pose.PoseLandmark.LEFT_WRIST]
    # nose = results.pose_landmarks.landmark[mp.solutions.pose.PoseLandmark.NOSE]
    #
    # # 简单的动作识别规则：如果左手腕的y坐标小于鼻子的y坐标，我们假设这是一个“举手”动作
    # if left_wrist.y < nose.y:
    #     return "举手"
    # else:
    #     return "站立"

    return "现在不检测"
