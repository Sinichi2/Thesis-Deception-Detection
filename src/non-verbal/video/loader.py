def loader_many(base_paths, target_size=None, max_frames=None):
    import os, cv2
    videos, labels = [], []
    for base_path in base_paths:
        for label_name in os.listdir(base_path):
            subfolder = os.path.join(base_path, label_name)
            if not os.path.isdir(subfolder):
                continue
            for filename in os.listdir(subfolder):
                file_path = os.path.join(subfolder, filename)
                cap = cv2.VideoCapture(file_path)
                frames, count = [], 0
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    if target_size:
                        frame = cv2.resize(frame, target_size)
                    frames.append(frame)
                    count += 1
                    if max_frames and count >= max_frames:
                        break
                cap.release()
                if frames:
                    videos.append(frames)
                    labels.append(label_name)
    return videos, labels
