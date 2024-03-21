import cv2


def resize_frame(frame, target_width=720):
    """
    调整帧的大小，保持纵横比不变。

    参数:
    - frame: 输入的图像帧
    - target_width: 目标宽度

    返回:
    - resized_frame: 调整大小后的图像帧
    """
    height, width = frame.shape[:2]
    scale = target_width / width
    target_height = int(height * scale)
    resized_frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LINEAR)
    return resized_frame


def draw_text(frame, text, position=(20, 30), font_scale=1, color=(0, 255, 0), thickness=2):
    """
    在图像帧上绘制文本。

    参数:
    - frame: 输入的图像帧
    - text: 要绘制的文本字符串
    - position: 文本在图像上的位置
    - font_scale: 字体大小
    - color: 文本颜色
    - thickness: 文本线条粗细

    返回:
    - frame: 绘制了文本的图像帧
    """
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)
    return frame


def convert_to_grayscale(frame):
    """
    将图像帧转换为灰度图。

    参数:
    - frame: 输入的彩色图像帧

    返回:
    - grayscale_frame: 转换为灰度的图像帧
    """
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return grayscale_frame


def overlay_image(background, overlay, position=(0, 0), opacity=1):
    """
    将一个图像覆盖到另一个图像上。

    参数:
    - background: 背景图像
    - overlay: 覆盖图像
    - position: 覆盖图像在背景图像上的位置
    - opacity: 覆盖图像的不透明度

    返回:
    - output: 合成的图像
    """
    x, y = position
    overlay_height, overlay_width = overlay.shape[:2]
    background[y:y + overlay_height, x:x + overlay_width] = cv2.addWeighted(
        background[y:y + overlay_height, x:x + overlay_width], 1 - opacity, overlay, opacity, 0)
    return background
