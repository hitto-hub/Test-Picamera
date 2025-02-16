from picamera2 import Picamera2
import time

def main():
    # Picamera2インスタンスの生成
    picam2 = Picamera2()

    # カメラの設定（デフォルト設定の場合）
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)

    # カメラの起動
    picam2.start()
    print("カメラが起動しました。3秒後に写真を撮影します...")
    time.sleep(3)  # 少し待機

    # 写真の撮影
    image = picam2.capture_array()

    # 画像を保存
    import cv2  # OpenCVライブラリがある場合（無ければpip install opencv-python）
    cv2.imwrite("capture.jpg", image)
    print("写真を 'capture.jpg' に保存しました。")

    # カメラの停止
    picam2.stop()

if __name__ == '__main__':
    main()
