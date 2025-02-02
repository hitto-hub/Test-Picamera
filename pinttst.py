from picamera2 import Picamera2
import time
import cv2  # OpenCVライブラリ

def main():
    # Picamera2インスタンスの生成
    picam2 = Picamera2()

    # 静止画用の設定を作成して適用
    camera_config = picam2.create_still_configuration()
    picam2.configure(camera_config)

    # カメラの起動
    picam2.start()
    print("カメラが起動しました。3秒後に写真を撮影します...")
    time.sleep(3)  # 少し待機

    # 写真の撮影
    image = picam2.capture_array()

    # もし image が RGB 形式なら BGR に変換
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 画像を保存
    cv2.imwrite("capture.jpg", image)
    print("写真を 'capture.jpg' に保存しました。")

    # カメラの停止
    picam2.stop()

if __name__ == '__main__':
    main()
