# Visual-Based Virtual Fitness Coach

🌐 [简体中文版本](README_zh-CN.md) | **English Version**

A computer vision-powered fitness coaching system that uses deep learning technology to capture fitness movements through cameras, providing real-time exercise recognition and guidance feedback to help users perform personal fitness training in a more scientific and safe manner.

## Features

- **Real-time Video Capture**: Uses computer or mobile device cameras to capture user's fitness movements
- **Human Detection & Pose Estimation**: Quickly and accurately detects human bodies from videos and estimates their poses
- **Action Recognition**: Utilizes deep learning models to recognize user's fitness movements
- **Instant Feedback**: Provides immediate feedback for movement improvement based on action recognition results

## Project Structure

A typical intelligent fitness coaching system may include the following main components:

- **Image Capture Module**: Uses cameras to capture fitness movements in real-time
- **Human Detection Module**: Detects and extracts the fitness enthusiast's body from captured images
- **Pose Estimation Module**: Performs skeletal key point detection on detected human bodies to estimate their poses
- **Action Recognition Module**: Classifies current movements based on human pose information using deep neural networks
- **Guidance Feedback Module**: Compares recognized movements with standard movement templates to provide real-time fitness guidance and feedback

```
visual-based-virtual-fitness-coach/
├── data/                  # Data directory for training data and model files
│   ├── models/            # Pre-trained models and trained model files
│   └── videos/            # Test video files
├── docs/                  # Project documentation including design docs and user manuals
├── src/                   # Source code directory
│   ├── capture.py         # Image capture module for video stream capture and processing
│   ├── detection.py       # Human detection module for detecting human bodies from images
│   ├── pose_estimation_v1.py # Pose estimation module v1 for pose key point detection
│   ├── pose_estimation_v2.py # Pose estimation module v2 for pose key point detection
│   ├── action_recognition.py # Action recognition module for movement recognition and classification
│   └── feedback.py        # Guidance feedback module providing feedback based on action recognition
├── tests/                 # Test code directory containing unit and integration tests
│   ├── test_capture.py
│   ├── test_detection.py
│   └── test_pose_estimation.py
├── utils/                 # Utility code directory for helper functions and utility classes
│   └── utils.py           # Common utility functions for image processing, data conversion, etc.
├── requirements.txt       # Project dependency file listing all external library versions
└── main.py                # Main program entry point integrating all modules for complete functionality
```

## Getting Started

### Requirements

- Python 3.7+
- Compatible operating systems: Windows, macOS, Linux
- Camera (webcam or built-in camera)

### Installation

First, clone the project to your local machine:

```bash
git clone https://github.com/Snake-Konginchrist/visual-based-virtual-fitness-coach.git
cd visual-based-virtual-fitness-coach
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running

Start the intelligent fitness coaching system:

```bash
python main.py
```

## Usage Instructions

1. Ensure your camera is connected and working properly
2. After running the program, stand in front of the camera and begin your fitness movements
3. The system will display real-time video and provide movement guidance feedback

## Development

### Project Structure

See the [Project Structure](#project-structure) section above for detailed information.

### Adding New Action Recognition Models

1. Train your model and save it
2. Place the model file in the `data/models` directory
3. Modify `action_recognition.py` to use the new model for action recognition

## Contributing

We welcome all forms of contributions, whether it's suggestions for new features, code improvements, documentation updates, or bug reports. Please contact us through GitHub issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Thanks to all the authors of open-source projects and libraries whose work has provided tremendous help for the development of this project.

## Contact Information

- GitHub: [Snake-Konginchrist](https://github.com/Snake-Konginchrist)
- Gitee: [Snake-Konginchrist](https://gitee.com/Snake-Konginchrist)
- Developer Email: [developer@skstudio.cn](mailto:developer@skstudio.cn)
- Business Cooperation Email: [contact@skstudio.cn](mailto:contact@skstudio.cn)
- Official Website (China): [彩旗工作室](https://www.skstudio.cn)
- Official Website (International): [SK Studio](https://www.sihuangtech.com)
- QQ Group for Open Source Discussion: [Click to join the QQ Group](https://qm.qq.com/q/tkZHCKiY36)
- Discord Server for Open Source Discussion: [Click to join the Discord community](https://discord.gg/thWGWq7CwA)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Snake-Konginchrist/visual-based-virtual-fitness-coach&type=Date)](https://www.star-history.com/#Snake-Konginchrist/visual-based-virtual-fitness-coach&Date)