def provide_feedback(detected_action):
    """
    根据识别出的动作类别提供反馈。
    """
    if detected_action == "标准动作":
        feedback = "干得好，继续保持。"
    else:
        feedback = "请调整你的姿势。"
    return feedback
