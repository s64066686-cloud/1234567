        # 얼굴 위에 상태 표시
        ty = y - 10 if y > 60 else y + h + 25

        cv2.putText(
            img, status, (x, ty),
            cv2.FONT_HERSHEY_SIMPLEX, 0.7,
            color, 2
        )

        # 얼굴 바로 옆에 좌표 표시
        coordinate_text = f"X:{cx} Y:{cy}"

        cv2.putText(
            img, coordinate_text,
            (x + w + 10, cy),  # 얼굴 오른쪽에 표시
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (255, 255, 0), 2
        )
